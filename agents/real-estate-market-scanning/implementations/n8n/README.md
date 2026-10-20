# Real Estate Market Scanning

This folder contains the **Real Estate Market Scanning** workflow. Its executable nodes use `code`, `emailSend`, `filter`, `httpRequest`, `scheduleTrigger`, `set`, `slack`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`real-estate-market-scanning.json`](real-estate-market-scanning.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Market Scan

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Market Scan | `scheduleTrigger` | Inspect parameters |
| BatchData API Configuration | `set` | Inspect parameters |
| Query BatchData Properties | `httpRequest` | POST |
| Get Previous Results | `code` | Inspect parameters |
| Compare Results | `code` | Inspect parameters |
| Split Properties | `splitOut` | Inspect parameters |
| Filter High Potential | `filter` | Inspect parameters |
| Get Property Details | `httpRequest` | Inspect parameters |
| Format Email Content | `set` | Inspect parameters |
| Send Email Alert | `emailSend` | Inspect parameters |
| Post to Slack | `slack` | Inspect parameters |

## Connection map

- Compare Results → Split Properties (`main`, output 0, input 0)
- Split Properties → Filter High Potential (`main`, output 0, input 0)
- Format Email Content → Send Email Alert (`main`, output 0, input 0)
- Format Email Content → Post to Slack (`main`, output 0, input 0)
- Get Previous Results → Compare Results (`main`, output 0, input 0)
- Get Property Details → Format Email Content (`main`, output 0, input 0)
- Schedule Market Scan → BatchData API Configuration (`main`, output 0, input 0)
- Filter High Potential → Get Property Details (`main`, output 0, input 0)
- Query BatchData Properties → Get Previous Results (`main`, output 0, input 0)
- BatchData API Configuration → Query BatchData Properties (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1748_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1748_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
