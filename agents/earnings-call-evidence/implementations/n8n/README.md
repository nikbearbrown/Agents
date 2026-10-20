# My workflow 7

This folder contains the **My workflow 7** workflow. Its executable nodes use `code`, `httpRequest`, `postgres`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`earnings-call-evidence.json`](earnings-call-evidence.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`, `httpHeaderAuth`, `postgres`

**Entry nodes:** Webhook: Receive Transcript

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook: Receive Transcript | `webhook` | Inspect parameters |
| Validate Input | `code` | Inspect parameters |
| DB: Insert earnings_call | `postgres` | executeQuery |
| Set Call Context | `set` | Inspect parameters |
| Process Section Response | `code` | Inspect parameters |
| DB: Insert transcript_section | `postgres` | executeQuery |
| Route by Section Type | `switch` | Inspect parameters |
| Process Guidance Response | `code` | Inspect parameters |
| Process Risk Response | `code` | Inspect parameters |
| Process QA Response | `code` | Inspect parameters |
| DB: Insert guidance_signal | `postgres` | executeQuery |
| DB: Insert risk_admission | `postgres` | executeQuery |
| DB: Insert qa_pressure | `postgres` | executeQuery |
| DB: Log Agent Run | `postgres` | executeQuery |
| Fetch All Signals for Summary | `postgres` | executeQuery |
| Process Summary Response | `code` | Inspect parameters |
| DB: Insert call_summary | `postgres` | executeQuery |
| DB: Mark Call Complete | `postgres` | executeQuery |
| Final Response | `code` | Inspect parameters |
| Webhook Response | `respondToWebhook` | Inspect parameters |
| Groq: Generate Call Summary | `httpRequest` | POST |
| Groq: Parse Transcript Sections | `httpRequest` | POST |
| Groq: Extract Guidance Signals | `httpRequest` | POST |
| Groq: Extract Risk Admissions | `httpRequest` | POST |
| Groq: Map QA Pressure | `httpRequest` | POST |
| Execute a SQL query | `postgres` | executeQuery |

## Connection map

- Webhook: Receive Transcript → Validate Input (`main`, output 0, input 0)
- Validate Input → DB: Insert earnings_call (`main`, output 0, input 0)
- DB: Insert earnings_call → Set Call Context (`main`, output 0, input 0)
- Set Call Context → Groq: Parse Transcript Sections (`main`, output 0, input 0)
- Process Section Response → DB: Insert transcript_section (`main`, output 0, input 0)
- DB: Insert transcript_section → Route by Section Type (`main`, output 0, input 0)
- Route by Section Type → Groq: Extract Guidance Signals (`main`, output 0, input 0)
- Route by Section Type → Groq: Extract Risk Admissions (`main`, output 0, input 0)
- Route by Section Type → Groq: Map QA Pressure (`main`, output 1, input 0)
- Route by Section Type → Groq: Extract Risk Admissions (`main`, output 2, input 0)
- Route by Section Type → Groq: Extract Guidance Signals (`main`, output 2, input 0)
- Process Guidance Response → DB: Insert guidance_signal (`main`, output 0, input 0)
- Process Risk Response → DB: Insert risk_admission (`main`, output 0, input 0)
- Process QA Response → DB: Insert qa_pressure (`main`, output 0, input 0)
- DB: Insert guidance_signal → DB: Log Agent Run (`main`, output 0, input 0)
- DB: Insert risk_admission → DB: Log Agent Run (`main`, output 0, input 0)
- DB: Insert qa_pressure → DB: Log Agent Run (`main`, output 0, input 0)
- DB: Log Agent Run → Fetch All Signals for Summary (`main`, output 0, input 0)
- Fetch All Signals for Summary → Groq: Generate Call Summary (`main`, output 0, input 0)
- Process Summary Response → DB: Insert call_summary (`main`, output 0, input 0)
- DB: Insert call_summary → DB: Mark Call Complete (`main`, output 0, input 0)
- DB: Mark Call Complete → Final Response (`main`, output 0, input 0)
- Final Response → Webhook Response (`main`, output 0, input 0)
- Groq: Generate Call Summary → Process Summary Response (`main`, output 0, input 0)
- Groq: Parse Transcript Sections → Process Section Response (`main`, output 0, input 0)
- Groq: Extract Guidance Signals → Process Guidance Response (`main`, output 0, input 0)
- Groq: Extract Risk Admissions → Process Risk Response (`main`, output 0, input 0)
- Groq: Map QA Pressure → Process QA Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
