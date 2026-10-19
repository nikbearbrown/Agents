# Social Media Publisher

This folder contains the **Social Media Publisher** workflow. Its executable nodes use `form`, `formTrigger`, `httpRequest`, `if`, `set`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`social-media-publisher.json`](social-media-publisher.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Post photo | `httpRequest` | POST |
| Post video | `httpRequest` | POST |
| KO Video | `form` | completion |
| OK Video | `form` | completion |
| KO Photo | `form` | completion |
| OK Photo | `form` | completion |
| Success Photo? | `if` | Inspect parameters |
| Success Video? | `if` | Inspect parameters |
| Result Photo | `set` | Inspect parameters |
| Result Video | `set` | Inspect parameters |
| Video or Photo? | `switch` | Inspect parameters |

## Connection map

- Post photo → Result Photo (`main`, output 0, input 0)
- Post video → Result Video (`main`, output 0, input 0)
- Result Photo → Success Photo? (`main`, output 0, input 0)
- Result Video → Success Video? (`main`, output 0, input 0)
- Success Photo? → OK Photo (`main`, output 0, input 0)
- Success Photo? → KO Photo (`main`, output 1, input 0)
- Success Video? → OK Video (`main`, output 0, input 0)
- Success Video? → KO Video (`main`, output 1, input 0)
- Video or Photo? → Post photo (`main`, output 0, input 0)
- Video or Photo? → Post video (`main`, output 1, input 0)
- On form submission → Video or Photo? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1968_Form_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/1968_Form_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
