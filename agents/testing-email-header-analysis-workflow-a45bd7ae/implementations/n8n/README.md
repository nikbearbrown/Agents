# Testing Email Header Analysis Workflow

This folder contains the **Testing Email Header Analysis Workflow** workflow. Its executable nodes use `aggregate`, `code`, `gmailTrigger`, `httpRequest`, `if`, `limit`, `merge`, `noOp`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`testing-email-header-analysis-workflow-a45bd7ae.json`](testing-email-header-analysis-workflow-a45bd7ae.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** Gmail Trigger, Gmail - Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Gmail - Extract Received Headers | `code` | Inspect parameters |
| Gmail - Extract Original From IP | `set` | Inspect parameters |
| Gmail - Original IP Found? | `if` | Inspect parameters |
| Gmail - Query IP Quality Score API | `httpRequest` | Inspect parameters |
| Gmail - Query IP API | `httpRequest` | Inspect parameters |
| Gmail - Authentication-Results Header? | `if` | Inspect parameters |
| Gmail - Received-SPF Header? | `if` | Inspect parameters |
| Gmail - Extract Authentication-Results Header | `code` | Inspect parameters |
| Gmail - Extract Received-SPF Header | `code` | Inspect parameters |
| Gmail - Determine Auth Values | `set` | Inspect parameters |
| Gmail - Set SPF Value | `set` | Inspect parameters |
| Gmail - No SPF Found | `set` | Inspect parameters |
| Gmail - Format Output | `set` | Inspect parameters |
| Gmail - DKIM Signature Found | `set` | Inspect parameters |
| Gmail - DKIM-Signature Header? | `if` | Inspect parameters |
| Gmail - No DKIM Signature Found | `set` | Inspect parameters |
| Gmail - Set DMARC Value | `set` | Inspect parameters |
| Gmail - Extract DMARC Header | `code` | Inspect parameters |
| Gmail - DMARC Header? | `if` | Inspect parameters |
| Gmail - No DMARC Header | `set` | Inspect parameters |
| Set Gmail Headers Here | `set` | Inspect parameters |
| Format Individual Auth Outputs1 | `set` | Inspect parameters |
| Format Combined Auth Output1 | `set` | Inspect parameters |
| Gmail - Webhook | `webhook` | Inspect parameters |
| Gmail - Remove Extra Received Headers | `limit` | Inspect parameters |
| Gmail - Merge | `merge` | Inspect parameters |
| Gmail - Aggregate | `aggregate` | Inspect parameters |
| Gmail - Set Headers | `set` | Inspect parameters |
| Gmail - Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Aggregate Received-SPF Headers1 | `aggregate` | Inspect parameters |
| Set Gmail Webhook Headers Here | `set` | Inspect parameters |
| Skip IP Check | `noOp` | Inspect parameters |

## Connection map

- Gmail - Merge → Gmail - Aggregate (`main`, output 0, input 0)
- Gmail Trigger → Set Gmail Headers Here (`main`, output 0, input 0)
- Skip IP Check → Gmail - Authentication-Results Header? (`main`, output 0, input 0)
- Gmail - Webhook → Set Gmail Webhook Headers Here (`main`, output 0, input 0)
- Gmail - Aggregate → Format Individual Auth Outputs1 (`main`, output 0, input 0)
- Gmail - Set Headers → Gmail - Extract Received Headers (`main`, output 0, input 0)
- Gmail - No SPF Found → Gmail - Merge (`main`, output 0, input 0)
- Gmail - Query IP API → Gmail - Authentication-Results Header? (`main`, output 0, input 0)
- Gmail - DMARC Header? → Gmail - Extract DMARC Header (`main`, output 0, input 0)
- Gmail - DMARC Header? → Gmail - No DMARC Header (`main`, output 1, input 0)
- Gmail - Format Output → Gmail - Respond to Webhook (`main`, output 0, input 0)
- Gmail - Set SPF Value → Gmail - Merge (`main`, output 0, input 0)
- Set Gmail Headers Here → Gmail - Set Headers (`main`, output 0, input 0)
- Gmail - No DMARC Header → Gmail - Merge (`main`, output 0, input 2)
- Gmail - Set DMARC Value → Gmail - Merge (`main`, output 0, input 2)
- Gmail - Original IP Found? → Gmail - Query IP Quality Score API (`main`, output 0, input 0)
- Gmail - Original IP Found? → Skip IP Check (`main`, output 1, input 0)
- Format Combined Auth Output1 → Gmail - Format Output (`main`, output 0, input 0)
- Gmail - DKIM Signature Found → Gmail - Merge (`main`, output 0, input 1)
- Gmail - Extract DMARC Header → Gmail - Set DMARC Value (`main`, output 0, input 0)
- Gmail - Received-SPF Header? → Gmail - Extract Received-SPF Header (`main`, output 0, input 0)
- Gmail - Received-SPF Header? → Gmail - No SPF Found (`main`, output 1, input 0)
- Gmail - Determine Auth Values → Format Combined Auth Output1 (`main`, output 0, input 0)
- Gmail - DKIM-Signature Header? → Gmail - DKIM Signature Found (`main`, output 0, input 0)
- Gmail - DKIM-Signature Header? → Gmail - No DKIM Signature Found (`main`, output 1, input 0)
- Set Gmail Webhook Headers Here → Gmail - Set Headers (`main`, output 0, input 0)
- Aggregate Received-SPF Headers1 → Gmail - Set SPF Value (`main`, output 0, input 0)
- Format Individual Auth Outputs1 → Gmail - Format Output (`main`, output 0, input 0)
- Gmail - No DKIM Signature Found → Gmail - Merge (`main`, output 0, input 1)
- Gmail - Extract Original From IP → Gmail - Original IP Found? (`main`, output 0, input 0)
- Gmail - Extract Received Headers → Gmail - Remove Extra Received Headers (`main`, output 0, input 0)
- Gmail - Query IP Quality Score API → Gmail - Query IP API (`main`, output 0, input 0)
- Gmail - Extract Received-SPF Header → Aggregate Received-SPF Headers1 (`main`, output 0, input 0)
- Gmail - Remove Extra Received Headers → Gmail - Extract Original From IP (`main`, output 0, input 0)
- Gmail - Authentication-Results Header? → Gmail - Extract Authentication-Results Header (`main`, output 0, input 0)
- Gmail - Authentication-Results Header? → Gmail - Received-SPF Header? (`main`, output 1, input 0)
- Gmail - Authentication-Results Header? → Gmail - DKIM-Signature Header? (`main`, output 1, input 0)
- Gmail - Authentication-Results Header? → Gmail - DMARC Header? (`main`, output 1, input 0)
- Gmail - Extract Authentication-Results Header → Gmail - Determine Auth Values (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0674_Limit_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0674_Limit_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
