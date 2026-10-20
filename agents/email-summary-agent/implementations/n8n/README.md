# Email Summary Agent

This folder contains the **Email Summary Agent** workflow. Its executable nodes use `aggregate`, `gmail`, `openAi`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`email-summary-agent.json`](email-summary-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Daily 7AM Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Daily 7AM Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch Emails - Past 24 Hours | `gmail` | getAll |
| Organize Email Data - Morning | `aggregate` | Inspect parameters |
| Summarize Emails with OpenAI - Morning | `openAi` | Inspect parameters |
| Send Summary - Morning | `gmail` | Inspect parameters |

## Connection map

- Daily 7AM Trigger → Fetch Emails - Past 24 Hours (`main`, output 0, input 0)
- Fetch Emails - Past 24 Hours → Organize Email Data - Morning (`main`, output 0, input 0)
- Organize Email Data - Morning → Summarize Emails with OpenAI - Morning (`main`, output 0, input 0)
- Summarize Emails with OpenAI - Morning → Send Summary - Morning (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1544_Aggregate_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/1544_Aggregate_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
