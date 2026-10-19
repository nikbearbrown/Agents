# Convert URL HTML to Markdown and Get Page Links

This folder contains the **Convert URL HTML to Markdown and Get Page Links** workflow. Its executable nodes use `httpRequest`, `limit`, `manualTrigger`, `noOp`, `set`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`convert-url-html-to-markdown-and-get-page-links.json`](convert-url-html-to-markdown-and-get-page-links.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Connect to your own data source | `noOp` | Inspect parameters |
| Get urls from own data source | `noOp` | Inspect parameters |
| Example fields from data source | `set` | Inspect parameters |
| 40 items at a time | `limit` | Inspect parameters |
| 10 at a time | `splitInBatches` | Inspect parameters |
| Markdown data and Links | `set` | Inspect parameters |
| Split out page URLs | `splitOut` | Inspect parameters |
| Retrieve Page Markdown and Links | `httpRequest` | POST |

## Connection map

- Wait → 10 at a time (`main`, output 0, input 0)
- 10 at a time → Retrieve Page Markdown and Links (`main`, output 1, input 0)
- 40 items at a time → 10 at a time (`main`, output 0, input 0)
- Split out page URLs → 40 items at a time (`main`, output 0, input 0)
- Markdown data and Links → Connect to your own data source (`main`, output 0, input 0)
- Get urls from own data source → Example fields from data source (`main`, output 0, input 0)
- Connect to your own data source → Wait (`main`, output 0, input 0)
- Example fields from data source → Split out page URLs (`main`, output 0, input 0)
- Retrieve Page Markdown and Links → Markdown data and Links (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get urls from own data source (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0609_Wait_Limit_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0609_Wait_Limit_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
