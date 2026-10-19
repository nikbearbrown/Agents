# http request and get file github and n8n workflow detail

This folder contains the **http request and get file github and n8n workflow detail** workflow. Its executable nodes use `cron`, `function`, `github`, `httpRequest`, `manualTrigger`, `merge`, `noOp`, `set`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-get-file-github-and-n8n-workflow-detail.json`](http-request-and-get-file-github-and-n8n-workflow-detail.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`

**Entry nodes:** On clicking 'execute', Daily @ 20:00

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| dataArray | `function` | Inspect parameters |
| N8N Workflows | `httpRequest` | Inspect parameters |
| GitHub | `github` | file / get |
| Merge | `merge` | Inspect parameters |
| N8N Workflow Detail | `httpRequest` | Inspect parameters |
| github_status | `switch` | Inspect parameters |
| same | `noOp` | Inspect parameters |
| different | `noOp` | Inspect parameters |
| new | `noOp` | Inspect parameters |
| GitHub Edit | `github` | file / edit |
| GitHub Create | `github` | file |
| isDiffOrNew | `function` | Inspect parameters |
| Daily @ 20:00 | `cron` | Inspect parameters |
| OneAtATime | `splitInBatches` | Inspect parameters |
| Globals | `set` | Inspect parameters |

## Connection map

- new → GitHub Create (`main`, output 0, input 0)
- same → OneAtATime (`main`, output 0, input 0)
- Merge → isDiffOrNew (`main`, output 0, input 0)
- GitHub → Merge (`main`, output 0, input 0)
- Globals → N8N Workflows (`main`, output 0, input 0)
- dataArray → OneAtATime (`main`, output 0, input 0)
- different → GitHub Edit (`main`, output 0, input 0)
- OneAtATime → GitHub (`main`, output 0, input 0)
- OneAtATime → N8N Workflow Detail (`main`, output 0, input 0)
- GitHub Edit → OneAtATime (`main`, output 0, input 0)
- isDiffOrNew → github_status (`main`, output 0, input 0)
- Daily @ 20:00 → Globals (`main`, output 0, input 0)
- GitHub Create → OneAtATime (`main`, output 0, input 0)
- N8N Workflows → dataArray (`main`, output 0, input 0)
- github_status → same (`main`, output 0, input 0)
- github_status → different (`main`, output 1, input 0)
- github_status → new (`main`, output 2, input 0)
- N8N Workflow Detail → Merge (`main`, output 0, input 1)
- On clicking 'execute' → Globals (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/1149_GitHub_Manual_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/1149_GitHub_Manual_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
