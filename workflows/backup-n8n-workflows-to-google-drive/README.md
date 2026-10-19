# backup n8n workflows to google drive

This folder contains the **backup n8n workflows to google drive** workflow. Its executable nodes use `code`, `discord`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `gmail`, `googleDrive`, `if`, `limit`, `n8n`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`backup-n8n-workflows-to-google-drive.json`](backup-n8n-workflows-to-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`, `gmailOAuth2`, `googleDriveOAuth2Api`, `n8nApi`

**Entry nodes:** Schedule Trigger, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get all n8n Workflows | `n8n` | Inspect parameters |
| Backup to Google Drive2 | `googleDrive` | update |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Backup to Google Drive4 | `googleDrive` | Inspect parameters |
| ifDriveEmpty | `if` | Inspect parameters |
| firstWorkflowJson | `set` | Inspect parameters |
| JsonToFile | `code` | Inspect parameters |
| CodeJsonToFile1 | `code` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Workflow Data | `executionData` | Inspect parameters |
| successEmail | `gmail` | Inspect parameters |
| failureEmail | `gmail` | Inspect parameters |
| getDriveFileData | `googleDrive` | fileFolder |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Parameters | `set` | Inspect parameters |
| Discord | `discord` | message |

## Connection map

- Limit → successEmail (`main`, output 0, input 0)
- Limit → Discord (`main`, output 0, input 0)
- JsonToFile → Backup to Google Drive4 (`main`, output 0, input 0)
- Parameters → getDriveFileData (`main`, output 0, input 0)
- ifDriveEmpty → CodeJsonToFile1 (`main`, output 0, input 0)
- ifDriveEmpty → firstWorkflowJson (`main`, output 1, input 0)
- Workflow Data → Parameters (`main`, output 0, input 0)
- CodeJsonToFile1 → Backup to Google Drive2 (`main`, output 0, input 0)
- Loop Over Items → Limit (`main`, output 0, input 0)
- Loop Over Items → Execute Workflow (`main`, output 1, input 0)
- Execute Workflow → Loop Over Items (`main`, output 0, input 0)
- Schedule Trigger → Get all n8n Workflows (`main`, output 0, input 0)
- getDriveFileData → ifDriveEmpty (`main`, output 0, input 0)
- firstWorkflowJson → JsonToFile (`main`, output 0, input 0)
- Get all n8n Workflows → Loop Over Items (`main`, output 0, input 0)
- Backup to Google Drive2 → failureEmail (`main`, output 1, input 0)
- Backup to Google Drive4 → failureEmail (`main`, output 1, input 0)
- When Executed by Another Workflow → Workflow Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0897_Limit_Code_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0897_Limit_Code_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
