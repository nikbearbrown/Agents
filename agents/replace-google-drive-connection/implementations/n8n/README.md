# Replace Google Drive connection

This folder contains the **Replace Google Drive connection** workflow. Its executable nodes use `airtable`, `code`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`replace-google-drive-connection.json`](replace-google-drive-connection.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** Google Drive Trigger, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive | `googleDrive` | download |
| Upload File | `httpRequest` | POST |
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| Create Invoice | `airtable` | create |
| Create Line Item | `airtable` | create |
| OpenAI - Extract Line Items | `httpRequest` | POST |
| Set Fields | `set` | Inspect parameters |
| Process Line Items | `code` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Webhook → Set Fields (`main`, output 0, input 0)
- Set Fields → OpenAI - Extract Line Items (`main`, output 0, input 0)
- Google Drive → Upload File (`main`, output 0, input 0)
- Create Invoice → Process Line Items (`main`, output 0, input 0)
- Process Line Items → Create Line Item (`main`, output 0, input 0)
- Google Drive Trigger → Google Drive (`main`, output 0, input 0)
- OpenAI - Extract Line Items → Create Invoice (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0669_Code_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0669_Code_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
