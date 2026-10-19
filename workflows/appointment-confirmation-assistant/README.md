# agente

This folder contains the **agente** workflow. Its executable nodes use `agent`, `convertToFile`, `evolutionApi`, `googleTasksTool`, `lmChatOpenAi`, `lmChatOpenRouter`, `mcpClientTool`, `memoryPostgresChat`, `openAi`, `scheduleTrigger`, `set`, `switch`, `telegram`, `telegramTool`, `telegramTrigger`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`appointment-confirmation-assistant.json`](appointment-confirmation-assistant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `evolutionApi`, `googleTasksOAuth2Api`, `openAiApi`, `openRouterApi`, `postgres`, `telegramApi`

**Entry nodes:** Receber Mensagem Telegram, Gatilho diário, Webhook1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Assistente clinica interno | `agent` | Inspect parameters |
| Google Tasks | `googleTasksTool` | Inspect parameters |
| MCP Google Calendar | `mcpClientTool` | Inspect parameters |
| Receber Mensagem Telegram | `telegramTrigger` | Inspect parameters |
| Postgres Chat Memory | `memoryPostgresChat` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Assistente Clínica | `agent` | Inspect parameters |
| Enviar alerta de cancelamento | `telegramTool` | Inspect parameters |
| Gatilho diário | `scheduleTrigger` | Inspect parameters |
| Assistente de confirmação | `agent` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Postgres Chat Memory1 | `memoryPostgresChat` | Inspect parameters |
| MCP Google Calendar2 | `mcpClientTool` | Inspect parameters |
| MCP GMAIL | `mcpClientTool` | Inspect parameters |
| MCP CALENDAR | `mcpClientTool` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| OpenRouter Chat Model1 | `lmChatOpenRouter` | Inspect parameters |
| Webhook1 | `webhook` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| OpenAI | `openAi` | audio / transcribe |
| Evolution API | `evolutionApi` | chat-api / get-media-base64 |
| Convert to File | `convertToFile` | toBinary |
| OpenAI1 | `openAi` | image / analyze |
| AI Agent2 | `agent` | Inspect parameters |
| OpenRouter Chat Model2 | `lmChatOpenRouter` | Inspect parameters |
| Evolution API2 | `evolutionApi` | messages-api |
| CallToHuman | `toolWorkflow` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| REMINDER | `evolutionApi` | messages-api |

## Connection map

- OpenAI → Assistente Clínica (`main`, output 0, input 0)
- Switch → Assistente Clínica (`main`, output 0, input 0)
- Switch → OpenAI1 (`main`, output 1, input 0)
- Switch → Evolution API (`main`, output 2, input 0)
- OpenAI1 → AI Agent2 (`main`, output 0, input 0)
- AI Agent → Evolution API2 (`main`, output 0, input 0)
- Webhook1 → Edit Fields1 (`main`, output 0, input 0)
- AI Agent2 → Assistente Clínica (`main`, output 0, input 0)
- MCP GMAIL → Assistente de confirmação (`ai_tool`, output 0, input 0)
- CallToHuman → Assistente Clínica (`ai_tool`, output 0, input 0)
- Edit Fields1 → Switch (`main`, output 0, input 0)
- Google Tasks → Assistente clinica interno (`ai_tool`, output 0, input 0)
- MCP CALENDAR → Assistente de confirmação (`ai_tool`, output 0, input 0)
- Evolution API → Convert to File (`main`, output 0, input 0)
- Convert to File → OpenAI (`main`, output 0, input 0)
- Gatilho diário → Assistente de confirmação (`main`, output 0, input 0)
- OpenAI Chat Model → Assistente Clínica (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Assistente clinica interno (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Assistente de confirmação (`ai_languageModel`, output 0, input 0)
- Assistente Clínica → AI Agent (`main`, output 0, input 0)
- MCP Google Calendar → Assistente clinica interno (`ai_tool`, output 0, input 0)
- MCP Google Calendar2 → Assistente Clínica (`ai_tool`, output 0, input 0)
- Postgres Chat Memory → Assistente clinica interno (`ai_memory`, output 0, input 0)
- Postgres Chat Memory1 → Assistente Clínica (`ai_memory`, output 0, input 0)
- OpenRouter Chat Model1 → AI Agent (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model2 → AI Agent2 (`ai_languageModel`, output 0, input 0)
- Receber Mensagem Telegram → Assistente clinica interno (`main`, output 0, input 0)
- Assistente clinica interno → Telegram (`main`, output 0, input 0)
- Assistente de confirmação → REMINDER (`main`, output 0, input 0)
- Enviar alerta de cancelamento → Assistente Clínica (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletaskstool/1103_Googletaskstool_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googletaskstool/1103_Googletaskstool_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
