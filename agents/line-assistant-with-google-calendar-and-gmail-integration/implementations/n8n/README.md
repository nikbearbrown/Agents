# LINE Assistant with Google Calendar and Gmail Integration

This folder contains the **LINE Assistant with Google Calendar and Gmail Integration** workflow. Its executable nodes use `agent`, `gmailTool`, `googleCalendarTool`, `httpRequest`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `set`, `switch`, `toolWikipedia`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`line-assistant-with-google-calendar-and-gmail-integration.json`](line-assistant-with-google-calendar-and-gmail-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`

**Entry nodes:** Line Receiving

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Switch Between Text and Others | `switch` | Inspect parameters |
| Line Receiving | `webhook` | Inspect parameters |
| Error Handling from AI Response | `switch` | Inspect parameters |
| Text Cleansing | `set` | Inspect parameters |
| Line Answering (Error Case) | `httpRequest` | POST |
| Line Answering (Ordinary Case) | `httpRequest` | POST |
| Google Calendar Create | `googleCalendarTool` | Inspect parameters |
| Google Calendar Read | `googleCalendarTool` | getAll |
| Gmail Read | `gmailTool` | getAll |

## Connection map

- OpenAI → Error Handling from AI Response (`main`, output 0, input 0)
- AI Agent → OpenAI (`main`, output 0, input 0)
- Wikipedia → AI Agent (`ai_tool`, output 0, input 0)
- Gmail Read → AI Agent (`ai_tool`, output 0, input 0)
- Line Receiving → Switch Between Text and Others (`main`, output 0, input 0)
- Text Cleansing → Line Answering (Ordinary Case) (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Calendar Read → AI Agent (`ai_tool`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Google Calendar Create → AI Agent (`ai_tool`, output 0, input 0)
- Switch Between Text and Others → AI Agent (`main`, output 0, input 0)
- Switch Between Text and Others → Line Answering (Error Case) (`main`, output 1, input 0)
- Error Handling from AI Response → Text Cleansing (`main`, output 0, input 0)
- Error Handling from AI Response → Line Answering (Error Case) (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1778_HTTP_Googlecalendartool_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1778_HTTP_Googlecalendartool_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
