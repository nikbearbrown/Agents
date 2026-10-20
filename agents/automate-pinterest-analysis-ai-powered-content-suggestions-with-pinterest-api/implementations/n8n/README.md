# Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API

This folder contains the **Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API** workflow. Its executable nodes use `agent`, `airtable`, `airtableTool`, `chainSummarization`, `code`, `gmail`, `httpRequest`, `lmChatOpenAi`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automate-pinterest-analysis-ai-powered-content-suggestions-with-pinterest-api.json`](automate-pinterest-analysis-ai-powered-content-suggestions-with-pinterest-api.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`, `openAiApi`

**Entry nodes:** 8:00am Morning Scheduled Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Airtable2 | `airtableTool` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| 8:00am Morning Scheduled Trigger | `scheduleTrigger` | Inspect parameters |
| Pull List of Pinterest Pins From Account | `httpRequest` | Inspect parameters |
| Update Data Field To Include Organic | `code` | Inspect parameters |
| Create Record Within Pinterest Data Table | `airtable` | upsert |
| Pinterest Analysis AI Agent | `agent` | Inspect parameters |
| Pinterest Data Analysis Summary LLM | `chainSummarization` | Inspect parameters |
| Send Marketing Trends & Pinterest Analysis To Marketing Manager | `gmail` | Inspect parameters |

## Connection map

- Airtable2 → Pinterest Analysis AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Pinterest Analysis AI Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Pinterest Data Analysis Summary LLM (`ai_languageModel`, output 0, input 0)
- Pinterest Analysis AI Agent → Pinterest Data Analysis Summary LLM (`main`, output 0, input 0)
- 8:00am Morning Scheduled Trigger → Pull List of Pinterest Pins From Account (`main`, output 0, input 0)
- Pinterest Data Analysis Summary LLM → Send Marketing Trends & Pinterest Analysis To Marketing Manager (`main`, output 0, input 0)
- Update Data Field To Include Organic → Create Record Within Pinterest Data Table (`main`, output 0, input 0)
- Update Data Field To Include Organic → Pinterest Analysis AI Agent (`main`, output 0, input 0)
- Pull List of Pinterest Pins From Account → Update Data Field To Include Organic (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1331_Code_Schedule_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1331_Code_Schedule_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
