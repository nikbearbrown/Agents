# Automatically Update YouTube Video Descriptions with Inserted Text

This folder contains the **Automatically Update YouTube Video Descriptions with Inserted Text** workflow. Its executable nodes use `code`, `manualTrigger`, `set`, `splitInBatches`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automatically-update-youtube-video-descriptions-with-inserted-text.json`](automatically-update-youtube-video-descriptions-with-inserted-text.json): sanitized, inactive import copy with an overview sticky note.
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
| Get All Videos | `youTube` | video |
| Update Video Description | `youTube` | video / update |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set String to Insert | `set` | Inspect parameters |
| Loop Over Videos | `splitInBatches` | Inspect parameters |
| Get Specific Video | `youTube` | video / get |
| Create New Video Description with Row Inserted | `code` | Inspect parameters |

## Connection map

- Get All Videos → Loop Over Videos (`main`, output 0, input 0)
- Loop Over Videos → Get Specific Video (`main`, output 1, input 0)
- Get Specific Video → Create New Video Description with Row Inserted (`main`, output 0, input 0)
- Set String to Insert → Get All Videos (`main`, output 0, input 0)
- Update Video Description → Loop Over Videos (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set String to Insert (`main`, output 0, input 0)
- Create New Video Description with Row Inserted → Update Video Description (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0773_Code_Manual_Update_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0773_Code_Manual_Update_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
