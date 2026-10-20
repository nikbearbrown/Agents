# Walkthrough and Overview

This folder contains the **Walkthrough and Overview** workflow. Its executable nodes use `airtable`, `airtableTrigger`, `code`, `httpRequest`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`walkthrough-and-overview.json`](walkthrough-and-overview.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Entered View  "First Task - Create Task"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Automated Task | `airtable` | get |
| Create Task | `httpRequest` | POST |
| Get Task Template | `airtable` | get |
| Get Assignee | `airtable` | get |
| Get Client | `airtable` | get |
| Calculate Dates | `code` | Inspect parameters |
| Update Automated Record | `httpRequest` | PATCH |
| Notify Assignee | `slack` | Inspect parameters |
| Entered View  "First Task - Create Task" | `airtableTrigger` | Inspect parameters |
| Airtable Base ID's | `set` | Inspect parameters |

## Connection map

- Get Client → Calculate Dates (`main`, output 0, input 0)
- Create Task → Update Automated Record (`main`, output 0, input 0)
- Get Assignee → Get Client (`main`, output 0, input 0)
- Calculate Dates → Create Task (`main`, output 0, input 0)
- Get Task Template → Get Assignee (`main`, output 0, input 0)
- Airtable Base ID's → Get Automated Task (`main`, output 0, input 0)
- Get Automated Task → Get Task Template (`main`, output 0, input 0)
- Update Automated Record → Notify Assignee (`main`, output 0, input 0)
- Entered View  "First Task - Create Task" → Airtable Base ID's (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0393_Code_Slack_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0393_Code_Slack_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
