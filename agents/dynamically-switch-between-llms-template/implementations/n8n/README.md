# Dynamically switch between LLMs Template

This folder contains the **Dynamically switch between LLMs Template** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `if`, `lmChatOpenAi`, `noOp`, `sentimentAnalysis`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dynamically-switch-between-llms-template.json`](dynamically-switch-between-llms-template.json): sanitized, inactive import copy with an overview sticky note.
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
| Switch Model | `code` | Inspect parameters |
| Set LLM index | `set` | Inspect parameters |
| Increase LLM index | `set` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Check for expected error | `if` | Inspect parameters |
| Loop finished without results | `set` | Inspect parameters |
| Unexpected error | `set` | Inspect parameters |
| Return result | `set` | Inspect parameters |
| OpenAI 4o-mini | `lmChatOpenAi` | Inspect parameters |
| OpenAI 4o | `lmChatOpenAi` | Inspect parameters |
| OpenAI o1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Validate response | `sentimentAnalysis` | Inspect parameters |
| Generate response | `chainLlm` | Inspect parameters |

## Connection map

- OpenAI 4o → Switch Model (`ai_languageModel`, output 0, input 0)
- OpenAI o1 → Switch Model (`ai_languageModel`, output 0, input 0)
- Switch Model → Generate response (`ai_languageModel`, output 0, input 0)
- Set LLM index → Generate response (`main`, output 0, input 0)
- OpenAI 4o-mini → Switch Model (`ai_languageModel`, output 0, input 0)
- Generate response → Validate response (`main`, output 0, input 0)
- Generate response → Check for expected error (`main`, output 1, input 0)
- OpenAI Chat Model → Validate response (`ai_languageModel`, output 0, input 0)
- Validate response → Return result (`main`, output 0, input 0)
- Validate response → Increase LLM index (`main`, output 1, input 0)
- Increase LLM index → No Operation, do nothing (`main`, output 0, input 0)
- Check for expected error → Loop finished without results (`main`, output 0, input 0)
- Check for expected error → Unexpected error (`main`, output 1, input 0)
- No Operation, do nothing → Set LLM index (`main`, output 0, input 0)
- When chat message received → Set LLM index (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/1838_Noop_Stickynote_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/1838_Noop_Stickynote_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
