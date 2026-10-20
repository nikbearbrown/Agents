# Trigger scan on Qualys agent

This folder contains the **Trigger scan on Qualys agent** workflow. Its executable nodes use `executeWorkflowTrigger`, `httpRequest`, `if`, `manualTrigger`, `merge`, `noOp`, `set`, `slack`, `splitInBatches`, `wait`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`trigger-scan-on-qualys-agent.json`](trigger-scan-on-qualys-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `qualysApi`, `slackApi`

**Entry nodes:** Execute Workflow Trigger, When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start VM Scan in Qualys | `httpRequest` | POST |
| Convert XML to JSON | `xml` | Inspect parameters |
| Fetch Scan Results | `httpRequest` | GET |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait 5 Min | `wait` | Inspect parameters |
| Convert XML to JSON1 | `xml` | Inspect parameters |
| Check if Scan Finished | `if` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Post Receipt | `slack` | Inspect parameters |
| Confirm Waiting | `slack` | update |
| Delete Receipt | `slack` | delete |
| Demo Data | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Post Vulnerability Scan Summary to Slack | `slack` | Inspect parameters |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Begin Wait Loop | `noOp` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Save receipt message timestamp | `set` | Inspect parameters |
| Global Variables & Slack Channel | `set` | Inspect parameters |

## Connection map

- Merge → Start VM Scan in Qualys (`main`, output 0, input 0)
- Merge1 → Loop Over Items (`main`, output 0, input 0)
- Demo Data → Merge (`main`, output 0, input 1)
- Wait 5 Min → Fetch Scan Results (`main`, output 0, input 0)
- Post Receipt → Save receipt message timestamp (`main`, output 0, input 0)
- Begin Wait Loop → Merge1 (`main`, output 0, input 0)
- Confirm Waiting → Merge1 (`main`, output 0, input 1)
- Loop Over Items → Wait 5 Min (`main`, output 1, input 0)
- Fetch Scan Results → Convert XML to JSON1 (`main`, output 0, input 0)
- Convert XML to JSON → Confirm Waiting (`main`, output 0, input 0)
- Convert XML to JSON → Begin Wait Loop (`main`, output 0, input 0)
- Convert XML to JSON1 → Check if Scan Finished (`main`, output 0, input 0)
- Check if Scan Finished → Delete Receipt (`main`, output 0, input 0)
- Check if Scan Finished → Post Vulnerability Scan Summary to Slack (`main`, output 0, input 0)
- Check if Scan Finished → Loop Over Items (`main`, output 1, input 0)
- Start VM Scan in Qualys → Convert XML to JSON (`main`, output 0, input 0)
- Execute Workflow Trigger → Demo Data (`main`, output 0, input 0)
- Execute Workflow Trigger → Global Variables & Slack Channel (`main`, output 0, input 0)
- When clicking "Test workflow" → Demo Data (`main`, output 0, input 0)
- When clicking "Test workflow" → Global Variables & Slack Channel (`main`, output 0, input 0)
- Save receipt message timestamp → Merge (`main`, output 0, input 0)
- Global Variables & Slack Channel → Post Receipt (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0620_Wait_Slack_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0620_Wait_Slack_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
