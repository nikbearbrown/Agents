# Send Slack message from Webflow form submission

This folder contains the **Send Slack message from Webflow form submission** workflow. Its executable nodes use `code`, `if`, `set`, `slack`, `webflowTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-slack-message-from-webflow-form-submission.json`](send-slack-message-from-webflow-form-submission.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`, `webflowApi`

**Entry nodes:** Webflow Form Submission Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Does the channel exist? | `if` | Inspect parameters |
| Send slack message to channel | `slack` | Inspect parameters |
| Create Slack channel with form name | `slack` | channel |
| Transform data to send message | `set` | Inspect parameters |
| Notify #general channel of newly created channel | `slack` | Inspect parameters |
| Webflow Form Submission Trigger | `webflowTrigger` | Inspect parameters |
| Compose Slack message | `code` | Inspect parameters |
| List Slack Channels | `slack` | channel / getAll |
| Check if Webflow form has an existing channel | `code` | Inspect parameters |

## Connection map

- List Slack Channels → Check if Webflow form has an existing channel (`main`, output 0, input 0)
- Compose Slack message → Send slack message to channel (`main`, output 0, input 0)
- Does the channel exist? → Compose Slack message (`main`, output 0, input 0)
- Does the channel exist? → Create Slack channel with form name (`main`, output 1, input 0)
- Transform data to send message → Compose Slack message (`main`, output 0, input 0)
- Webflow Form Submission Trigger → List Slack Channels (`main`, output 0, input 0)
- Create Slack channel with form name → Transform data to send message (`main`, output 0, input 0)
- Create Slack channel with form name → Notify #general channel of newly created channel (`main`, output 0, input 0)
- Check if Webflow form has an existing channel → Does the channel exist? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1958_Code_Slack_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1958_Code_Slack_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
