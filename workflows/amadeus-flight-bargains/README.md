# Amadeus Flight Bargains

This folder contains the **Amadeus Flight Bargains** workflow. Its executable nodes use `code`, `filter`, `gmail`, `httpRequest`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`amadeus-flight-bargains.json`](amadeus-flight-bargains.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `oAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| CarrierNameLookup | `code` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Get Dates | `code` | Inspect parameters |
| Merge & Extract | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Under Price | `filter` | Inspect parameters |
| FromTo | `set` | Inspect parameters |
| Amadeus Flight Search | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Carrier Codes | `httpRequest` | Inspect parameters |

## Connection map

- Wait → Loop Over Items (`main`, output 0, input 0)
- FromTo → CarrierNameLookup (`main`, output 0, input 0)
- Get Dates → Loop Over Items (`main`, output 0, input 0)
- Under Price → Gmail (`main`, output 0, input 0)
- Loop Over Items → Merge & Extract (`main`, output 0, input 0)
- Loop Over Items → Amadeus Flight Search (`main`, output 1, input 0)
- Merge & Extract → Under Price (`main`, output 0, input 0)
- Schedule Trigger → FromTo (`main`, output 0, input 0)
- CarrierNameLookup → Get Dates (`main`, output 0, input 0)
- Amadeus Flight Search → Wait (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0596_Wait_Code_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0596_Wait_Code_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
