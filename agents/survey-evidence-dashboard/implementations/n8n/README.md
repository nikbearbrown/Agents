# My workflow 5

This folder contains the **My workflow 5** workflow. Its executable nodes use `code`, `cron`, `extractFromFile`, `httpRequest`, `mySql`, `openAi`, `slack`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`survey-evidence-dashboard.json`](survey-evidence-dashboard.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mySql`, `openAiApi`

**Entry nodes:** Survey Data Webhook, Daily Survey Check

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Survey Data Webhook | `webhook` | Inspect parameters |
| Daily Survey Check | `cron` | Inspect parameters |
| Validate Survey Data | `code` | Inspect parameters |
| Clean and Preprocess Data | `code` | Inspect parameters |
| Prepare Analysis Prompt | `code` | Inspect parameters |
| Prepare Segmentation Prompt | `code` | Inspect parameters |
| Aggregate and Enrich Results | `code` | Inspect parameters |
| Prepare Slack Notification | `code` | Inspect parameters |
| Send Slack Notification | `slack` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Extract from File | `extractFromFile` | Inspect parameters |
| Message a model | `openAi` | Inspect parameters |
| Message a model1 | `openAi` | Inspect parameters |
| Update Grafana Dashboards | `httpRequest` | POST |
| Prepare Grafana Config | `code` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Code1 | `code` | Inspect parameters |
| Insert Sentiment Distribution | `mySql` | Inspect parameters |
| Insert NPS Score | `mySql` | Inspect parameters |
| Fetch UID | `httpRequest` | Inspect parameters |

## Connection map

- Survey Data Webhook → HTTP Request (`main`, output 0, input 0)
- Daily Survey Check → HTTP Request (`main`, output 0, input 0)
- Validate Survey Data → Clean and Preprocess Data (`main`, output 0, input 0)
- Clean and Preprocess Data → Prepare Analysis Prompt (`main`, output 0, input 0)
- Prepare Analysis Prompt → Message a model (`main`, output 0, input 0)
- Prepare Segmentation Prompt → Message a model1 (`main`, output 0, input 0)
- Aggregate and Enrich Results → Prepare Slack Notification (`main`, output 0, input 0)
- Aggregate and Enrich Results → Code (`main`, output 0, input 0)
- Prepare Slack Notification → Send Slack Notification (`main`, output 0, input 0)
- HTTP Request → Extract from File (`main`, output 0, input 0)
- Extract from File → Code1 (`main`, output 0, input 0)
- Message a model → Prepare Segmentation Prompt (`main`, output 0, input 0)
- Message a model1 → Aggregate and Enrich Results (`main`, output 0, input 0)
- Prepare Grafana Config → Update Grafana Dashboards (`main`, output 0, input 0)
- Code → Switch (`main`, output 0, input 0)
- Switch → Insert Sentiment Distribution (`main`, output 0, input 0)
- Switch → Insert NPS Score (`main`, output 1, input 0)
- Code1 → Validate Survey Data (`main`, output 0, input 0)
- Insert Sentiment Distribution → Fetch UID (`main`, output 0, input 0)
- Insert NPS Score → Fetch UID (`main`, output 0, input 0)
- Fetch UID → Prepare Grafana Config (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
