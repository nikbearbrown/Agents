# Workflow stats

This folder contains the **Workflow stats** workflow. Its executable nodes use `aggregate`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `html`, `manualTrigger`, `merge`, `moveBinaryData`, `n8n`, `respondToWebhook`, `set`, `sort`, `webhook`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-stats.json`](workflow-stats.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** When clicking "Test workflow", Execute Workflow Trigger, Request HTML dashboard, Request xsl template

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| nodes-section | `code` | Inspect parameters |
| workflows-section | `set` | Inspect parameters |
| tags-section | `code` | Inspect parameters |
| globals-section | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Convert to XML | `xml` | Inspect parameters |
| Create HTML | `html` | Inspect parameters |
| Move Binary Data | `moveBinaryData` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Respond to Webhook2 | `respondToWebhook` | Inspect parameters |
| Final template | `set` | Inspect parameters |
| Template elements | `set` | Inspect parameters |
| Sort-workflows | `sort` | Inspect parameters |
| Sort-nodes | `sort` | Inspect parameters |
| Sort-tags | `sort` | Inspect parameters |
| Aggregate-workflows | `aggregate` | Inspect parameters |
| Aggregate-nodes | `aggregate` | Inspect parameters |
| Aggregate-tags | `aggregate` | Inspect parameters |
| n8n-get-workflows | `n8n` | Inspect parameters |
| Prepare JSON object | `executeWorkflow` | Inspect parameters |
| get-nodes-via-jmespath | `set` | Inspect parameters |
| Request HTML dashboard | `webhook` | Inspect parameters |
| Request xsl template | `webhook` | Inspect parameters |
| Final-json | `merge` | Inspect parameters |
| webhook-section | `code` | Inspect parameters |
| Sort-whooks | `sort` | Inspect parameters |
| Aggregate-whooks | `aggregate` | Inspect parameters |

## Connection map

- Sort-tags → Aggregate-tags (`main`, output 0, input 0)
- Sort-nodes → Aggregate-nodes (`main`, output 0, input 0)
- Create HTML → Move Binary Data (`main`, output 0, input 0)
- Sort-whooks → Aggregate-whooks (`main`, output 0, input 0)
- tags-section → Sort-tags (`main`, output 0, input 0)
- nodes-section → Sort-nodes (`main`, output 0, input 0)
- Aggregate-tags → Final-json (`main`, output 0, input 3)
- Convert to XML → Create HTML (`main`, output 0, input 0)
- Final template → Respond to Webhook2 (`main`, output 0, input 0)
- Sort-workflows → Aggregate-workflows (`main`, output 0, input 0)
- Aggregate-nodes → Final-json (`main`, output 0, input 2)
- globals-section → Final-json (`main`, output 0, input 0)
- webhook-section → Sort-whooks (`main`, output 0, input 0)
- Aggregate-whooks → Final-json (`main`, output 0, input 4)
- Move Binary Data → Respond to Webhook (`main`, output 0, input 0)
- Template elements → Final template (`main`, output 0, input 0)
- n8n-get-workflows → get-nodes-via-jmespath (`main`, output 0, input 0)
- workflows-section → nodes-section (`main`, output 0, input 0)
- workflows-section → tags-section (`main`, output 0, input 0)
- workflows-section → globals-section (`main`, output 0, input 0)
- workflows-section → Sort-workflows (`main`, output 0, input 0)
- workflows-section → webhook-section (`main`, output 0, input 0)
- Aggregate-workflows → Final-json (`main`, output 0, input 1)
- Prepare JSON object → Convert to XML (`main`, output 0, input 0)
- Request xsl template → Template elements (`main`, output 0, input 0)
- Request HTML dashboard → Prepare JSON object (`main`, output 0, input 0)
- get-nodes-via-jmespath → workflows-section (`main`, output 0, input 0)
- Execute Workflow Trigger → n8n-get-workflows (`main`, output 0, input 0)
- When clicking "Test workflow" → n8n-get-workflows (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1401_Code_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1401_Code_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
