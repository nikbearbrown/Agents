# Submit batch request to Anthropic

This folder contains the **Submit batch request to Anthropic** workflow. Its executable nodes use `aggregate`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `filter`, `httpRequest`, `if`, `manualTrigger`, `memoryBufferWindow`, `memoryManager`, `merge`, `set`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`submit-batch-request-to-anthropic.json`](submit-batch-request-to-anthropic.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`

**Entry nodes:** When Executed by Another Workflow, Run example

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Submit batch | `httpRequest` | POST |
| Check batch status | `httpRequest` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Get results | `httpRequest` | Inspect parameters |
| Parse response | `code` | Inspect parameters |
| If ended processing | `if` | Inspect parameters |
| Batch Status Poll Interval | `wait` | Inspect parameters |
| Run example | `manualTrigger` | Inspect parameters |
| One query example | `set` | Inspect parameters |
| Delete original properties | `set` | Inspect parameters |
| Construct 'requests' array | `aggregate` | Inspect parameters |
| Set desired 'anthropic-version' | `set` | Inspect parameters |
| Execute Workflow 'Process Multiple Prompts in Parallel with Anthropic Claude Batch API' | `executeWorkflow` | Inspect parameters |
| Build batch 'request' object for single query | `code` | Inspect parameters |
| Simple Memory Store | `memoryBufferWindow` | Inspect parameters |
| Fill Chat Memory with example data | `memoryManager` | Inspect parameters |
| Build batch 'request' object from Chat Memory and execution data | `code` | Inspect parameters |
| Load Chat Memory Data | `memoryManager` | Inspect parameters |
| First Prompt Result | `executionData` | Inspect parameters |
| Second Prompt Result | `executionData` | Inspect parameters |
| Split Out Parsed Results | `splitOut` | Inspect parameters |
| Filter Second Prompt Results | `filter` | Inspect parameters |
| Filter First Prompt Results | `filter` | Inspect parameters |
| Join two example requests into array | `merge` | Inspect parameters |
| Append execution data for single query example | `set` | Inspect parameters |
| Append execution data for chat memory example | `set` | Inspect parameters |
| Truncate Chat Memory | `memoryManager` | Inspect parameters |

## Connection map

- Get results → Parse response (`main`, output 0, input 0)
- Run example → One query example (`main`, output 0, input 0)
- Run example → Truncate Chat Memory (`main`, output 0, input 0)
- Submit batch → If ended processing (`main`, output 0, input 0)
- Parse response → Split Out Parsed Results (`main`, output 0, input 0)
- One query example → Append execution data for single query example (`main`, output 0, input 0)
- Check batch status → If ended processing (`main`, output 0, input 0)
- If ended processing → Get results (`main`, output 0, input 0)
- If ended processing → Batch Status Poll Interval (`main`, output 1, input 0)
- Simple Memory Store → Load Chat Memory Data (`ai_memory`, output 0, input 0)
- Simple Memory Store → Fill Chat Memory with example data (`ai_memory`, output 0, input 0)
- Simple Memory Store → Truncate Chat Memory (`ai_memory`, output 0, input 0)
- Truncate Chat Memory → Fill Chat Memory with example data (`main`, output 0, input 0)
- Load Chat Memory Data → Append execution data for chat memory example (`main`, output 0, input 0)
- Batch Status Poll Interval → Check batch status (`main`, output 0, input 0)
- Construct 'requests' array → Set desired 'anthropic-version' (`main`, output 0, input 0)
- Delete original properties → Join two example requests into array (`main`, output 0, input 1)
- Filter First Prompt Results → First Prompt Result (`main`, output 0, input 0)
- Filter Second Prompt Results → Second Prompt Result (`main`, output 0, input 0)
- Set desired 'anthropic-version' → Execute Workflow 'Process Multiple Prompts in Parallel with Anthropic Claude Batch API' (`main`, output 0, input 0)
- When Executed by Another Workflow → Submit batch (`main`, output 0, input 0)
- Fill Chat Memory with example data → Load Chat Memory Data (`main`, output 0, input 0)
- Join two example requests into array → Construct 'requests' array (`main`, output 0, input 0)
- Append execution data for chat memory example → Build batch 'request' object from Chat Memory and execution data (`main`, output 0, input 0)
- Build batch 'request' object for single query → Delete original properties (`main`, output 0, input 0)
- Append execution data for single query example → Build batch 'request' object for single query (`main`, output 0, input 0)
- Build batch 'request' object from Chat Memory and execution data → Join two example requests into array (`main`, output 0, input 0)
- Execute Workflow 'Process Multiple Prompts in Parallel with Anthropic Claude Batch API' → Filter First Prompt Results (`main`, output 0, input 0)
- Execute Workflow 'Process Multiple Prompts in Parallel with Anthropic Claude Batch API' → Filter Second Prompt Results (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0826_Wait_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0826_Wait_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
