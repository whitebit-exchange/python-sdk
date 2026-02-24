"""Fix import statements in generated code."""

import os
import re
from pathlib import Path


def fix_init_py(file_path: Path) -> bool:
    """Fix imports in __init__.py file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Check if this is an api/__init__.py or models/__init__.py
        parent_name = file_path.parent.name

        if parent_name == "api":
            # In api/__init__.py, imports should be:
            # from .codes_api import CodesApi
            # NOT from .api.codes_api
            content = re.sub(
                r"^from \.api\.",
                "from .",
                content,
                flags=re.MULTILINE
            )
        elif parent_name == "models":
            # In models/__init__.py, imports should be:
            # from .some_model import SomeModel
            # NOT from .models.some_model or from main_api_generated.models.xxx
            content = re.sub(
                r"^from \.models\.",
                "from .",
                content,
                flags=re.MULTILINE
            )
            # Fix absolute imports
            content = re.sub(
                r"^from (main_api_generated|public_api_generated|oauth2_api_generated)\.models\.",
                "from .",
                content,
                flags=re.MULTILINE
            )
        else:
            # In main __init__.py, fix api and models imports
            content = re.sub(
                r"^from api\.",
                "from .api.",
                content,
                flags=re.MULTILINE
            )
            content = re.sub(
                r"^from models\.",
                "from .models.",
                content,
                flags=re.MULTILINE
            )
            # Fix absolute package imports (main_api_generated, public_api_generated, oauth2_api_generated)
            content = re.sub(
                r"^from (main_api_generated|public_api_generated|oauth2_api_generated)\.",
                r"from .",
                content,
                flags=re.MULTILINE
            )

        # Only write if changed
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def fix_api_and_model_files(base_dir: Path) -> int:
    """Fix imports in all API and model files."""
    fixed_count = 0

    # Fix imports in all .py files
    for py_file in base_dir.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue  # Already handled separately

        try:
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # Determine the package name from the path
            # e.g., main_api_generated, public_api_generated, oauth2_api_generated
            parts = py_file.parts
            if "main_api_generated" in parts:
                pkg_name = "main_api_generated"
            elif "public_api_generated" in parts:
                pkg_name = "public_api_generated"
            elif "oauth2_api_generated" in parts:
                pkg_name = "oauth2_api_generated"
            else:
                continue

            # Check if file is in api/ subdirectory
            if py_file.parent.name == "api":
                # In api/*.py files, fix model imports
                # from main_api_generated.models.xxx -> from ..models.xxx
                content = re.sub(
                    rf"from {pkg_name}\.models\.",
                    "from ..models.",
                    content
                )
                # from main_api_generated.api_client -> from ..api_client
                content = re.sub(
                    rf"from {pkg_name}\.api_client",
                    "from ..api_client",
                    content
                )
                # from main_api_generated.configuration -> from ..configuration
                content = re.sub(
                    rf"from {pkg_name}\.configuration",
                    "from ..configuration",
                    content
                )
                # from main_api_generated.api_response -> from ..api_response
                content = re.sub(
                    rf"from {pkg_name}\.api_response",
                    "from ..api_response",
                    content
                )
                # from main_api_generated.rest -> from ..rest
                content = re.sub(
                    rf"from {pkg_name}\.rest",
                    "from ..rest",
                    content
                )
                # from main_api_generated.exceptions -> from ..exceptions
                content = re.sub(
                    rf"from {pkg_name}\.exceptions",
                    "from ..exceptions",
                    content
                )
            elif py_file.parent.name == "models":
                # In models/*.py files, fix imports to other models
                # from main_api_generated.models.xxx -> from .xxx
                content = re.sub(
                    rf"from {pkg_name}\.models\.",
                    "from .",
                    content
                )
            else:
                # In base files (api_client.py, configuration.py, rest.py, etc.)
                # Fix absolute imports to relative imports

                # import main_api_generated.models -> from . import models
                content = re.sub(
                    rf"^import {pkg_name}\.models$",
                    "from . import models",
                    content,
                    flags=re.MULTILINE
                )
                # import main_api_generated.xxx -> from . import xxx
                content = re.sub(
                    rf"^import {pkg_name}\.(\w+)$",
                    r"from . import \1",
                    content,
                    flags=re.MULTILINE
                )

                # from main_api_generated import xxx -> from . import xxx
                content = re.sub(
                    rf"^from {pkg_name} import ",
                    "from . import ",
                    content,
                    flags=re.MULTILINE
                )

                # from main_api_generated.models.xxx -> from .models.xxx
                content = re.sub(
                    rf"from {pkg_name}\.models\.",
                    "from .models.",
                    content
                )
                # from main_api_generated.api_client -> from .api_client
                content = re.sub(
                    rf"from {pkg_name}\.api_client",
                    "from .api_client",
                    content
                )
                # from main_api_generated.configuration -> from .configuration
                content = re.sub(
                    rf"from {pkg_name}\.configuration",
                    "from .configuration",
                    content
                )
                # from main_api_generated.api_response -> from .api_response
                content = re.sub(
                    rf"from {pkg_name}\.api_response",
                    "from .api_response",
                    content
                )
                # from main_api_generated.rest -> from .rest
                content = re.sub(
                    rf"from {pkg_name}\.rest",
                    "from .rest",
                    content
                )
                # from main_api_generated.exceptions -> from .exceptions
                content = re.sub(
                    rf"from {pkg_name}\.exceptions",
                    "from .exceptions",
                    content
                )

                # Fix references in code like main_api_generated.models -> models
                content = re.sub(
                    rf"{pkg_name}\.models",
                    "models",
                    content
                )

            # Only write if changed
            if content != original_content:
                with open(py_file, "w", encoding="utf-8") as f:
                    f.write(content)
                fixed_count += 1

        except Exception as e:
            print(f"Error processing {py_file}: {e}")
            continue

    return fixed_count


def main():
    """Fix imports in all generated files."""
    print("🔧 Fixing import statements in generated code...")

    base_dir = Path("whitebit_sdk/http/generated")

    if not base_dir.exists():
        print(f"❌ Directory not found: {base_dir}")
        return

    # Fix __init__.py files
    init_files = list(base_dir.rglob("__init__.py"))
    print(f"Found {len(init_files)} __init__.py files")

    init_fixed = 0
    for init_file in init_files:
        if fix_init_py(init_file):
            print(f"  ✓ Fixed: {init_file.relative_to('whitebit_sdk/http/generated')}")
            init_fixed += 1

    # Fix API and model files
    print("\nFixing imports in API and model files...")
    files_fixed = fix_api_and_model_files(base_dir)
    print(f"  ✓ Fixed {files_fixed} API/model files")

    print(f"\n✅ Fixed {init_fixed} __init__.py files and {files_fixed} other files")


if __name__ == "__main__":
    main()
