# Telegram channel to Readeck & Hoarder

This folder contains the **Telegram channel to Readeck & Hoarder** workflow. Its executable nodes use `code`, `httpRequest`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`telegram-channel-to-readeck-hoarder.json`](telegram-channel-to-readeck-hoarder.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| not_saved_links_hd | `code` | Inspect parameters |
| not_saved_links_rd | `code` | Inspect parameters |
| saved_links_rd | `set` | Inspect parameters |
| save_link_rd | `httpRequest` | POST |
| save_link_hd | `httpRequest` | POST |
| get_links_rd | `httpRequest` | Inspect parameters |
| get_links_hd | `httpRequest` | Inspect parameters |
| saved_links_hd | `set` | Inspect parameters |
| channel_links_tg | `code` | Inspect parameters |
| channel_items_tg | `httpRequest` | Inspect parameters |

## Connection map

- Split Out → saved_links_hd (`main`, output 0, input 0)
- get_links_hd → Split Out (`main`, output 0, input 0)
- get_links_rd → saved_links_rd (`main`, output 0, input 0)
- saved_links_hd → not_saved_links_hd (`main`, output 0, input 0)
- saved_links_rd → not_saved_links_rd (`main`, output 0, input 0)
- Schedule Trigger → channel_items_tg (`main`, output 0, input 0)
- channel_items_tg → channel_links_tg (`main`, output 0, input 0)
- channel_links_tg → get_links_rd (`main`, output 0, input 0)
- channel_links_tg → get_links_hd (`main`, output 0, input 0)
- not_saved_links_hd → save_link_hd (`main`, output 0, input 0)
- not_saved_links_rd → save_link_rd (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1468_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1468_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
