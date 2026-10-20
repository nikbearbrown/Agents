# Triggered from Slack Parent Workflow

This folder contains the **Triggered from Slack Parent Workflow** workflow. Its executable nodes use `executeWorkflowTrigger`, `httpRequest`, `if`, `set`, `slack`, `splitInBatches`, `wait`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`triggered-from-slack-parent-workflow.json`](triggered-from-slack-parent-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `qualysApi`, `slackApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Global Variables | `set` | Inspect parameters |
| Fetch Report IDs | `httpRequest` | GET |
| Convert XML To JSON | `xml` | Inspect parameters |
| Launch Report | `httpRequest` | POST |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait 1 Minute | `wait` | Inspect parameters |
| Check Status of Report | `httpRequest` | GET |
| Is Report Finished? | `if` | Inspect parameters |
| Download Report | `httpRequest` | GET |
| Slack | `slack` | file |
| Convert Report Launch XML to JSON | `xml` | Inspect parameters |
| Convert Report List to JSON | `xml` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Demo Data | `set` | Inspect parameters |

## Connection map

- Demo Data → Global Variables (`main`, output 0, input 0)
- Launch Report → Convert Report Launch XML to JSON (`main`, output 0, input 0)
- Wait 1 Minute → Check Status of Report (`main`, output 0, input 0)
- Download Report → Slack (`main`, output 0, input 0)
- Loop Over Items → Wait 1 Minute (`main`, output 1, input 0)
- Fetch Report IDs → Convert XML To JSON (`main`, output 0, input 0)
- Global Variables → Fetch Report IDs (`main`, output 0, input 0)
- Convert XML To JSON → Launch Report (`main`, output 0, input 0)
- Is Report Finished? → Download Report (`main`, output 0, input 0)
- Is Report Finished? → Loop Over Items (`main`, output 1, input 0)
- Check Status of Report → Convert Report List to JSON (`main`, output 0, input 0)
- Execute Workflow Trigger → Demo Data (`main`, output 0, input 0)
- Convert Report List to JSON → Is Report Finished? (`main`, output 0, input 0)
- Convert Report Launch XML to JSON → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0621_Wait_Slack_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0621_Wait_Slack_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
