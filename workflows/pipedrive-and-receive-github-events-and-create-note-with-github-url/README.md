# pipedrive and receive github events and create note with github url

This folder contains the **pipedrive and receive github events and create note with github url** workflow. Its executable nodes use `githubTrigger`, `httpRequest`, `if`, `pipedrive`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pipedrive-and-receive-github-events-and-create-note-with-github-url.json`](pipedrive-and-receive-github-events-and-create-note-with-github-url.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `pipedriveApi`

**Entry nodes:** On fork

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| person exists | `if` | Inspect parameters |
| Set person Id | `set` | Inspect parameters |
| Create lead | `pipedrive` | lead |
| On fork | `githubTrigger` | Inspect parameters |
| Create person | `pipedrive` | person |
| Create note with github url | `pipedrive` | note |
| Get Github user information | `httpRequest` | Inspect parameters |
| Search forkee in Pipedrive by email | `pipedrive` | person / search |

## Connection map

- On fork → Get Github user information (`main`, output 0, input 0)
- Create lead → Create note with github url (`main`, output 0, input 0)
- Create person → Set person Id (`main`, output 0, input 0)
- Set person Id → Create lead (`main`, output 0, input 0)
- person exists → Set person Id (`main`, output 0, input 0)
- person exists → Create person (`main`, output 1, input 0)
- Get Github user information → Search forkee in Pipedrive by email (`main`, output 0, input 0)
- Search forkee in Pipedrive by email → person exists (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0252_HTTP_GitHub_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0252_HTTP_GitHub_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
