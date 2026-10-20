# Scrape Today's Github Trend 13 Top Repositories

This folder contains the **Scrape Today's Github Trend 13 Top Repositories** workflow. Its executable nodes use `html`, `httpRequest`, `manualTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scrape-today-s-github-trend-13-top-repositories.json`](scrape-today-s-github-trend-13-top-repositories.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Extract Box | `html` | extractHtmlContent |
| Request to Github Trend | `httpRequest` | Inspect parameters |
| Turn to a list | `splitOut` | Inspect parameters |
| Set Result Variables | `set` | Inspect parameters |
| Extract repository data | `html` | extractHtmlContent |
| Extract all repositories | `html` | extractHtmlContent |

## Connection map

- Extract Box → Extract all repositories (`main`, output 0, input 0)
- Turn to a list → Extract repository data (`main`, output 0, input 0)
- Extract repository data → Set Result Variables (`main`, output 0, input 0)
- Request to Github Trend → Extract Box (`main`, output 0, input 0)
- Extract all repositories → Turn to a list (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Request to Github Trend (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1351_Manual_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1351_Manual_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
