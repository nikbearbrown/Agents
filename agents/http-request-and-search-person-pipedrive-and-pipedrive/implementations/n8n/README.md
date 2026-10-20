# http request and search person pipedrive and pipedrive

This folder contains the **http request and search person pipedrive and pipedrive** workflow. Its executable nodes use `githubTrigger`, `httpRequest`, `if`, `noOp`, `pipedrive`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-search-person-pipedrive-and-pipedrive.json`](http-request-and-search-person-pipedrive-and-pipedrive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `pipedriveApi`

**Entry nodes:** ON Pull Request

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| HTTP Request | `httpRequest` | Inspect parameters |
| Search PR user in Pipedrive by email | `pipedrive` | person / search |
| person exists | `if` | Inspect parameters |
| Pipedrive | `pipedrive` | note |
| NoOp | `noOp` | Inspect parameters |
| ON Pull Request | `githubTrigger` | Inspect parameters |

## Connection map

- HTTP Request → Search PR user in Pipedrive by email (`main`, output 0, input 0)
- person exists → Pipedrive (`main`, output 0, input 0)
- person exists → NoOp (`main`, output 1, input 0)
- ON Pull Request → HTTP Request (`main`, output 0, input 0)
- Search PR user in Pipedrive by email → person exists (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0253_HTTP_GitHub_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0253_HTTP_GitHub_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
