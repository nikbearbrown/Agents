# 🌐 Confluence Page AI Powered Chatbot

This folder contains the **🌐 Confluence Page AI Powered Chatbot** workflow. Its executable nodes use `agent`, `httpRequest`, `lmChatOpenAi`, `manualChatTrigger`, `markdown`, `memoryBufferWindow`, `set`, `splitOut`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`confluence-page-ai-powered-chatbot.json`](confluence-page-ai-powered-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Confluence Page Storage View | `httpRequest` | Inspect parameters |
| HTML to Markdown | `markdown` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| When chat message received | `manualChatTrigger` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Chat Response | `set` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Search By ID | `httpRequest` | Inspect parameters |
| Page Schema | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Send Telegram Message | `telegram` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |

## Connection map

- Globals → Search By ID (`main`, output 0, input 0)
- AI Agent → Chat Response (`main`, output 0, input 0)
- AI Agent → Send Telegram Message (`main`, output 0, input 0)
- Split Out → Page Schema (`main`, output 0, input 0)
- Page Schema → Confluence Page Storage View (`main`, output 0, input 0)
- gpt-4o-mini → AI Agent (`ai_languageModel`, output 0, input 0)
- Search By ID → Split Out (`main`, output 0, input 0)
- HTML to Markdown → AI Agent (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- When chat message received → Globals (`main`, output 0, input 0)
- Confluence Page Storage View → HTML to Markdown (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1919_Telegram_Splitout_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1919_Telegram_Splitout_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
