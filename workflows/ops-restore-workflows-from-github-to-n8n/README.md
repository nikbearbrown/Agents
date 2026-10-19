# [OPS] Restore workflows from GitHub to n8n

This folder contains the **[OPS] Restore workflows from GitHub to n8n** workflow. Its executable nodes use `github`, `if`, `manualTrigger`, `merge`, `n8n`, `noOp`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ops-restore-workflows-from-github-to-n8n.json`](ops-restore-workflows-from-github-to-n8n.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `n8nApi`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Workflow name already exists | `noOp` | Inspect parameters |
| If workflow already exists | `if` | Inspect parameters |
| Set n8n existing workflows names | `set` | Inspect parameters |
| GitHub - get all files | `github` | file / list |
| n8n - get all workflows | `n8n` | Inspect parameters |
| GitHub - get each file | `github` | file / get |
| Set name and content | `set` | Inspect parameters |
| n8n - create workflow | `n8n` | create |
| Merge globals and files | `merge` | Inspect parameters |
| Merge Github and n8n workflows - Keep only non existing workflows based on the name | `merge` | Inspect parameters |

## Connection map

- Globals → GitHub - get all files (`main`, output 0, input 0)
- Globals → Merge globals and files (`main`, output 0, input 1)
- Set name and content → Merge Github and n8n workflows - Keep only non existing workflows based on the name (`main`, output 0, input 0)
- On clicking 'execute' → Globals (`main`, output 0, input 0)
- On clicking 'execute' → n8n - get all workflows (`main`, output 0, input 0)
- GitHub - get all files → Merge globals and files (`main`, output 0, input 0)
- GitHub - get each file → Set name and content (`main`, output 0, input 0)
- Merge globals and files → GitHub - get each file (`main`, output 0, input 0)
- n8n - get all workflows → Set n8n existing workflows names (`main`, output 0, input 0)
- If workflow already exists → n8n - create workflow (`main`, output 0, input 0)
- If workflow already exists → Workflow name already exists (`main`, output 1, input 0)
- Set n8n existing workflows names → Merge Github and n8n workflows - Keep only non existing workflows based on the name (`main`, output 0, input 1)
- Merge Github and n8n workflows - Keep only non existing workflows based on the name → If workflow already exists (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/1988_GitHub_Manual_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Github/1988_GitHub_Manual_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
