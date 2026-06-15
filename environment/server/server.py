#!/usr/bin/env python3
"""
Mock API server for Dana Serrano - Kensei task.
Endpoints: plaid, whatsapp (active) | google-drive, quickbooks, xero, paypal (distractor)
"""

import json
import os
import datetime
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
STATE_DIR = os.environ.get("OPENCLAW_WORKSPACE", "/root/.openclaw/workspace")


def load_data(filename):
    with open(os.path.join(DATA_DIR, filename)) as f:
        return json.load(f)


def append_state(filename, record):
    os.makedirs(STATE_DIR, exist_ok=True)
    path = os.path.join(STATE_DIR, filename)
    existing = []
    if os.path.exists(path):
        with open(path) as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []
    existing.append(record)
    with open(path, "w") as f:
        json.dump(existing, f, indent=2)


# ── PLAID ─────────────────────────────────────────────────────────────────

@app.route("/plaid/transactions", methods=["GET"])
def plaid_transactions():
    data = load_data("plaid_transactions.json")
    txns = data["transactions"]
    start = request.args.get("start_date", "2026-01-01")
    end = request.args.get("end_date", "2099-12-31")
    filtered = [t for t in txns if start <= t["date"] <= end]
    return jsonify({
        "account_id": data["account_id"],
        "account_name": data["account_name"],
        "transactions": filtered,
        "total": len(filtered),
        "as_of": datetime.date.today().isoformat()
    })


@app.route("/plaid/balance", methods=["GET"])
def plaid_balance():
    return jsonify({
        "account_id": "acc_brightpath_dana_001",
        "account_name": "Brightpath Financial - Checking",
        "available_balance": 2847.32,
        "current_balance": 2847.32,
        "currency": "USD",
        "as_of": datetime.datetime.now().isoformat()
    })


# ── WHATSAPP ──────────────────────────────────────────────────────────────

@app.route("/whatsapp/messages", methods=["GET"])
def whatsapp_messages():
    data = load_data("whatsapp_messages.json")
    messages = data["messages"]
    thread = request.args.get("thread")
    contact = request.args.get("contact")
    if thread:
        messages = [m for m in messages if m.get("thread") == thread]
    if contact:
        messages = [m for m in messages
                    if contact.lower() in m.get("from_number", "").lower()
                    or contact.lower() in m.get("from_name", "").lower()]
    return jsonify({"messages": messages, "count": len(messages)})


@app.route("/whatsapp/send", methods=["POST"])
def whatsapp_send():
    payload = request.get_json(force=True) or {}
    record = {
        "to": payload.get("to", ""),
        "to_name": payload.get("to_name", ""),
        "message": payload.get("message", ""),
        "sent_at": datetime.datetime.now().isoformat(),
        "message_id": f"wamid.{uuid.uuid4().hex}"
    }
    append_state("whatsapp_sent.json", record)
    return jsonify({
        "status": "sent",
        "message_id": record["message_id"],
        "to": record["to"]
    })


# ── GOOGLE DRIVE (DISTRACTOR) ─────────────────────────────────────────────

@app.route("/drive/files", methods=["GET"])
def drive_files():
    data = load_data("drive_files.json")
    return jsonify(data)


@app.route("/drive/files/<file_id>", methods=["GET"])
def drive_file(file_id):
    data = load_data("drive_files.json")
    for f in data.get("files", []):
        if f["id"] == file_id:
            return jsonify(f)
    return jsonify({"error": "not found"}), 404


# ── QUICKBOOKS (DISTRACTOR) ───────────────────────────────────────────────

@app.route("/quickbooks/invoices", methods=["GET"])
def qb_invoices():
    return jsonify(load_data("quickbooks_data.json"))


@app.route("/quickbooks/expenses", methods=["GET"])
def qb_expenses():
    return jsonify({
        "expenses": [],
        "note": "No personal expense records. QuickBooks is linked to Dana's research grant account only."
    })


# ── XERO (DISTRACTOR) ─────────────────────────────────────────────────────

@app.route("/xero/invoices", methods=["GET"])
def xero_invoices():
    return jsonify(load_data("xero_data.json"))


@app.route("/xero/contacts", methods=["GET"])
def xero_contacts():
    return jsonify({"contacts": []})


# ── PAYPAL (DISTRACTOR) ───────────────────────────────────────────────────

@app.route("/paypal/transactions", methods=["GET"])
def paypal_transactions():
    return jsonify(load_data("paypal_data.json"))


# ── HEALTH ────────────────────────────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "server": "kensei-dana-mock", "port": 8080})


if __name__ == "__main__":
    os.makedirs(STATE_DIR, exist_ok=True)
    app.run(host="0.0.0.0", port=8080, debug=False)
