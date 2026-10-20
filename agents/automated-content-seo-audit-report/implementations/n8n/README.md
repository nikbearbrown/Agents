# Automated Content SEO Audit Report

This folder contains the **Automated Content SEO Audit Report** workflow. Its executable nodes use `code`, `convertToFile`, `httpRequest`, `if`, `manualTrigger`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-content-seo-audit-report.json`](automated-content-seo-audit-report.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Start’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set Fields | `set` | Inspect parameters |
| When clicking ‘Start’ | `manualTrigger` | Inspect parameters |
| Check Task Status | `httpRequest` | Inspect parameters |
| Create Task | `httpRequest` | POST |
| If | `if` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Get RAW Audit Data | `httpRequest` | POST |
| Extract URLs | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Query GSC API | `httpRequest` | POST |
| Wait1 | `wait` | Inspect parameters |
| Map GSC Data to URL | `set` | Inspect parameters |
| Merge GSC Data with RAW Data | `code` | Inspect parameters |
| Build Report Structure | `code` | Inspect parameters |
| Generate HTML Report | `code` | Inspect parameters |
| Extract 404 & 301 | `code` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Map URLs Data | `code` | Inspect parameters |
| Get Source URLs Data | `httpRequest` | POST |
| Download Report | `convertToFile` | toText |

## Connection map

- If → Get RAW Audit Data (`main`, output 0, input 0)
- If → Wait (`main`, output 1, input 0)
- Wait → Check Task Status (`main`, output 0, input 0)
- Wait1 → Map GSC Data to URL (`main`, output 0, input 0)
- Set Fields → Create Task (`main`, output 0, input 0)
- Create Task → Check Task Status (`main`, output 0, input 0)
- Extract URLs → Loop Over Items (`main`, output 0, input 0)
- Map URLs Data → Loop Over Items1 (`main`, output 0, input 0)
- Query GSC API → Wait1 (`main`, output 0, input 0)
- Loop Over Items → Merge GSC Data with RAW Data (`main`, output 0, input 0)
- Loop Over Items → Query GSC API (`main`, output 1, input 0)
- Loop Over Items1 → Build Report Structure (`main`, output 0, input 0)
- Loop Over Items1 → Get Source URLs Data (`main`, output 1, input 0)
- Check Task Status → If (`main`, output 0, input 0)
- Extract 404 & 301 → Loop Over Items1 (`main`, output 0, input 0)
- Get RAW Audit Data → Extract URLs (`main`, output 0, input 0)
- Map GSC Data to URL → Loop Over Items (`main`, output 0, input 0)
- Generate HTML Report → Download Report (`main`, output 0, input 0)
- Get Source URLs Data → Map URLs Data (`main`, output 0, input 0)
- Build Report Structure → Generate HTML Report (`main`, output 0, input 0)
- When clicking ‘Start’ → Set Fields (`main`, output 0, input 0)
- Merge GSC Data with RAW Data → Extract 404 & 301 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1696_Wait_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1696_Wait_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
