# What-If Simulation Agent

This folder contains the **What-If Simulation Agent** workflow. Its executable nodes use `code`, `httpRequest`, `postgres`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`what-if-simulation-agent.json`](what-if-simulation-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`, `postgres`

**Entry nodes:** 🎯 Webhook — Receive Simulation Request

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| 🎯 Webhook — Receive Simulation Request | `webhook` | Inspect parameters |
| 🔍 Parse & Validate Input | `code` | Inspect parameters |
| 📈 Sim 1 — Growth vs Sentiment Tradeoff | `code` | Inspect parameters |
| ⚖️ Sim 2 — Risk Appetite Simulator | `code` | Inspect parameters |
| 🎯 Sim 3 — Threshold Break Simulator | `code` | Inspect parameters |
| 🧠 Aggregate & Score All Simulations | `code` | Inspect parameters |
| 🤖 Groq — Generate Investment Insights | `httpRequest` | POST |
| 🔄 Parse Groq Response | `code` | Inspect parameters |
| 🗄️ Prepare DB Record | `code` | Inspect parameters |
| 💾 Save to PostgreSQL | `postgres` | executeQuery |
| 📊 Build Final Response | `code` | Inspect parameters |
| ✅ Respond to Webhook | `respondToWebhook` | Inspect parameters |
| 📝 Build AI Prompt | `code` | Inspect parameters |

## Connection map

- 🎯 Webhook — Receive Simulation Request → 🔍 Parse & Validate Input (`main`, output 0, input 0)
- 🔍 Parse & Validate Input → 📈 Sim 1 — Growth vs Sentiment Tradeoff (`main`, output 0, input 0)
- 📈 Sim 1 — Growth vs Sentiment Tradeoff → ⚖️ Sim 2 — Risk Appetite Simulator (`main`, output 0, input 0)
- ⚖️ Sim 2 — Risk Appetite Simulator → 🎯 Sim 3 — Threshold Break Simulator (`main`, output 0, input 0)
- 🎯 Sim 3 — Threshold Break Simulator → 🧠 Aggregate & Score All Simulations (`main`, output 0, input 0)
- 🧠 Aggregate & Score All Simulations → 📝 Build AI Prompt (`main`, output 0, input 0)
- 🤖 Groq — Generate Investment Insights → 🔄 Parse Groq Response (`main`, output 0, input 0)
- 🔄 Parse Groq Response → 🗄️ Prepare DB Record (`main`, output 0, input 0)
- 🗄️ Prepare DB Record → 💾 Save to PostgreSQL (`main`, output 0, input 0)
- 💾 Save to PostgreSQL → 📊 Build Final Response (`main`, output 0, input 0)
- 📊 Build Final Response → ✅ Respond to Webhook (`main`, output 0, input 0)
- 📝 Build AI Prompt → 🤖 Groq — Generate Investment Insights (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
