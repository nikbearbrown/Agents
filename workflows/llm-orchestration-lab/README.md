# LLM Chaining examples

This folder contains the **LLM Chaining examples** workflow. Its executable nodes use `agent`, `chainLlm`, `httpRequest`, `lmChatAnthropic`, `manualTrigger`, `markdown`, `memoryBufferWindow`, `memoryManager`, `merge`, `noOp`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`llm-orchestration-lab.json`](llm-orchestration-lab.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`

**Entry nodes:** When clicking ‘Test workflow’, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| HTTP Request | `httpRequest` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Anthropic Chat Model1 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Chat Model2 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Chat Model3 | `lmChatAnthropic` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Clean memory | `memoryManager` | Inspect parameters |
| Initial prompts | `set` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Reshape | `set` | Inspect parameters |
| Anthropic Chat Model4 | `lmChatAnthropic` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Basic LLM Chain4 | `chainLlm` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Anthropic Chat Model5 | `lmChatAnthropic` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| CONNECT ME | `noOp` | Inspect parameters |
| CONNECT ME1 | `noOp` | Inspect parameters |
| CONNECT ME2 | `noOp` | Inspect parameters |
| Initial prompts1 | `set` | Inspect parameters |
| LLM Chain - Step 1 | `chainLlm` | Inspect parameters |
| LLM Chain - Step 2 | `chainLlm` | Inspect parameters |
| LLM Chain - Step 3 | `chainLlm` | Inspect parameters |
| LLM Chain - Step 4 | `chainLlm` | Inspect parameters |
| All LLM steps here - sequentially | `agent` | Inspect parameters |
| LLM steps - parallel | `httpRequest` | POST |
| Merge output with initial prompts | `merge` | Inspect parameters |
| Merge output with initial prompts1 | `merge` | Inspect parameters |

## Connection map

- Merge → All LLM steps here - sequentially (`main`, output 0, input 0)
- Merge → Merge output with initial prompts1 (`main`, output 0, input 0)
- Merge2 → LLM steps - parallel (`main`, output 0, input 0)
- Merge2 → Merge output with initial prompts (`main`, output 0, input 0)
- Reshape → Split Out (`main`, output 0, input 0)
- Webhook → Basic LLM Chain4 (`main`, output 0, input 0)
- Split Out → Merge (`main`, output 0, input 1)
- CONNECT ME → LLM Chain - Step 1 (`main`, output 0, input 0)
- Split Out1 → Merge2 (`main`, output 0, input 1)
- CONNECT ME1 → Clean memory (`main`, output 0, input 0)
- CONNECT ME1 → Merge (`main`, output 0, input 0)
- CONNECT ME2 → Initial prompts1 (`main`, output 0, input 0)
- CONNECT ME2 → Merge2 (`main`, output 0, input 0)
- Clean memory → Initial prompts (`main`, output 0, input 0)
- HTTP Request → Markdown (`main`, output 0, input 0)
- Simple Memory → All LLM steps here - sequentially (`ai_memory`, output 0, input 0)
- Simple Memory → Clean memory (`ai_memory`, output 0, input 0)
- Initial prompts → Reshape (`main`, output 0, input 0)
- Initial prompts1 → Split Out1 (`main`, output 0, input 0)
- LLM Chain - Step 1 → LLM Chain - Step 2 (`main`, output 0, input 0)
- LLM Chain - Step 2 → LLM Chain - Step 3 (`main`, output 0, input 0)
- LLM Chain - Step 3 → LLM Chain - Step 4 (`main`, output 0, input 0)
- Anthropic Chat Model → LLM Chain - Step 1 (`ai_languageModel`, output 0, input 0)
- LLM steps - parallel → Merge output with initial prompts (`main`, output 0, input 1)
- Anthropic Chat Model1 → LLM Chain - Step 2 (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model2 → LLM Chain - Step 3 (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model3 → LLM Chain - Step 4 (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model4 → All LLM steps here - sequentially (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model5 → Basic LLM Chain4 (`ai_languageModel`, output 0, input 0)
- All LLM steps here - sequentially → Merge output with initial prompts1 (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → HTTP Request (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0958_Splitout_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0958_Splitout_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
