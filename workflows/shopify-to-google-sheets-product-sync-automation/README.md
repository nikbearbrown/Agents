# Shopify to Google Sheets Product Sync Automation

This folder contains the **Shopify to Google Sheets Product Sync Automation** workflow. Its executable nodes use `code`, `googleSheets`, `graphql`, `if`, `noOp`, `scheduleTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`shopify-to-google-sheets-product-sync-automation.json`](shopify-to-google-sheets-product-sync-automation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Wait1 | `wait` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Shopify get products | `graphql` | Inspect parameters |
| Split output | `code` | Inspect parameters |
| Check if there is next page | `if` | Inspect parameters |
| writing first product details | `googleSheets` | append |
| Set cursor | `set` | Inspect parameters |
| writing remaning product info to google sheets | `googleSheets` | append |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| update Curser | `googleSheets` | update |
| If | `if` | Inspect parameters |
| Code | `code` | Inspect parameters |
| BatchSize | `set` | Inspect parameters |
| LastCursor | `googleSheets` | Inspect parameters |
| shopify-initial | `graphql` | Inspect parameters |
| Check cursor is not empty | `if` | Inspect parameters |

## Connection map

- If → shopify-initial (`main`, output 0, input 0)
- If → Code (`main`, output 1, input 0)
- Code → Shopify get products (`main`, output 0, input 0)
- Wait1 → Set cursor (`main`, output 0, input 0)
- BatchSize → LastCursor (`main`, output 0, input 0)
- LastCursor → If (`main`, output 0, input 0)
- Set cursor → Shopify get products (`main`, output 0, input 0)
- Split output → writing remaning product info to google sheets (`main`, output 0, input 0)
- shopify-initial → writing first product details (`main`, output 0, input 0)
- Schedule Trigger → BatchSize (`main`, output 0, input 0)
- Shopify get products → Split output (`main`, output 0, input 0)
- Shopify get products → Check cursor is not empty (`main`, output 0, input 0)
- Check cursor is not empty → update Curser (`main`, output 0, input 0)
- Check if there is next page → No Operation, do nothing (`main`, output 0, input 0)
- Check if there is next page → Wait1 (`main`, output 1, input 0)
- writing first product details → Code (`main`, output 0, input 0)
- writing remaning product info to google sheets → Check if there is next page (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1743_Wait_Code_Sync_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1743_Wait_Code_Sync_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
