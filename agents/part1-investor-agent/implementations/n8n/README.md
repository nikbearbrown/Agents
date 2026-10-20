# Part1 -Investor_ Agent

This folder contains the **Part1 -Investor_ Agent** workflow. Its executable nodes use `code`, `postgres`, `respondToWebhook`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`part1-investor-agent.json`](part1-investor-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`

**Entry nodes:** Webhook - Chat Interface

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook - Chat Interface | `webhook` | Inspect parameters |
| Parse User Question | `code` | Inspect parameters |
| DB - Get Recent Deals | `postgres` | executeQuery |
| Format Chatbot Response | `code` | Inspect parameters |
| Send Response | `respondToWebhook` | Inspect parameters |
| Get top investor | `postgres` | executeQuery |
| Route by Query Type  | `switch` | Inspect parameters |
| Investor Profile SQL node | `postgres` | executeQuery |
| Startup Investors SQL node | `postgres` | executeQuery |

## Connection map

- Webhook - Chat Interface → Parse User Question (`main`, output 0, input 0)
- Parse User Question → Route by Query Type  (`main`, output 0, input 0)
- DB - Get Recent Deals → Format Chatbot Response (`main`, output 0, input 0)
- Format Chatbot Response → Send Response (`main`, output 0, input 0)
- Get top investor → Format Chatbot Response (`main`, output 0, input 0)
- Route by Query Type  → Get top investor (`main`, output 0, input 0)
- Route by Query Type  → DB - Get Recent Deals (`main`, output 1, input 0)
- Route by Query Type  → Investor Profile SQL node (`main`, output 2, input 0)
- Route by Query Type  → Startup Investors SQL node (`main`, output 3, input 0)
- Investor Profile SQL node → Format Chatbot Response (`main`, output 0, input 0)
- Startup Investors SQL node → Format Chatbot Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
