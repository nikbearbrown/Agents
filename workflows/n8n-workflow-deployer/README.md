# n8n workflow deployer

This folder contains the **n8n workflow deployer** workflow. Its executable nodes use `code`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`n8n-workflow-deployer.json`](n8n-workflow-deployer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’, Google Drive Trigger -ToDeploy folder

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Existing Workflow Tags | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Extract JSON object from File | `extractFromFile` | fromJson |
| Clean JSON file ready for import | `code` | Inspect parameters |
| Set n8n API URL & Tag ID variables | `set` | Inspect parameters |
| Create n8n Workflow | `httpRequest` | POST |
| Set Workflow Tag | `httpRequest` | PUT |
| Capture Name If Fails To Create Workflow | `code` | Inspect parameters |
| Move JSON file to Deployed folder | `googleDrive` | move |
| Download n8n JSON File | `googleDrive` | download |
| Set n8n URL variable | `set` | Inspect parameters |
| Google Drive Trigger -ToDeploy folder | `googleDriveTrigger` | Inspect parameters |

## Connection map

- Set Workflow Tag → Move JSON file to Deployed folder (`main`, output 0, input 0)
- Create n8n Workflow → Set Workflow Tag (`main`, output 0, input 0)
- Create n8n Workflow → Capture Name If Fails To Create Workflow (`main`, output 1, input 0)
- Set n8n URL variable → Get Existing Workflow Tags (`main`, output 0, input 0)
- Download n8n JSON File → Extract JSON object from File (`main`, output 0, input 0)
- Extract JSON object from File → Clean JSON file ready for import (`main`, output 0, input 0)
- Clean JSON file ready for import → Create n8n Workflow (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set n8n URL variable (`main`, output 0, input 0)
- Set n8n API URL & Tag ID variables → Download n8n JSON File (`main`, output 0, input 0)
- Google Drive Trigger -ToDeploy folder → Set n8n API URL & Tag ID variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1814_Code_Extractfromfile_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1814_Code_Extractfromfile_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
