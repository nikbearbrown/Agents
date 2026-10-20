# Create Threads on Bluesky

This folder contains the **Create Threads on Bluesky** workflow. Its executable nodes use `code`, `httpRequest`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-threads-on-bluesky.json`](create-threads-on-bluesky.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Run Daily at 9 AM

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create Bluesky Session | `httpRequest` | POST |
| Create Reply | `httpRequest` | POST |
| Run Daily at 9 AM | `scheduleTrigger` | Inspect parameters |
| Set Bluesky Credentials | `set` | Inspect parameters |
| Create Reply Text | `code` | Inspect parameters |
| Create Sibling Text | `code` | Inspect parameters |
| Create Sibling | `httpRequest` | POST |
| Loop Posts | `splitInBatches` | Inspect parameters |
| Create Initial Post | `httpRequest` | POST |
| Create Post | `httpRequest` | POST |
| Wait | `wait` | Inspect parameters |
| Create Post Text | `code` | Inspect parameters |
| Create Sibling Array | `code` | Inspect parameters |
| Create Sibling Text (Loop) | `code` | Inspect parameters |

## Connection map

- Wait → Loop Posts (`main`, output 0, input 0)
- Loop Posts → Create Sibling Text (Loop) (`main`, output 1, input 0)
- Create Post → Wait (`main`, output 0, input 0)
- Create Reply → Create Sibling Text (`main`, output 0, input 0)
- Create Sibling → Create Sibling Array (`main`, output 0, input 0)
- Create Post Text → Create Initial Post (`main`, output 0, input 0)
- Create Reply Text → Create Reply (`main`, output 0, input 0)
- Run Daily at 9 AM → Set Bluesky Credentials (`main`, output 0, input 0)
- Create Initial Post → Create Reply Text (`main`, output 0, input 0)
- Create Sibling Text → Create Sibling (`main`, output 0, input 0)
- Create Sibling Array → Loop Posts (`main`, output 0, input 0)
- Create Bluesky Session → Create Post Text (`main`, output 0, input 0)
- Set Bluesky Credentials → Create Bluesky Session (`main`, output 0, input 0)
- Create Sibling Text (Loop) → Create Post (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1135_Wait_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1135_Wait_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
