# Scalable Webhook Orchestrator

This folder contains the **Scalable Webhook Orchestrator** workflow. Its executable nodes use `httpRequest`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scalable-webhook-orchestrator.json`](scalable-webhook-orchestrator.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Parse Input | `set` | Inspect parameters |
| Route by action | `switch` | Inspect parameters |
| HTTP Service A | `httpRequest` | POST |
| Compose Ping | `set` | Inspect parameters |
| Compose Result | `set` | Inspect parameters |
| Respond | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook → Parse Input (`main`, output 0, input 0)
- Parse Input → Route by action (`main`, output 0, input 0)
- Route by action → Compose Ping (`main`, output 0, input 0)
- Route by action → HTTP Service A (`main`, output 1, input 0)
- HTTP Service A → Compose Result (`main`, output 0, input 0)
- Compose Ping → Respond (`main`, output 0, input 0)
- Compose Result → Respond (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Templates/9001_Scalable_Webhook_Orchestrator_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Templates/9001_Scalable_Webhook_Orchestrator_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
