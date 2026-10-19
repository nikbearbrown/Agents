# Workflow B — Synthesize & Store Clusters

This folder contains the **Workflow B — Synthesize & Store Clusters** workflow. Its executable nodes use `code`, `executeWorkflowTrigger`, `lmChatAnthropic`, `postgres`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-b-synthesize-store-clusters.json`](workflow-b-synthesize-store-clusters.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `postgres`

**Entry nodes:** Workflow Trigger, Webhook — Receive Request

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Fetch Unprocessed Items | `postgres` | executeQuery |
| Group By Topic Tag | `code` | Inspect parameters |
| Claude — Synthesize Cluster | `lmChatAnthropic` | Inspect parameters |
| Parse Claude Response | `code` | Inspect parameters |
| Store — Insert Cluster | `postgres` | executeQuery |
| Build Cluster Source Links | `code` | Inspect parameters |
| Store — Insert Source Links | `postgres` | executeQuery |
| Mark Raw Items Processed | `postgres` | executeQuery |
| Fetch Clusters for Webhook | `postgres` | executeQuery |
| Format Webhook Output | `code` | Inspect parameters |
| Webhook — Receive Request | `webhook` | Inspect parameters |
| Webhook — Send Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Workflow Trigger → Fetch Unprocessed Items (`main`, output 0, input 0)
- Fetch Unprocessed Items → Group By Topic Tag (`main`, output 0, input 0)
- Group By Topic Tag → Claude — Synthesize Cluster (`main`, output 0, input 0)
- Claude — Synthesize Cluster → Parse Claude Response (`main`, output 0, input 0)
- Parse Claude Response → Store — Insert Cluster (`main`, output 0, input 0)
- Store — Insert Cluster → Build Cluster Source Links (`main`, output 0, input 0)
- Store — Insert Cluster → Mark Raw Items Processed (`main`, output 0, input 0)
- Build Cluster Source Links → Store — Insert Source Links (`main`, output 0, input 0)
- Mark Raw Items Processed → Fetch Clusters for Webhook (`main`, output 0, input 0)
- Fetch Clusters for Webhook → Format Webhook Output (`main`, output 0, input 0)
- Format Webhook Output → Webhook — Receive Request (`main`, output 0, input 0)
- Webhook — Receive Request → Webhook — Send Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
