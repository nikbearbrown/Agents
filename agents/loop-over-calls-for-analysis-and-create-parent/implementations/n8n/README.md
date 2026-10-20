# Loop over calls for analysis and Create Parent

This folder contains the **Loop over calls for analysis and Create Parent** workflow. Its executable nodes use `aggregate`, `compareDatasets`, `executeWorkflow`, `executeWorkflowTrigger`, `merge`, `noOp`, `notion`, `set`, `slack`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`loop-over-calls-for-analysis-and-create-parent.json`](loop-over-calls-for-analysis-and-create-parent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`, `slackApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop to next call | `noOp` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Create Notion DB Page | `notion` | databasePage |
| Post Slack Receipt | `slack` | Inspect parameters |
| AI Team Processor | `executeWorkflow` | Inspect parameters |
| Update Slack Progress | `slack` | update |
| Merge call data and parent notion id | `merge` | Inspect parameters |
| Reduce down to 1 object | `aggregate` | Inspect parameters |
| Get all older Calls | `notion` | databasePage / getAll |
| Isolate Only Call IDs | `set` | Inspect parameters |
| Only Process New Calls | `compareDatasets` | Inspect parameters |
| Reduce down to One object | `aggregate` | Inspect parameters |
| Bundle Slack Message Data | `aggregate` | Inspect parameters |
| Merge Slack and Call Data | `merge` | Inspect parameters |
| Loop Over Calls | `splitInBatches` | Inspect parameters |
| Bundle Notion Parent Object Data | `aggregate` | Inspect parameters |
| Bundle Processed Calls | `aggregate` | Inspect parameters |
| Post Completed Calls Message | `slack` | Inspect parameters |

## Connection map

- Loop Over Calls → Bundle Processed Calls (`main`, output 0, input 0)
- Loop Over Calls → Merge call data and parent notion id (`main`, output 1, input 0)
- Loop Over Calls → Create Notion DB Page (`main`, output 1, input 0)
- AI Team Processor → Update Slack Progress (`main`, output 0, input 0)
- Loop to next call → Loop Over Calls (`main`, output 0, input 0)
- Post Slack Receipt → Bundle Slack Message Data (`main`, output 0, input 0)
- Get all older Calls → Isolate Only Call IDs (`main`, output 0, input 0)
- Create Notion DB Page → Bundle Notion Parent Object Data (`main`, output 0, input 0)
- Isolate Only Call IDs → Only Process New Calls (`main`, output 0, input 1)
- Update Slack Progress → Loop to next call (`main`, output 0, input 0)
- Bundle Processed Calls → Post Completed Calls Message (`main`, output 0, input 0)
- Only Process New Calls → Reduce down to One object (`main`, output 0, input 0)
- Only Process New Calls → Merge Slack and Call Data (`main`, output 0, input 1)
- Reduce down to 1 object → Get all older Calls (`main`, output 0, input 0)
- Execute Workflow Trigger → Only Process New Calls (`main`, output 0, input 0)
- Execute Workflow Trigger → Reduce down to 1 object (`main`, output 0, input 0)
- Bundle Slack Message Data → Merge Slack and Call Data (`main`, output 0, input 0)
- Merge Slack and Call Data → Loop Over Calls (`main`, output 0, input 0)
- Reduce down to One object → Post Slack Receipt (`main`, output 0, input 0)
- Bundle Notion Parent Object Data → Merge call data and parent notion id (`main`, output 0, input 1)
- Merge call data and parent notion id → AI Team Processor (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0761_Slack_Comparedatasets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Slack/0761_Slack_Comparedatasets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
