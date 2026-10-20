# Reply draft with OpenAI Assistant

This folder contains the **Reply draft with OpenAI Assistant** workflow. Its executable nodes use `code`, `gmail`, `httpRequest`, `limit`, `markdown`, `openAi`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`reply-draft-with-openai-assistant.json`](reply-draft-with-openai-assistant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Schedule trigger (1 min)

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Remove AI label from email | `gmail` | thread / removeLabels |
| Add email draft to thread | `httpRequest` | POST |
| Convert raw to base64 | `code` | Inspect parameters |
| Build email raw | `set` | Inspect parameters |
| Convert response to HTML | `markdown` | Inspect parameters |
| Map fields for further processing | `set` | Inspect parameters |
| Ask OpenAI Assistant | `openAi` | assistant |
| Get single message content | `gmail` | get |
| Return last message in thread | `limit` | Inspect parameters |
| Get thread messages | `gmail` | thread / get |
| Loop over threads | `splitInBatches` | Inspect parameters |
| Get threads with specific labels | `gmail` | thread |
| Schedule trigger (1 min) | `scheduleTrigger` | Inspect parameters |

## Connection map

- Build email raw → Convert raw to base64 (`main`, output 0, input 0)
- Loop over threads → Get single message content (`main`, output 0, input 0)
- Loop over threads → Get thread messages (`main`, output 1, input 0)
- Get thread messages → Return last message in thread (`main`, output 0, input 0)
- Ask OpenAI Assistant → Map fields for further processing (`main`, output 0, input 0)
- Convert raw to base64 → Add email draft to thread (`main`, output 0, input 0)
- Convert response to HTML → Build email raw (`main`, output 0, input 0)
- Schedule trigger (1 min) → Get threads with specific labels (`main`, output 0, input 0)
- Add email draft to thread → Remove AI label from email (`main`, output 0, input 0)
- Get single message content → Ask OpenAI Assistant (`main`, output 0, input 0)
- Return last message in thread → Loop over threads (`main`, output 0, input 0)
- Get threads with specific labels → Loop over threads (`main`, output 0, input 0)
- Map fields for further processing → Convert response to HTML (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0473_Limit_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0473_Limit_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
