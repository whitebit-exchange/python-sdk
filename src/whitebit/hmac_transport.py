"""
WhiteBit HMAC authentication transport for the Python SDK.

Usage::

    from whitebit import WhitebitApi
    from whitebit.hmac_transport import HmacTransport
    import httpx

    client = WhitebitApi(
        txc_apikey="YOUR_API_KEY",
        token="YOUR_TOKEN",
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
        body.setdefault("nonce", int(time.time() * 1000))
        body.setdefault("request", path)
        body.setdefault("nonceWindow", True)

        new_raw = json.dumps(body, separators=(",", ":")).encode()
        payload = base64.b64encode(new_raw).decode()
        signature = hmac.new(
            self._api_secret.encode(),
            payload.encode(),
            hashlib.sha512,
        ).hexdigest()

        headers = self._clean_headers(request, strip_keys=("content-length",))
        headers["X-TXC-PAYLOAD"]   = payload
        headers["X-TXC-SIGNATURE"] = signature

        patched = httpx.Request(
            method=request.method,
            url=request.url,
            headers=headers,
            content=new_raw,
        )
        return self._wrapped.handle_request(patched)
