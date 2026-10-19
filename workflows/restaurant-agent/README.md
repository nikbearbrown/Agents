# Restaurant Agent

This folder contains the **Restaurant Agent** workflow. Its executable nodes use `agent`, `googleSheetsTool`, `lmChatOpenAi`, `memoryBufferWindow`, `respondToWebhook`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`restaurant-agent.json`](restaurant-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Restaurant AI Agent | `agent` | Inspect parameters |
| Menu | `toolWorkflow` | Inspect parameters |
| Get Reservations Availability | `googleSheetsTool` | Inspect parameters |
| Update Confirmed Reservation | `googleSheetsTool` | appendOrUpdate |
| Update Reservation Availability | `googleSheetsTool` | update |
| Get Confirmed Reservation | `googleSheetsTool` | appendOrUpdate |
| Get Orders | `googleSheetsTool` | Inspect parameters |
| Update Orders | `googleSheetsTool` | appendOrUpdate |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |

## Connection map

- Restaurant AI Agent → Respond to Webhook (`main`, output 0, input 0)
- Menu → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Get Reservations Availability → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Update Confirmed Reservation → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Update Reservation Availability → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Get Confirmed Reservation → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Get Orders → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- Update Orders → Restaurant AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Restaurant AI Agent (`ai_languageModel`, output 0, input 0)
- Webhook → Restaurant AI Agent (`main`, output 0, input 0)
- Simple Memory → Restaurant AI Agent (`ai_memory`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
