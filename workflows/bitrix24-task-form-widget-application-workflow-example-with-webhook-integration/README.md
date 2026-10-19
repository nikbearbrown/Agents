# Bitrix24 Task Form Widget Application Workflow example with Webhook Integration

This folder contains the **Bitrix24 Task Form Widget Application Workflow example with Webhook Integration** workflow. Its executable nodes use `code`, `convertToFile`, `extractFromFile`, `function`, `httpRequest`, `if`, `merge`, `readWriteFile`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`bitrix24-task-form-widget-application-workflow-example-with-webhook-integration.json`](bitrix24-task-form-widget-application-workflow-example-with-webhook-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Bitrix24 Handler

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Bitrix24 Handler | `webhook` | Inspect parameters |
| Extract Credentials | `set` | Inspect parameters |
| Check Event Type | `code` | Inspect parameters |
| Is Installation? | `if` | Inspect parameters |
| Register Placement | `httpRequest` | POST |
| Process Settings | `function` | Inspect parameters |
| Installation Response | `respondToWebhook` | Inspect parameters |
| Has Valid Settings? | `if` | Inspect parameters |
| Get Task Data | `httpRequest` | POST |
| Format Task Data | `function` | Inspect parameters |
| Task View Response | `respondToWebhook` | Inspect parameters |
| Error Response | `respondToWebhook` | Inspect parameters |
| Save Installation Settings | `readWriteFile` | write |
| Set Settings Data | `set` | Inspect parameters |
| Create Settings File | `convertToFile` | toJson |
| Read Installation Settings | `readWriteFile` | Inspect parameters |
| If Installation finished | `if` | Inspect parameters |
| Installation finished Response | `respondToWebhook` | Inspect parameters |
| Merge Installation info | `merge` | Inspect parameters |
| Extract Installation Settings | `extractFromFile` | fromJson |
| Merge request data with installation settings | `merge` | Inspect parameters |

## Connection map

- Get Task Data → Format Task Data (`main`, output 0, input 0)
- Bitrix24 Handler → Extract Credentials (`main`, output 0, input 0)
- Check Event Type → Is Installation? (`main`, output 0, input 0)
- Format Task Data → Task View Response (`main`, output 0, input 0)
- Is Installation? → If Installation finished (`main`, output 0, input 0)
- Is Installation? → Read Installation Settings (`main`, output 1, input 0)
- Is Installation? → Merge request data with installation settings (`main`, output 1, input 0)
- Process Settings → Has Valid Settings? (`main`, output 0, input 0)
- Set Settings Data → Create Settings File (`main`, output 0, input 0)
- Register Placement → Merge Installation info (`main`, output 0, input 0)
- Extract Credentials → Check Event Type (`main`, output 0, input 0)
- Has Valid Settings? → Get Task Data (`main`, output 0, input 0)
- Has Valid Settings? → Error Response (`main`, output 1, input 0)
- Create Settings File → Save Installation Settings (`main`, output 0, input 0)
- Merge Installation info → Installation Response (`main`, output 0, input 0)
- If Installation finished → Installation finished Response (`main`, output 0, input 0)
- If Installation finished → Register Placement (`main`, output 1, input 0)
- If Installation finished → Set Settings Data (`main`, output 1, input 0)
- Read Installation Settings → Extract Installation Settings (`main`, output 0, input 0)
- Save Installation Settings → Merge Installation info (`main`, output 0, input 1)
- Extract Installation Settings → Merge request data with installation settings (`main`, output 0, input 1)
- Merge request data with installation settings → Process Settings (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1356_Code_Webhook_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1356_Code_Webhook_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
