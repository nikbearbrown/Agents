# spy tool

This folder contains the **spy tool** workflow. Its executable nodes use `agent`, `code`, `formTrigger`, `gmailTool`, `httpRequest`, `lmChatOpenAi`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`spy-tool.json`](spy-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `httpBasicAuth`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** New espionage assignment

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Gmail | `gmailTool` | Inspect parameters |
| parse results | `code` | Inspect parameters |
| convert message to website url & instruction | `httpRequest` | POST |
| New espionage assignment | `formTrigger` | Inspect parameters |
| wait 1 day | `wait` | Inspect parameters |
| scrape page - 1 | `httpRequest` | POST |
| scrape page - 2 | `httpRequest` | POST |
| send e-mail? | `agent` | Inspect parameters |

## Connection map

- Gmail → send e-mail? (`ai_tool`, output 0, input 0)
- wait 1 day → scrape page - 2 (`main`, output 0, input 0)
- send e-mail? → scrape page - 1 (`main`, output 0, input 0)
- parse results → scrape page - 1 (`main`, output 0, input 0)
- scrape page - 1 → wait 1 day (`main`, output 0, input 0)
- scrape page - 2 → send e-mail? (`main`, output 0, input 0)
- OpenAI Chat Model → send e-mail? (`ai_languageModel`, output 0, input 0)
- New espionage assignment → convert message to website url & instruction (`main`, output 0, input 0)
- convert message to website url & instruction → parse results (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1801_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1801_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
