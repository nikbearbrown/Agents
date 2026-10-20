# Check To Do on Notion and send message on Slack

This folder contains the **Check To Do on Notion and send message on Slack** workflow. Its executable nodes use `cron`, `if`, `noOp`, `notion`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`check-to-do-on-notion-and-send-message-on-slack.json`](check-to-do-on-notion-and-send-message-on-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `slackApi`

**Entry nodes:** Cron

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Cron | `cron` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |
| Get To Dos | `notion` | block / getAll |
| If task assigned to Harshil? | `if` | Inspect parameters |
| Create a Direct Message | `slack` | channel / open |
| Send a Direct Message | `slack` | Inspect parameters |

## Connection map

- Cron → Get To Dos (`main`, output 0, input 0)
- Get To Dos → If task assigned to Harshil? (`main`, output 0, input 0)
- Create a Direct Message → Send a Direct Message (`main`, output 0, input 0)
- If task assigned to Harshil? → Create a Direct Message (`main`, output 0, input 0)
- If task assigned to Harshil? → NoOp (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0809_Noop_Slack_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0809_Noop_Slack_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
