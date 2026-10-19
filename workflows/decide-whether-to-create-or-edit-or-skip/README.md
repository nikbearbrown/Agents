# Decide Whether to Create or Edit or Skip

This folder contains the **Decide Whether to Create or Edit or Skip** workflow. Its executable nodes use `aggregate`, `filter`, `gitlab`, `if`, `manualTrigger`, `n8n`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`decide-whether-to-create-or-edit-or-skip.json`](decide-whether-to-create-or-edit-or-skip.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gitlabApi`, `n8nApi`

**Entry nodes:** Backup Now - Manual Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Backup Now - Manual Trigger | `manualTrigger` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Create New File(s) | `gitlab` | file |
| Edit Existing File(s) | `gitlab` | file / edit |
| Derive Filename From Workflow Name | `set` | Inspect parameters |
| Fetch Existing File Content | `gitlab` | file / get |
| Skip Unchanged Files | `filter` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch List of Existing Files | `gitlab` | file / list |
| Combine Gitlab Existing Files as Single List Item | `aggregate` | Inspect parameters |
| File Exists in Gitlab? | `if` | Inspect parameters |

## Connection map

- n8n → Derive Filename From Workflow Name (`main`, output 0, input 0)
- Globals → Fetch List of Existing Files (`main`, output 0, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- Skip Unchanged Files → Edit Existing File(s) (`main`, output 0, input 0)
- File Exists in Gitlab? → Fetch Existing File Content (`main`, output 0, input 0)
- File Exists in Gitlab? → Create New File(s) (`main`, output 1, input 0)
- Backup Now - Manual Trigger → Globals (`main`, output 0, input 0)
- Fetch Existing File Content → Skip Unchanged Files (`main`, output 0, input 0)
- Fetch List of Existing Files → Combine Gitlab Existing Files as Single List Item (`main`, output 0, input 0)
- Derive Filename From Workflow Name → File Exists in Gitlab? (`main`, output 0, input 0)
- Combine Gitlab Existing Files as Single List Item → n8n (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gitlab/0557_Gitlab_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gitlab/0557_Gitlab_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
