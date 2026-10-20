# ⚡📽️ Ultimate AI-Powered Chatbot for YouTube Summarization & Analysis

This folder contains the **⚡📽️ Ultimate AI-Powered Chatbot for YouTube Summarization & Analysis** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `set`, `splitOut`, `summarize`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ultimate-ai-powered-chatbot-for-youtube-summarization-analysis.json`](ultimate-ai-powered-chatbot-for-youtube-summarization-analysis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When Executed by Another Workflow, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get YouTube Transcript | `code` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| YouTube Video Agent | `agent` | Inspect parameters |
| Create YouTube API URL | `code` | Inspect parameters |
| Split Out Transcript Segments | `splitOut` | Inspect parameters |
| Combine Transcript Segments | `summarize` | Inspect parameters |
| Get YouTube Video Details | `httpRequest` | Inspect parameters |
| Merge YouTube Details & Transcript | `merge` | Inspect parameters |
| Create One JSON Object | `aggregate` | Inspect parameters |
| Respond with YouTube Details & Transcript | `set` | Inspect parameters |
| Workflow Variables | `set` | Inspect parameters |
| YouTube Processing Tool | `toolWorkflow` | Inspect parameters |
| DeepSeek-V3   Chat | `lmChatOpenAi` | Inspect parameters |

## Connection map

- gpt-4o-mini1 → YouTube Video Agent (`ai_languageModel`, output 0, input 0)
- Workflow Variables → Create YouTube API URL (`main`, output 0, input 0)
- Workflow Variables → Get YouTube Transcript (`main`, output 0, input 0)
- Window Buffer Memory → YouTube Video Agent (`ai_memory`, output 0, input 0)
- Create One JSON Object → Respond with YouTube Details & Transcript (`main`, output 0, input 0)
- Create YouTube API URL → Get YouTube Video Details (`main`, output 0, input 0)
- Get YouTube Transcript → Split Out Transcript Segments (`main`, output 0, input 0)
- YouTube Processing Tool → YouTube Video Agent (`ai_tool`, output 0, input 0)
- Get YouTube Video Details → Merge YouTube Details & Transcript (`main`, output 0, input 0)
- When chat message received → YouTube Video Agent (`main`, output 0, input 0)
- Combine Transcript Segments → Merge YouTube Details & Transcript (`main`, output 0, input 1)
- Split Out Transcript Segments → Combine Transcript Segments (`main`, output 0, input 0)
- When Executed by Another Workflow → Workflow Variables (`main`, output 0, input 0)
- Merge YouTube Details & Transcript → Create One JSON Object (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1463_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1463_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
