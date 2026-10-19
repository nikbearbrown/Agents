# receive notion events and webhook and update database page notion

This folder contains the **receive notion events and webhook and update database page notion** workflow. Its executable nodes use `function`, `interval`, `notion`, `notionTrigger`, `signl4`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-notion-events-and-webhook-and-update-database-page-notion.json`](receive-notion-events-and-webhook-and-update-database-page-notion.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `signl4Api`

**Entry nodes:** Notion Trigger, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Function | `function` | Inspect parameters |
| Notion Trigger | `notionTrigger` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Function | `function` | Inspect parameters |
| Notion Update | `notion` | databasePage / update |
| Interval | `interval` | Inspect parameters |
| SIGNL4 Resolve | `signl4` | resolve |
| SIGNL4 Alert | `signl4` | Inspect parameters |
| Notion Update Read | `notion` | databasePage / update |
| Notion Read Open | `notion` | databasePage / getAll |
| Notion Read New | `notion` | databasePage / getAll |
| Notion Update Final | `notion` | databasePage / update |
| SIGNL4 Alert 2 | `signl4` | Inspect parameters |

## Connection map

- Webhook → Function (`main`, output 0, input 0)
- Function → Notion Update (`main`, output 0, input 0)
- Interval → Notion Read Open (`main`, output 0, input 0)
- Interval → Notion Read New (`main`, output 0, input 0)
- Notion Trigger → SIGNL4 Alert (`main`, output 0, input 0)
- SIGNL4 Alert 2 → Notion Update Read (`main`, output 0, input 0)
- SIGNL4 Resolve → Notion Update Final (`main`, output 0, input 0)
- Notion Read New → SIGNL4 Alert 2 (`main`, output 0, input 0)
- Notion Read Open → SIGNL4 Resolve (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"duplicate_node_names": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Signl4/0055_Signl4_Interval_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Signl4/0055_Signl4_Interval_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
