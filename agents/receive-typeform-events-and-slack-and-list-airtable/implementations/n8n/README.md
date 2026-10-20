# receive typeform events and slack and list airtable

This folder contains the **receive typeform events and slack and list airtable** workflow. Its executable nodes use `airtable`, `dropcontact`, `if`, `set`, `slack`, `typeformTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-typeform-events-and-slack-and-list-airtable.json`](receive-typeform-events-and-slack-and-list-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `dropcontactApi`, `slackApi`, `typeformApi`

**Entry nodes:** Typeform Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Typeform Trigger | `typeformTrigger` | Inspect parameters |
| Slack1 | `slack` | Inspect parameters |
| Airtable - Contact List | `airtable` | list |
| Airtable - Update Contacts1 | `airtable` | update |
| Slack | `slack` | Inspect parameters |
| Set - Contacts to update | `set` | Inspect parameters |
| Dropcontact | `dropcontact` | Inspect parameters |
| Contact ID empty ? | `if` | Inspect parameters |
| Airtable - Create Contacts | `airtable` | append |
| Set - Contacts to create | `set` | Inspect parameters |

## Connection map

- Dropcontact → Airtable - Contact List (`main`, output 0, input 0)
- Typeform Trigger → Dropcontact (`main`, output 0, input 0)
- Contact ID empty ? → Set - Contacts to update (`main`, output 0, input 0)
- Contact ID empty ? → Set - Contacts to create (`main`, output 1, input 0)
- Airtable - Contact List → Contact ID empty ? (`main`, output 0, input 0)
- Set - Contacts to create → Airtable - Update Contacts1 (`main`, output 0, input 0)
- Set - Contacts to update → Airtable - Create Contacts (`main`, output 0, input 0)
- Airtable - Create Contacts → Slack (`main`, output 0, input 0)
- Airtable - Update Contacts1 → Slack1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0124_Slack_Typeform_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0124_Slack_Typeform_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
