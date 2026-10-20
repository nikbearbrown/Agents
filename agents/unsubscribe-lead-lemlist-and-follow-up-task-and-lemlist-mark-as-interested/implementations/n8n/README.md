# unsubscribe lead lemlist and follow up task and lemlist mark as interested

This folder contains the **unsubscribe lead lemlist and follow up task and lemlist mark as interested** workflow. Its executable nodes use `httpRequest`, `hubspot`, `lemlist`, `lemlistTrigger`, `merge`, `openAi`, `slack`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`unsubscribe-lead-lemlist-and-follow-up-task-and-lemlist-mark-as-interested.json`](unsubscribe-lead-lemlist-and-follow-up-task-and-lemlist-mark-as-interested.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`, `lemlistApi`, `openAiApi`

**Entry nodes:** Lemlist - Lead Replied

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Lemlist - Unsubscribe | `lemlist` | lead / unsubscribe |
| follow up task | `hubspot` | engagement |
| Switch | `switch` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| lemlist - Mark as interested | `httpRequest` | Inspect parameters |
| HubSpot - Create Deal | `hubspot` | Inspect parameters |
| HubSpot - Get contact ID | `hubspot` | contact |
| Slack | `slack` | Inspect parameters |
| HubSpot - Get contact ID1 | `hubspot` | contact |
| Slack1 | `slack` | Inspect parameters |
| Lemlist - Lead Replied | `lemlistTrigger` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |

## Connection map

- Merge → Switch (`main`, output 0, input 0)
- OpenAI → Merge (`main`, output 0, input 0)
- Switch → Lemlist - Unsubscribe (`main`, output 0, input 0)
- Switch → lemlist - Mark as interested (`main`, output 1, input 0)
- Switch → HubSpot - Get contact ID (`main`, output 1, input 0)
- Switch → HubSpot - Get contact ID1 (`main`, output 2, input 0)
- Switch → Slack1 (`main`, output 3, input 0)
- HubSpot - Create Deal → Slack (`main`, output 0, input 0)
- Lemlist - Lead Replied → OpenAI (`main`, output 0, input 0)
- Lemlist - Lead Replied → Merge (`main`, output 0, input 1)
- HubSpot - Get contact ID → HubSpot - Create Deal (`main`, output 0, input 0)
- HubSpot - Get contact ID1 → follow up task (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Lemlist/0283_Lemlist_Slack_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Lemlist/0283_Lemlist_Slack_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
