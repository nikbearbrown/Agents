# Workflow Importer

This folder contains the **Workflow Importer** workflow. Its executable nodes use `code`, `executeCommand`, `extractFromFile`, `filter`, `form`, `formTrigger`, `httpRequest`, `if`, `merge`, `n8n`, `noOp`, `readWriteFile`, `removeDuplicates`, `renameKeys`, `set`, `sort`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-importer.json`](workflow-importer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract from File | `extractFromFile` | fromJson |
| Export Credentials | `executeCommand` | Inspect parameters |
| Get Credentials Data | `readWriteFile` | Inspect parameters |
| Binary to JSON | `extractFromFile` | fromJson |
| Merge | `merge` | Inspect parameters |
| Collect Credentials to Replace | `merge` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Prepare Request Data | `code` | Inspect parameters |
| Get Workflows | `httpRequest` | Inspect parameters |
| No Operation | `noOp` | Inspect parameters |
| Determine Workflow Source | `if` | Inspect parameters |
| Error1 | `form` | completion |
| Error | `form` | completion |
| Split Out Workflows | `splitOut` | Inspect parameters |
| Get Workflow Names | `code` | Inspect parameters |
| Sort by updatedAt DESC | `sort` | Inspect parameters |
| No Operation1 | `noOp` | Inspect parameters |
| Rename Keys | `renameKeys` | Inspect parameters |
| Create Workflow | `n8n` | create |
| Upload File | `form` | Inspect parameters |
| Choose Workflow | `form` | Inspect parameters |
| Success | `form` | completion |
| Choose Instance | `form` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Generate Instance Options | `code` | Inspect parameters |
| Get Selected Workflow | `code` | Inspect parameters |
| Split Out Nodes | `splitOut` | Inspect parameters |
| Filter Out Nodes Having Credentials | `filter` | Inspect parameters |
| Extract Credentials | `set` | Inspect parameters |
| Remove Duplicate Credentials by Name | `removeDuplicates` | Inspect parameters |
| Map Credentials | `form` | Inspect parameters |
| Get Selected Credentials | `code` | Inspect parameters |
| Add Old Names | `set` | Inspect parameters |
| Replace Credentials in Workflow | `code` | Inspect parameters |
| Generate Credential Options | `code` | Inspect parameters |
| Create Empty Credentials | `n8n` | credential |
| Get Missing Credentials | `code` | Inspect parameters |

## Connection map

- Merge → No Operation1 (`main`, output 0, input 0)
- Settings → Generate Instance Options (`main`, output 0, input 0)
- Rename Keys → Merge (`main`, output 0, input 1)
- Upload File → Extract from File (`main`, output 0, input 0)
- No Operation → Merge (`main`, output 0, input 0)
- Add Old Names → Collect Credentials to Replace (`main`, output 0, input 0)
- Get Workflows → Split Out Workflows (`main`, output 0, input 0)
- Get Workflows → Error (`main`, output 1, input 0)
- No Operation1 → Split Out Nodes (`main`, output 0, input 0)
- Binary to JSON → Rename Keys (`main`, output 0, input 0)
- Choose Instance → Prepare Request Data (`main`, output 0, input 0)
- Choose Workflow → Get Selected Workflow (`main`, output 0, input 0)
- Create Workflow → Success (`main`, output 0, input 0)
- Create Workflow → Error1 (`main`, output 1, input 0)
- Map Credentials → Get Missing Credentials (`main`, output 0, input 0)
- Map Credentials → Get Selected Credentials (`main`, output 0, input 0)
- Split Out Nodes → Filter Out Nodes Having Credentials (`main`, output 0, input 0)
- Extract from File → Export Credentials (`main`, output 0, input 0)
- Extract from File → No Operation (`main`, output 0, input 0)
- Export Credentials → Get Credentials Data (`main`, output 0, input 0)
- Get Workflow Names → Choose Workflow (`main`, output 0, input 0)
- On form submission → Determine Workflow Source (`main`, output 0, input 0)
- Extract Credentials → Remove Duplicate Credentials by Name (`main`, output 0, input 0)
- Split Out Workflows → Sort by updatedAt DESC (`main`, output 0, input 0)
- Get Credentials Data → Binary to JSON (`main`, output 0, input 0)
- Prepare Request Data → Get Workflows (`main`, output 0, input 0)
- Get Selected Workflow → Export Credentials (`main`, output 0, input 0)
- Get Selected Workflow → No Operation (`main`, output 0, input 0)
- Sort by updatedAt DESC → Get Workflow Names (`main`, output 0, input 0)
- Get Missing Credentials → Create Empty Credentials (`main`, output 0, input 0)
- Create Empty Credentials → Add Old Names (`main`, output 0, input 0)
- Get Selected Credentials → Collect Credentials to Replace (`main`, output 0, input 1)
- Determine Workflow Source → Upload File (`main`, output 0, input 0)
- Determine Workflow Source → Settings (`main`, output 1, input 0)
- Generate Instance Options → Choose Instance (`main`, output 0, input 0)
- Generate Credential Options → Map Credentials (`main`, output 0, input 0)
- Collect Credentials to Replace → Replace Credentials in Workflow (`main`, output 0, input 0)
- Replace Credentials in Workflow → Create Workflow (`main`, output 0, input 0)
- Filter Out Nodes Having Credentials → Extract Credentials (`main`, output 0, input 0)
- Remove Duplicate Credentials by Name → Generate Credential Options (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1169_Splitout_Code_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1169_Splitout_Code_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
