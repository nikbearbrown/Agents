# Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened

This folder contains the **Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `jira`, `noOp`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`notify-user-in-slack-of-quarantined-email-and-create-jira-ticket-if-opened.json`](notify-user-in-slack-of-quarantined-email-and-create-jira-ticket-if-opened.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `jiraSoftwareCloudApi`, `slackApi`, `slackOAuth2Api`

**Entry nodes:** Receive Sublime Security Alert

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| has email been opened? | `if` | Inspect parameters |
| Receive Sublime Security Alert | `webhook` | Inspect parameters |
| Get message details in Sublime Security | `httpRequest` | Inspect parameters |
| Jira Software | `jira` | Inspect parameters |
| lookup slack user by email | `httpRequest` | Inspect parameters |
| user found? | `if` | Inspect parameters |
| Found, notify user | `slack` | Inspect parameters |
| Not Found, Do Nothing | `noOp` | Inspect parameters |
| No, do nothing | `noOp` | Inspect parameters |
| Yes, prep flaggedRules table | `code` | Inspect parameters |

## Connection map

- user found? → Found, notify user (`main`, output 0, input 0)
- user found? → Not Found, Do Nothing (`main`, output 1, input 0)
- has email been opened? → Yes, prep flaggedRules table (`main`, output 0, input 0)
- has email been opened? → No, do nothing (`main`, output 1, input 0)
- lookup slack user by email → user found? (`main`, output 0, input 0)
- Yes, prep flaggedRules table → Jira Software (`main`, output 0, input 0)
- Receive Sublime Security Alert → Get message details in Sublime Security (`main`, output 0, input 0)
- Get message details in Sublime Security → has email been opened? (`main`, output 0, input 0)
- Get message details in Sublime Security → lookup slack user by email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1541_Webhook_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1541_Webhook_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
