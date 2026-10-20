# 💥workflow n8n d'Auto-Post sur les réseaux sociaux - vide

This folder contains the **💥workflow n8n d'Auto-Post sur les réseaux sociaux - vide** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-n8n-d-auto-post-sur-les-reseaux-sociaux-vide.json`](workflow-n8n-d-auto-post-sur-les-reseaux-sociaux-vide.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Assign Social Media IDs | `set` | Inspect parameters |
| Get my video | `googleSheets` | Inspect parameters |
| Upload Video to Blotato | `httpRequest` | POST |
| INSTAGRAM | `httpRequest` | POST |
| YOUTUBE | `httpRequest` | POST |
| TIKTOK | `httpRequest` | POST |
| FACEBOOK | `httpRequest` | POST |
| THREADS | `httpRequest` | POST |
| TWETTER | `httpRequest` | POST |
| LINKEDIN | `httpRequest` | POST |
| BLUESKY | `httpRequest` | POST |
| PINTEREST | `httpRequest` | POST |
| Google Sheets | `googleSheets` | update |

## Connection map

- Get my video → Assign Social Media IDs (`main`, output 0, input 0)
- Schedule Trigger → Get my video (`main`, output 0, input 0)
- Assign Social Media IDs → Upload Video to Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → INSTAGRAM (`main`, output 0, input 0)
- Upload Video to Blotato → YOUTUBE (`main`, output 0, input 0)
- Upload Video to Blotato → TIKTOK (`main`, output 0, input 0)
- Upload Video to Blotato → FACEBOOK (`main`, output 0, input 0)
- Upload Video to Blotato → THREADS (`main`, output 0, input 0)
- Upload Video to Blotato → TWITTER (`main`, output 0, input 0)
- Upload Video to Blotato → LINKEDIN (`main`, output 0, input 0)
- Upload Video to Blotato → BLUESKY (`main`, output 0, input 0)
- Upload Video to Blotato → PINTEREST (`main`, output 0, input 0)
- Upload Video to Blotato → Google Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_target": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1367_HTTP_Schedule_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1367_HTTP_Schedule_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
