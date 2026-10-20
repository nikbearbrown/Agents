# receive schedule events and google sheets and chain llm

This folder contains the **receive schedule events and google sheets and chain llm** workflow. Its executable nodes use `chainLlm`, `facebookGraphApi`, `googleSheets`, `httpRequest`, `lmChatGoogleGemini`, `outputParserStructured`, `scheduleTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-google-sheets-and-chain-llm.json`](receive-schedule-events-and-google-sheets-and-chain-llm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `googlePalmApi`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Scheduled Start: Check for New Posts

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Scheduled Start: Check for New Posts | `scheduleTrigger` | Inspect parameters |
| 1. Get Next Post Idea from Sheet | `googleSheets` | Inspect parameters |
| 2. Prepare Input Variables (Topic, Audience, etc.) | `set` | Inspect parameters |
| 3a. Generate Content Concept (Gemini) | `chainLlm` | Inspect parameters |
| (LLM Model for Concept) | `lmChatGoogleGemini` | Inspect parameters |
| (Parse Concept JSON) | `outputParserStructured` | Inspect parameters |
| 3b. Generate Image Prompt Options (Gemini) | `chainLlm` | Inspect parameters |
| (LLM Model for Prompts) | `lmChatGoogleGemini` | Inspect parameters |
| (Parse Prompts JSON) | `outputParserStructured` | Inspect parameters |
| 3c. Generate Post Caption (Gemini) | `chainLlm` | Inspect parameters |
| (LLM Model for Caption) | `lmChatGoogleGemini` | Inspect parameters |
| (Parse Caption JSON) | `outputParserStructured` | Inspect parameters |
| 4. Generate Image using Prompt 1 (Replicate Flux) | `httpRequest` | POST |
| 5. Prepare Data for Instagram API | `set` | Inspect parameters |
| 6a. Create Instagram Media Container | `facebookGraphApi` | Inspect parameters |
| 6b. Wait for Container Processing | `wait` | Inspect parameters |
| 6c. Publish Post to Instagram | `facebookGraphApi` | Inspect parameters |
| 7. Update Post Status in Sheet | `googleSheets` | update |

## Connection map

- (Parse Caption JSON) → 3c. Generate Post Caption (Gemini) (`ai_outputParser`, output 0, input 0)
- (Parse Concept JSON) → 3a. Generate Content Concept (Gemini) (`ai_outputParser`, output 0, input 0)
- (Parse Prompts JSON) → 3b. Generate Image Prompt Options (Gemini) (`ai_outputParser`, output 0, input 0)
- (LLM Model for Caption) → 3c. Generate Post Caption (Gemini) (`ai_languageModel`, output 0, input 0)
- (LLM Model for Concept) → 3a. Generate Content Concept (Gemini) (`ai_languageModel`, output 0, input 0)
- (LLM Model for Prompts) → 3b. Generate Image Prompt Options (Gemini) (`ai_languageModel`, output 0, input 0)
- 6c. Publish Post to Instagram → 7. Update Post Status in Sheet (`main`, output 0, input 0)
- 1. Get Next Post Idea from Sheet → 2. Prepare Input Variables (Topic, Audience, etc.) (`main`, output 0, input 0)
- 5. Prepare Data for Instagram API → 6a. Create Instagram Media Container (`main`, output 0, input 0)
- 6b. Wait for Container Processing → 6c. Publish Post to Instagram (`main`, output 0, input 0)
- 3c. Generate Post Caption (Gemini) → 4. Generate Image using Prompt 1 (Replicate Flux) (`main`, output 0, input 0)
- 6a. Create Instagram Media Container → 6b. Wait for Container Processing (`main`, output 0, input 0)
- Scheduled Start: Check for New Posts → 1. Get Next Post Idea from Sheet (`main`, output 0, input 0)
- 3a. Generate Content Concept (Gemini) → 3b. Generate Image Prompt Options (Gemini) (`main`, output 0, input 0)
- 3b. Generate Image Prompt Options (Gemini) → 3c. Generate Post Caption (Gemini) (`main`, output 0, input 0)
- 4. Generate Image using Prompt 1 (Replicate Flux) → 5. Prepare Data for Instagram API (`main`, output 0, input 0)
- 2. Prepare Input Variables (Topic, Audience, etc.) → 3a. Generate Content Concept (Gemini) (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0905_Wait_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0905_Wait_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
