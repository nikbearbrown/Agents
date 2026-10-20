# Monitor Competitor Pricing

This folder contains the **Monitor Competitor Pricing** workflow. Its executable nodes use `airtop`, `code`, `filter`, `googleSheets`, `manualTrigger`, `merge`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`monitor-competitor-pricing.json`](monitor-competitor-pricing.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtopApi`, `googleSheetsOAuth2Api`, `slackApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get Pricing URLs | `googleSheets` | Inspect parameters |
| Check pricing | `airtop` | extraction / query |
| Parse response | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Update pricing | `googleSheets` | update |
| Notify pricing change | `slack` | Inspect parameters |
| Filter out similar | `filter` | Inspect parameters |

## Connection map

- Merge → Parse response (`main`, output 0, input 0)
- Check pricing → Merge (`main`, output 0, input 0)
- Parse response → Filter out similar (`main`, output 0, input 0)
- Get Pricing URLs → Check pricing (`main`, output 0, input 0)
- Get Pricing URLs → Merge (`main`, output 0, input 1)
- Filter out similar → Update pricing (`main`, output 0, input 0)
- Filter out similar → Notify pricing change (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Pricing URLs (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1759_Code_Filter_Monitor_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1759_Code_Filter_Monitor_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
