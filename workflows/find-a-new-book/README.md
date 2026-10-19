# Find a New Book

This folder contains the **Find a New Book** workflow. Its executable nodes use `cron`, `emailSend`, `function`, `httpRequest`, `if`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`find-a-new-book.json`](find-a-new-book.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** On clicking 'execute', Every Friday at 11:00 AM

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Every Friday at 11:00 AM | `cron` | Inspect parameters |
| Set Subject | `set` | Inspect parameters |
| Retrieve Book Count | `httpRequest` | Inspect parameters |
| Check Book Count | `if` | Inspect parameters |
| Select Random Book | `function` | Inspect parameters |
| Retrieve Detailed Book Info | `httpRequest` | Inspect parameters |
| Retrieve Basic Book Info | `httpRequest` | Inspect parameters |
| Book Recommendation | `set` | Inspect parameters |
| Filtered Book Info | `set` | Inspect parameters |
| Create Author String | `function` | Inspect parameters |
| Send No Book Email | `emailSend` | Inspect parameters |
| Send Book Email | `emailSend` | Inspect parameters |

## Connection map

- Set Subject → Retrieve Book Count (`main`, output 0, input 0)
- Check Book Count → Select Random Book (`main`, output 0, input 0)
- Check Book Count → Send No Book Email (`main`, output 1, input 0)
- Filtered Book Info → Create Author String (`main`, output 0, input 0)
- Select Random Book → Retrieve Basic Book Info (`main`, output 0, input 0)
- Book Recommendation → Send Book Email (`main`, output 0, input 0)
- Retrieve Book Count → Check Book Count (`main`, output 0, input 0)
- Create Author String → Book Recommendation (`main`, output 0, input 0)
- On clicking 'execute' → Set Subject (`main`, output 0, input 0)
- Every Friday at 11:00 AM → Set Subject (`main`, output 0, input 0)
- Retrieve Basic Book Info → Retrieve Detailed Book Info (`main`, output 0, input 0)
- Retrieve Detailed Book Info → Filtered Book Info (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0119_Manual_Cron_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0119_Manual_Cron_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
