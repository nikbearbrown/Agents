# x402

This folder contains the **x402** workflow. Its executable nodes use `code`, `if`, `oneShot`, `oneShotSynch`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`x402.json`](x402.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `oneShotOAuth2Api`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Check for presence of X-HEADER | `if` | Inspect parameters |
| Decode & Validate X-Payment | `code` | Inspect parameters |
| Simulate Payment | `oneShot` | simulate |
| On Successful Payment Simulation | `if` | Inspect parameters |
| 1Shot API Submit & Wait | `oneShotSynch` | Inspect parameters |
| Ensure Well Formatted Payment Payload | `if` | Inspect parameters |
| Response: Missing or Invalid Payment Headers | `respondToWebhook` | Inspect parameters |
| Response: Payment Invalid | `respondToWebhook` | Inspect parameters |
| Response: 200 - Payment Successful | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → Check for presence of X-HEADER (`main`, output 0, input 0)
- Check for presence of X-HEADER → Decode & Validate X-Payment (`main`, output 0, input 0)
- Check for presence of X-HEADER → Response: Missing or Invalid Payment Headers (`main`, output 1, input 0)
- Decode & Validate X-Payment → Ensure Well Formatted Payment Payload (`main`, output 0, input 0)
- Simulate Payment → On Successful Payment Simulation (`main`, output 0, input 0)
- On Successful Payment Simulation → 1Shot API Submit & Wait (`main`, output 0, input 0)
- On Successful Payment Simulation → Response: Payment Invalid (`main`, output 1, input 0)
- 1Shot API Submit & Wait → Response: 200 - Payment Successful (`main`, output 0, input 0)
- 1Shot API Submit & Wait → Response: Payment Invalid (`main`, output 1, input 0)
- Ensure Well Formatted Payment Payload → Simulate Payment (`main`, output 0, input 0)
- Ensure Well Formatted Payment Payload → Response: Missing or Invalid Payment Headers (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/1Shot-API/n8n-nodes-1shot/blob/099288d799a12a856e15f3f680ef0fd990e7cb43/x402.json](https://github.com/1Shot-API/n8n-nodes-1shot/blob/099288d799a12a856e15f3f680ef0fd990e7cb43/x402.json). License: **MIT**; preserve [the notice](../../../../licenses/1Shot-API--n8n-nodes-1shot.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
