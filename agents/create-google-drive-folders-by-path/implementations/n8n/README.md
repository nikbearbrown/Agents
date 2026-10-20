# Create Google Drive Folders by Path

This folder contains the **Create Google Drive Folders by Path** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `googleDrive`, `if`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-google-drive-folders-by-path.json`](create-google-drive-folders-by-path.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set parameters for next run | `code` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Dummy input data | `set` | Inspect parameters |
| Split the desired path | `code` | Inspect parameters |
| Create desired path | `code` | Inspect parameters |
| Check if top folder exists | `googleDrive` | fileFolder |
| If top folder doesn't exist | `if` | Inspect parameters |
| Create new subfolder | `googleDrive` | folder |
| If path has been completely created | `if` | Inspect parameters |
| Return the ID of the last folder | `set` | Inspect parameters |

## Connection map

- Dummy input data → Split the desired path (`main`, output 0, input 0)
- Create desired path → Check if top folder exists (`main`, output 0, input 0)
- Create new subfolder → Set parameters for next run (`main`, output 0, input 0)
- Split the desired path → Create desired path (`main`, output 0, input 0)
- Execute Workflow Trigger → Split the desired path (`main`, output 0, input 0)
- Check if top folder exists → If top folder doesn't exist (`main`, output 0, input 0)
- If top folder doesn't exist → Create new subfolder (`main`, output 0, input 0)
- If top folder doesn't exist → Set parameters for next run (`main`, output 1, input 0)
- Set parameters for next run → If path has been completely created (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Dummy input data (`main`, output 0, input 0)
- If path has been completely created → Return the ID of the last folder (`main`, output 0, input 0)
- If path has been completely created → Create desired path (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0891_Code_Manual_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0891_Code_Manual_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
