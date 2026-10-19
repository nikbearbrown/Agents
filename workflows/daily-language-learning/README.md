# Daily Language Learning

This folder contains the **Daily Language Learning** workflow. Its executable nodes use `airtable`, `cron`, `function`, `hackerNews`, `lingvaNex`, `set`, `vonage`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`daily-language-learning.json`](daily-language-learning.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`, `lingvaNexApi`, `vonageApi`

**Entry nodes:** Daily trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Daily trigger | `cron` | Inspect parameters |
| Get top 3 articles | `hackerNews` | all |
| Extract words | `function` | Inspect parameters |
| Translate | `lingvaNex` | Inspect parameters |
| Filter data  | `set` | Inspect parameters |
| Save today's words | `airtable` | append |
| Craft message | `function` | Inspect parameters |
| Send SMS | `vonage` | Inspect parameters |

## Connection map

- Translate → Filter data  (`main`, output 0, input 0)
- Filter data  → Craft message (`main`, output 0, input 0)
- Filter data  → Save today's words (`main`, output 0, input 0)
- Craft message → Send SMS (`main`, output 0, input 0)
- Daily trigger → Get top 3 articles (`main`, output 0, input 0)
- Extract words → Translate (`main`, output 0, input 0)
- Get top 3 articles → Extract words (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Airtable/1138_Airtable_Vonage_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Airtable/1138_Airtable_Vonage_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
