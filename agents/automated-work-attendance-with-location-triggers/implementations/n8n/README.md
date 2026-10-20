# Automated Work Attendance with Location Triggers

This folder contains the **Automated Work Attendance with Location Triggers** workflow. Its executable nodes use `code`, `googleDrive`, `googleSheets`, `if`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-work-attendance-with-location-triggers.json`](automated-work-attendance-with-location-triggers.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Google Drive | `googleDrive` | fileFolder |
| Create Worksheet | `googleSheets` | spreadsheet |
| Return if Null | `code` | Inspect parameters |
| Doesn't exist? | `if` | Inspect parameters |
| Set Logging Details | `set` | Inspect parameters |
| Create Log | `googleSheets` | append |

## Connection map

- Webhook → Google Drive (`main`, output 0, input 0)
- Google Drive → Return if Null (`main`, output 0, input 0)
- Doesn't exist? → Create Worksheet (`main`, output 0, input 0)
- Doesn't exist? → Set Logging Details (`main`, output 1, input 0)
- Return if Null → Doesn't exist? (`main`, output 0, input 0)
- Create Worksheet → Set Logging Details (`main`, output 0, input 0)
- Set Logging Details → Create Log (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2008_Code_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2008_Code_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
