# Backup workflows to git repository on Gitea

This folder contains the **Backup workflows to git repository on Gitea** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `n8n`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`backup-workflows-to-git-repository-on-gitea.json`](backup-workflows-to-git-repository-on-gitea.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `n8nApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Globals | `set` | Inspect parameters |
| n8n | `n8n` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| SetDataUpdateNode | `set` | Inspect parameters |
| SetDataCreateNode | `set` | Inspect parameters |
| Base64EncodeUpdate | `code` | Inspect parameters |
| Base64EncodeCreate | `code` | Inspect parameters |
| Exist | `if` | Inspect parameters |
| Changed | `if` | Inspect parameters |
| PutGitea | `httpRequest` | PUT |
| GetGitea | `httpRequest` | Inspect parameters |
| PostGitea | `httpRequest` | POST |
| ForEach | `splitInBatches` | Inspect parameters |

## Connection map

- n8n → ForEach (`main`, output 0, input 0)
- Exist → SetDataUpdateNode (`main`, output 0, input 0)
- Exist → SetDataCreateNode (`main`, output 1, input 0)
- Changed → PutGitea (`main`, output 0, input 0)
- Changed → ForEach (`main`, output 1, input 0)
- ForEach → GetGitea (`main`, output 1, input 0)
- Globals → n8n (`main`, output 0, input 0)
- GetGitea → Exist (`main`, output 0, input 0)
- PutGitea → ForEach (`main`, output 0, input 0)
- PostGitea → ForEach (`main`, output 0, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- SetDataCreateNode → Base64EncodeCreate (`main`, output 0, input 0)
- SetDataUpdateNode → Base64EncodeUpdate (`main`, output 0, input 0)
- Base64EncodeCreate → PostGitea (`main`, output 0, input 0)
- Base64EncodeUpdate → Changed (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1426_Code_Schedule_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1426_Code_Schedule_Export_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
