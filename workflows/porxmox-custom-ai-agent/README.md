# Porxmox Custom AI Agent

This folder contains the **Porxmox Custom AI Agent** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `gmailTrigger`, `httpRequest`, `if`, `lmChatGoogleGemini`, `merge`, `outputParserAutofixing`, `outputParserStructured`, `switch`, `telegramTrigger`, `toolHttpRequest`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`porxmox-custom-ai-agent.json`](porxmox-custom-ai-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `httpHeaderAuth`, `telegramApi`

**Entry nodes:** When chat message received, Telegram Trigger, Gmail Trigger, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| HTTP Request1 | `httpRequest` | =POST |
| Proxmox API Documentation | `toolHttpRequest` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Proxmox | `toolHttpRequest` | Inspect parameters |
| HTTP Request | `httpRequest` | =GET |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Proxmox API Wiki | `toolHttpRequest` | Inspect parameters |
| Structure Response | `code` | Inspect parameters |
| Structgure Response from Proxmox | `code` | Inspect parameters |
| Format Response and Hide Sensitive Data | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| HTTP Request2 | `httpRequest` | =POST |
| Merge | `merge` | Inspect parameters |
| HTTP Request3 | `httpRequest` | DELETE |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| HTTP Request4 | `httpRequest` | DELETE |
| Merge1 | `merge` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Switch | `switch` | Inspect parameters |

## Connection map

- If → HTTP Request1 (`main`, output 0, input 0)
- If → HTTP Request2 (`main`, output 1, input 0)
- If1 → HTTP Request3 (`main`, output 0, input 0)
- If1 → HTTP Request4 (`main`, output 1, input 0)
- Merge → Structgure Response from Proxmox (`main`, output 0, input 0)
- Merge1 → Structgure Response from Proxmox (`main`, output 0, input 0)
- Switch → HTTP Request (`main`, output 0, input 0)
- Switch → If (`main`, output 1, input 0)
- Switch → If1 (`main`, output 4, input 0)
- Proxmox → AI Agent (`ai_tool`, output 0, input 0)
- AI Agent → Switch (`main`, output 0, input 0)
- HTTP Request → Structure Response (`main`, output 0, input 0)
- HTTP Request1 → Merge (`main`, output 0, input 0)
- HTTP Request2 → Merge (`main`, output 0, input 1)
- HTTP Request3 → Merge1 (`main`, output 0, input 0)
- HTTP Request4 → Merge1 (`main`, output 0, input 1)
- Proxmox API Wiki → AI Agent (`ai_tool`, output 0, input 0)
- Structure Response → AI Agent1 (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Google Gemini Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- Proxmox API Documentation → AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Structgure Response from Proxmox → Format Response and Hide Sensitive Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0690_Telegram_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0690_Telegram_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
