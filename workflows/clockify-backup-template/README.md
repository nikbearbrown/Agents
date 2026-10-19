# Clockify Backup Template

This folder contains the **Clockify Backup Template** workflow. Its executable nodes use `clockify`, `compareDatasets`, `extractFromFile`, `filter`, `github`, `httpRequest`, `if`, `scheduleTrigger`, `set`, `splitOut`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clockify-backup-template.json`](clockify-backup-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clockifyApi`, `githubApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract from File | `extractFromFile` | fromJson |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Set month indexes | `set` | Inspect parameters |
| Split Out indexes | `splitOut` | Inspect parameters |
| Set intervals | `set` | Inspect parameters |
| Skip empty reports | `filter` | Inspect parameters |
| Get first workspace | `clockify` | workspace |
| Get detailed monthly report | `httpRequest` | POST |
| Check if file exists in GitHub | `github` | file / get |
| Point to new data | `set` | Inspect parameters |
| Check for 404 error message | `if` | Inspect parameters |
| Update file in GitHub | `github` | file / edit |
| Create file in GitHub | `github` | file |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Globals → Set month indexes (`main`, output 0, input 0)
- Set intervals → Get detailed monthly report (`main`, output 0, input 0)
- Compare Datasets → Update file in GitHub (`main`, output 0, input 0)
- Schedule Trigger → Get first workspace (`main`, output 0, input 0)
- Extract from File → Compare Datasets (`main`, output 0, input 1)
- Point to new data → Compare Datasets (`main`, output 0, input 0)
- Set month indexes → Split Out indexes (`main`, output 0, input 0)
- Split Out indexes → Set intervals (`main`, output 0, input 0)
- Skip empty reports → Create file in GitHub (`main`, output 0, input 0)
- Get first workspace → Globals (`main`, output 0, input 0)
- Check for 404 error message → Skip empty reports (`main`, output 0, input 0)
- Check for 404 error message → Stop and Error (`main`, output 1, input 0)
- Get detailed monthly report → Check if file exists in GitHub (`main`, output 0, input 0)
- Check if file exists in GitHub → Point to new data (`main`, output 0, input 0)
- Check if file exists in GitHub → Extract from File (`main`, output 0, input 0)
- Check if file exists in GitHub → Check for 404 error message (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1896_Stopanderror_Splitout_Export_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1896_Stopanderror_Splitout_Export_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
