# ... or watch set up video [10 min]

This folder contains the **... or watch set up video [10 min]** workflow. Its executable nodes use `httpRequest`, `if`, `openAi`, `postgres`, `postgresTool`, `set`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`or-watch-set-up-video-10-min.json`](or-watch-set-up-video-10-min.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `postgres`, `supabaseApi`

**Entry nodes:** Scenario 2 Start - Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI1 | `openAi` | assistant |
| Insert Transcription Part | `postgres` | executeQuery |
| Create Note | `postgresTool` | executeQuery |
| Create Recall bot | `httpRequest` | POST |
| Create OpenAI thread | `httpRequest` | POST |
| Create data record | `supabase` | Inspect parameters |
| Scenario 1 Start - Edit Fields | `set` | Inspect parameters |
| Scenario 2 Start - Webhook | `webhook` | Inspect parameters |
| If Jimmy word | `if` | Inspect parameters |

## Connection map

- Create Note → OpenAI1 (`ai_tool`, output 0, input 0)
- If Jimmy word → OpenAI1 (`main`, output 0, input 0)
- Create Recall bot → Create OpenAI thread (`main`, output 0, input 0)
- Create OpenAI thread → Create data record (`main`, output 0, input 0)
- Insert Transcription Part → If Jimmy word (`main`, output 0, input 0)
- Scenario 2 Start - Webhook → Insert Transcription Part (`main`, output 0, input 0)
- Scenario 1 Start - Edit Fields → Create Recall bot (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 5}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/0666_Postgres_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/0666_Postgres_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
