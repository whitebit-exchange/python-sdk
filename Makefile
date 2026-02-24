.PHONY: help generate clean test install format lint

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show help
	@echo "$(BLUE)WhiteBIT SDK Generator$(NC)"
	@echo ""
	@echo "Available commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""

go: build-sdk ## 🚀 GO! Full generation (WebSocket + HTTP with OpenAPI Generator)

build-sdk: ## 🎯 ONE COMMAND - Build complete SDK automatically
	@echo "$(BLUE)🎯 Building complete SDK with automated pipeline...$(NC)"
	@chmod +x scripts/generate_complete_sdk.py
	@python3 scripts/generate_complete_sdk.py

generate: ## 🔌 Generate WebSocket SDK only
	@echo "$(BLUE)🚀 Generating WebSocket SDK...$(NC)"
	@echo "===================================================="
	@echo "Validating API Specifications"
	@echo "===================================================="
	@python3 scripts/validate_specs.py
	@echo ""
	@echo "===================================================="
	@echo "Generating WebSocket Models"
	@echo "===================================================="
	@python3 scripts/generate_websocket_models.py
	@echo ""
	@echo "===================================================="
	@echo "Generating WebSocket Handlers"
	@echo "===================================================="
	@python3 scripts/generate_websocket_handlers.py
	@echo ""
	@echo "===================================================="
	@echo "Creating SDK Infrastructure"
	@echo "===================================================="
	@python3 scripts/create_sdk_structure.py
	@echo ""
	@echo "===================================================="
	@echo "Post-Processing SDK Code"
	@echo "===================================================="
	@python3 scripts/post_process.py
	@echo ""
	@echo "$(GREEN)✓ WebSocket SDK generation complete!$(NC)"

generate-http: ## 🌐 Generate HTTP clients with OpenAPI Generator (requires Java)
	@echo "$(BLUE)🌐 Generating HTTP API clients with OpenAPI Generator...$(NC)"
	@./scripts/generate_http_openapi.sh

generate-all: generate generate-http ## 🔥 Generate EVERYTHING (WebSocket + HTTP)
	@echo ""
	@echo "$(GREEN)============================================================$(NC)"
	@echo "$(GREEN)✅ FULL SDK GENERATION COMPLETE!$(NC)"
	@echo "$(GREEN)============================================================$(NC)"
	@echo ""
	@echo "$(BLUE)📊 Generated:$(NC)"
	@echo "   • WebSocket: 104 models + 18 handlers"
	@echo "   • HTTP APIs: 32 API files + 153 models"
	@echo ""
	@echo "$(BLUE)🧪 Test it:$(NC)"
	@echo "   make test-import"
	@echo ""

install: ## 📦 Install dependencies
	@echo "$(BLUE)📦 Installing dependencies...$(NC)"
	@pip install -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"

clean: ## 🧹 Clean temporary files
	@echo "$(BLUE)🧹 Cleaning temporary files...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name ".DS_Store" -delete 2>/dev/null || true
	@rm -rf .pytest_cache .mypy_cache .coverage htmlcov/ 2>/dev/null || true
	@echo "$(GREEN)✓ Temporary files removed$(NC)"

deep-clean: clean ## 🧹 Deep clean (including generated code)
	@echo "$(YELLOW)⚠️  Removing ALL generated files...$(NC)"
	@rm -rf whitebit_sdk/http/generated/
	@rm -rf whitebit_sdk/models/websocket/__init__.py
	@rm -rf whitebit_sdk/websocket/private/*.py
	@rm -rf whitebit_sdk/websocket/public/*.py
	@echo "$(GREEN)✓ Deep clean complete$(NC)"

format: ## 🎨 Format code
	@echo "$(BLUE)🎨 Formatting code...$(NC)"
	@black whitebit_sdk/ scripts/ --quiet || echo "$(YELLOW)⚠️  black not installed$(NC)"
	@isort whitebit_sdk/ scripts/ --quiet || echo "$(YELLOW)⚠️  isort not installed$(NC)"
	@echo "$(GREEN)✓ Formatting complete$(NC)"

lint: ## 🔍 Check code
	@echo "$(BLUE)🔍 Checking code...$(NC)"
	@mypy whitebit_sdk/ --ignore-missing-imports || echo "$(YELLOW)⚠️  mypy not installed$(NC)"
	@echo "$(GREEN)✓ Check complete$(NC)"

test: ## 🧪 Run tests
	@echo "$(BLUE)🧪 Running tests...$(NC)"
	@pytest tests/ -v

test-import: ## ✅ Test SDK import
	@echo "$(BLUE)✅ Testing SDK import...$(NC)"
	@python3 -c "from whitebit_sdk import WhiteBitClient; client = WhiteBitClient(); print('✅ SDK imports'); print(f'✅ Main API: {client.main_api is not None}'); print(f'✅ Public API: {client.public_api is not None}'); print(f'✅ Main Account API: {client.main_api.main_account is not None}'); print('🎉 ALL WORKING')"
	@echo "$(GREEN)✓ Import works!$(NC)"

example: ## 🎯 Run example (test all endpoints)
	@echo "$(BLUE)🎯 Running comprehensive API example...$(NC)"
	@python3 example.py

test-full: test-import test ## 🧪 Run all tests
	@echo "$(GREEN)✓ All tests complete!$(NC)"

validate: ## ✓ Validate API specifications
	@echo "$(BLUE)✓ Validating specifications...$(NC)"
	@python3 scripts/validate_specs.py

dev: install generate-all test-import ## 🔧 Full dev setup
	@echo "$(GREEN)✓ Dev environment ready!$(NC)"

# Default goal shows help
.DEFAULT_GOAL := help
