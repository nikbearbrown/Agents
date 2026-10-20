# Import Odoo Product Images from Google Drive

This folder contains the **Import Odoo Product Images from Google Drive** workflow. Its executable nodes use `code`, `extractFromFile`, `filter`, `googleChat`, `googleDrive`, `manualTrigger`, `odoo`, `scheduleTrigger`, `summarize`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`import-odoo-product-images-from-google-drive.json`](import-odoo-product-images-from-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleChatOAuth2Api`, `googleDriveOAuth2Api`, `odooApi`

**Entry nodes:** Schedule Trigger, Click Manual

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Filter Images | `filter` | Inspect parameters |
| Find Files | `googleDrive` | fileFolder |
| Decorate Images | `code` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Move Images | `googleDrive` | move |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Sum Images | `summarize` | Inspect parameters |
| Announce | `googleChat` | Inspect parameters |
| Find Templates | `odoo` | custom / getAll |
| Download Images Templates | `googleDrive` | download |
| Update Images Templates | `odoo` | custom / update |
| Find Products | `odoo` | custom / getAll |
| Download Images Products | `googleDrive` | download |
| Update Images Products | `odoo` | custom / update |
| Convert Base64 Images Templates | `extractFromFile` | binaryToPropery |
| Convert Base64 Images Products | `extractFromFile` | binaryToPropery |
| Search Old Images | `googleDrive` | fileFolder |
| Drop Old Images | `googleDrive` | deleteFile |
| Click Manual | `manualTrigger` | Inspect parameters |

## Connection map

- Switch → Find Templates (`main`, output 0, input 0)
- Switch → Find Products (`main`, output 1, input 0)
- Find Files → Filter Images (`main`, output 0, input 0)
- Sum Images → Announce (`main`, output 0, input 0)
- Move Images → Sum Images (`main`, output 0, input 0)
- Click Manual → Find Files (`main`, output 0, input 0)
- Filter Images → Decorate Images (`main`, output 0, input 0)
- Find Products → Download Images Products (`main`, output 0, input 0)
- Find Templates → Download Images Templates (`main`, output 0, input 0)
- Decorate Images → Switch (`main`, output 0, input 0)
- Decorate Images → Move Images (`main`, output 0, input 0)
- Decorate Images → Search Old Images (`main`, output 0, input 0)
- Schedule Trigger → Find Files (`main`, output 0, input 0)
- Search Old Images → Drop Old Images (`main`, output 0, input 0)
- Download Images Products → Convert Base64 Images Products (`main`, output 0, input 0)
- Download Images Templates → Convert Base64 Images Templates (`main`, output 0, input 0)
- Convert Base64 Images Products → Update Images Products (`main`, output 0, input 0)
- Convert Base64 Images Templates → Update Images Templates (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Odoo/0977_Odoo_Code_Import_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Odoo/0977_Odoo_Code_Import_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
