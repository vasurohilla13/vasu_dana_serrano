# Skill: whatsapp

## Description
Read and send WhatsApp messages for Dana Serrano. Sending requires explicit approval per AGENTS.md rules.

## Base URL
`$WHATSAPP_API_URL` (e.g., http://localhost:8080/whatsapp)

## Endpoints

### GET /whatsapp/messages
Returns all messages across all threads.

**Query params:**
- `thread` — filter by thread/contact name (e.g., "Val Serrano")
- `contact` — filter by contact name or number

**Example:**
```bash
curl "$WHATSAPP_API_URL/messages"
curl "$WHATSAPP_API_URL/messages?thread=Val+Serrano"
```

### POST /whatsapp/send
Send a WhatsApp message. This action is IRREVERSIBLE and triggers AGENTS.md confirmation rules.

**WARNING:** Per AGENTS.md — never send messages to family contacts (Mama, Papa, Val, Marco, Abuelita, Tia Lupe) without explicit send approval from Dana. Drafts are allowed, sending is NOT without a go-ahead.

**Body:**
```json
{
  "to": "+14155550525",
  "to_name": "Val",
  "message": "text here"
}
```

## Notes
- Reading messages is always permitted.
- Sending to any contact requires explicit confirmation from Dana before calling POST /whatsapp/send.
