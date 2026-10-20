# Notion to Linkedin

This folder contains the **Notion to Linkedin** workflow. Its executable nodes use `aggregate`, `code`, `httpRequest`, `linkedIn`, `merge`, `notion`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`notion-to-linkedin.json`](notion-to-linkedin.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `linkedInOAuth2Api`, `notionApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Merge | `merge` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Filter the table for the day's post | `notion` | databasePage / getAll |
| Fetch the content on the page | `notion` | block / getAll |
| Aggregate the Notion blocks | `aggregate` | Inspect parameters |
| Format the post | `code` | Inspect parameters |
| Download image | `httpRequest` | Inspect parameters |
| Publish on LinkedIn | `linkedIn` | Inspect parameters |
| Update post status in notion database | `notion` | databasePage / update |

## Connection map

- Merge → Publish on LinkedIn (`main`, output 0, input 0)
- Download image → Merge (`main`, output 0, input 1)
- Format the post → Merge (`main`, output 0, input 0)
- Schedule Trigger → Filter the table for the day's post (`main`, output 0, input 0)
- Publish on LinkedIn → Update post status in notion database (`main`, output 0, input 0)
- Aggregate the Notion blocks → Format the post (`main`, output 0, input 0)
- Aggregate the Notion blocks → Download image (`main`, output 0, input 0)
- Fetch the content on the page → Aggregate the Notion blocks (`main`, output 0, input 0)
- Filter the table for the day's post → Fetch the content on the page (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1939_Linkedin_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1939_Linkedin_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
