# 👆 Set instance url instead of `{{ $vars.instance_url }}` (or set the env variable if you have that feature)

This folder contains the **👆 Set instance url instead of `{{ $vars.instance_url }}` (or set the env variable if you have that feature)** workflow. Its executable nodes use `httpRequest`, `if`, `n8n`, `notion`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`set-instance-url-instead-of-vars-instance-url-or-set-the-env-variable-if-you-have-that-feature.json`](set-instance-url-instead-of-vars-instance-url-or-set-the-env-variable-if-you-have-that-feature.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `notionApi`

**Entry nodes:** Every 15 minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Every 15 minutes | `scheduleTrigger` | Inspect parameters |
| Get all workflows with tag | `n8n` | Inspect parameters |
| Set fields | `set` | Inspect parameters |
| Get notion page with workflow id | `httpRequest` | POST |
| Map fields | `set` | Inspect parameters |
| if newly added workflow | `if` | Inspect parameters |
| Add to Notion | `notion` | databasePage |
| Update in Notion | `notion` | databasePage / update |

## Connection map

- Map fields → if newly added workflow (`main`, output 0, input 0)
- Set fields → Get notion page with workflow id (`main`, output 0, input 0)
- Every 15 minutes → Get all workflows with tag (`main`, output 0, input 0)
- if newly added workflow → Add to Notion (`main`, output 0, input 0)
- if newly added workflow → Update in Notion (`main`, output 1, input 0)
- Get all workflows with tag → Set fields (`main`, output 0, input 0)
- Get notion page with workflow id → Map fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0448_Schedule_HTTP_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0448_Schedule_HTTP_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
