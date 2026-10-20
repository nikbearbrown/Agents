# Squarespace Fulfillment Automation with n8n

This folder contains the **Squarespace Fulfillment Automation with n8n** workflow. Its executable nodes use `filter`, `httpRequest`, `manualTrigger`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`squarespace-fulfillment-automation-with-n8n.json`](squarespace-fulfillment-automation-with-n8n.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `oAuth2Api`

**Entry nodes:** On clicking 'execute', Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Split Out Order  | `splitOut` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Query pending Orders | `httpRequest` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Fulfill Order | `httpRequest` | POST |
| Filter Orders | `filter` | Inspect parameters |

## Connection map

- Globals → Query pending Orders (`main`, output 0, input 0)
- Filter Orders → Loop Over Items (`main`, output 0, input 0)
- Fulfill Order → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Fulfill Order (`main`, output 1, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- Split Out Order  → Filter Orders (`main`, output 0, input 0)
- Query pending Orders → Split Out Order  (`main`, output 0, input 0)
- On clicking 'execute' → Globals (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0810_Splitout_Schedule_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0810_Splitout_Schedule_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
