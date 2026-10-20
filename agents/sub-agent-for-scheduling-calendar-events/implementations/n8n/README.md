# Sub-Agent for scheduling calendar events

This folder contains the **Sub-Agent for scheduling calendar events** workflow. Its executable nodes use `agent`, `chatTrigger`, `lmChatOpenAi`, `memoryBufferWindow`, `respondToWebhook`, `set`, `toolHttpRequest`, `toolWorkflow`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sub-agent-for-scheduling-calendar-events.json`](sub-agent-for-scheduling-calendar-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When chat message received, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| calendarAgent | `toolWorkflow` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| taskAgent | `toolWorkflow` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Map Fields | `set` | Inspect parameters |
| Map Fields1 | `set` | Inspect parameters |
| Exclude Previews from Speech | `set` | Inspect parameters |
| Main Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| HTTP Request | `toolHttpRequest` | POST |
| Settings | `set` | Inspect parameters |
| Format output | `set` | Inspect parameters |
| Notion Task Agent | `agent` | Inspect parameters |
| Window Buffer Memory1 | `memoryBufferWindow` | Inspect parameters |
| Get calendar availability | `toolHttpRequest` | POST |
| Book appointment | `toolHttpRequest` | POST |
| Google Calendar Agent | `agent` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Settings1 | `set` | Inspect parameters |
| Format output1 | `set` | Inspect parameters |
| Window Buffer Memory2 | `memoryBufferWindow` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Webhook → Map Fields (`main`, output 0, input 0)
- Settings → Notion Task Agent (`main`, output 0, input 0)
- Settings1 → Google Calendar Agent (`main`, output 0, input 0)
- taskAgent → Main Agent (`ai_tool`, output 0, input 0)
- Main Agent → Exclude Previews from Speech (`main`, output 0, input 0)
- Map Fields → Main Agent (`main`, output 0, input 0)
- Map Fields1 → Main Agent (`main`, output 0, input 0)
- HTTP Request → Notion Task Agent (`ai_tool`, output 0, input 0)
- calendarAgent → Main Agent (`ai_tool`, output 0, input 0)
- Book appointment → Google Calendar Agent (`ai_tool`, output 0, input 0)
- Notion Task Agent → Format output (`main`, output 0, input 0)
- OpenAI Chat Model → Notion Task Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Google Calendar Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Main Agent (`ai_languageModel`, output 0, input 0)
- Window Buffer Memory → Main Agent (`ai_memory`, output 0, input 0)
- Google Calendar Agent → Format output1 (`main`, output 0, input 0)
- Window Buffer Memory1 → Notion Task Agent (`ai_memory`, output 0, input 0)
- Window Buffer Memory2 → Google Calendar Agent (`ai_memory`, output 0, input 0)
- Get calendar availability → Google Calendar Agent (`ai_tool`, output 0, input 0)
- When chat message received → Map Fields1 (`main`, output 0, input 0)
- Exclude Previews from Speech → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/0590_Respondtowebhook_Stickynote_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/0590_Respondtowebhook_Stickynote_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
