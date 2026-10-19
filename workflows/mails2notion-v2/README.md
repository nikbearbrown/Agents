# mails2notion V2

This folder contains the **mails2notion V2** workflow. Its executable nodes use `agent`, `airtable`, `code`, `filter`, `gmail`, `gmailTrigger`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `noOp`, `outputParserStructured`, `set`, `toolCalculator`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mails2notion-v2.json`](mails2notion-v2.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`, `openAiApi`

**Entry nodes:** Gmail Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Add Label "Processed" | `gmail` | addLabels |
| Active Routes Only | `filter` | Inspect parameters |
| Extract Route ID | `set` | Inspect parameters |
| Deactivate Route | `airtable` | update |
| Add Label "Error" | `gmail` | addLabels |
| Send notification about deactivated route | `gmail` | Inspect parameters |
| Send notification about missing route | `gmail` | Inspect parameters |
| Get Route by ID | `airtable` | get |
| Create Notion Page | `httpRequest` | POST |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Filter for unprocessed mails | `filter` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Required labels | `filter` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Format Notion Page Blocks | `code` | Inspect parameters |
| Get all labels | `gmail` | label |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Calculator1 | `toolCalculator` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Generate Actionable Task | `agent` | Inspect parameters |
| Get Summary & Meta Data | `agent` | Inspect parameters |

## Connection map

- Globals → Filter for unprocessed mails (`main`, output 0, input 0)
- Calculator → Get Summary & Meta Data (`ai_tool`, output 0, input 0)
- Calculator1 → Generate Actionable Task (`ai_tool`, output 0, input 0)
- Gmail Trigger → Globals (`main`, output 0, input 0)
- Get all labels → Required labels (`main`, output 0, input 0)
- Get Route by ID → Active Routes Only (`main`, output 0, input 0)
- Get Route by ID → No Operation, do nothing (`main`, output 1, input 0)
- Deactivate Route → Send notification about deactivated route (`main`, output 0, input 0)
- Extract Route ID → Get Route by ID (`main`, output 0, input 0)
- OpenAI Chat Model → Get Summary & Meta Data (`ai_languageModel`, output 0, input 0)
- Active Routes Only → Generate Actionable Task (`main`, output 0, input 0)
- Create Notion Page → Add Label "Processed" (`main`, output 0, input 0)
- Create Notion Page → Deactivate Route (`main`, output 1, input 0)
- OpenAI Chat Model1 → Generate Actionable Task (`ai_languageModel`, output 0, input 0)
- Get Summary & Meta Data → Format Notion Page Blocks (`main`, output 0, input 0)
- Generate Actionable Task → Get Summary & Meta Data (`main`, output 0, input 0)
- No Operation, do nothing → Send notification about missing route (`main`, output 0, input 0)
- Structured Output Parser → Get Summary & Meta Data (`ai_outputParser`, output 0, input 0)
- Format Notion Page Blocks → Create Notion Page (`main`, output 0, input 0)
- Structured Output Parser1 → Generate Actionable Task (`ai_outputParser`, output 0, input 0)
- Filter for unprocessed mails → Extract Route ID (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all labels (`main`, output 0, input 0)
- Send notification about missing route → Add Label "Error" (`main`, output 0, input 0)
- Send notification about deactivated route → Add Label "Error" (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1921_Code_Filter_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1921_Code_Filter_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
