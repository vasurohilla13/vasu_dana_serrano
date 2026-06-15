#!/usr/bin/env bash
# Verifier entry point for dana_serrano_wedding_receipts_001

set -euo pipefail

WORKSPACE="${OPENCLAW_WORKSPACE:-/root/.openclaw/workspace}"
TESTS_DIR="$(dirname "$0")"

echo "=== Kensei Task Verifier: dana_serrano_wedding_receipts_001 ==="
echo "Workspace: $WORKSPACE"
echo ""

# Install test dependencies if needed
pip install openpyxl pytest --quiet 2>/dev/null || true

# Run pytest
echo "--- Running deterministic assertions ---"
cd "$TESTS_DIR"
pytest test_outputs.py -v --tb=short

echo ""
echo "--- Verification complete ---"
