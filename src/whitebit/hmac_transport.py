"""
WhiteBit HMAC authentication transport for the Python SDK.

Usage::

    from whitebit import WhitebitApi
    from whitebit.hmac_transport import HmacTransport
    import httpx

    client = WhitebitApi(
        api_key="YOUR_API_KEY",
        txc_payload="",
        txc_signature="",
        httpx_client=httpx.Client(transport=HmacTransport(api_secret="YOUR_API_SECRET")),
    )
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from typing import Optional
from urllib.parse import urlparse

import httpx


class HmacTransport(httpx.BaseTransport):
    """
    httpx transport that injects WhiteBit HMAC authentication headers
    (X-TXC-PAYLOAD, X-TXC-SIGNATURE) into every POST request.
    """

    def __init__(self, api_secret: str, wrapped: Optional[httpx.BaseTransport] = None) -> None:
        self._api_secret = api_secret
        self._wrapped = wrapped or httpx.HTTPTransport()

    @staticmethod
    def _clean_headers(request: httpx.Request, *, strip_keys: tuple = ()) -> dict:
        """Return headers dict with empty Bearer and any extra keys removed."""
        headers = {}
        for k, v in request.headers.items():
            kl = k.lower()
            if kl in strip_keys:
                continue
            # Drop "Authorization: Bearer " (empty token emitted by the SDK)
            if kl == "authorization" and v.strip() in ("Bearer", "Bearer "):
                continue
            headers[k] = v
        return headers

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        path = urlparse(str(request.url)).path
        if request.method != "POST" or not path.startswith("/api/v4/"):
            clean = self._clean_headers(request)
            if len(clean) != len(dict(request.headers)):
                request = httpx.Request(
                    method=request.method, url=request.url,
                    headers=clean, content=b"".join(request.stream),  # type: ignore[arg-type]
                )
            return self._wrapped.handle_request(request)

        raw = b"".join(request.stream)  # type: ignore[arg-type]

        # Treat empty body as `{}` — API still requires nonce/request fields
        if not raw:
            raw = b"{}"

        try:
            body: dict = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError):
            clean = self._clean_headers(request)
            patched = httpx.Request(
                method=request.method, url=request.url,
                headers=clean, content=raw,
            )
            return self._wrapped.handle_request(patched)
        # request/nonce: fill if falsy, not just if absent. Some endpoints'
        # generated request models declare request/nonce as required (OpenAPI
        # marks them required for the wire contract, since they're mandatory
        # for non-SDK callers), so they're always serialized as their zero
        # value ("" / 0) when the caller doesn't set them — which setdefault
        # would never touch since the key is already present. "" and 0 are
        # never legitimate caller-supplied values for these two fields, so
        # treating them as absent is safe and still lets an explicitly-set
        # nonce survive.
        if not body.get("request"):
            body["request"] = path
        if not body.get("nonce"):
            body["nonce"] = int(time.time() * 1000)
        # nonceWindow is genuinely optional in every spec and defaults to
        # false server-side — an explicit `nonceWindow: False` from the
        # caller must survive, so only fill it in when the key is missing.
        if body.get("nonceWindow") is None:
            body["nonceWindow"] = True

        new_raw = json.dumps(body, separators=(",", ":")).encode()
        payload = base64.b64encode(new_raw).decode()
        signature = hmac.new(
            self._api_secret.encode(),
            payload.encode(),
            hashlib.sha512,
        ).hexdigest()

        # Strip any pre-existing X-TXC-PAYLOAD/X-TXC-SIGNATURE (the SDK client sends empty
        # placeholders for these from its txc_payload/txc_signature constructor args).
        # request.headers.items() yields lowercase keys, but re-adding them below under
        # their canonical case would otherwise create a *second*, distinct dict entry
        # instead of replacing the placeholder — httpx then sends both as repeated
        # headers, and the server reads the first (empty) one ("Payload not provided").
        headers = self._clean_headers(
            request, strip_keys=("content-length", "x-txc-payload", "x-txc-signature")
        )
        headers["X-TXC-PAYLOAD"]   = payload
        headers["X-TXC-SIGNATURE"] = signature

        patched = httpx.Request(
            method=request.method,
            url=request.url,
            headers=headers,
            content=new_raw,
        )
        return self._wrapped.handle_request(patched)
