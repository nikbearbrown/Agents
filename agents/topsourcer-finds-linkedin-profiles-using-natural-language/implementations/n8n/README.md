# TopSourcer - Finds LinkedIn Profiles using natural language

This folder contains the **TopSourcer - Finds LinkedIn Profiles using natural language** workflow. Its executable nodes use `chatTrigger`, `code`, `googleSheets`, `httpRequest`, `if`, `openAi`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`topsourcer-finds-linkedin-profiles-using-natural-language.json`](topsourcer-finds-linkedin-profiles-using-natural-language.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Wait | `wait` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Create a new sheet | `googleSheets` | create |
| Add columns to new sheet | `googleSheets` | append |
| set page number for google search | `code` | Inspect parameters |
| Extracts all linkedin urls from the google http response | `code` | Inspect parameters |
| Google Boolean Search | `httpRequest` | Inspect parameters |
| Generate a Boolean Search String | `openAi` | Inspect parameters |
| If desired results not reached | `if` | Inspect parameters |
| Appends the results to the sheet | `googleSheets` | append |
| Adds 10 to start - Go to next page | `code` | Inspect parameters |
| Columns to add | `code` | Inspect parameters |

## Connection map

- Wait → Google Boolean Search (`main`, output 0, input 0)
- Columns to add → Add columns to new sheet (`main`, output 0, input 0)
- Create a new sheet → Columns to add (`main`, output 0, input 0)
- Google Boolean Search → Extracts all linkedin urls from the google http response (`main`, output 0, input 0)
- Add columns to new sheet → set page number for google search (`main`, output 0, input 0)
- When chat message received → Generate a Boolean Search String (`main`, output 0, input 0)
- If desired results not reached → Wait (`main`, output 0, input 0)
- Appends the results to the sheet → Adds 10 to start - Go to next page (`main`, output 0, input 0)
- Generate a Boolean Search String → Create a new sheet (`main`, output 0, input 0)
- set page number for google search → If desired results not reached (`main`, output 0, input 0)
- Adds 10 to start - Go to next page → If desired results not reached (`main`, output 0, input 0)
- Extracts all linkedin urls from the google http response → Appends the results to the sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1717_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1717_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
