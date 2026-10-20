# Custom Branded n8n Chatbot

This folder contains the **Custom Branded n8n Chatbot** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `microsoftOutlook`, `respondToWebhook`, `set`, `switch`, `toolHttpRequest`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`custom-branded-n8n-chatbot.json`](custom-branded-n8n-chatbot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftOutlookOAuth2Api`, `openAiApi`

**Entry nodes:** Execute Workflow Trigger, Chat Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Make Appointment | `toolHttpRequest` | POST |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| varResponse | `set` | Inspect parameters |
| freeTimeSlots | `code` | Inspect parameters |
| Get Events | `httpRequest` | Inspect parameters |
| Get Availability | `toolWorkflow` | Inspect parameters |
| Send Message | `toolWorkflow` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| varMessageResponse | `set` | Inspect parameters |
| Send Message1 | `microsoftOutlook` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| If | `if` | Inspect parameters |
| Respond With Initial Message | `respondToWebhook` | Inspect parameters |

## Connection map

- If → AI Agent (`main`, output 0, input 0)
- If → Respond With Initial Message (`main`, output 1, input 0)
- Switch → Get Events (`main`, output 0, input 0)
- Switch → Send Message1 (`main`, output 1, input 0)
- AI Agent → Respond to Webhook (`main`, output 0, input 0)
- Get Events → freeTimeSlots (`main`, output 0, input 0)
- Chat Trigger → If (`main`, output 0, input 0)
- Send Message → AI Agent (`ai_tool`, output 0, input 0)
- Send Message1 → varMessageResponse (`main`, output 0, input 0)
- freeTimeSlots → varResponse (`main`, output 0, input 0)
- Get Availability → AI Agent (`ai_tool`, output 0, input 0)
- Make Appointment → AI Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Execute Workflow Trigger → Switch (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0700_Code_Respondtowebhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0700_Code_Respondtowebhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
