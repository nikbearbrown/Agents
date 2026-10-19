# Get event triggered notifications / updates on preferred messaging channels with TwentyCRM

This folder contains the **Get event triggered notifications / updates on preferred messaging channels with TwentyCRM** workflow. Its executable nodes use `gmail`, `googleSheets`, `if`, `set`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-event-triggered-notifications-updates-on-preferred-messaging-channels-with-twentycrm.json`](get-event-triggered-notifications-updates-on-preferred-messaging-channels-with-twentycrm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** on new twentycrm event

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| filter required data #eventType mandatory | `set` | Inspect parameters |
| events log | `googleSheets` | append |
| message channel evaluation | `if` | Inspect parameters |
| on new twentycrm event | `webhook` | Inspect parameters |
| email channel for delete eventType | `gmail` | Inspect parameters |
| message channel for all other eventTypes | `slack` | Inspect parameters |

## Connection map

- events log → message channel evaluation (`main`, output 0, input 0)
- on new twentycrm event → filter required data #eventType mandatory (`main`, output 0, input 0)
- message channel evaluation → email channel for delete eventType (`main`, output 0, input 0)
- message channel evaluation → message channel for all other eventTypes (`main`, output 1, input 0)
- filter required data #eventType mandatory → events log (`main`, output 0, input 0)
- filter required data #eventType mandatory → message channel evaluation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1477_Webhook_Slack_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1477_Webhook_Slack_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
