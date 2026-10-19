# YogiAI

This folder contains the **YogiAI** workflow. Its executable nodes use `agent`, `chainLlm`, `code`, `googleSheets`, `googleSheetsTool`, `httpRequest`, `lmChatAzureOpenAi`, `outputParserAutofixing`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`yogiai.json`](yogiai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `azureOpenAiApi`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Trigger 2130 YogaPosesToday

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Azure OpenAI Chat Model2 | `lmChatAzureOpenAi` | Inspect parameters |
| YogaLog | `googleSheets` | append |
| Azure OpenAI Chat Model3 | `lmChatAzureOpenAi` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Azure OpenAI Chat Model1 | `lmChatAzureOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| PosesDatabase1 | `googleSheetsTool` | Inspect parameters |
| YogaLog2 | `googleSheets` | append |
| Split Out | `splitOut` | Inspect parameters |
| Trigger 2130 YogaPosesToday | `scheduleTrigger` | Inspect parameters |
| Azure OpenAI Chat Model5 | `lmChatAzureOpenAi` | Inspect parameters |
| Get PoseName | `googleSheets` | Inspect parameters |
| WritePosesToday | `chainLlm` | Inspect parameters |
| RewritePosesToday | `chainLlm` | Inspect parameters |
| Azure OpenAI Chat Model | `lmChatAzureOpenAi` | Inspect parameters |
| WriteJSONflex | `chainLlm` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Auto-fixing Output Parser1 | `outputParserAutofixing` | Inspect parameters |
| Azure OpenAI Chat Model6 | `lmChatAzureOpenAi` | Inspect parameters |
| Azure OpenAI Chat Model4 | `lmChatAzureOpenAi` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Line Push with Flex Bubble | `httpRequest` | POST |
| CombineAll | `set` | Inspect parameters |
| Fix JSON | `chainLlm` | Inspect parameters |

## Connection map

- Code → WriteJSONflex (`main`, output 0, input 0)
- YogaLog → AI Agent (`main`, output 0, input 0)
- AI Agent → Split Out (`main`, output 0, input 0)
- Fix JSON → Line Push with Flex Bubble (`main`, output 0, input 0)
- Split Out → YogaLog2 (`main`, output 0, input 0)
- CombineAll → Fix JSON (`main`, output 0, input 0)
- Get PoseName → Code (`main`, output 0, input 0)
- WriteJSONflex → WritePosesToday (`main`, output 0, input 0)
- PosesDatabase1 → AI Agent (`ai_tool`, output 0, input 0)
- WritePosesToday → RewritePosesToday (`main`, output 0, input 0)
- RewritePosesToday → CombineAll (`main`, output 0, input 0)
- Azure OpenAI Chat Model → WriteJSONflex (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model2 → WritePosesToday (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model3 → AI Agent (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model4 → Fix JSON (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model5 → RewritePosesToday (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model6 → Auto-fixing Output Parser1 (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → Auto-fixing Output Parser1 (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser1 → WriteJSONflex (`ai_outputParser`, output 0, input 0)
- Line Push with Flex Bubble → YogaLog (`main`, output 0, input 0)
- Trigger 2130 YogaPosesToday → Get PoseName (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0740_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0740_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
