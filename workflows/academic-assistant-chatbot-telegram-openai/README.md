# Academic Assistant Chatbot (Telegram + OpenAI)

This folder contains the **Academic Assistant Chatbot (Telegram + OpenAI)** workflow. Its executable nodes use `noOp`, `stopAndError`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`academic-assistant-chatbot-telegram-openai.json`](academic-assistant-chatbot-telegram-openai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| OpenAI Chat Model | `noOp` | Inspect parameters |
| Academic Assistant AI Agent | `noOp` | Inspect parameters |
| Send Telegram Response | `telegram` | Inspect parameters |
| Error Handler | `stopAndError` | Inspect parameters |

## Connection map

- 20a2d959-5412-447b-a2c4-7736b6b758b3 → error-handler-20a2d959-5412-447b-a2c4-7736b6b758b3-d3388f15 (`main`, output 0, input 0)
- 8b30f207-8204-4548-8f51-38c387d98ae9 → error-handler-8b30f207-8204-4548-8f51-38c387d98ae9-061eba47 (`main`, output 0, input 0)
- 15bb5fd5-7dfe-4da9-830c-e1d905831640 → error-handler-15bb5fd5-7dfe-4da9-830c-e1d905831640-68c06fa7 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_source": 3, "missing_connection_target": 3}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/Academic Assistant Chatbot (Telegram + OpenAI).json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/Academic Assistant Chatbot (Telegram + OpenAI).json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
