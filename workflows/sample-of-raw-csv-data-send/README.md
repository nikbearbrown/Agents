# Sample of Raw CSV Data Send

This folder contains the **Sample of Raw CSV Data Send** workflow. Its executable nodes use `aggregate`, `code`, `extractFromFile`, `httpRequest`, `if`, `respondToWebhook`, `set`, `slack`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sample-of-raw-csv-data-send.json`](sample-of-raw-csv-data-send.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** POST

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract From File | `extractFromFile` | Inspect parameters |
| Error Response | `respondToWebhook` | Inspect parameters |
| Success Response | `respondToWebhook` | Inspect parameters |
| Change Field | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Send to Error Channel | `slack` | Inspect parameters |
| Convert Raw Text To CSV | `code` | Inspect parameters |
| Check if Value | `if` | Inspect parameters |
| Send Raw CSV | `httpRequest` | POST |
| POST | `webhook` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| Success Response2 | `respondToWebhook` | Inspect parameters |

## Connection map

- POST → Switch (`main`, output 0, input 0)
- Switch → Extract From File (`main`, output 0, input 0)
- Switch → Change Field (`main`, output 1, input 0)
- Switch → Error Response (`main`, output 2, input 0)
- Switch → Error Response (`main`, output 3, input 0)
- Aggregate → Success Response (`main`, output 0, input 0)
- Aggregate1 → Success Response2 (`main`, output 0, input 0)
- Change Field → Convert Raw Text To CSV (`main`, output 0, input 0)
- Change Field → Error Response (`main`, output 1, input 0)
- Check if Value → Aggregate1 (`main`, output 0, input 0)
- Check if Value → Error Response (`main`, output 1, input 0)
- Error Response → Send to Error Channel (`main`, output 0, input 0)
- Error Response → Send to Error Channel (`main`, output 1, input 0)
- Success Response → Send to Error Channel (`main`, output 1, input 0)
- Extract From File → Aggregate (`main`, output 0, input 0)
- Extract From File → Error Response (`main`, output 1, input 0)
- Success Response2 → Send to Error Channel (`main`, output 1, input 0)
- Convert Raw Text To CSV → Check if Value (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0686_Code_Webhook_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0686_Code_Webhook_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
