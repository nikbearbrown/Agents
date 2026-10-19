# Clockify to Syncro

This folder contains the **Clockify to Syncro** workflow. Its executable nodes use `function`, `googleSheets`, `httpRequest`, `if`, `noOp`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`clockify-to-syncro.json`](clockify-to-syncro.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpHeaderAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| ForGoogle | `set` | Inspect parameters |
| ForSyncro | `set` | Inspect parameters |
| FindMatch | `googleSheets` | lookup |
| IF | `if` | Inspect parameters |
| NewSyncroTimer | `httpRequest` | Inspect parameters |
| UpdateSyncroTimer | `httpRequest` | Inspect parameters |
| EnvVariables | `set` | Inspect parameters |
| SetTechnicians | `set` | Inspect parameters |
| MatchTechnician | `function` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| NoOp | `noOp` | Inspect parameters |

## Connection map

- IF → UpdateSyncroTimer (`main`, output 0, input 0)
- IF → NewSyncroTimer (`main`, output 1, input 0)
- IF1 → EnvVariables (`main`, output 0, input 0)
- IF1 → NoOp (`main`, output 1, input 0)
- Webhook → IF1 (`main`, output 0, input 0)
- FindMatch → IF (`main`, output 0, input 0)
- ForGoogle → Google Sheets (`main`, output 0, input 0)
- ForSyncro → SetTechnicians (`main`, output 0, input 0)
- EnvVariables → ForSyncro (`main`, output 0, input 0)
- NewSyncroTimer → ForGoogle (`main`, output 0, input 0)
- SetTechnicians → MatchTechnician (`main`, output 0, input 0)
- MatchTechnician → FindMatch (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0935_HTTP_GoogleSheets_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0935_HTTP_GoogleSheets_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
