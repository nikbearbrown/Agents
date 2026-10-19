# AI Concierge

This folder contains the **AI Concierge** workflow. Its executable nodes use `agent`, `chatTrigger`, `googleSheetsTool`, `lmChatOpenAi`, `memoryBufferWindow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-concierge.json`](ai-concierge.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Get Inventory | `googleSheetsTool` | Inspect parameters |
| Get FAQ | `googleSheetsTool` | Inspect parameters |
| Orders | `googleSheetsTool` | Inspect parameters |

## Connection map

- When chat message received → AI Agent (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Get Inventory → AI Agent (`ai_tool`, output 0, input 0)
- Get FAQ → AI Agent (`ai_tool`, output 0, input 0)
- Orders → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
