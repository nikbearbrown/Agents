# Extract engaging moments from YouTube video

This folder contains the **Extract engaging moments from YouTube video** workflow. Its executable nodes use `aggregate`, `filter`, `httpRequest`, `if`, `noOp`, `respondToWebhook`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-engaging-moments-from-youtube-video.json`](extract-engaging-moments-from-youtube-video.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| HTTP Request | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| has intensity data? | `if` | Inspect parameters |
| No intensity data available for video | `noOp` | Inspect parameters |
| intensity > 0.6 | `filter` | Inspect parameters |
| Filter out moments close to each other | `filter` | Inspect parameters |
| Input variables | `set` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Create each moment (human readable) | `set` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| millisecs to seconds | `set` | Inspect parameters |
| prepare response | `set` | Inspect parameters |
| Respond with "no results" | `respondToWebhook` | Inspect parameters |
| Respond with moments | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → Input variables (`main`, output 0, input 0)
- Aggregate → prepare response (`main`, output 0, input 0)
- Split Out → intensity > 0.6 (`main`, output 0, input 0)
- HTTP Request → has intensity data? (`main`, output 0, input 0)
- Input variables → HTTP Request (`main`, output 0, input 0)
- intensity > 0.6 → millisecs to seconds (`main`, output 0, input 0)
- prepare response → Respond with moments (`main`, output 0, input 0)
- has intensity data? → Split Out (`main`, output 0, input 0)
- has intensity data? → No intensity data available for video (`main`, output 1, input 0)
- millisecs to seconds → Filter out moments close to each other (`main`, output 0, input 0)
- Create each moment (human readable) → Aggregate (`main`, output 0, input 0)
- No intensity data available for video → Respond with "no results" (`main`, output 0, input 0)
- Filter out moments close to each other → Create each moment (human readable) (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0449_Splitout_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0449_Splitout_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
