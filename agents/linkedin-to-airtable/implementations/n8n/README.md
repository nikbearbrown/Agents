# Linkedin to Airtable

This folder contains the **Linkedin to Airtable** workflow. Its executable nodes use `airtable`, `filter`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-to-airtable.json`](linkedin-to-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch LinkedIn Likes | `httpRequest` | Inspect parameters |
| Split Liked Posts | `splitOut` | Inspect parameters |
| Filter Insightful & Recent | `filter` | Inspect parameters |
| Format Content Idea | `set` | Inspect parameters |
| Prepare for Airtable | `splitOut` | Inspect parameters |
| Save to Airtable | `airtable` | create |

## Connection map

- Schedule Trigger → Fetch LinkedIn Likes (`main`, output 0, input 0)
- Split Liked Posts → Filter Insightful & Recent (`main`, output 0, input 0)
- Format Content Idea → Prepare for Airtable (`main`, output 0, input 0)
- Fetch LinkedIn Likes → Split Liked Posts (`main`, output 0, input 0)
- Prepare for Airtable → Save to Airtable (`main`, output 0, input 0)
- Filter Insightful & Recent → Format Content Idea (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1888_Splitout_Schedule_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1888_Splitout_Schedule_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
