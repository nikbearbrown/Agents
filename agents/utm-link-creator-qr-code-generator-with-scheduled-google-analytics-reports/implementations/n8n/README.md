# UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports

This folder contains the **UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports** workflow. Its executable nodes use `agent`, `airtable`, `code`, `gmail`, `googleAnalyticsTool`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports.json`](utm-link-creator-qr-code-generator-with-scheduled-google-analytics-reports.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`, `googleAnalyticsOAuth2`, `openAiApi`

**Entry nodes:** Create UTM Link & Send To Database, Schedule Google Analytics Report To Marketing Manager

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Google Analytics | `googleAnalyticsTool` | Inspect parameters |
| Create UTM Link & Send To Database | `manualTrigger` | Inspect parameters |
| Set UTM Parameters For Link | `set` | Inspect parameters |
| Create UTM Link With Parameters | `code` | Inspect parameters |
| Submit UTM Link To Database | `airtable` | upsert |
| Create QR Code With Submitted QR Link | `httpRequest` | Inspect parameters |
| Schedule Google Analytics Report To Marketing Manager | `scheduleTrigger` | Inspect parameters |
| Google Analytics Data Analysis Agent | `agent` | Inspect parameters |
| Send Summary Report To Marketing Manager | `gmail` | Inspect parameters |

## Connection map

- Google Analytics → Google Analytics Data Analysis Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model1 → Google Analytics Data Analysis Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Google Analytics Data Analysis Agent (`ai_memory`, output 0, input 0)
- Set UTM Parameters For Link → Create UTM Link With Parameters (`main`, output 0, input 0)
- Create UTM Link With Parameters → Create QR Code With Submitted QR Link (`main`, output 0, input 0)
- Create UTM Link With Parameters → Submit UTM Link To Database (`main`, output 0, input 0)
- Create UTM Link & Send To Database → Set UTM Parameters For Link (`main`, output 0, input 0)
- Google Analytics Data Analysis Agent → Send Summary Report To Marketing Manager (`main`, output 0, input 0)
- Schedule Google Analytics Report To Marketing Manager → Google Analytics Data Analysis Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1710_Code_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1710_Code_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
