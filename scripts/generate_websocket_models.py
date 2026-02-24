#!/usr/bin/env python3
"""Generate Pydantic models from AsyncAPI specifications."""

import sys
from pathlib import Path
import yaml
from typing import Dict, Any

def parse_asyncapi_schema(spec: Dict[str, Any]) -> list:
    """Extract schemas from AsyncAPI spec."""
    schemas = []

    if 'components' in spec and 'schemas' in spec['components']:
        for schema_name, schema_def in spec['components']['schemas'].items():
            schemas.append({
                'name': schema_name,
                'definition': schema_def
            })

    return schemas

def generate_pydantic_model(schema_name: str, schema_def: Dict[str, Any]) -> str:
    """Generate Pydantic model code from schema definition."""
    lines = []
    lines.append(f"class {schema_name}(BaseModel):")
    lines.append('    """Generated from AsyncAPI schema."""')

    properties = schema_def.get('properties', {})
    required = schema_def.get('required', [])

    if not properties:
        lines.append('    pass')
        return '\n    '.join(lines)

    for prop_name, prop_def in properties.items():
        prop_type = prop_def.get('type', 'Any')
        description = prop_def.get('description', '')

        # Map JSON types to Python types
        type_mapping = {
            'string': 'str',
            'integer': 'int',
            'number': 'float',
            'boolean': 'bool',
            'array': 'List[Any]',
            'object': 'Dict[str, Any]',
            'null': 'None'
        }

        python_type = type_mapping.get(prop_type, 'Any')

        # Make optional if not required
        if prop_name not in required:
            python_type = f'Optional[{python_type}]'
            default = ' = None'
        else:
            default = ''

        # Clean description - remove problematic characters
        if description:
            clean_desc = description.replace('\n', ' ').replace('  ', ' ').strip()
            lines.append(f'    {prop_name}: {python_type}{default}')
        else:
            lines.append(f'    {prop_name}: {python_type}{default}')

    return '\n    '.join(lines)

def main():
    """Generate WebSocket models from AsyncAPI specs."""
    print("=" * 50)
    print("Generating WebSocket Models")
    print("=" * 50)

    api_dir = Path(__file__).parent.parent / "api" / "asyncapi"
    output_dir = Path(__file__).parent.parent / "whitebit_sdk" / "models" / "websocket"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all AsyncAPI specs
    asyncapi_files = list(api_dir.rglob("*.yaml"))

    print(f"\nFound {len(asyncapi_files)} AsyncAPI specifications\n")

    all_models = []

    for spec_file in sorted(asyncapi_files):
        print(f"Processing {spec_file.name}...")

        with open(spec_file, 'r', encoding='utf-8') as f:
            spec = yaml.safe_load(f)

        schemas = parse_asyncapi_schema(spec)

        for schema in schemas:
            model_code = generate_pydantic_model(schema['name'], schema['definition'])
            all_models.append(model_code)
            print(f"  → Generated model: {schema['name']}")

    # Write models file
    output_file = output_dir / "__init__.py"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('"""WebSocket API models generated from AsyncAPI specs."""\n\n')
        f.write('from typing import Any, Dict, List, Optional\n')
        f.write('from pydantic import BaseModel\n\n')
        f.write('__all__ = []\n\n')

        for model in all_models:
            f.write(model + '\n\n')

    print(f"\n✓ Generated {len(all_models)} models in {output_file}")
    print("=" * 50)

if __name__ == "__main__":
    main()
