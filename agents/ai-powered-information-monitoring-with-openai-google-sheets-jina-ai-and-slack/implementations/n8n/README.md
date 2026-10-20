# AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack

This folder contains the **AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack** workflow. Its executable nodes use `chainLlm`, `code`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `noOp`, `rssFeedRead`, `scheduleTrigger`, `set`, `slack`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-information-monitoring-with-openai-google-sheets-jina-ai-and-slack.json`](ai-powered-information-monitoring-with-openai-google-sheets-jina-ai-and-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `openAiApi`, `slackOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| RSS Read | `rssFeedRead` | Inspect parameters |
| Relevance Classification for Topic Monitoring | `textClassifier` | Inspect parameters |
| Google Sheets - Get RSS Feed url followed | `googleSheets` | Inspect parameters |
| Slack1 | `slack` | Inspect parameters |
| Google Sheets - Get article monitored database | `googleSheets` | Inspect parameters |
| Code | `code` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| If | `if` | Inspect parameters |
| Jina AI - Read URL | `httpRequest` | Inspect parameters |
| Set field - existing_url | `set` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Set fields - Not relevant articles | `set` | Inspect parameters |
| Google Sheets - Add relevant articles | `googleSheets` | append |
| Google Sheets - Add relevant article | `googleSheets` | append |
| Set Fields - Relevant Articles | `set` | Inspect parameters |

## Connection map

- If → Relevance Classification for Topic Monitoring (`main`, output 0, input 0)
- If → No Operation, do nothing (`main`, output 1, input 0)
- Code → If (`main`, output 0, input 0)
- RSS Read → Code (`main`, output 0, input 0)
- Basic LLM Chain → Slack1 (`main`, output 0, input 0)
- Basic LLM Chain → Set Fields - Relevant Articles (`main`, output 0, input 0)
- Schedule Trigger → Google Sheets - Get article monitored database (`main`, output 0, input 0)
- OpenAI Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Jina AI - Read URL → Basic LLM Chain (`main`, output 0, input 0)
- OpenAI Chat Model1 → Relevance Classification for Topic Monitoring (`ai_languageModel`, output 0, input 0)
- Set field - existing_url → Google Sheets - Get RSS Feed url followed (`main`, output 0, input 0)
- Set Fields - Relevant Articles → Google Sheets - Add relevant article (`main`, output 0, input 0)
- Set fields - Not relevant articles → Google Sheets - Add relevant articles (`main`, output 0, input 0)
- Google Sheets - Get RSS Feed url followed → RSS Read (`main`, output 0, input 0)
- Relevance Classification for Topic Monitoring → Jina AI - Read URL (`main`, output 0, input 0)
- Relevance Classification for Topic Monitoring → Set fields - Not relevant articles (`main`, output 1, input 0)
- Google Sheets - Get article monitored database → Set field - existing_url (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1281_Code_Schedule_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1281_Code_Schedule_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
