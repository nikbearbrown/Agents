# query for upwork job posts and receive schedule events and find existing entries

This folder contains the **query for upwork job posts and receive schedule events and find existing entries** workflow. Its executable nodes use `httpRequest`, `if`, `merge`, `mongoDb`, `scheduleTrigger`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`query-for-upwork-job-posts-and-receive-schedule-events-and-find-existing-entries.json`](query-for-upwork-job-posts-and-receive-schedule-events-and-find-existing-entries.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpQueryAuth`, `mongoDb`, `slackApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Assign parameters | `set` | Inspect parameters |
| Query For Upwork Job Posts | `httpRequest` | POST |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| If Working Hours | `if` | Inspect parameters |
| Find Existing Entries | `mongoDb` | Inspect parameters |
| Output New Entries | `merge` | Inspect parameters |
| Add New Entries To MongoDB | `mongoDb` | insert |
| Send message in #general | `slack` | Inspect parameters |

## Connection map

- If Working Hours → Assign parameters (`main`, output 0, input 0)
- Schedule Trigger → If Working Hours (`main`, output 0, input 0)
- Assign parameters → Query For Upwork Job Posts (`main`, output 0, input 0)
- Output New Entries → Add New Entries To MongoDB (`main`, output 0, input 0)
- Output New Entries → Send message in #general (`main`, output 0, input 0)
- Find Existing Entries → Output New Entries (`main`, output 0, input 0)
- Query For Upwork Job Posts → Find Existing Entries (`main`, output 0, input 0)
- Query For Upwork Job Posts → Output New Entries (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0711_Schedule_Slack_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0711_Schedule_Slack_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
