# Schedule Mon - Friday @ 09:00am

This folder contains the **Schedule Mon - Friday @ 09:00am** workflow. Its executable nodes use `cron`, `filter`, `notion`, `set`, `slack`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`schedule-mon-friday-09-00am.json`](schedule-mon-friday-09-00am.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `slackOAuth2Api`

**Entry nodes:** Schedule Mon - Friday @ 09:00am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter incomplete tasks only | `filter` | Inspect parameters |
| Get All Slack Users (Darryn) | `slack` | user / getAll |
| Get To Dos from Tasks Database | `notion` | databasePage / getAll |
| Schedule Mon - Friday @ 09:00am | `cron` | Inspect parameters |
| Set Notion User Emails | `set` | Inspect parameters |
| Set Slack User Full Name | `set` | Inspect parameters |
| Send a Direct Message to User 1 | `slack` | Inspect parameters |
| Send a Direct Message to User 2 | `slack` | Inspect parameters |
| Switch for Notion Users Emails | `switch` | Inspect parameters |
| Filter Slack User 1 Full Name | `filter` | Inspect parameters |
| Filter Slack User 2 Full Name | `filter` | Inspect parameters |

## Connection map

- Set Notion User Emails → Set Slack User Full Name (`main`, output 0, input 0)
- Set Slack User Full Name → Get To Dos from Tasks Database (`main`, output 0, input 0)
- Filter incomplete tasks only → Get All Slack Users (Darryn) (`main`, output 0, input 0)
- Get All Slack Users (Darryn) → Switch for Notion Users Emails (`main`, output 0, input 0)
- Filter Slack User 1 Full Name → Send a Direct Message to User 1 (`main`, output 0, input 0)
- Filter Slack User 2 Full Name → Send a Direct Message to User 2 (`main`, output 0, input 0)
- Get To Dos from Tasks Database → Filter incomplete tasks only (`main`, output 0, input 0)
- Switch for Notion Users Emails → Filter Slack User 1 Full Name (`main`, output 0, input 0)
- Switch for Notion Users Emails → Filter Slack User 2 Full Name (`main`, output 1, input 0)
- Schedule Mon - Friday @ 09:00am → Set Notion User Emails (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0612_Filter_Slack_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0612_Filter_Slack_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
