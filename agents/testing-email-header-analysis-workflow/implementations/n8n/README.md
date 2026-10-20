# Testing Email Header Analysis Workflow

This folder contains the **Testing Email Header Analysis Workflow** workflow. Its executable nodes use `aggregate`, `code`, `httpRequest`, `if`, `limit`, `merge`, `microsoftOutlookTrigger`, `noOp`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`testing-email-header-analysis-workflow.json`](testing-email-header-analysis-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftOutlookOAuth2Api`

**Entry nodes:** Trigger on New Email, Webhook1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Trigger on New Email | `microsoftOutlookTrigger` | Inspect parameters |
| Retrieve Headers of Email | `httpRequest` | Inspect parameters |
| Extract Received Headers | `code` | Inspect parameters |
| Remove Extra Received Headers | `limit` | Inspect parameters |
| Extract Original From IP | `set` | Inspect parameters |
| Query IP Quality Score API | `httpRequest` | Inspect parameters |
| Query IP API | `httpRequest` | Inspect parameters |
| Authentication-Results Header? | `if` | Inspect parameters |
| Extract Authentication-Results Header | `code` | Inspect parameters |
| Received-SPF Header? | `if` | Inspect parameters |
| DKIM-Signature Header? | `if` | Inspect parameters |
| Set SPF Value | `set` | Inspect parameters |
| Extract Received-SPF Header | `code` | Inspect parameters |
| DKIM Signature Found | `set` | Inspect parameters |
| DMARC Header? | `if` | Inspect parameters |
| No DMARC Header | `set` | Inspect parameters |
| Extract DMARC Header | `code` | Inspect parameters |
| Set DMARC Value | `set` | Inspect parameters |
| Original IP Found? | `if` | Inspect parameters |
| No DKIM Signature Found | `set` | Inspect parameters |
| Determine Auth Values | `set` | Inspect parameters |
| No SPF Found | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Format Webhook Output | `set` | Inspect parameters |
| Format Individual Auth Outputs | `set` | Inspect parameters |
| Format Combined Auth Output | `set` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Webhook1 | `webhook` | Inspect parameters |
| Set Headers | `set` | Inspect parameters |
| Aggregate Received-SPF Headers | `aggregate` | Inspect parameters |
| Set Headers Here | `set` | Inspect parameters |
| Set Webhook Headers Here | `set` | Inspect parameters |

## Connection map

- Merge → Aggregate (`main`, output 0, input 0)
- Webhook1 → Set Webhook Headers Here (`main`, output 0, input 0)
- Aggregate → Format Individual Auth Outputs (`main`, output 0, input 0)
- Set Headers → Extract Received Headers (`main`, output 0, input 0)
- No SPF Found → Merge (`main`, output 0, input 0)
- Query IP API → Authentication-Results Header? (`main`, output 0, input 0)
- DMARC Header? → Extract DMARC Header (`main`, output 0, input 0)
- DMARC Header? → No DMARC Header (`main`, output 1, input 0)
- Set SPF Value → Merge (`main`, output 0, input 0)
- No DMARC Header → Merge (`main`, output 0, input 2)
- Set DMARC Value → Merge (`main`, output 0, input 2)
- Set Headers Here → Set Headers (`main`, output 0, input 0)
- Original IP Found? → Query IP Quality Score API (`main`, output 0, input 0)
- Original IP Found? → No Operation, do nothing (`main`, output 1, input 0)
- DKIM Signature Found → Merge (`main`, output 0, input 1)
- Extract DMARC Header → Set DMARC Value (`main`, output 0, input 0)
- Received-SPF Header? → Extract Received-SPF Header (`main`, output 0, input 0)
- Received-SPF Header? → No SPF Found (`main`, output 1, input 0)
- Trigger on New Email → Retrieve Headers of Email (`main`, output 0, input 0)
- Determine Auth Values → Format Combined Auth Output (`main`, output 0, input 0)
- Format Webhook Output → Respond to Webhook (`main`, output 0, input 0)
- DKIM-Signature Header? → DKIM Signature Found (`main`, output 0, input 0)
- DKIM-Signature Header? → No DKIM Signature Found (`main`, output 1, input 0)
- No DKIM Signature Found → Merge (`main`, output 0, input 1)
- Extract Original From IP → Original IP Found? (`main`, output 0, input 0)
- Extract Received Headers → Remove Extra Received Headers (`main`, output 0, input 0)
- No Operation, do nothing → Authentication-Results Header? (`main`, output 0, input 0)
- Set Webhook Headers Here → Set Headers (`main`, output 0, input 0)
- Retrieve Headers of Email → Set Headers Here (`main`, output 0, input 0)
- Query IP Quality Score API → Query IP API (`main`, output 0, input 0)
- Extract Received-SPF Header → Aggregate Received-SPF Headers (`main`, output 0, input 0)
- Format Combined Auth Output → Format Webhook Output (`main`, output 0, input 0)
- Remove Extra Received Headers → Extract Original From IP (`main`, output 0, input 0)
- Aggregate Received-SPF Headers → Set SPF Value (`main`, output 0, input 0)
- Authentication-Results Header? → Extract Authentication-Results Header (`main`, output 0, input 0)
- Authentication-Results Header? → Received-SPF Header? (`main`, output 1, input 0)
- Authentication-Results Header? → DKIM-Signature Header? (`main`, output 1, input 0)
- Authentication-Results Header? → DMARC Header? (`main`, output 1, input 0)
- Format Individual Auth Outputs → Format Webhook Output (`main`, output 0, input 0)
- Extract Authentication-Results Header → Determine Auth Values (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0673_Limit_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0673_Limit_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
