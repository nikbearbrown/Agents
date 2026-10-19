# modelo do chatbot

This folder contains the **modelo do chatbot** workflow. Its executable nodes use `chatTrigger`, `if`, `memoryPostgresChat`, `mySqlTool`, `openAi`, `set`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`modelo-do-chatbot.json`](modelo-do-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`, `openAiApi`, `postgres`

**Entry nodes:** Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If | `if` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |
| OpenAI | `openAi` | assistant |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| Postgres Chat Memory1 | `memoryPostgresChat` | Inspect parameters |
| Products in Daatabase | `mySqlTool` | executeQuery |
| Knowledge Base | `toolHttpRequest` | Inspect parameters |
| External API | `toolHttpRequest` | POST |
| OpenAI2 | `openAi` | assistant |

## Connection map

- If → Edit Fields1 (`main`, output 0, input 0)
- If → OpenAI2 (`main`, output 1, input 0)
- OpenAI → Edit Fields2 (`main`, output 0, input 0)
- Chat Trigger → If (`main`, output 0, input 0)
- Edit Fields1 → OpenAI (`main`, output 0, input 0)
- Edit Fields2 → OpenAI2 (`main`, output 0, input 0)
- External API → OpenAI2 (`ai_tool`, output 0, input 0)
- Knowledge Base → OpenAI2 (`ai_tool`, output 0, input 0)
- Postgres Chat Memory → OpenAI2 (`ai_memory`, output 0, input 0)
- Postgres Chat Memory1 → OpenAI (`ai_memory`, output 0, input 0)
- Products in Daatabase → OpenAI2 (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mysqltool/1372_Mysqltool_Stickynote_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mysqltool/1372_Mysqltool_Stickynote_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
