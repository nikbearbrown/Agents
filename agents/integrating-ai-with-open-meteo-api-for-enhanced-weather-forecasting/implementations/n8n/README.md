# Integrating AI with Open-Meteo API for Enhanced Weather Forecasting

This folder contains the **Integrating AI with Open-Meteo API for Enhanced Weather Forecasting** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `toolHttpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting.json`](integrating-ai-with-open-meteo-api-for-enhanced-weather-forecasting.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Generic AI Tool Agent | `agent` | Inspect parameters |
| Chat Memory Buffer | `memoryBufferWindow` | Inspect parameters |
| A tool to get the weather forecast based on geolocation | `toolHttpRequest` | Inspect parameters |
| A tool for inputting the city and obtaining geolocation | `toolHttpRequest` | Inspect parameters |

## Connection map

- OpenAI Chat Model → Generic AI Tool Agent (`ai_languageModel`, output 0, input 0)
- Chat Memory Buffer → When chat message received (`ai_memory`, output 0, input 0)
- Chat Memory Buffer → Generic AI Tool Agent (`ai_memory`, output 0, input 0)
- When chat message received → Generic AI Tool Agent (`main`, output 0, input 0)
- A tool for inputting the city and obtaining geolocation → Generic AI Tool Agent (`ai_tool`, output 0, input 0)
- A tool to get the weather forecast based on geolocation → Generic AI Tool Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1509_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/1509_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
