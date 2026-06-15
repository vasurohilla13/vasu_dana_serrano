FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY server/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy server code and data
COPY server/ /app/server/

# Copy skills
COPY skills/ /app/skills/

# Copy personas
COPY personas/ /app/personas/

# Copy artifacts into workspace
COPY artifacts/inputs/files/ /root/.openclaw/workspace/

# Set up workspace directory
RUN mkdir -p /root/.openclaw/workspace

# Environment variables for API discovery
ENV PLAID_API_URL=http://localhost:8080/plaid
ENV WHATSAPP_API_URL=http://localhost:8080/whatsapp
ENV GOOGLE_DRIVE_API_URL=http://localhost:8080/drive
ENV QUICKBOOKS_API_URL=http://localhost:8080/quickbooks
ENV XERO_API_URL=http://localhost:8080/xero
ENV PAYPAL_API_URL=http://localhost:8080/paypal
ENV OPENCLAW_WORKSPACE=/root/.openclaw/workspace

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
