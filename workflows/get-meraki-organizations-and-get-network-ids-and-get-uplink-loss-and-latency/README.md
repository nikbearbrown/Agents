# get meraki organizations and get network ids and get uplink loss and latency

This folder contains the **get meraki organizations and get network ids and get uplink loss and latency** workflow. Its executable nodes use `code`, `httpRequest`, `manualTrigger`, `merge`, `microsoftTeams`, `redis`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-meraki-organizations-and-get-network-ids-and-get-uplink-loss-and-latency.json`](get-meraki-organizations-and-get-network-ids-and-get-uplink-loss-and-latency.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** When clicking "Execute Workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Get Meraki Organizations | `httpRequest` | Inspect parameters |
| Get Network IDs | `httpRequest` | Inspect parameters |
| Get Org Name & ID | `set` | Inspect parameters |
| Combine latency to its respective Network | `merge` | Inspect parameters |
| Makes Latency and Loss Filterable | `set` | Inspect parameters |
| Filters Problematic sites | `code` | Inspect parameters |
| Average Latency & Loss over 5m | `code` | Inspect parameters |
| Get Uplink Loss and Latency | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Sets Network Variables | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Check if Alert Exists | `redis` | get |
| Create Response | `code` | Inspect parameters |
| Message Techs | `microsoftTeams` | chatMessage |
| Log the Alert | `redis` | set |

## Connection map

- Merge → Message Techs (`main`, output 0, input 0)
- Message Techs → Log the Alert (`main`, output 0, input 0)
- Create Response → Merge (`main`, output 0, input 0)
- Get Network IDs → Sets Network Variables (`main`, output 0, input 0)
- Schedule Trigger → Get Meraki Organizations (`main`, output 0, input 0)
- Get Org Name & ID → Get Network IDs (`main`, output 0, input 0)
- Check if Alert Exists → Create Response (`main`, output 0, input 0)
- Sets Network Variables → Combine latency to its respective Network (`main`, output 0, input 0)
- Get Meraki Organizations → Get Org Name & ID (`main`, output 0, input 0)
- Get Meraki Organizations → Get Uplink Loss and Latency (`main`, output 0, input 0)
- Filters Problematic sites → Check if Alert Exists (`main`, output 0, input 0)
- Filters Problematic sites → Merge (`main`, output 0, input 1)
- Get Uplink Loss and Latency → Combine latency to its respective Network (`main`, output 0, input 1)
- Average Latency & Loss over 5m → Filters Problematic sites (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Get Meraki Organizations (`main`, output 0, input 0)
- Makes Latency and Loss Filterable → Average Latency & Loss over 5m (`main`, output 0, input 0)
- Combine latency to its respective Network → Makes Latency and Loss Filterable (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/0387_Redis_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Redis/0387_Redis_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
