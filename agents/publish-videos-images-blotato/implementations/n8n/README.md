# Publish Videos & Images - Blotato

This folder contains the **Publish Videos & Images - Blotato** workflow. Its executable nodes use `airtable`, `code`, `formTrigger`, `httpRequest`, `manualTrigger`, `openAi`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`publish-videos-images-blotato.json`](publish-videos-images-blotato.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’, Pinterest System (tm)

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| [Instagram] Publish via Blotato | `httpRequest` | POST |
| [Facebook] Publish via Blotato | `httpRequest` | POST |
| [Linkedin] Publish via Blotato | `httpRequest` | POST |
| [Tiktok] Publish via Blotato | `httpRequest` | POST |
| [Pinterest] Publish via Blotato | `httpRequest` | POST |
| [Youtube] Publish via Blotato | `httpRequest` | POST |
| [Threads] Publish via Blotato | `httpRequest` | POST |
| [Twitter] Publish via Blotato | `httpRequest` | POST |
| [Bluesky] Publish via Blotato | `httpRequest` | POST |
| Prepare for Publish | `set` | Inspect parameters |
| Airtable | `airtable` | Inspect parameters |
| Upload Video to Blotato | `httpRequest` | POST |
| Upload Image to Blotato | `httpRequest` | POST |
| Ensure Valid YouTube Title | `openAi` | Inspect parameters |
| Airtable: Posted Instagram | `airtable` | update |
| Airtable: Posted Instagram1 | `airtable` | update |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Airtable Record ID | `set` | Inspect parameters |
| Pinterest System (tm) | `formTrigger` | Inspect parameters |
| Grab Pinterest Board Page | `httpRequest` | Inspect parameters |
| Pinterest Page Sleuth | `code` | Inspect parameters |

## Connection map

- Airtable → Ensure Valid YouTube Title (`main`, output 0, input 0)
- Airtable Record ID → Airtable (`main`, output 0, input 0)
- Prepare for Publish → Upload Image to Blotato (`main`, output 0, input 0)
- Pinterest System (tm) → Grab Pinterest Board Page (`main`, output 0, input 0)
- Upload Image to Blotato → Upload Video to Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Instagram] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Facebook] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Linkedin] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Tiktok] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Youtube] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Threads] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Twitter] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Bluesky] Publish via Blotato (`main`, output 0, input 0)
- Upload Video to Blotato → [Pinterest] Publish via Blotato (`main`, output 0, input 0)
- Grab Pinterest Board Page → Pinterest Page Sleuth (`main`, output 0, input 0)
- Ensure Valid YouTube Title → Prepare for Publish (`main`, output 0, input 0)
- [Instagram] Publish via Blotato → Airtable: Posted Instagram (`main`, output 0, input 0)
- [Instagram] Publish via Blotato → Airtable: Posted Instagram1 (`main`, output 1, input 0)
- When clicking ‘Test workflow’ → Airtable Record ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1178_Code_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1178_Code_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
