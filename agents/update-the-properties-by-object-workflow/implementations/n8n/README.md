# Update the properties by object Workflow

This folder contains the **Update the properties by object Workflow** workflow. Its executable nodes use `code`, `extractFromFile`, `filter`, `form`, `formTrigger`, `googleSheets`, `httpRequest`, `if`, `manualTrigger`, `merge`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`update-the-properties-by-object-workflow.json`](update-the-properties-by-object-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `hubspotDeveloperApi`, `hubspotOAuth2Api`

**Entry nodes:** Start here to update your field list, File upload form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split by object | `splitOut` | Inspect parameters |
| Fetch properties from Hubspot | `httpRequest` | Inspect parameters |
| Define crm_type | `code` | Inspect parameters |
| Split results | `splitOut` | Inspect parameters |
| Transforms the results | `code` | Inspect parameters |
| Append to Google sheet | `googleSheets` | append |
| Erase Google sheet | `googleSheets` | clear |
| Define array of objects | `set` | Inspect parameters |
| Start here to update your field list | `manualTrigger` | Inspect parameters |
| File upload form | `formTrigger` | Inspect parameters |
| To get the first line of file | `extractFromFile` | text |
| Set the real fields | `set` | Inspect parameters |
| Get the fields from the sheet | `googleSheets` | Inspect parameters |
| Merge fields and data | `merge` | Inspect parameters |
| Check if all fields from input are defined | `code` | Inspect parameters |
| If all fields are defined | `if` | Inspect parameters |
| Creates the correspondance table | `code` | Inspect parameters |
| Form to set the correponding field for each input field | `form` | Inspect parameters |
| Get the content of file | `extractFromFile` | Inspect parameters |
| Split all records to import | `splitOut` | Inspect parameters |
| Define properties | `set` | Inspect parameters |
| Uploads to Hubspot | `httpRequest` | POST |
| Form response | `form` | completion |
| Remove hidden and starting with hs_ props fields | `filter` | Inspect parameters |
| Set the values for each field | `code` | Inspect parameters |
| Set the values for each field1 | `code` | Inspect parameters |

## Connection map

- Split results → Remove hidden and starting with hs_ props fields (`main`, output 0, input 0)
- Define crm_type → Split results (`main`, output 0, input 0)
- Split by object → Fetch properties from Hubspot (`main`, output 0, input 0)
- File upload form → To get the first line of file (`main`, output 0, input 0)
- File upload form → Get the content of file (`main`, output 0, input 0)
- Define properties → Uploads to Hubspot (`main`, output 0, input 0)
- Erase Google sheet → Define array of objects (`main`, output 0, input 0)
- Uploads to Hubspot → Form response (`main`, output 0, input 0)
- Set the real fields → Merge fields and data (`main`, output 0, input 1)
- Merge fields and data → Get the fields from the sheet (`main`, output 0, input 0)
- Transforms the results → Append to Google sheet (`main`, output 0, input 0)
- Define array of objects → Split by object (`main`, output 0, input 0)
- Get the content of file → Merge fields and data (`main`, output 0, input 0)
- If all fields are defined → Set the values for each field (`main`, output 0, input 0)
- If all fields are defined → Creates the correspondance table (`main`, output 1, input 0)
- Split all records to import → Define properties (`main`, output 0, input 0)
- Fetch properties from Hubspot → Define crm_type (`main`, output 0, input 0)
- Get the fields from the sheet → Check if all fields from input are defined (`main`, output 0, input 0)
- Set the values for each field → Split all records to import (`main`, output 0, input 0)
- To get the first line of file → Set the real fields (`main`, output 0, input 0)
- Set the values for each field1 → Split all records to import (`main`, output 0, input 0)
- Creates the correspondance table → Form to set the correponding field for each input field (`main`, output 0, input 0)
- Start here to update your field list → Erase Google sheet (`main`, output 0, input 0)
- Check if all fields from input are defined → If all fields are defined (`main`, output 0, input 0)
- Remove hidden and starting with hs_ props fields → Transforms the results (`main`, output 0, input 0)
- Form to set the correponding field for each input field → Set the values for each field1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0895_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0895_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
