#!/usr/bin/env bash
# Entrypoint: starts the mock API server then hands off to the agent runner

set -euo pipefail

echo "[entrypoint] Starting mock API server..."
cd /app/server
python server.py &
SERVER_PID=$!

# Wait for server to be ready
for i in $(seq 1 15); do
    if curl -sf http://localhost:8080/health > /dev/null 2>&1; then
        echo "[entrypoint] Mock API server ready on port 8080"
        break
    fi
    sleep 1
done

echo "[entrypoint] Workspace contents:"
ls -la "$OPENCLAW_WORKSPACE/"

echo "[entrypoint] Environment API URLs:"
echo "  PLAID_API_URL=$PLAID_API_URL"
echo "  WHATSAPP_API_URL=$WHATSAPP_API_URL"
echo "  GOOGLE_DRIVE_API_URL=$GOOGLE_DRIVE_API_URL"
echo "  QUICKBOOKS_API_URL=$QUICKBOOKS_API_URL"
echo "  XERO_API_URL=$XERO_API_URL"
echo "  PAYPAL_API_URL=$PAYPAL_API_URL"

# Hand off to agent or keep server alive for eval harness
exec "$@"
