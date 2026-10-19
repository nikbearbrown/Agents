# search person pipedrive and get person pipedrive and open ai

This folder contains the **search person pipedrive and get person pipedrive and open ai** workflow. Its executable nodes use `code`, `gmailTrigger`, `if`, `openAi`, `pipedrive`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-person-pipedrive-and-get-person-pipedrive-and-open-ai.json`](search-person-pipedrive-and-get-person-pipedrive-and-open-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `pipedriveApi`

**Entry nodes:** Email box 1, Email box 2

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Search Person in CRM | `pipedrive` | person / search |
| In campaign? | `if` | Inspect parameters |
| Get person from CRM | `pipedrive` | person / get |
| Is interested? | `openAi` | chat |
| Get email | `set` | Inspect parameters |
| Create deal in CRM | `pipedrive` | Inspect parameters |
| IF interested | `if` | Inspect parameters |
| Get response | `code` | Inspect parameters |
| Email box 1 | `gmailTrigger` | Inspect parameters |
| Email box 2 | `gmailTrigger` | Inspect parameters |

## Connection map

- Get email → Search Person in CRM (`main`, output 0, input 0)
- Email box 1 → Get email (`main`, output 0, input 0)
- Email box 2 → Get email (`main`, output 0, input 0)
- Get response → IF interested (`main`, output 0, input 0)
- In campaign? → Is interested? (`main`, output 0, input 0)
- IF interested → Create deal in CRM (`main`, output 0, input 0)
- Is interested? → Get response (`main`, output 0, input 0)
- Get person from CRM → In campaign? (`main`, output 0, input 0)
- Search Person in CRM → Get person from CRM (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0379_Code_Pipedrive_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0379_Code_Pipedrive_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
