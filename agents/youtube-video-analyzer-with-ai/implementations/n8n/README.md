# YouTube Video Analyzer with AI

This folder contains the **YouTube Video Analyzer with AI** workflow. Its executable nodes use `chainLlm`, `code`, `emailSend`, `httpRequest`, `if`, `lmChatDeepSeek`, `lmChatOpenAi`, `lmChatOpenRouter`, `manualTrigger`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-video-analyzer-with-ai.json`](youtube-video-analyzer-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `deepSeekApi`, `httpHeaderAuth`, `openAiApi`, `openRouterApi`, `smtp`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| YouTube Video ID | `code` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| DeepSeek Chat Model | `lmChatDeepSeek` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Generate transcript | `httpRequest` | POST |
| Exist? | `if` | Inspect parameters |
| Analyze LLM Chain | `chainLlm` | Inspect parameters |
| Set YouTube URL | `set` | Inspect parameters |
| Get transcript | `set` | Inspect parameters |
| Get Fulltext | `code` | Inspect parameters |

## Connection map

- Exist? → Get Fulltext (`main`, output 0, input 0)
- Get Fulltext → Analyze LLM Chain (`main`, output 0, input 0)
- Get transcript → Exist? (`main`, output 0, input 0)
- Set YouTube URL → YouTube Video ID (`main`, output 0, input 0)
- YouTube Video ID → Generate transcript (`main`, output 0, input 0)
- Analyze LLM Chain → Send Email (`main`, output 0, input 0)
- DeepSeek Chat Model → Analyze LLM Chain (`ai_languageModel`, output 0, input 0)
- Generate transcript → Get transcript (`main`, output 0, input 0)
- Structured Output Parser → Analyze LLM Chain (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Set YouTube URL (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1461_Code_Manual_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1461_Code_Manual_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
