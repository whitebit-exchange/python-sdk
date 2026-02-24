"""Signature generation utilities."""

import base64
import hashlib
import hmac
import json
from typing import Any, Dict


def generate_signature(payload: str, secret: str) -> str:
    """Generate HMAC-SHA512 signature."""
    signature = hmac.new(
        secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha512
    ).hexdigest()
    return signature


def create_signed_payload(data: Dict[str, Any], secret: str) -> tuple[str, str]:
    """Create signed payload for API request."""
    payload_str = json.dumps(data, separators=(",", ":"))
    payload_b64 = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")
    signature = generate_signature(payload_b64, secret)
    return payload_b64, signature
