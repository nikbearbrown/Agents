# Get Comments from Facebook Page

This folder contains the **Get Comments from Facebook Page** workflow. Its executable nodes use `code`, `facebookGraphApi`, `filter`, `manualTrigger`, `merge`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-comments-from-facebook-page.json`](get-comments-from-facebook-page.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Split Out Comments | `splitOut` | Inspect parameters |
| Filter Out Null Comments | `filter` | Inspect parameters |
| Select Result Field | `set` | Inspect parameters |
| Split Out Posts | `splitOut` | Inspect parameters |
| Facebook Graph API : Get Post from Page | `facebookGraphApi` | Inspect parameters |
| Facebook : Get Each Post Comments | `facebookGraphApi` | Inspect parameters |
| Merge Post & Comments | `merge` | Inspect parameters |
| Reverse Item to Match another Branch | `code` | Inspect parameters |
| Set PageID & Number of Latest Posts | `set` | Inspect parameters |

## Connection map

- Split Out Posts → Facebook : Get Each Post Comments (`main`, output 0, input 0)
- Split Out Posts → Reverse Item to Match another Branch (`main`, output 0, input 0)
- Split Out Comments → Select Result Field (`main`, output 0, input 0)
- Merge Post & Comments → Filter Out Null Comments (`main`, output 0, input 0)
- Filter Out Null Comments → Split Out Comments (`main`, output 0, input 0)
- Facebook : Get Each Post Comments → Merge Post & Comments (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set PageID & Number of Latest Posts (`main`, output 0, input 0)
- Set PageID & Number of Latest Posts → Facebook Graph API : Get Post from Page (`main`, output 0, input 0)
- Reverse Item to Match another Branch → Merge Post & Comments (`main`, output 0, input 1)
- Facebook Graph API : Get Post from Page → Split Out Posts (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1058_Splitout_Code_Import_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1058_Splitout_Code_Import_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
