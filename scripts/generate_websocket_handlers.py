#!/usr/bin/env python3
"""Generate WebSocket handler classes from AsyncAPI specs."""

import sys
from pathlib import Path
import yaml
from typing import Dict, Any

HANDLER_TEMPLATE = '''"""WebSocket handler for {channel_name}."""

from typing import Any, Callable, Optional
import asyncio
from ..base import BaseWebSocketHandler

class {class_name}(BaseWebSocketHandler):
    """Handler for {channel_name} WebSocket channel."""

    def __init__(self, ws_client):
        super().__init__(ws_client)
        self.channel_name = "{channel_name}"

    async def request(self, *args, **kwargs) -> Any:
        """Send request to {channel_name}."""
        method = "{method_prefix}_request"
        return await self.send_request(method, list(args))

    async def subscribe(self, *args, on_update: Optional[Callable] = None, **kwargs) -> None:
        """Subscribe to {channel_name} updates."""
        method = "{method_prefix}_subscribe"
        await self.send_request(method, list(args))

        if on_update:
            self.register_update_handler("{method_prefix}_update", on_update)

    async def unsubscribe(self) -> None:
        """Unsubscribe from {channel_name}."""
        method = "{method_prefix}_unsubscribe"
        await self.send_request(method, [])
'''

def extract_channel_info(spec: Dict[str, Any], spec_file: Path) -> Dict[str, str]:
    """Extract channel information from AsyncAPI spec."""
    info = spec.get('info', {})
    title = info.get('title', spec_file.stem)

    # Try to find method prefix from spec
    operations = spec.get('operations', {})
    method_prefix = spec_file.stem  # fallback

    # Extract from operations
    for op_name, op_def in operations.items():
        if 'sendRequest' in op_name or 'Request' in op_name:
            messages = op_def.get('messages', [])
            if messages:
                # Try to extract method name
                msg_ref = messages[0].get('$ref', '')
                if 'messages' in msg_ref:
                    method_name = msg_ref.split('/')[-1]
                    if 'Request' in method_name:
                        method_prefix = method_name.replace('Request', '').replace('request', '')
                        break

    return {
        'channel_name': title,
        'method_prefix': method_prefix,
        'class_name': ''.join(word.capitalize() for word in method_prefix.split('_')) + 'Handler'
    }

def main():
    """Generate WebSocket handlers from AsyncAPI specs."""
    print("=" * 50)
    print("Generating WebSocket Handlers")
    print("=" * 50)

    api_dir = Path(__file__).parent.parent / "api" / "asyncapi"

    # Generate for private channels
    private_dir = api_dir / "private"
    private_output = Path(__file__).parent.parent / "whitebit_sdk" / "websocket" / "private"
    private_output.mkdir(parents=True, exist_ok=True)

    # Generate for public channels
    public_dir = api_dir / "public"
    public_output = Path(__file__).parent.parent / "whitebit_sdk" / "websocket" / "public"
    public_output.mkdir(parents=True, exist_ok=True)

    for channel_type, (input_dir, output_dir) in [
        ("private", (private_dir, private_output)),
        ("public", (public_dir, public_output))
    ]:
        print(f"\nGenerating {channel_type} handlers...")

        if not input_dir.exists():
            print(f"  Warning: {input_dir} not found, skipping")
            continue

        spec_files = list(input_dir.glob("*.yaml"))

        for spec_file in sorted(spec_files):
            print(f"  Processing {spec_file.name}...")

            with open(spec_file, 'r', encoding='utf-8') as f:
                spec = yaml.safe_load(f)

            channel_info = extract_channel_info(spec, spec_file)

            # Generate handler file
            handler_code = HANDLER_TEMPLATE.format(**channel_info)

            output_file = output_dir / f"{spec_file.stem}.py"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(handler_code)

            print(f"    → Generated {channel_info['class_name']}")

        # Create __init__.py
        init_file = output_dir / "__init__.py"
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write(f'"""{channel_type.capitalize()} WebSocket handlers."""\n\n')
            f.write('__all__ = []\n')

    print("\n✓ WebSocket handlers generated")
    print("=" * 50)

if __name__ == "__main__":
    main()
