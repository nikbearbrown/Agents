# Backup workflows to git repository

This folder contains the **Backup workflows to git repository** workflow. Its executable nodes use `code`, `github`, `if`, `n8n`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`backup-workflows-to-git-repository.json`](backup-workflows-to-git-repository.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `n8nApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| GitHub | `github` | file / get |
| Globals | `set` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| If | `if` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Create new file and commit | `github` | file |
| Update file content and commit | `github` | file / edit |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- If → Code (`main`, output 0, input 0)
- If → Create new file and commit (`main`, output 1, input 0)
- If1 → Update file content and commit (`main`, output 0, input 0)
- If1 → Loop Over Items (`main`, output 1, input 0)
- n8n → Loop Over Items (`main`, output 0, input 0)
- Code → If1 (`main`, output 0, input 0)
- GitHub → If (`main`, output 0, input 0)
- Globals → n8n (`main`, output 0, input 0)
- Loop Over Items → GitHub (`main`, output 1, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- Create new file and commit → Loop Over Items (`main`, output 0, input 0)
- Update file content and commit → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0628_Code_Schedule_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0628_Code_Schedule_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
