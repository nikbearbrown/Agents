# Threads

This folder contains the **Threads** workflow. Its executable nodes use `formTrigger`, `httpRequest`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`threads.json`](threads.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Form Trigger | `formTrigger` | Inspect parameters |
| Create Thread | `httpRequest` | POST |
| Publish Thread | `httpRequest` | POST |
| Wait | `wait` | Inspect parameters |
| Exchange Token | `httpRequest` | Inspect parameters |
| Credentials | `set` | Inspect parameters |

## Connection map

- Form Trigger → Set Fields (`main`, output 0, input 0)
- Create Thread → Wait (`main`, output 0, input 0)
- Wait → Publish Thread (`main`, output 0, input 0)
- Exchange Token → Create Thread (`main`, output 0, input 0)
- Set Fields → Exchange Token (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_source": 1, "missing_connection_target": 1}`.

Source: [https://github.com/Imran-farhat/social-media-post-automation-n8n/blob/cdaf86db3306bdbbce6e770dd4af256f1492c85b/Threads.json](https://github.com/Imran-farhat/social-media-post-automation-n8n/blob/cdaf86db3306bdbbce6e770dd4af256f1492c85b/Threads.json). License: **MIT**; preserve [the notice](../../licenses/Imran-farhat--social-media-post-automation-n8n.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
