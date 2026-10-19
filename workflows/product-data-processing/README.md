# Product Data Processing

This folder contains the **Product Data Processing** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `if`, `notion`, `set`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`product-data-processing.json`](product-data-processing.json): sanitized, inactive import copy with an overview sticky note.
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
| Check if Product Data Found | `if` | Inspect parameters |
| Create Product Data Object1 | `notion` | databasePage |
| Create Product Feedback Data Object | `notion` | databasePage |
| Check if AI Use Case Data Found | `if` | Inspect parameters |
| Check if AI Mentioned On Call | `if` | Inspect parameters |
| Wait for rate limiting - AI Use Case | `wait` | Inspect parameters |
| Wait for rate limiting - Product Data | `wait` | Inspect parameters |
| Split Out Product Data | `splitOut` | Inspect parameters |
| Bundle AI Use Case Data to 1 object | `aggregate` | Inspect parameters |
| Bundle Product Feedback Data to 1 object | `aggregate` | Inspect parameters |
| Merge AI Use Case Thread | `set` | Inspect parameters |
| Merge Product Feedback Thread | `set` | Inspect parameters |
| Update Call with AI Data Summary | `notion` | databasePage / update |

## Connection map

- Split Out Product Data → Create Product Feedback Data Object (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Product Data Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if AI Use Case Data Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if AI Mentioned On Call (`main`, output 0, input 0)
- Check if Product Data Found → Wait for rate limiting - Product Data (`main`, output 0, input 0)
- Check if Product Data Found → Merge Product Feedback Thread (`main`, output 1, input 0)
- Create Product Data Object1 → Bundle AI Use Case Data to 1 object (`main`, output 0, input 0)
- Check if AI Mentioned On Call → Update Call with AI Data Summary (`main`, output 0, input 0)
- Check if AI Use Case Data Found → Wait for rate limiting - AI Use Case (`main`, output 0, input 0)
- Check if AI Use Case Data Found → Merge AI Use Case Thread (`main`, output 1, input 0)
- Bundle AI Use Case Data to 1 object → Merge AI Use Case Thread (`main`, output 0, input 0)
- Create Product Feedback Data Object → Bundle Product Feedback Data to 1 object (`main`, output 0, input 0)
- Wait for rate limiting - AI Use Case → Create Product Data Object1 (`main`, output 0, input 0)
- Wait for rate limiting - Product Data → Split Out Product Data (`main`, output 0, input 0)
- Bundle Product Feedback Data to 1 object → Merge Product Feedback Thread (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0765_Wait_Splitout_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0765_Wait_Splitout_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
