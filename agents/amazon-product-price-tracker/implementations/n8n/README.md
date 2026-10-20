# Amazon Product Price Tracker

This folder contains the **Amazon Product Price Tracker** workflow. Its executable nodes use `emailSend`, `googleSheets`, `httpRequest`, `if`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`amazon-product-price-tracker.json`](amazon-product-price-tracker.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `smtp`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Products to Monitor | `googleSheets` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Scrapeops - Amazon Product | `httpRequest` | Inspect parameters |
| Fields | `set` | Inspect parameters |
| Last Price | `set` | Inspect parameters |
| Price Change | `set` | Inspect parameters |
| Alert Status | `set` | Inspect parameters |
| Insert - Price History | `googleSheets` | append |
| Update - Products to Monitor | `googleSheets` | update |
| Send Email | `emailSend` | Inspect parameters |
| Check Valid Price | `if` | Inspect parameters |
| Alert Decision | `if` | Inspect parameters |
| Setup | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Setup → Products to Monitor (`main`, output 0, input 0)
- Fields → Check Valid Price (`main`, output 0, input 0)
- Last Price → Scrapeops - Amazon Product (`main`, output 0, input 0)
- Send Email → Loop Over Items (`main`, output 0, input 0)
- Alert Status → Update - Products to Monitor (`main`, output 0, input 0)
- Price Change → Alert Status (`main`, output 0, input 0)
- Alert Decision → Send Email (`main`, output 0, input 0)
- Alert Decision → Loop Over Items (`main`, output 1, input 0)
- Loop Over Items → Last Price (`main`, output 1, input 0)
- Schedule Trigger → Setup (`main`, output 0, input 0)
- Check Valid Price → Price Change (`main`, output 0, input 0)
- Check Valid Price → Loop Over Items (`main`, output 1, input 0)
- Products to Monitor → Loop Over Items (`main`, output 0, input 0)
- Insert - Price History → Alert Decision (`main`, output 0, input 0)
- Scrapeops - Amazon Product → Fields (`main`, output 0, input 0)
- Update - Products to Monitor → Insert - Price History (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1697_Schedule_HTTP_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1697_Schedule_HTTP_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
