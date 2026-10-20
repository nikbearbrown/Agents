# receive telegram events and addlabels gmail tool and removelabels gmail tool

This folder contains the **receive telegram events and addlabels gmail tool and removelabels gmail tool** workflow. Its executable nodes use `agent`, `aggregate`, `filter`, `gmail`, `gmailTool`, `lmChatOpenRouter`, `manualTrigger`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-addlabels-gmail-tool-and-removelabels-gmail-tool.json`](receive-telegram-events-and-addlabels-gmail-tool-and-removelabels-gmail-tool.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openRouterApi`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| mail_label_setter | `gmailTool` | addLabels |
| mail_archiver | `gmailTool` | removeLabels |
| Aggregate | `aggregate` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| OpenRouter Chat Model1 | `lmChatOpenRouter` | Inspect parameters |
| Reporter | `agent` | Inspect parameters |
| Get mails in INBOX | `gmail` | getAll |
| Filter processed | `filter` | Inspect parameters |
| Categoriser | `agent` | Inspect parameters |

## Connection map

- Reporter → Telegram (`main`, output 0, input 0)
- Aggregate → Reporter (`main`, output 0, input 0)
- Categoriser → Aggregate (`main`, output 0, input 0)
- mail_archiver → Categoriser (`ai_tool`, output 0, input 0)
- Filter processed → Categoriser (`main`, output 0, input 0)
- Telegram Trigger → Get mails in INBOX (`main`, output 0, input 0)
- mail_label_setter → Categoriser (`ai_tool`, output 0, input 0)
- Get mails in INBOX → Filter processed (`main`, output 0, input 0)
- OpenRouter Chat Model → Categoriser (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model1 → Reporter (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Get mails in INBOX (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0884_Telegram_Filter_Export_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0884_Telegram_Filter_Export_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
