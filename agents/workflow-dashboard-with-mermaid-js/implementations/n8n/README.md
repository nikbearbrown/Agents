# Workflow dashboard with mermaid.js

This folder contains the **Workflow dashboard with mermaid.js** workflow. Its executable nodes use `aggregate`, `code`, `manualTrigger`, `n8n`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-dashboard-with-mermaid-js.json`](workflow-dashboard-with-mermaid-js.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** When clicking ‘Test workflow’, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Respond with Mermaid | `respondToWebhook` | Inspect parameters |
| List workflows | `n8n` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Single workflow | `n8n` | get |
| Switch | `switch` | Inspect parameters |
| Send Page | `respondToWebhook` | Inspect parameters |
| Prepare workflow list | `set` | Inspect parameters |
| CONFIG | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- Code → Respond with Mermaid (`main`, output 0, input 0)
- CONFIG → Send Page (`main`, output 0, input 0)
- Switch → List workflows (`main`, output 0, input 0)
- Switch → Single workflow (`main`, output 1, input 0)
- Webhook → Switch (`main`, output 0, input 0)
- Aggregate → CONFIG (`main`, output 0, input 0)
- List workflows → Prepare workflow list (`main`, output 0, input 0)
- Single workflow → Code (`main`, output 0, input 0)
- Prepare workflow list → Aggregate (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Switch (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1713_Code_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1713_Code_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
