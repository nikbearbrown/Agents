# Setting Up Slack App Event Subscriptions

This folder contains the **Setting Up Slack App Event Subscriptions** workflow. Its executable nodes use `agent`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `microsoftOutlookTool`, `respondToWebhook`, `set`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`setting-up-slack-app-event-subscriptions.json`](setting-up-slack-app-event-subscriptions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftOutlookOAuth2Api`, `openAiApi`, `slackApi`

**Entry nodes:** On BOT/APP Mention

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Search All Outlook Events | `microsoftOutlookTool` | event |
| Create New Calendar Event | `microsoftOutlookTool` | event / create |
| Get Available Calendars | `microsoftOutlookTool` | calendar |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Outlook Calendar Assistant | `agent` | Inspect parameters |
| Send Reply | `slack` | Inspect parameters |
| Respond to Challenge | `respondToWebhook` | Inspect parameters |
| Is Auth Challenge? | `if` | Inspect parameters |
| Get Message | `set` | Inspect parameters |
| On BOT/APP Mention | `webhook` | Inspect parameters |

## Connection map

- Get Message → Outlook Calendar Assistant (`main`, output 0, input 0)
- Simple Memory → Outlook Calendar Assistant (`ai_memory`, output 0, input 0)
- OpenAI Chat Model → Outlook Calendar Assistant (`ai_languageModel`, output 0, input 0)
- Is Auth Challenge? → Respond to Challenge (`main`, output 0, input 0)
- Is Auth Challenge? → Get Message (`main`, output 1, input 0)
- On BOT/APP Mention → Is Auth Challenge? (`main`, output 0, input 0)
- Get Available Calendars → Outlook Calendar Assistant (`ai_tool`, output 0, input 0)
- Create New Calendar Event → Outlook Calendar Assistant (`ai_tool`, output 0, input 0)
- Search All Outlook Events → Outlook Calendar Assistant (`ai_tool`, output 0, input 0)
- Outlook Calendar Assistant → Send Reply (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0834_Webhook_Slack_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0834_Webhook_Slack_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
