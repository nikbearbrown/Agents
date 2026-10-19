# Create Custom Presentations per Lead

This folder contains the **Create Custom Presentations per Lead** workflow. Its executable nodes use `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `googleSheets`, `googleSlides`, `merge`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-custom-presentations-per-lead.json`](create-custom-presentations-per-lead.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `googleSlidesOAuth2Api`

**Entry nodes:** New Leads Arrived

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Download by ID | `googleDrive` | download |
| MoveToLeadListFolder | `googleDrive` | move |
| Add Presentation ID to Lead List | `googleSheets` | update |
| Get all Leads | `googleSheets` | Inspect parameters |
| Create new Sheet | `googleSheets` | spreadsheet |
| Merge Data for new Lead Document | `googleSheets` | append |
| New Leads Arrived | `googleDriveTrigger` | Inspect parameters |
| File Type? | `switch` | Inspect parameters |
| Combine Empty New Document with CSV Data | `merge` | Inspect parameters |
| Create Custom Presentation | `googleSlides` | replaceText |
| Extract Information from CSV file | `extractFromFile` | Inspect parameters |
| Copy Presentation Template | `googleDrive` | copy |

## Connection map

- File Type? → Download by ID (`main`, output 0, input 0)
- Get all Leads → MoveToLeadListFolder (`main`, output 0, input 0)
- Download by ID → Extract Information from CSV file (`main`, output 0, input 0)
- Download by ID → Create new Sheet (`main`, output 0, input 0)
- Create new Sheet → Combine Empty New Document with CSV Data (`main`, output 0, input 0)
- New Leads Arrived → File Type? (`main`, output 0, input 0)
- MoveToLeadListFolder → Copy Presentation Template (`main`, output 0, input 0)
- Copy Presentation Template → Create Custom Presentation (`main`, output 0, input 0)
- Create Custom Presentation → Add Presentation ID to Lead List (`main`, output 0, input 0)
- Merge Data for new Lead Document → Get all Leads (`main`, output 0, input 0)
- Extract Information from CSV file → Combine Empty New Document with CSV Data (`main`, output 0, input 1)
- Combine Empty New Document with CSV Data → Merge Data for new Lead Document (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/1845_Googleslides_Extractfromfile_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/1845_Googleslides_Extractfromfile_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
