# Fetch reports from Qualys

This folder contains the **Fetch reports from Qualys** workflow. Its executable nodes use `executeWorkflow`, `filter`, `httpRequest`, `if`, `manualTrigger`, `n8n`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `theHiveProject`, `wait`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-reports-from-qualys.json`](fetch-reports-from-qualys.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `qualysApi`, `theHiveProjectApi`

**Entry nodes:** When clicking "Test workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Global Variables | `set` | Inspect parameters |
| Fetch Reports from Qualys | `httpRequest` | GET |
| Remove Already Processed Reports | `filter` | Inspect parameters |
| Any Reports to Process? | `if` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Update Timestamp | `n8n` | update |
| Get Last Timestamp | `executeWorkflow` | Inspect parameters |
| XML | `xml` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Create Case | `theHiveProject` | case |
| Download Report | `httpRequest` | GET |
| Add Report As Attachment | `theHiveProject` | case / addAttachment |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- XML → Split Out (`main`, output 0, input 0)
- Wait → Create Case (`main`, output 0, input 0)
- Split Out → Remove Already Processed Reports (`main`, output 0, input 0)
- Create Case → Download Report (`main`, output 0, input 0)
- Download Report → Add Report As Attachment (`main`, output 0, input 0)
- Loop Over Items → Update Timestamp (`main`, output 0, input 0)
- Loop Over Items → Wait (`main`, output 1, input 0)
- Global Variables → Get Last Timestamp (`main`, output 0, input 0)
- Schedule Trigger → Global Variables (`main`, output 0, input 0)
- Get Last Timestamp → Fetch Reports from Qualys (`main`, output 0, input 0)
- Any Reports to Process? → Loop Over Items (`main`, output 0, input 0)
- Any Reports to Process? → Update Timestamp (`main`, output 1, input 0)
- Add Report As Attachment → Loop Over Items (`main`, output 0, input 0)
- Fetch Reports from Qualys → XML (`main`, output 0, input 0)
- When clicking "Test workflow" → Global Variables (`main`, output 0, input 0)
- Remove Already Processed Reports → Any Reports to Process? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0627_Wait_Splitout_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0627_Wait_Splitout_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
