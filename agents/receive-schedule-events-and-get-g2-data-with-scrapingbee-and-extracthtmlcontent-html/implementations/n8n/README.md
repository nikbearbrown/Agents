# receive schedule events and get g2 data with scrapingbee and extracthtmlcontent html

This folder contains the **receive schedule events and get g2 data with scrapingbee and extracthtmlcontent html** workflow. Its executable nodes use `code`, `googleSheets`, `html`, `httpRequest`, `itemLists`, `markdown`, `merge`, `scheduleTrigger`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-get-g2-data-with-scrapingbee-and-extracthtmlcontent-html.json`](receive-schedule-events-and-get-g2-data-with-scrapingbee-and-extracthtmlcontent-html.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Execute workflow every day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Add your competitors here | `code` | Inspect parameters |
| Execute workflow every day | `scheduleTrigger` | Inspect parameters |
| Get G2 data with ScrapingBee | `httpRequest` | Inspect parameters |
| Get review section HTML | `html` | extractHtmlContent |
| Iterate on reviews | `itemLists` | Inspect parameters |
| Extract structured data | `html` | extractHtmlContent |
| Convert Review HTML to Markdown | `markdown` | Inspect parameters |
| Get all past reviews | `googleSheets` | Inspect parameters |
| Continue only if review is new | `merge` | Inspect parameters |
| Send new review to Slack | `slack` | Inspect parameters |
| Add new review to Google Sheets | `googleSheets` | append |

## Connection map

- Iterate on reviews → Extract structured data (`main`, output 0, input 0)
- Get all past reviews → Continue only if review is new (`main`, output 0, input 0)
- Extract structured data → Convert Review HTML to Markdown (`main`, output 0, input 0)
- Get review section HTML → Iterate on reviews (`main`, output 0, input 0)
- Add your competitors here → Get G2 data with ScrapingBee (`main`, output 0, input 0)
- Execute workflow every day → Get all past reviews (`main`, output 0, input 0)
- Execute workflow every day → Add your competitors here (`main`, output 0, input 0)
- Get G2 data with ScrapingBee → Get review section HTML (`main`, output 0, input 0)
- Continue only if review is new → Add new review to Google Sheets (`main`, output 0, input 0)
- Continue only if review is new → Send new review to Slack (`main`, output 0, input 0)
- Convert Review HTML to Markdown → Continue only if review is new (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0370_Code_Schedule_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0370_Code_Schedule_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
