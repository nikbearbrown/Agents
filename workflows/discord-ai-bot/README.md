# Discord AI bot

This folder contains the **Discord AI bot** workflow. Its executable nodes use `discord`, `manualTrigger`, `noOp`, `openAi`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`discord-ai-bot.json`](discord-ai-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** When clicking "Execute Workflow", Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Analyze user request | `openAi` | chat |
| Select category | `switch` | Inspect parameters |
| Parse JSON | `set` | Inspect parameters |
| User Success Dept | `discord` | Inspect parameters |
| IT Dept | `discord` | Inspect parameters |
| Helpdesk | `discord` | Inspect parameters |

## Connection map

- Webhook → Analyze user request (`main`, output 0, input 0)
- Parse JSON → Select category (`main`, output 0, input 0)
- Select category → User Success Dept (`main`, output 0, input 0)
- Select category → IT Dept (`main`, output 1, input 0)
- Select category → Helpdesk (`main`, output 2, input 0)
- Select category → No Operation, do nothing (`main`, output 3, input 0)
- Analyze user request → Parse JSON (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Analyze user request (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0270_Webhook_Discord_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0270_Webhook_Discord_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
