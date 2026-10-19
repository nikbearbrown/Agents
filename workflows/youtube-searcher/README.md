# Youtube Searcher

This folder contains the **Youtube Searcher** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `httpRequest`, `if`, `manualTrigger`, `postgres`, `set`, `splitInBatches`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-searcher.json`](youtube-searcher.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`, `youTubeOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Items | `splitInBatches` | Inspect parameters |
| find_video_data1 | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| fetch_last_registered | `postgres` | executeQuery |
| get_videos | `youTube` | video |
| if_is_empty | `if` | Inspect parameters |
| Postgres | `postgres` | executeQuery |
| insert_items | `postgres` | executeQuery |
| create_table | `postgres` | executeQuery |
| remove_shorts | `code` | Inspect parameters |
| create_query | `code` | Inspect parameters |
| structure_data | `code` | Inspect parameters |
| if_empty | `if` | Inspect parameters |
| already_populated | `set` | Inspect parameters |
| map_data | `set` | Inspect parameters |
| sanitize_data | `code` | Inspect parameters |
| see table | `postgres` | executeQuery |
| drop table | `postgres` | executeQuery |

## Connection map

- Postgres → sanitize_data (`main`, output 0, input 0)
- if_empty → map_data (`main`, output 0, input 0)
- if_empty → Loop Over Items (`main`, output 1, input 0)
- map_data → structure_data (`main`, output 0, input 0)
- get_videos → if_is_empty (`main`, output 0, input 0)
- if_is_empty → find_video_data1 (`main`, output 0, input 0)
- if_is_empty → already_populated (`main`, output 1, input 0)
- create_query → insert_items (`main`, output 0, input 0)
- insert_items → Loop Over Items (`main`, output 0, input 0)
- remove_shorts → if_empty (`main`, output 0, input 0)
- structure_data → create_query (`main`, output 0, input 0)
- Loop Over Items → fetch_last_registered (`main`, output 1, input 0)
- find_video_data1 → remove_shorts (`main`, output 0, input 0)
- already_populated → Loop Over Items (`main`, output 0, input 0)
- fetch_last_registered → get_videos (`main`, output 0, input 0)
- Execute Workflow Trigger → Postgres (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1788_Postgres_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Postgres/1788_Postgres_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
