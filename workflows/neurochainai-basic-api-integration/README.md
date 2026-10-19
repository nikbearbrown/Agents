# NeurochainAI Basic API Integration

This folder contains the **NeurochainAI Basic API Integration** workflow. Its executable nodes use `code`, `httpRequest`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`neurochainai-basic-api-integration.json`](neurochainai-basic-api-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Code | `code` | Inspect parameters |
| HTTP Request3 | `httpRequest` | Inspect parameters |
| Telegram2 | `telegram` | Inspect parameters |
| Telegram1 | `telegram` | sendPhoto |
| Telegram4 | `telegram` | deleteMessage |
| Telegram3 | `telegram` | Inspect parameters |
| Telegram5 | `telegram` | deleteMessage |
| Telegram6 | `telegram` | Inspect parameters |
| Telegram7 | `telegram` | deleteMessage |
| NeurochainAI - REST API | `httpRequest` | POST |
| TYPING - ACTION | `telegram` | sendChatAction |
| AI Response | `telegram` | Inspect parameters |
| No response | `telegram` | Inspect parameters |
| Prompt too short | `telegram` | Inspect parameters |
| Switch2 | `switch` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| NeurochainAI - Flux | `httpRequest` | POST |
| Switch1 | `switch` | Inspect parameters |

## Connection map

- Code → HTTP Request3 (`main`, output 0, input 0)
- Code1 → Telegram2 (`main`, output 0, input 0)
- Switch → Code1 (`main`, output 0, input 0)
- Switch → TYPING - ACTION (`main`, output 1, input 0)
- Switch → TYPING - ACTION (`main`, output 2, input 0)
- Switch1 → Telegram6 (`main`, output 0, input 0)
- Switch1 → Telegram3 (`main`, output 1, input 0)
- Switch2 → No response (`main`, output 0, input 0)
- Switch2 → Prompt too short (`main`, output 1, input 0)
- Telegram1 → Telegram4 (`main`, output 0, input 0)
- Telegram2 → NeurochainAI - Flux (`main`, output 0, input 0)
- Telegram3 → Telegram5 (`main`, output 0, input 0)
- Telegram6 → Telegram7 (`main`, output 0, input 0)
- HTTP Request3 → Telegram1 (`main`, output 0, input 0)
- TYPING - ACTION → NeurochainAI - REST API (`main`, output 0, input 0)
- Telegram Trigger → Switch (`main`, output 0, input 0)
- NeurochainAI - Flux → Code (`main`, output 0, input 0)
- NeurochainAI - Flux → Switch1 (`main`, output 1, input 0)
- NeurochainAI - REST API → AI Response (`main`, output 0, input 0)
- NeurochainAI - REST API → Switch2 (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1631_HTTP_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1631_HTTP_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
