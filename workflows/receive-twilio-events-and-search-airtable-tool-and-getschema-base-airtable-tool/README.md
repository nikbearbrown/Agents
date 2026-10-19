# receive twilio events and search airtable tool and getschema base airtable tool

This folder contains the **receive twilio events and search airtable tool and getschema base airtable tool** workflow. Its executable nodes use `agent`, `airtable`, `airtableTool`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `twilio`, `twilioTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-twilio-events-and-search-airtable-tool-and-getschema-base-airtable-tool.json`](receive-twilio-events-and-search-airtable-tool-and-getschema-base-airtable-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`, `twilioApi`

**Entry nodes:** Twilio Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Twilio Trigger | `twilioTrigger` | Inspect parameters |
| Search Available Courses | `airtableTool` | search |
| Get Course Database Schema | `airtableTool` | base / getSchema |
| Get User Message | `set` | Inspect parameters |
| Send SMS reply | `twilio` | Inspect parameters |
| Append to Call Log | `airtable` | create |
| Course Assistant Agent | `agent` | Inspect parameters |
| Get List of Professors | `airtableTool` | search |
| Get List of Departments | `airtableTool` | search |
| Model | `lmChatOpenAi` | Inspect parameters |
| Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Model → Course Assistant Agent (`ai_languageModel`, output 0, input 0)
- Memory → Course Assistant Agent (`ai_memory`, output 0, input 0)
- Twilio Trigger → Get User Message (`main`, output 0, input 0)
- Get User Message → Course Assistant Agent (`main`, output 0, input 0)
- Append to Call Log → Send SMS reply (`main`, output 0, input 0)
- Course Assistant Agent → Append to Call Log (`main`, output 0, input 0)
- Get List of Professors → Course Assistant Agent (`ai_tool`, output 0, input 0)
- Get List of Departments → Course Assistant Agent (`ai_tool`, output 0, input 0)
- Search Available Courses → Course Assistant Agent (`ai_tool`, output 0, input 0)
- Get Course Database Schema → Course Assistant Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Twilio/0841_Twilio_Stickynote_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Twilio/0841_Twilio_Stickynote_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
