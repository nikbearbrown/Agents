# Marketing Insights Processing

This folder contains the **Marketing Insights Processing** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `if`, `notion`, `set`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`marketing-insights-processing.json`](marketing-insights-processing.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Create Marketing Insight Data | `notion` | databasePage |
| Check if Recurring Topics Found | `if` | Inspect parameters |
| Wait for rate limiting - Recurring | `wait` | Inspect parameters |
| Split Out Recurring Topics | `splitOut` | Inspect parameters |
| Create Recurring Topics Data | `notion` | databasePage |
| Bundle Recurring Topics Data to 1 object | `aggregate` | Inspect parameters |
| Merge Recurring Topics Thread | `set` | Inspect parameters |
| Check if Marketing Insight Data Found | `if` | Inspect parameters |
| Wait for rate limiting - Marketing Insights | `wait` | Inspect parameters |
| Split out Insights | `splitOut` | Inspect parameters |
| Bundle Marketing Insights Data to 1 object | `aggregate` | Inspect parameters |
| Merge Marketing Insights Thread | `set` | Inspect parameters |
| Check if Actionable Insights Data Found | `if` | Inspect parameters |
| Wait for rate limiting - Actionable Insights | `wait` | Inspect parameters |
| Split Out Actionable Insights | `splitOut` | Inspect parameters |
| Create Actionable Insights Data | `notion` | databasePage |
| Bundle Actionable Insights Data to 1 object | `aggregate` | Inspect parameters |
| Merge Actionable Insights Thread | `set` | Inspect parameters |

## Connection map

- Split out Insights → Create Marketing Insight Data (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Marketing Insight Data Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Recurring Topics Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Actionable Insights Data Found (`main`, output 0, input 0)
- Split Out Recurring Topics → Create Recurring Topics Data (`main`, output 0, input 0)
- Create Recurring Topics Data → Bundle Recurring Topics Data to 1 object (`main`, output 0, input 0)
- Create Marketing Insight Data → Bundle Marketing Insights Data to 1 object (`main`, output 0, input 0)
- Split Out Actionable Insights → Create Actionable Insights Data (`main`, output 0, input 0)
- Check if Recurring Topics Found → Wait for rate limiting - Recurring (`main`, output 0, input 0)
- Check if Recurring Topics Found → Merge Recurring Topics Thread (`main`, output 1, input 0)
- Create Actionable Insights Data → Bundle Actionable Insights Data to 1 object (`main`, output 0, input 0)
- Wait for rate limiting - Recurring → Split Out Recurring Topics (`main`, output 0, input 0)
- Check if Marketing Insight Data Found → Wait for rate limiting - Marketing Insights (`main`, output 0, input 0)
- Check if Marketing Insight Data Found → Merge Marketing Insights Thread (`main`, output 1, input 0)
- Check if Actionable Insights Data Found → Wait for rate limiting - Actionable Insights (`main`, output 0, input 0)
- Check if Actionable Insights Data Found → Merge Actionable Insights Thread (`main`, output 1, input 0)
- Bundle Recurring Topics Data to 1 object → Merge Recurring Topics Thread (`main`, output 0, input 0)
- Bundle Marketing Insights Data to 1 object → Merge Marketing Insights Thread (`main`, output 0, input 0)
- Bundle Actionable Insights Data to 1 object → Merge Actionable Insights Thread (`main`, output 0, input 0)
- Wait for rate limiting - Marketing Insights → Split out Insights (`main`, output 0, input 0)
- Wait for rate limiting - Actionable Insights → Split Out Actionable Insights (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0764_Wait_Splitout_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0764_Wait_Splitout_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
