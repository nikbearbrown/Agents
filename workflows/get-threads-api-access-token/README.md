# Get Threads API Access Token

This folder contains the **Get Threads API Access Token** workflow. Its executable nodes use `code`, `function`, `httpRequest`, `merge`, `noOp`, `notion`, `scheduleTrigger`, `splitInBatches`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-threads-api-access-token.json`](get-threads-api-access-token.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`

**Entry nodes:** Get Posts Schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Refresh Token | `httpRequest` | Inspect parameters |
| Get Post | `httpRequest` | Inspect parameters |
| Get Post ID | `function` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Replace Me | `noOp` | Inspect parameters |
| Threads / Comments | `httpRequest` | Inspect parameters |
| Threads / Root | `httpRequest` | Inspect parameters |
| Comment's Filter | `code` | Inspect parameters |
| Root's Filter | `code` | Inspect parameters |
| Threads ID | `notion` | databasePage / getAll |
| Extract IDs | `function` | Inspect parameters |
| Compare IDs | `function` | Inspect parameters |
| Create Page | `notion` | databasePage |
| Upload Medias | `httpRequest` | Inspect parameters |
| If Post Exist | `switch` | Inspect parameters |
| Threads Post | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Run This First to Get Long Live Access Token | `httpRequest` | Inspect parameters |
| Get Posts Schedule | `scheduleTrigger` | Inspect parameters |

## Connection map

- Merge → Threads Post (`main`, output 0, input 0)
- Get Post → Get Post ID (`main`, output 0, input 0)
- Replace Me → Loop Over Items (`main`, output 0, input 0)
- Threads ID → Extract IDs (`main`, output 0, input 0)
- Compare IDs → If Post Exist (`main`, output 0, input 0)
- Create Page → Upload Medias (`main`, output 0, input 0)
- Extract IDs → Compare IDs (`main`, output 0, input 0)
- Get Post ID → Loop Over Items (`main`, output 0, input 0)
- Threads Post → Threads ID (`main`, output 0, input 0)
- If Post Exist → Create Page (`main`, output 0, input 0)
- If Post Exist → Replace Me (`main`, output 1, input 0)
- Refresh Token → Get Post (`main`, output 0, input 0)
- Root's Filter → Merge (`main`, output 0, input 0)
- Upload Medias → Replace Me (`main`, output 0, input 0)
- Threads / Root → Root's Filter (`main`, output 0, input 0)
- Loop Over Items → Threads / Root (`main`, output 1, input 0)
- Loop Over Items → Threads / Comments (`main`, output 1, input 0)
- Comment's Filter → Merge (`main`, output 0, input 1)
- Get Posts Schedule → Refresh Token (`main`, output 0, input 0)
- Threads / Comments → Comment's Filter (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0706_Code_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0706_Code_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
