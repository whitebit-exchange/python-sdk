"""Authentication utilities."""

import time
from typing import Any, Dict

from .signature import create_signed_payload


def generate_nonce() -> str:
    """Generate nonce for API request."""
    return str(int(time.time() * 1000))


def create_auth_headers(api_key: str, payload: str, signature: str) -> Dict[str, str]:
    """Create authentication headers."""
    return {
        "X-TXC-APIKEY": api_key,
        "X-TXC-PAYLOAD": payload,
        "X-TXC-SIGNATURE": signature,
        "Content-Type": "application/json",
    }


def prepare_private_request(
    endpoint: str, data: Dict[str, Any], api_key: str, api_secret: str
) -> tuple[Dict[str, str], str]:
    """Prepare private API request with signature."""
    nonce = generate_nonce()

    request_data = {"request": endpoint, "nonce": nonce, **data}

    payload, signature = create_signed_payload(request_data, api_secret)
    headers = create_auth_headers(api_key, payload, signature)

    return headers, payload
