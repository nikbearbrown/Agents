# List existing Snapshots

This folder contains the **List existing Snapshots** workflow. Its executable nodes use `dateTime`, `httpRequest`, `if`, `manualTrigger`, `merge`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-existing-snapshots.json`](list-existing-snapshots.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set snapshot attributes | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Credential | `set` | Inspect parameters |
| Authorization | `httpRequest` | POST |
| List instances | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| UUID | `httpRequest` | Inspect parameters |
| TRACE ID | `httpRequest` | Inspect parameters |
| List snapshots | `httpRequest` | Inspect parameters |
| UUID1 | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| get Date & Time | `dateTime` | Inspect parameters |
| Delete existing snapshot | `httpRequest` | DELETE |
| Create a new snapshot | `httpRequest` | POST |
| Create a new snapshot1 | `httpRequest` | POST |
| UUID2 | `httpRequest` | Inspect parameters |
| UUID3 | `httpRequest` | Inspect parameters |
| UUID4 | `httpRequest` | Inspect parameters |
| Formatted Date | `dateTime` | formatDate |
| Whether snapshot there is no snapshot | `if` | Inspect parameters |
| set snapshot attributes | `set` | Inspect parameters |

## Connection map

- UUID → TRACE ID (`main`, output 0, input 0)
- Merge → Whether snapshot there is no snapshot (`main`, output 0, input 0)
- UUID1 → List snapshots (`main`, output 0, input 0)
- UUID2 → Create a new snapshot (`main`, output 0, input 0)
- UUID3 → Delete existing snapshot (`main`, output 0, input 0)
- UUID4 → Create a new snapshot1 (`main`, output 0, input 0)
- TRACE ID → List instances (`main`, output 0, input 0)
- Split Out → UUID1 (`main`, output 0, input 0)
- Split Out → Merge (`main`, output 0, input 1)
- Credential → Authorization (`main`, output 0, input 0)
- Authorization → UUID (`main`, output 0, input 0)
- Formatted Date → Credential (`main`, output 0, input 0)
- List instances → Split Out (`main`, output 0, input 0)
- List snapshots → Merge (`main`, output 0, input 0)
- get Date & Time → Formatted Date (`main`, output 0, input 0)
- Schedule Trigger → get Date & Time (`main`, output 0, input 0)
- Set snapshot attributes → UUID3 (`main`, output 0, input 0)
- set snapshot attributes → UUID2 (`main`, output 0, input 0)
- Delete existing snapshot → UUID4 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → get Date & Time (`main`, output 0, input 0)
- Whether snapshot there is no snapshot → set snapshot attributes (`main`, output 0, input 0)
- Whether snapshot there is no snapshot → Set snapshot attributes (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0570_Splitout_Datetime_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0570_Splitout_Datetime_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
