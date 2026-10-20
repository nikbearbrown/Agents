# Property Lead Contact Enrichment from CRM

This folder contains the **Property Lead Contact Enrichment from CRM** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `hubspot`, `manualTrigger`, `scheduleTrigger`, `set`, `spreadsheetFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`property-lead-contact-enrichment-from-crm.json`](property-lead-contact-enrichment-from-crm.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking "Execute Workflow", Daily Schedule

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Daily Schedule | `scheduleTrigger` | Inspect parameters |
| Search Properties API | `httpRequest` | POST |
| Configure Search Parameters | `set` | Inspect parameters |
| Filter Property Results | `code` | Inspect parameters |
| Get Owner Contact Info | `httpRequest` | POST |
| Format Lead Data | `code` | Inspect parameters |
| Create Excel Spreadsheet | `spreadsheetFile` | toFile |
| Push to CRM | `hubspot` | Inspect parameters |
| Email Notification | `emailSend` | Inspect parameters |
| Summarize Results | `code` | Inspect parameters |

## Connection map

- Daily Schedule → Configure Search Parameters (`main`, output 0, input 0)
- Format Lead Data → Create Excel Spreadsheet (`main`, output 0, input 0)
- Format Lead Data → Push to CRM (`main`, output 0, input 0)
- Format Lead Data → Summarize Results (`main`, output 0, input 0)
- Summarize Results → Email Notification (`main`, output 0, input 0)
- Search Properties API → Filter Property Results (`main`, output 0, input 0)
- Get Owner Contact Info → Format Lead Data (`main`, output 0, input 0)
- Filter Property Results → Get Owner Contact Info (`main`, output 0, input 0)
- Create Excel Spreadsheet → Email Notification (`main`, output 0, input 0)
- Configure Search Parameters → Search Properties API (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Configure Search Parameters (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Emailsend/1628_Emailsend_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Emailsend/1628_Emailsend_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
