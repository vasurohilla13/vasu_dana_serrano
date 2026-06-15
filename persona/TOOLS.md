# TOOLS — Dana Serrano

This file lists the tools and APIs available to agents acting on Dana's behalf.
All tool usage must comply with rules in AGENTS.md.

---

## Active Tools (required for most tasks)

### Plaid API
- **Base URL:** `$PLAID_API_URL`
- **Purpose:** Dana's authoritative bank transaction record
- **Endpoints:**
  - `GET /transactions?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` — filtered transaction list
  - `GET /balance` — current account balance
- **Authority:** Plaid amounts override receipt images when there is a discrepancy
- **Docs:** `mock_data/plaid-api/README.md`

### WhatsApp API
- **Base URL:** `$WHATSAPP_API_URL`
- **Purpose:** Read Dana's WhatsApp messages; send only with explicit approval
- **Endpoints:**
  - `GET /messages?thread=&contact=` — read messages
  - `POST /send` — **requires explicit approval in task prompt before calling**
- **Docs:** `mock_data/whatsapp-api/README.md`

---

## Distractor Tools (available but not relevant to most tasks)

### Google Drive API
- **Base URL:** `$GOOGLE_DRIVE_API_URL`
- **Purpose:** Dana's research document storage — IRB drafts, case report, rotation schedules
- **Note:** Personal finance files are NOT stored on Drive. Do not look here for receipts or budget files.
- **Docs:** `mock_data/google-drive-api/README.md`

### QuickBooks API
- **Base URL:** `$QUICKBOOKS_API_URL`
- **Purpose:** Research grant accounting only — not personal expenses
- **Docs:** `mock_data/quickbooks-api/README.md`

### Xero API
- **Base URL:** `$XERO_API_URL`
- **Note:** Dana does not have an active Xero organization
- **Docs:** `mock_data/xero-api/README.md`

### PayPal API
- **Base URL:** `$PAYPAL_API_URL`
- **Purpose:** Occasional personal purchases — not used for wedding expenses
- **Docs:** `mock_data/paypal-api/README.md`

---

## Workspace

- **Path:** `/root/.openclaw/workspace` (env: `$OPENCLAW_WORKSPACE`)
- All input files are pre-loaded here at task start
- Agent output files should be written here
- Key output files expected: `file_05.xlsx` (updated), `flagged_items.json`, `summary.md`
