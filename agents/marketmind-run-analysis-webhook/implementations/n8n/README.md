# MarketMind - Run Analysis (Webhook)

This folder contains the **MarketMind - Run Analysis (Webhook)** workflow. Its executable nodes use `executeCommand`, `function`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`marketmind-run-analysis-webhook.json`](marketmind-run-analysis-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook Trigger | `webhook` | Inspect parameters |
| Set Inputs | `set` | Inspect parameters |
| Execute main.py | `executeCommand` | Inspect parameters |
| Parse Final Report | `function` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook Trigger → Set Inputs (`main`, output 0, input 0)
- Set Inputs → Execute main.py (`main`, output 0, input 0)
- Execute main.py → Parse Final Report (`main`, output 0, input 0)
- Parse Final Report → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
