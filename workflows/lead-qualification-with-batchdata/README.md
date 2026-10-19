# Lead Qualification with BatchData

This folder contains the **Lead Qualification with BatchData** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`lead-qualification-with-batchdata.json`](lead-qualification-with-batchdata.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** CRM New Lead Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| CRM New Lead Webhook | `webhook` | Inspect parameters |
| Fetch Lead Data | `httpRequest` | Inspect parameters |
| BatchData Property Lookup | `httpRequest` | Inspect parameters |
| Score And Qualify Lead | `code` | Inspect parameters |
| Update CRM Lead | `httpRequest` | PUT |
| Is High-Value Lead? | `if` | Inspect parameters |
| Create Immediate Follow-up Task | `httpRequest` | POST |
| Send Slack Notification | `slack` | Inspect parameters |

## Connection map

- Fetch Lead Data → BatchData Property Lookup (`main`, output 0, input 0)
- Update CRM Lead → Is High-Value Lead? (`main`, output 0, input 0)
- Is High-Value Lead? → Create Immediate Follow-up Task (`main`, output 0, input 0)
- Is High-Value Lead? → Send Slack Notification (`main`, output 1, input 0)
- CRM New Lead Webhook → Fetch Lead Data (`main`, output 0, input 0)
- Score And Qualify Lead → Update CRM Lead (`main`, output 0, input 0)
- BatchData Property Lookup → Score And Qualify Lead (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1910_Code_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1910_Code_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
