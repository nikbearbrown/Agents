# 🧠 Give Your AI Agent Chatbot Long Term Memory Tools Router

This folder contains the **🧠 Give Your AI Agent Chatbot Long Term Memory Tools Router** workflow. Its executable nodes use `agent`, `chainLlm`, `chatTrigger`, `executeWorkflowTrigger`, `gmail`, `googleDocs`, `lmChatOpenAi`, `memoryBufferWindow`, `set`, `switch`, `telegram`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`give-your-ai-agent-chatbot-long-term-memory-tools-router.json`](give-your-ai-agent-chatbot-long-term-memory-tools-router.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDocsOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** When Executed by Another Workflow, Ⓜ️ When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Save Long Term Memories | `googleDocs` | update |
| Saved response | `set` | Inspect parameters |
| Respond with long term memories | `set` | Inspect parameters |
| Retrieve Long Term Memories3 | `googleDocs` | get |
| Send Success Message to Telegram | `telegram` | Inspect parameters |
| Email Workflow Stats | `gmail` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| 📤Send Memories to Telegram | `toolWorkflow` | Inspect parameters |
| 📫Send Memories to Gmail | `toolWorkflow` | Inspect parameters |
| 🧠Save Memories | `toolWorkflow` | Inspect parameters |
| 🔎Retrieve Memories | `toolWorkflow` | Inspect parameters |
| 🤯Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| 🧠 AI Agent w/Long Term Memory | `agent` | Inspect parameters |
| 🤖OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Ⓜ️ When chat message received | `chatTrigger` | Inspect parameters |
| Prepare Telegram Message | `chainLlm` | Inspect parameters |
| Prepare Gmail Message | `chainLlm` | Inspect parameters |
| Retrieve Long Term Memories | `googleDocs` | get |
| Memory Tool Router | `switch` | Inspect parameters |
| Retrieve Long Term Memories2 | `googleDocs` | get |

## Connection map

- 🧠Save Memories → 🧠 AI Agent w/Long Term Memory (`ai_tool`, output 0, input 0)
- Memory Tool Router → Save Long Term Memories (`main`, output 0, input 0)
- Memory Tool Router → Retrieve Long Term Memories (`main`, output 1, input 0)
- Memory Tool Router → Retrieve Long Term Memories2 (`main`, output 2, input 0)
- Memory Tool Router → Retrieve Long Term Memories3 (`main`, output 3, input 0)
- OpenAI Chat Model2 → Prepare Telegram Message (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Prepare Gmail Message (`ai_languageModel`, output 0, input 0)
- Prepare Gmail Message → Email Workflow Stats (`main`, output 0, input 0)
- 🔎Retrieve Memories → 🧠 AI Agent w/Long Term Memory (`ai_tool`, output 0, input 0)
- 🤖OpenAI Chat Model → 🧠 AI Agent w/Long Term Memory (`ai_languageModel`, output 0, input 0)
- Save Long Term Memories → Saved response (`main`, output 0, input 0)
- Prepare Telegram Message → Send Success Message to Telegram (`main`, output 0, input 0)
- 🤯Window Buffer Memory → 🧠 AI Agent w/Long Term Memory (`ai_memory`, output 0, input 0)
- 📫Send Memories to Gmail → 🧠 AI Agent w/Long Term Memory (`ai_tool`, output 0, input 0)
- Retrieve Long Term Memories → Respond with long term memories (`main`, output 0, input 0)
- Retrieve Long Term Memories2 → Prepare Telegram Message (`main`, output 0, input 0)
- Retrieve Long Term Memories3 → Prepare Gmail Message (`main`, output 0, input 0)
- 📤Send Memories to Telegram → 🧠 AI Agent w/Long Term Memory (`ai_tool`, output 0, input 0)
- When Executed by Another Workflow → Memory Tool Router (`main`, output 0, input 0)
- Ⓜ️ When chat message received → 🧠 AI Agent w/Long Term Memory (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1950_Telegram_Googledocs_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1950_Telegram_Googledocs_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
