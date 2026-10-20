# Search LinkedIn companies and add them to Airtable CRM

This folder contains the **Search LinkedIn companies and add them to Airtable CRM** workflow. Its executable nodes use `airtable`, `httpRequest`, `if`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-linkedin-companies-and-add-them-to-airtable-crm.json`](search-linkedin-companies-and-add-them-to-airtable-crm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Process Each Company | `splitInBatches` | Inspect parameters |
| Get Company Info | `httpRequest` | Inspect parameters |
| Filter Valid Companies | `if` | Inspect parameters |
| Check If Company Exists | `airtable` | search |
| Is New Company? | `if` | Inspect parameters |
| Add Company to CRM | `airtable` | create |
| Set Variables | `set` | Inspect parameters |
| Search Companies | `httpRequest` | Inspect parameters |
| Extract Company Data | `splitOut` | Inspect parameters |

## Connection map

- Set Variables → Search Companies (`main`, output 0, input 0)
- Is New Company? → Add Company to CRM (`main`, output 0, input 0)
- Is New Company? → Process Each Company (`main`, output 1, input 0)
- Get Company Info → Filter Valid Companies (`main`, output 0, input 0)
- Search Companies → Extract Company Data (`main`, output 0, input 0)
- Add Company to CRM → Process Each Company (`main`, output 0, input 0)
- Extract Company Data → Process Each Company (`main`, output 0, input 0)
- Process Each Company → Get Company Info (`main`, output 1, input 0)
- Filter Valid Companies → Check If Company Exists (`main`, output 0, input 0)
- Filter Valid Companies → Process Each Company (`main`, output 1, input 0)
- Check If Company Exists → Is New Company? (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Variables (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1564_Splitout_Manual_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1564_Splitout_Manual_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
