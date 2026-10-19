# 💫 To setup this template

This folder contains the **💫 To setup this template** workflow. Its executable nodes use `filter`, `openAi`, `scheduleTrigger`, `set`, `todoist`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`to-setup-this-template.json`](to-setup-this-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `todoistApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Update priority in todoist | `todoist` | update |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get inbox tasks | `todoist` | getAll |
| Your Projects | `set` | Inspect parameters |
| Categorize | `openAi` | Inspect parameters |
| If task is not a subtask | `filter` | Inspect parameters |
| If other or ai hallucinates | `filter` | Inspect parameters |

## Connection map

- Categorize → If other or ai hallucinates (`main`, output 0, input 0)
- Your Projects → Get inbox tasks (`main`, output 0, input 0)
- Get inbox tasks → If task is not a subtask (`main`, output 0, input 0)
- Schedule Trigger → Your Projects (`main`, output 0, input 0)
- If task is not a subtask → Categorize (`main`, output 0, input 0)
- If other or ai hallucinates → Update priority in todoist (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0563_Schedule_Filter_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0563_Schedule_Filter_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
