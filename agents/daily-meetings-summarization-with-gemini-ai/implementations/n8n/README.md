# Daily meetings summarization with Gemini AI

This folder contains the **Daily meetings summarization with Gemini AI** workflow. Its executable nodes use `agent`, `googleCalendarTool`, `lmChatGoogleGemini`, `scheduleTrigger`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`daily-meetings-summarization-with-gemini-ai.json`](daily-meetings-summarization-with-gemini-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleCalendarOAuth2Api`, `googlePalmApi`, `slackApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Send response back to slack channel | `slack` | Inspect parameters |
| Google Calendar - Get Events | `googleCalendarTool` | getAll |
| Calendar AI Agent | `agent` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Schedule Trigger → Calendar AI Agent (`main`, output 0, input 0)
- Calendar AI Agent → Send response back to slack channel (`main`, output 0, input 0)
- Google Gemini Chat Model → Calendar AI Agent (`ai_languageModel`, output 0, input 0)
- Google Calendar - Get Events → Calendar AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1406_Schedule_Slack_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1406_Schedule_Slack_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
