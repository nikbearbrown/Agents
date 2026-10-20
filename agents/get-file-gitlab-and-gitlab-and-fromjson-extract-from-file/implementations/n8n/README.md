# get file gitlab and gitlab and fromjson extract from file

This folder contains the **get file gitlab and gitlab and fromjson extract from file** workflow. Its executable nodes use `code`, `extractFromFile`, `gitlab`, `manualTrigger`, `n8n`, `noOp`, `set`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-file-gitlab-and-gitlab-and-fromjson-extract-from-file.json`](get-file-gitlab-and-gitlab-and-fromjson-extract-from-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gitlabApi`, `n8nApi`

**Entry nodes:** When clicking "Test Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test Workflow" | `manualTrigger` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Result | `noOp` | Inspect parameters |
| Current workflow | `noOp` | Inspect parameters |
| Loop Over Workflows | `splitInBatches` | Inspect parameters |
| Get file | `gitlab` | file / get |
| File status | `code` | Inspect parameters |
| Status error | `set` | Inspect parameters |
| End Loop | `noOp` | Inspect parameters |
| Create file | `gitlab` | file |
| Extract From File | `extractFromFile` | fromJson |
| Switch | `switch` | Inspect parameters |
| New file version | `gitlab` | file / edit |
| Error output to normal output | `noOp` | Inspect parameters |
| Status new | `set` | Inspect parameters |
| Status diff | `set` | Inspect parameters |
| Status same | `set` | Inspect parameters |
| Retrieve all workflows | `n8n` | Inspect parameters |
| Save each version in a different field | `set` | Inspect parameters |

## Connection map

- Switch → Create file (`main`, output 0, input 0)
- Switch → Status same (`main`, output 1, input 0)
- Switch → New file version (`main`, output 2, input 0)
- Switch → Status error (`main`, output 3, input 0)
- Globals → Retrieve all workflows (`main`, output 0, input 0)
- End Loop → Loop Over Workflows (`main`, output 0, input 0)
- Get file → Extract From File (`main`, output 0, input 0)
- Get file → Error output to normal output (`main`, output 1, input 0)
- Status new → End Loop (`main`, output 0, input 0)
- Create file → Status new (`main`, output 0, input 0)
- Create file → Status error (`main`, output 1, input 0)
- File status → Switch (`main`, output 0, input 0)
- Status diff → End Loop (`main`, output 0, input 0)
- Status same → End Loop (`main`, output 0, input 0)
- Status error → End Loop (`main`, output 0, input 0)
- Current workflow → Get file (`main`, output 0, input 0)
- New file version → Status diff (`main`, output 0, input 0)
- New file version → Status error (`main`, output 1, input 0)
- Extract From File → Save each version in a different field (`main`, output 0, input 0)
- Loop Over Workflows → Result (`main`, output 0, input 0)
- Loop Over Workflows → Current workflow (`main`, output 1, input 0)
- Retrieve all workflows → Loop Over Workflows (`main`, output 0, input 0)
- Error output to normal output → File status (`main`, output 0, input 0)
- When clicking "Test Workflow" → Globals (`main`, output 0, input 0)
- Save each version in a different field → File status (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gitlab/0561_Gitlab_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gitlab/0561_Gitlab_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
