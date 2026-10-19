# Send Discord message from Webflow form submission

This folder contains the **Send Discord message from Webflow form submission** workflow. Its executable nodes use `code`, `discord`, `if`, `set`, `webflowTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-discord-message-from-webflow-form-submission.json`](send-discord-message-from-webflow-form-submission.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`, `webflowApi`

**Entry nodes:** Webflow Form Submission Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Does the channel exist? | `if` | Inspect parameters |
| Transform data to send message | `set` | Inspect parameters |
| Webflow Form Submission Trigger | `webflowTrigger` | Inspect parameters |
| Compose Slack message | `code` | Inspect parameters |
| List Discord Channels | `discord` | getAll |
| Filter existing Discord channel | `code` | Inspect parameters |
| Create Discord channel with form name | `discord` | Inspect parameters |
| Notify #general channel of newly created channel1 | `discord` | message |
| Send form submission to Discord channel | `discord` | message |

## Connection map

- Compose Slack message → Send form submission to Discord channel (`main`, output 0, input 0)
- List Discord Channels → Filter existing Discord channel (`main`, output 0, input 0)
- Does the channel exist? → Compose Slack message (`main`, output 0, input 0)
- Does the channel exist? → Create Discord channel with form name (`main`, output 1, input 0)
- Transform data to send message → Compose Slack message (`main`, output 0, input 0)
- Filter existing Discord channel → Does the channel exist? (`main`, output 0, input 0)
- Webflow Form Submission Trigger → List Discord Channels (`main`, output 0, input 0)
- Create Discord channel with form name → Transform data to send message (`main`, output 0, input 0)
- Create Discord channel with form name → Notify #general channel of newly created channel1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1819_Code_Discord_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1819_Code_Discord_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
