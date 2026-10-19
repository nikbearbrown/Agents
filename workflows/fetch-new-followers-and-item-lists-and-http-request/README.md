# fetch new followers and item lists and http request

This folder contains the **fetch new followers and item lists and http request** workflow. Its executable nodes use `editImage`, `function`, `httpRequest`, `itemLists`, `manualTrigger`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-new-followers-and-item-lists-and-http-request.json`](fetch-new-followers-and-item-lists-and-http-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `oAuth1Api`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Fetch new followers | `httpRequest` | Inspect parameters |
| Item Lists | `itemLists` | Inspect parameters |
| Function | `function` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Fetching images | `httpRequest` | Inspect parameters |
| Fetch bg | `httpRequest` | Inspect parameters |
| Resize | `editImage` | resize |
| Crop | `editImage` | multiStep |
| Edit Image | `editImage` | multiStep |
| Resize1 | `editImage` | resize |
| HTTP Request | `httpRequest` | Inspect parameters |

## Connection map

- Crop → Resize1 (`main`, output 0, input 0)
- Merge → Edit Image (`main`, output 0, input 0)
- Resize → Crop (`main`, output 0, input 0)
- Resize1 → Function (`main`, output 0, input 0)
- Fetch bg → Merge (`main`, output 0, input 0)
- Function → Merge (`main`, output 0, input 1)
- Edit Image → HTTP Request (`main`, output 0, input 0)
- Item Lists → Fetching images (`main`, output 0, input 0)
- Fetching images → Resize (`main`, output 0, input 0)
- Fetch new followers → Item Lists (`main`, output 0, input 0)
- On clicking 'execute' → Fetch new followers (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0137_Manual_Editimage_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0137_Manual_Editimage_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `fetch-new-followers-and-item-lists-and-http-request-f549bbbc` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
