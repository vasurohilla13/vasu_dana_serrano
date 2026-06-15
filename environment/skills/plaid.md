# Skill: plaid

## Description
Retrieve Dana Serrano's bank transactions and account balance from Brightpath Financial via the Plaid API.

## Base URL
`$PLAID_API_URL` (e.g., http://localhost:8080/plaid)

## Endpoints

### GET /plaid/transactions
Returns all bank transactions. Filter by date range using query params.

**Query params:**
- `start_date` (YYYY-MM-DD) — optional, default 2026-01-01
- `end_date` (YYYY-MM-DD) — optional, default today

**Example:**
```bash
curl "$PLAID_API_URL/transactions?start_date=2026-09-01&end_date=2026-10-12"
```

**Response fields per transaction:**
- `transaction_id` — unique ID
- `date` — YYYY-MM-DD
- `merchant_name` — name as it appears on the statement
- `amount` — positive = debit (money out), negative = credit (money in)
- `category` — spending category
- `pending` — bool

### GET /plaid/balance
Returns current account balance.

**Example:**
```bash
curl "$PLAID_API_URL/balance"
```

## Notes
- Plaid is the authoritative source for transaction amounts. If a receipt image shows a different amount than Plaid, use the Plaid amount and flag the discrepancy.
- Income and transfer transactions have negative amounts (credits into the account).
