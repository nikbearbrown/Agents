# CallForge - The AI Gong Sales Call Processor

This folder contains the **CallForge - The AI Gong Sales Call Processor** workflow. Its executable nodes use `aggregate`, `code`, `executeWorkflowTrigger`, `httpRequest`, `merge`, `salesforce`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`callforge-the-ai-gong-sales-call-processor.json`](callforge-the-ai-gong-sales-call-processor.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `salesforceOAuth2Api`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Retrieve detailed call data | `httpRequest` | Inspect parameters |
| Get transcript | `httpRequest` | Inspect parameters |
| Join Transcript to String | `set` | Inspect parameters |
| Isolate Notion Data | `set` | Inspect parameters |
| Join Affiliation | `code` | Inspect parameters |
| Join conversation | `code` | Inspect parameters |
| Extract SF Opp Data | `set` | Inspect parameters |
| Extract SF Opp Data1 | `set` | Inspect parameters |
| Get Opp Data | `salesforce` | opportunity / get |
| Get account data | `salesforce` | account / get |
| Extract Call Data | `splitOut` | Inspect parameters |
| Merge call and transcript Data | `merge` | Inspect parameters |
| Aggregate Gong Call Transcript | `aggregate` | Inspect parameters |
| Get External Attendees Emails | `set` | Inspect parameters |
| Combine Salesforce Opp Data | `merge` | Inspect parameters |
| Aggregate Salesforce data | `aggregate` | Inspect parameters |
| Merge Enriched Transcript Data | `merge` | Inspect parameters |

## Connection map

- Get Opp Data → Extract SF Opp Data (`main`, output 0, input 0)
- Get Opp Data → Get account data (`main`, output 0, input 0)
- Get transcript → Join Transcript to String (`main`, output 0, input 0)
- Get account data → Extract SF Opp Data1 (`main`, output 0, input 0)
- Join Affiliation → Join conversation (`main`, output 0, input 0)
- Extract Call Data → Merge call and transcript Data (`main`, output 0, input 1)
- Join conversation → Get External Attendees Emails (`main`, output 0, input 0)
- Join conversation → Aggregate Gong Call Transcript (`main`, output 0, input 0)
- Extract SF Opp Data → Combine Salesforce Opp Data (`main`, output 0, input 0)
- Extract SF Opp Data1 → Combine Salesforce Opp Data (`main`, output 0, input 1)
- Execute Workflow Trigger → Get transcript (`main`, output 0, input 0)
- Execute Workflow Trigger → Retrieve detailed call data (`main`, output 0, input 0)
- Aggregate Salesforce data → Merge Enriched Transcript Data (`main`, output 0, input 1)
- Join Transcript to String → Merge call and transcript Data (`main`, output 0, input 0)
- Combine Salesforce Opp Data → Aggregate Salesforce data (`main`, output 0, input 0)
- Retrieve detailed call data → Extract Call Data (`main`, output 0, input 0)
- Get External Attendees Emails → Get Opp Data (`main`, output 0, input 0)
- Aggregate Gong Call Transcript → Merge Enriched Transcript Data (`main`, output 0, input 0)
- Merge Enriched Transcript Data → Isolate Notion Data (`main`, output 0, input 0)
- Merge call and transcript Data → Join Affiliation (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0760_Splitout_Code_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0760_Splitout_Code_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
