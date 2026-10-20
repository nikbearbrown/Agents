# Orchestrator v2 - Enhanced

This folder contains the **Orchestrator v2 - Enhanced** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `emailSend`, `httpRequest`, `if`, `lmChatOllama`, `n8nDataStore`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`orchestrator-v2-enhanced.json`](orchestrator-v2-enhanced.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |
| The Brain | `chainLlm` | Inspect parameters |
| The Processor | `code` | Inspect parameters |
| The Router | `httpRequest` | Inspect parameters |
| Response Processor | `code` | Inspect parameters |
| Store Request Log | `n8nDataStore` | create |
| Store Analytics | `n8nDataStore` | create |
| Check for Email | `if` | Inspect parameters |
| Send Notification | `emailSend` | Inspect parameters |
| Generate Summary | `code` | Inspect parameters |

## Connection map

- Ollama Chat Model → The Brain (`ai_languageModel`, output 0, input 0)
- When chat message received → The Brain (`main`, output 0, input 0)
- The Brain → The Processor (`main`, output 0, input 0)
- The Processor → The Router (`main`, output 0, input 0)
- The Router → Response Processor (`main`, output 0, input 0)
- Response Processor → Store Request Log (`main`, output 0, input 0)
- Response Processor → Store Analytics (`main`, output 0, input 0)
- Store Request Log → Check for Email (`main`, output 0, input 0)
- Check for Email → Send Notification (`main`, output 0, input 0)
- Check for Email → Generate Summary (`main`, output 1, input 0)
- Send Notification → Generate Summary (`main`, output 0, input 0)
- Store Analytics → Check for Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
