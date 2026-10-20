# Sync Zendesk tickets to Slack threads

This folder contains the **Sync Zendesk tickets to Slack threads** workflow. Its executable nodes use `code`, `if`, `set`, `slack`, `webhook`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sync-zendesk-tickets-to-slack-threads.json`](sync-zendesk-tickets-to-slack-threads.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackOAuth2Api`, `zendeskApi`

**Entry nodes:** On new Zendesk ticket

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get ticket | `zendesk` | get |
| IF | `if` | Inspect parameters |
| Update ticket | `zendesk` | update |
| On new Zendesk ticket | `webhook` | Inspect parameters |
| Create thread | `slack` | Inspect parameters |
| Create reply on existing thread | `slack` | Inspect parameters |
| Configure | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |

## Connection map

- IF → Create reply on existing thread (`main`, output 0, input 0)
- IF → Create thread (`main`, output 1, input 0)
- Code → IF (`main`, output 0, input 0)
- Get ticket → Code (`main`, output 0, input 0)
- Create thread → Update ticket (`main`, output 0, input 0)
- On new Zendesk ticket → Get ticket (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0273_Code_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0273_Code_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
