# Integration Data Processing

This folder contains the **Integration Data Processing** workflow. Its executable nodes use `aggregate`, `executeWorkflowTrigger`, `httpRequest`, `if`, `notion`, `set`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`integration-data-processing.json`](integration-data-processing.json): sanitized, inactive import copy with an overview sticky note.
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
| Check if Competitor Data Found | `if` | Inspect parameters |
| Check if Integration Data Found | `if` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Check if objection found | `if` | Inspect parameters |
| Create Competitors in DB | `notion` | databasePage |
| Create Integrations | `notion` | databasePage |
| Update Call with Objection Summary | `notion` | databasePage / update |
| Check for use cases | `if` | Inspect parameters |
| Update Notion Call object with AI data | `notion` | databasePage / update |
| Split Out all objections | `splitOut` | Inspect parameters |
| Format Tag Data for notion | `set` | Inspect parameters |
| Bundle all Tags | `aggregate` | Inspect parameters |
| Add Objection Tag to Notion | `httpRequest` | PATCH |
| Wait for rate limiting again | `wait` | Inspect parameters |
| Merge Objection Threads | `set` | Inspect parameters |
| Wait for rate limiting - Integration | `wait` | Inspect parameters |
| Split Out Integration data | `splitOut` | Inspect parameters |
| Bundle Integration Data to 1 object | `aggregate` | Inspect parameters |
| Merge Integration Thread | `set` | Inspect parameters |
| Wait for rate limiting - Competitors | `wait` | Inspect parameters |
| Wait for rate limiting - Objection | `wait` | Inspect parameters |
| Wait for rate limiting - Use Cases | `wait` | Inspect parameters |
| Split Out Use Cases | `splitOut` | Inspect parameters |
| Create Use Cases | `notion` | databasePage |
| Bundle Use Case Data to 1 object | `aggregate` | Inspect parameters |
| Bundle Competitor Data to 1 object | `aggregate` | Inspect parameters |
| Split Out Competitor Data | `splitOut` | Inspect parameters |
| Get AI Response - Competitors | `set` | Inspect parameters |
| Merge Competitor Thread | `set` | Inspect parameters |
| Merge Use Case Thread | `set` | Inspect parameters |

## Connection map

- Bundle all Tags → Add Objection Tag to Notion (`main`, output 0, input 0)
- Create Use Cases → Bundle Use Case Data to 1 object (`main`, output 0, input 0)
- Check for use cases → Wait for rate limiting - Use Cases (`main`, output 0, input 0)
- Check for use cases → Merge Use Case Thread (`main`, output 1, input 0)
- Create Integrations → Bundle Integration Data to 1 object (`main`, output 0, input 0)
- Split Out Use Cases → Create Use Cases (`main`, output 0, input 0)
- Check if objection found → Wait for rate limiting - Objection (`main`, output 0, input 0)
- Check if objection found → Merge Objection Threads (`main`, output 1, input 0)
- Create Competitors in DB → Bundle Competitor Data to 1 object (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Integration Data Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if Competitor Data Found (`main`, output 0, input 0)
- Execute Workflow Trigger → Check if objection found (`main`, output 0, input 0)
- Execute Workflow Trigger → Update Notion Call object with AI data (`main`, output 0, input 0)
- Execute Workflow Trigger → Check for use cases (`main`, output 0, input 0)
- Split Out all objections → Format Tag Data for notion (`main`, output 0, input 0)
- Split Out Competitor Data → Create Competitors in DB (`main`, output 0, input 0)
- Format Tag Data for notion → Bundle all Tags (`main`, output 0, input 0)
- Split Out Integration data → Create Integrations (`main`, output 0, input 0)
- Add Objection Tag to Notion → Wait for rate limiting again (`main`, output 0, input 0)
- Wait for rate limiting again → Update Call with Objection Summary (`main`, output 0, input 0)
- Get AI Response - Competitors → Split Out Competitor Data (`main`, output 0, input 0)
- Check if Competitor Data Found → Wait for rate limiting - Competitors (`main`, output 0, input 0)
- Check if Competitor Data Found → Merge Competitor Thread (`main`, output 1, input 0)
- Check if Integration Data Found → Wait for rate limiting - Integration (`main`, output 0, input 0)
- Check if Integration Data Found → Merge Integration Thread (`main`, output 1, input 0)
- Bundle Use Case Data to 1 object → Merge Use Case Thread (`main`, output 0, input 0)
- Bundle Competitor Data to 1 object → Merge Competitor Thread (`main`, output 0, input 0)
- Update Call with Objection Summary → Merge Objection Threads (`main`, output 0, input 0)
- Wait for rate limiting - Objection → Split Out all objections (`main`, output 0, input 0)
- Wait for rate limiting - Use Cases → Split Out Use Cases (`main`, output 0, input 0)
- Bundle Integration Data to 1 object → Merge Integration Thread (`main`, output 0, input 0)
- Wait for rate limiting - Competitors → Get AI Response - Competitors (`main`, output 0, input 0)
- Wait for rate limiting - Integration → Split Out Integration data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0763_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0763_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
