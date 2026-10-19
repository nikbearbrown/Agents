# AI Customer-Support Assistant · WhatsApp Ready · Works for Any Business

This folder contains the **AI Customer-Support Assistant · WhatsApp Ready · Works for Any Business** workflow. Its executable nodes use `agent`, `code`, `if`, `lmChatOpenAi`, `memoryPostgresChat`, `toolHttpRequest`, `whatsApp`, `whatsAppTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-customer-support-assistant-whatsapp-ready-works-for-any-business.json`](ai-customer-support-assistant-whatsapp-ready-works-for-any-business.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `postgres`, `whatsAppApi`, `whatsAppTriggerApi`

**Entry nodes:** WhatsApp Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| list_links | `toolHttpRequest` | POST |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| WhatsApp Trigger | `whatsAppTrigger` | Inspect parameters |
| cleanAnswer | `code` | Inspect parameters |
| get_page | `toolHttpRequest` | POST |
| 24-hour window check | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| Send Pre-approved Template Message to Reopen the Conversation | `whatsApp` | Inspect parameters |
| Send AI Agent's Answer | `whatsApp` | send |
| Postgres Users Memory | `memoryPostgresChat` | Inspect parameters |

## Connection map

- If → cleanAnswer (`main`, output 0, input 0)
- If → Send Pre-approved Template Message to Reopen the Conversation (`main`, output 1, input 0)
- AI Agent → 24-hour window check (`main`, output 0, input 0)
- get_page → AI Agent (`ai_tool`, output 0, input 0)
- list_links → AI Agent (`ai_tool`, output 0, input 0)
- cleanAnswer → Send AI Agent's Answer (`main`, output 0, input 0)
- WhatsApp Trigger → AI Agent (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- 24-hour window check → If (`main`, output 0, input 0)
- Postgres Users Memory → AI Agent (`ai_memory`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Whatsapp/1521_Whatsapp_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Whatsapp/1521_Whatsapp_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
