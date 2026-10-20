# Backup Squarespace code Injections to Github

This folder contains the **Backup Squarespace code Injections to Github** workflow. Its executable nodes use `code`, `github`, `httpRequest`, `if`, `manualTrigger`, `merge`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`backup-squarespace-code-injections-to-github.json`](backup-squarespace-code-injections-to-github.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`

**Entry nodes:** On clicking 'execute', Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Squarespace data | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| Clean up Footers | `code` | Inspect parameters |
| Clean up Headers | `code` | Inspect parameters |
| Get Footer Injection | `set` | Inspect parameters |
| Get Header Injection | `set` | Inspect parameters |
| Edit Injection data | `github` | file / edit |
| Create Injection data | `github` | file |
| Globals | `set` | Inspect parameters |
| Merge Injections | `merge` | Inspect parameters |

## Connection map

- If → Create Injection data (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- Globals → Edit Injection data (`main`, output 0, input 0)
- Loop Over Items → Globals (`main`, output 1, input 0)
- Clean up Footers → Merge Injections (`main`, output 0, input 0)
- Clean up Headers → Merge Injections (`main`, output 0, input 1)
- Merge Injections → Loop Over Items (`main`, output 0, input 0)
- Schedule Trigger → Get Squarespace data (`main`, output 0, input 0)
- Edit Injection data → If (`main`, output 0, input 0)
- Get Footer Injection → Clean up Footers (`main`, output 0, input 0)
- Get Header Injection → Clean up Headers (`main`, output 0, input 0)
- Get Squarespace data → Get Header Injection (`main`, output 0, input 0)
- Get Squarespace data → Get Footer Injection (`main`, output 0, input 0)
- Create Injection data → Loop Over Items (`main`, output 0, input 0)
- On clicking 'execute' → Get Squarespace data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1844_Code_Schedule_Export_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1844_Code_Schedule_Export_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
