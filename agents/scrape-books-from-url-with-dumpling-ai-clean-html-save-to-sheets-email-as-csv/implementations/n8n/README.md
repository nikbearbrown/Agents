# Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV

This folder contains the **Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV** workflow. Its executable nodes use `convertToFile`, `gmail`, `googleSheetsTrigger`, `html`, `httpRequest`, `sort`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-books-from-url-with-dumpling-ai-clean-html-save-to-sheets-email-as-csv.json`](scrape-books-from-url-with-dumpling-ai-clean-html-save-to-sheets-email-as-csv.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsTriggerOAuth2Api`, `httpBasicAuth`, `httpHeaderAuth`

**Entry nodes:** Trigger- Watches For new URL in Spreadsheet

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Convert to CSV File | `convertToFile` | Inspect parameters |
| Extract all books from the page | `html` | extractHtmlContent |
| Sort by price | `sort` | Inspect parameters |
| Extract individual book price | `html` | extractHtmlContent |
| Send CSV via e-mail | `gmail` | Inspect parameters |
| Trigger- Watches For new URL in Spreadsheet | `googleSheetsTrigger` | Inspect parameters |
| Scrape Website Content with Dumpling AI | `httpRequest` | POST |
| Split HTML Array into Individual Books | `splitOut` | Inspect parameters |

## Connection map

- Sort by price → Convert to CSV File (`main`, output 0, input 0)
- Convert to CSV File → Send CSV via e-mail (`main`, output 0, input 0)
- Extract individual book price → Sort by price (`main`, output 0, input 0)
- Extract all books from the page → Split HTML Array into Individual Books (`main`, output 0, input 0)
- Split HTML Array into Individual Books → Extract individual book price (`main`, output 0, input 0)
- Scrape Website Content with Dumpling AI → Extract all books from the page (`main`, output 0, input 0)
- Trigger- Watches For new URL in Spreadsheet → Scrape Website Content with Dumpling AI (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1648_Splitout_Converttofile_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1648_Splitout_Converttofile_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
