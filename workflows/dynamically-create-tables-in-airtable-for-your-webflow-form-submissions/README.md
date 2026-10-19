# Dynamically create tables in Airtable for your Webflow form submissions

This folder contains the **Dynamically create tables in Airtable for your Webflow form submissions** workflow. Its executable nodes use `airtable`, `code`, `httpRequest`, `if`, `set`, `webflowTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dynamically-create-tables-in-airtable-for-your-webflow-form-submissions.json`](dynamically-create-tables-in-airtable-for-your-webflow-form-submissions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableOAuth2Api`, `airtableTokenApi`, `webflowApi`

**Entry nodes:** Webflow Submission Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webflow Submission Trigger | `webflowTrigger` | Inspect parameters |
| Prepare form submission for workflow | `set` | Inspect parameters |
| Get Form Index Reference Table ID | `code` | Inspect parameters |
| Does Index Reference Table Exist? | `if` | Inspect parameters |
| [AIRTABLE]  Create Index Reference Table | `httpRequest` | POST |
| [AIRTABLE] Get Base Schema from list | `airtable` | base / getSchema |
| [AIRTABLE] Create Webflow Form Table | `httpRequest` | POST |
| Set New Webflow Form Table ID | `code` | Inspect parameters |
| [AIRTABLE] Insert Record In Form Index Reference Table | `airtable` | create |
| [AIRTABLE] Insert Record In Webflow Form Table | `airtable` | create |
| [AIRTABLE] Find Webflow Form Record In Form Index Reference Table | `airtable` | search |
| Set Webflow Form Table ID | `code` | Inspect parameters |
| Does This Webflow Form Table Exist? | `if` | Inspect parameters |

## Connection map

- Set Webflow Form Table ID → Does This Webflow Form Table Exist? (`main`, output 0, input 0)
- Webflow Submission Trigger → Prepare form submission for workflow (`main`, output 0, input 0)
- Set New Webflow Form Table ID → [AIRTABLE] Insert Record In Form Index Reference Table (`main`, output 0, input 0)
- Does Index Reference Table Exist? → [AIRTABLE] Find Webflow Form Record In Form Index Reference Table (`main`, output 0, input 0)
- Does Index Reference Table Exist? → [AIRTABLE]  Create Index Reference Table (`main`, output 1, input 0)
- Get Form Index Reference Table ID → Does Index Reference Table Exist? (`main`, output 0, input 0)
- Does This Webflow Form Table Exist? → [AIRTABLE] Insert Record In Webflow Form Table (`main`, output 0, input 0)
- Does This Webflow Form Table Exist? → [AIRTABLE] Create Webflow Form Table (`main`, output 1, input 0)
- Prepare form submission for workflow → [AIRTABLE] Get Base Schema from list (`main`, output 0, input 0)
- [AIRTABLE] Create Webflow Form Table → Set New Webflow Form Table ID (`main`, output 0, input 0)
- [AIRTABLE] Get Base Schema from list → Get Form Index Reference Table ID (`main`, output 0, input 0)
- [AIRTABLE]  Create Index Reference Table → [AIRTABLE] Create Webflow Form Table (`main`, output 0, input 0)
- [AIRTABLE] Insert Record In Form Index Reference Table → [AIRTABLE] Insert Record In Webflow Form Table (`main`, output 0, input 0)
- [AIRTABLE] Find Webflow Form Record In Form Index Reference Table → Set Webflow Form Table ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1514_Code_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1514_Code_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
