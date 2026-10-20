# Click the `Execute Workflow` button and double click on the nodes to see the input and output items.

This folder contains the **Click the `Execute Workflow` button and double click on the nodes to see the input and output items.** workflow. Its executable nodes use `if`, `manualTrigger`, `n8nTrainingCustomerDatastore`, `n8nTrainingCustomerMessenger`, `noOp`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`click-the-execute-workflow-button-and-double-click-on-the-nodes-to-see-the-input-and-output-items-b41f2eba.json`](click-the-execute-workflow-button-and-double-click-on-the-nodes-to-see-the-input-and-output-items-b41f2eba.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Create approval URL | `set` | Inspect parameters |
| Wait for external approval | `wait` | Inspect parameters |
| Rest of the workflow placeholder | `noOp` | Inspect parameters |
| Customer Datastore | `n8nTrainingCustomerDatastore` | getAllPeople |
| SplitInBatches | `splitInBatches` | Inspect parameters |
| Wait for time interval | `wait` | Inspect parameters |
| If - Are we Finished? | `if` | Inspect parameters |
| Customer Messenger - Send URL to merchant | `n8nTrainingCustomerMessenger` | Inspect parameters |
| Customer Messenger - Send message to client | `n8nTrainingCustomerMessenger` | Inspect parameters |

## Connection map

- SplitInBatches → Wait for time interval (`main`, output 0, input 0)
- Customer Datastore → SplitInBatches (`main`, output 0, input 0)
- Create approval URL → Customer Messenger - Send URL to merchant (`main`, output 0, input 0)
- If - Are we Finished? → Create approval URL (`main`, output 0, input 0)
- If - Are we Finished? → SplitInBatches (`main`, output 1, input 0)
- On clicking 'execute' → Customer Datastore (`main`, output 0, input 0)
- Wait for time interval → Customer Messenger - Send message to client (`main`, output 0, input 0)
- Wait for external approval → Rest of the workflow placeholder (`main`, output 0, input 0)
- Customer Messenger - Send URL to merchant → Wait for external approval (`main`, output 0, input 0)
- Customer Messenger - Send message to client → If - Are we Finished? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/N8ntrainingcustomermessenger/0230_N8Ntrainingcustomermessenger_Wait_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/N8ntrainingcustomermessenger/0230_N8Ntrainingcustomermessenger_Wait_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
