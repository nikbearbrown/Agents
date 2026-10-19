# Generate New Keywords with Search Volumes⚒️⚒️🟢🟢

This folder contains the **Generate New Keywords with Search Volumes⚒️⚒️🟢🟢** workflow. Its executable nodes use `executeWorkflowTrigger`, `googleSheets`, `httpRequest`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-new-keywords-with-search-volumes.json`](generate-new-keywords-with-search-volumes.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleAdsOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Generate new keywords | `httpRequest` | POST |
| Edit Fields | `set` | Inspect parameters |
| Set Keywords | `set` | Inspect parameters |
| Upsert | `googleSheets` | append |
| Trigger | `executeWorkflowTrigger` | Inspect parameters |

## Connection map

- Trigger → Set Keywords (`main`, output 0, input 0)
- Split Out → Edit Fields (`main`, output 0, input 0)
- Edit Fields → Upsert (`main`, output 0, input 0)
- Set Keywords → Generate new keywords (`main`, output 0, input 0)
- Generate new keywords → Split Out (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1660_Splitout_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1660_Splitout_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
