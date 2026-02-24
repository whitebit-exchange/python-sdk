#!/bin/bash

# HTTP Client Generation using OpenAPI Generator
# This script generates Python async clients from OpenAPI specifications

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Generating HTTP API Clients with OpenAPI Generator${NC}"
echo "============================================================"

# Set Java path
export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"

# Verify tools
echo -e "\n${BLUE}📋 Verifying tools...${NC}"
if ! command -v java &> /dev/null; then
    echo -e "${RED}❌ Java not found. Please install Java 11+${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Java: $(java -version 2>&1 | grep version | cut -d'"' -f2)${NC}"

if ! command -v openapi-generator-cli &> /dev/null; then
    echo -e "${RED}❌ OpenAPI Generator CLI not found${NC}"
    exit 1
fi
echo -e "${GREEN}✓ OpenAPI Generator: $(openapi-generator-cli version)${NC}"

# Clean old generated code
echo -e "\n${BLUE}🧹 Cleaning old generated code...${NC}"
rm -rf whitebit_sdk/http/generated
mkdir -p whitebit_sdk/http/generated

# Function to generate client
generate_client() {
    local spec_file=$1
    local output_dir=$2
    local config_file=$3
    local api_name=$4

    echo -e "\n${BLUE}📦 Generating ${api_name}...${NC}"
    echo "   Spec: ${spec_file}"
    echo "   Output: ${output_dir}"
    echo "   Config: ${config_file}"

    # Remove output directory if exists
    rm -rf "${output_dir}"

    # Generate client
    openapi-generator-cli generate \
        -i "${spec_file}" \
        -g python \
        -o "${output_dir}" \
        -c "${config_file}" \
        --skip-validate-spec \
        --global-property=apis,models,supportingFiles \
        2>&1 | grep -E "(Successfully|Error|Warning)" || true

    if [ -d "${output_dir}" ]; then
        echo -e "${GREEN}✓ ${api_name} generated successfully${NC}"

        # Count generated files
        api_count=$(find "${output_dir}" -name "*_api.py" 2>/dev/null | wc -l | tr -d ' ')
        model_count=$(find "${output_dir}" -name "*.py" -path "*/models/*" 2>/dev/null | wc -l | tr -d ' ')

        echo -e "${GREEN}  → API files: ${api_count}${NC}"
        echo -e "${GREEN}  → Model files: ${model_count}${NC}"
    else
        echo -e "${RED}❌ Failed to generate ${api_name}${NC}"
        return 1
    fi
}

# Generate Main API Client
generate_client \
    "api/main_api_v4.yaml" \
    "whitebit_sdk/http/generated/main_api" \
    "configs/openapi/main_api_config.yaml" \
    "Main API"

# Generate Public API Client
generate_client \
    "api/http-v4.yaml" \
    "whitebit_sdk/http/generated/public_api" \
    "configs/openapi/public_api_config.yaml" \
    "Public API"

# Generate OAuth2 API Client
generate_client \
    "api/oauth2.yaml" \
    "whitebit_sdk/http/generated/oauth2_api" \
    "configs/openapi/oauth2_config.yaml" \
    "OAuth2 API"

# Create __init__.py files
echo -e "\n${BLUE}📝 Creating package structure...${NC}"

# Main generated package
cat > whitebit_sdk/http/generated/__init__.py << 'EOF'
"""Generated HTTP API clients."""
EOF

echo -e "${GREEN}✓ Package structure created${NC}"

# Summary
echo -e "\n${GREEN}============================================================${NC}"
echo -e "${GREEN}✅ HTTP API clients generated successfully!${NC}"
echo -e "${GREEN}============================================================${NC}"

echo -e "\n${YELLOW}📊 Summary:${NC}"
echo -e "   Generated packages:"
echo -e "   • whitebit_sdk/http/generated/main_api"
echo -e "   • whitebit_sdk/http/generated/public_api"
echo -e "   • whitebit_sdk/http/generated/oauth2_api"

# Post-generation fixes
echo -e "\n${BLUE}🔧 Fixing imports in generated code...${NC}"

# Fix API/Models __init__.py files
find whitebit_sdk/http/generated -name "__init__.py" -path "*/api/__init__.py" -exec sed -i '' 's/^from api\./from ./g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "__init__.py" -path "*/models/__init__.py" -exec sed -i '' 's/^from models\./from ./g' {} \; 2>/dev/null || true

# Fix absolute package imports to relative
find whitebit_sdk/http/generated -name "*.py" -type f -exec sed -i '' -E 's/from (main_api_generated|public_api_generated|oauth2_api_generated)\b/from ./g' {} \; 2>/dev/null || true

# Fix syntax errors from import fixes
find whitebit_sdk/http/generated -name "*.py" -type f -exec sed -i '' 's/from \. import\./from . import /g' {} \; 2>/dev/null || true

# Fix relative imports in package root files
find whitebit_sdk/http/generated -name "api_client.py" -exec sed -i '' 's/from \.\.configuration/from .configuration/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "api_client.py" -exec sed -i '' 's/from \.\.api_response/from .api_response/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "api_client.py" -exec sed -i '' 's/from \.\.exceptions/from .exceptions/g' {} \; 2>/dev/null || true

find whitebit_sdk/http/generated -name "rest.py" -exec sed -i '' 's/from \.\.exceptions/from .exceptions/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "rest.py" -exec sed -i '' 's/from \.\.configuration/from .configuration/g' {} \; 2>/dev/null || true

# Fix main __init__.py imports
find whitebit_sdk/http/generated -name "__init__.py" -not -path "*/api/*" -not -path "*/models/*" -exec sed -i '' 's/from \.\.api_response/from .api_response/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "__init__.py" -not -path "*/api/*" -not -path "*/models/*" -exec sed -i '' 's/from \.\.api_client/from .api_client/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "__init__.py" -not -path "*/api/*" -not -path "*/models/*" -exec sed -i '' 's/from \.\.configuration/from .configuration/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "__init__.py" -not -path "*/api/*" -not -path "*/models/*" -exec sed -i '' 's/from \.\.exceptions/from .exceptions/g' {} \; 2>/dev/null || true
find whitebit_sdk/http/generated -name "__init__.py" -not -path "*/api/*" -not -path "*/models/*" -exec sed -i '' 's/from \.\.models\./from .models./g' {} \; 2>/dev/null || true

echo -e "${GREEN}✓ All imports fixed${NC}"

echo -e "\n${YELLOW}📖 Next steps:${NC}"
echo -e "   1. ✅ Code generated and imports fixed automatically"
echo -e "   2. ✅ Wrapper classes ready in whitebit_sdk/http/"
echo -e "   3. Test: python3 -c 'from whitebit_sdk import WhiteBitClient; WhiteBitClient()'"

echo -e "\n${GREEN}✓ Done!${NC}"
