# Backup n8n Workflows to Bitbucket

This folder contains the **Backup n8n Workflows to Bitbucket** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `n8n`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`backup-n8n-workflows-to-bitbucket.json`](backup-n8n-workflows-to-bitbucket.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `n8nApi`

**Entry nodes:** Run Daily at 2 AM

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Calculate Wait Time | `code` | Inspect parameters |
| Run Daily at 2 AM | `scheduleTrigger` | Inspect parameters |
| Get All Workflows | `n8n` | Inspect parameters |
| Loop Workflows | `splitInBatches` | Inspect parameters |
| Get Existing Worfklow from Bitbucket | `httpRequest` | Inspect parameters |
| New or Changed? | `if` | Inspect parameters |
| Upload Workflow to Bitbucket | `httpRequest` | POST |
| Wait to Avoid Rate Limiting | `wait` | Inspect parameters |
| Set Bitbucket Workspace & Repository | `set` | Inspect parameters |

## Connection map

- Loop Workflows → Get Existing Worfklow from Bitbucket (`main`, output 1, input 0)
- New or Changed? → Upload Workflow to Bitbucket (`main`, output 0, input 0)
- New or Changed? → Wait to Avoid Rate Limiting (`main`, output 1, input 0)
- Get All Workflows → Loop Workflows (`main`, output 0, input 0)
- Run Daily at 2 AM → Set Bitbucket Workspace & Repository (`main`, output 0, input 0)
- Calculate Wait Time → Wait to Avoid Rate Limiting (`main`, output 0, input 0)
- Wait to Avoid Rate Limiting → Loop Workflows (`main`, output 0, input 0)
- Upload Workflow to Bitbucket → Calculate Wait Time (`main`, output 0, input 0)
- Get Existing Worfklow from Bitbucket → New or Changed? (`main`, output 0, input 0)
- Set Bitbucket Workspace & Repository → Get All Workflows (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0567_Wait_Code_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0567_Wait_Code_Export_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
