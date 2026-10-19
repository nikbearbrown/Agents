# Credentials Transfer

This folder contains the **Credentials Transfer** workflow. Its executable nodes use `code`, `executeCommand`, `extractFromFile`, `form`, `formTrigger`, `httpRequest`, `readWriteFile`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`credentials-transfer.json`](credentials-transfer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Success | `form` | completion |
| Error | `form` | completion |
| Create Credential | `httpRequest` | POST |
| Get Instance Names | `code` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Export Credentials | `executeCommand` | Inspect parameters |
| Get Credentials Data | `readWriteFile` | Inspect parameters |
| Binary to JSON | `extractFromFile` | fromJson |
| Get Credential Names | `code` | Inspect parameters |
| Choose Instance | `form` | Inspect parameters |
| Choose Credential | `form` | Inspect parameters |
| Prepare Request Data | `code` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |

## Connection map

- Settings → Get Instance Names (`main`, output 0, input 0)
- Binary to JSON → Get Credential Names (`main`, output 0, input 0)
- Choose Instance → Export Credentials (`main`, output 0, input 0)
- Choose Credential → Prepare Request Data (`main`, output 0, input 0)
- Create Credential → Success (`main`, output 0, input 0)
- Create Credential → Error (`main`, output 1, input 0)
- Export Credentials → Get Credentials Data (`main`, output 0, input 0)
- Get Instance Names → Choose Instance (`main`, output 0, input 0)
- On form submission → Settings (`main`, output 0, input 0)
- Get Credential Names → Choose Credential (`main`, output 0, input 0)
- Get Credentials Data → Binary to JSON (`main`, output 0, input 0)
- Prepare Request Data → Create Credential (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1984_Code_Executecommand_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1984_Code_Executecommand_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
