# has shared with external users and create google sheets and permissions to items

This folder contains the **has shared with external users and create google sheets and permissions to items** workflow. Its executable nodes use `aggregate`, `filter`, `gmail`, `googleDrive`, `googleSheets`, `noOp`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`has-shared-with-external-users-and-create-google-sheets-and-permissions-to-items.json`](has-shared-with-external-users-and-create-google-sheets-and-permissions-to-items.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Has Shared with External Users | `filter` | Inspect parameters |
| Create New Sheet | `googleSheets` | create |
| Normalise Fields | `set` | Inspect parameters |
| For Each File | `splitInBatches` | Inspect parameters |
| File Ref | `noOp` | Inspect parameters |
| Permissions To Items | `splitOut` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Flatten Rows | `set` | Inspect parameters |
| Rows to Items | `splitOut` | Inspect parameters |
| Send Email Report (Execute Once) | `gmail` | Inspect parameters |
| Get Recently Active Documents | `googleDrive` | fileFolder |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Filter Out Owner of Document | `filter` | Inspect parameters |
| Append to New Sheet | `googleSheets` | append |

## Connection map

- File Ref → Permissions To Items (`main`, output 0, input 0)
- Aggregate → For Each File (`main`, output 0, input 0)
- Flatten Rows → Rows to Items (`main`, output 0, input 0)
- For Each File → Flatten Rows (`main`, output 0, input 0)
- For Each File → File Ref (`main`, output 1, input 0)
- Rows to Items → Append to New Sheet (`main`, output 0, input 0)
- Create New Sheet → Get Recently Active Documents (`main`, output 0, input 0)
- Normalise Fields → Aggregate (`main`, output 0, input 0)
- Schedule Trigger → Create New Sheet (`main`, output 0, input 0)
- Append to New Sheet → Send Email Report (Execute Once) (`main`, output 0, input 0)
- Permissions To Items → Filter Out Owner of Document (`main`, output 0, input 0)
- Filter Out Owner of Document → Normalise Fields (`main`, output 0, input 0)
- Get Recently Active Documents → Has Shared with External Users (`main`, output 0, input 0)
- Has Shared with External Users → For Each File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0854_Splitout_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0854_Splitout_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
