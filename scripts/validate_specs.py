#!/usr/bin/env python3
"""Validate OpenAPI and AsyncAPI specifications."""

import sys
from pathlib import Path
import yaml

def validate_yaml_file(file_path: Path) -> bool:
    """Validate YAML file syntax."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✓ {file_path.name} - Valid YAML")
        return True
    except yaml.YAMLError as e:
        print(f"✗ {file_path.name} - Invalid YAML: {e}")
        return False
    except Exception as e:
        print(f"✗ {file_path.name} - Error: {e}")
        return False

def main():
    """Validate all API specifications."""
    print("=" * 50)
    print("Validating API Specifications")
    print("=" * 50)

    api_dir = Path(__file__).parent.parent / "api"

    if not api_dir.exists():
        print(f"Error: API directory not found: {api_dir}")
        sys.exit(1)

    # Find all YAML files
    yaml_files = list(api_dir.rglob("*.yaml"))

    if not yaml_files:
        print("No YAML files found in api/ directory")
        sys.exit(1)

    print(f"\nFound {len(yaml_files)} specification files\n")

    all_valid = True
    for yaml_file in sorted(yaml_files):
        if not validate_yaml_file(yaml_file):
            all_valid = False

    print("\n" + "=" * 50)
    if all_valid:
        print("✓ All specifications are valid!")
        print("=" * 50)
        sys.exit(0)
    else:
        print("✗ Some specifications have errors")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    main()
