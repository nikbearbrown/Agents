# #️⃣Nostr #damus AI Powered Reporting + Gmail + Telegram

This folder contains the **#️⃣Nostr #damus AI Powered Reporting + Gmail + Telegram** workflow. Its executable nodes use `aggregate`, `chainLlm`, `gmail`, `lmChatGoogleGemini`, `manualTrigger`, `markdown`, `merge`, `nostrobotsread`, `scheduleTrigger`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`nostr-damus-ai-powered-reporting-gmail-telegram.json`](nostr-damus-ai-powered-reporting-gmail-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get HTML | `markdown` | Inspect parameters |
| Gmail Themes | `gmail` | Inspect parameters |
| Get HTML Report | `markdown` | Inspect parameters |
| #damus Themes List | `chainLlm` | Inspect parameters |
| #damus Thread Themes | `chainLlm` | Inspect parameters |
| #damus Themes & Threads Report | `chainLlm` | Inspect parameters |
| gemini-2.0-flash-lite-preview | `lmChatGoogleGemini` | Inspect parameters |
| gemini-2.0-flash-lite-preview1 | `lmChatGoogleGemini` | Inspect parameters |
| gemini-2.0-flash-lite-preview2 | `lmChatGoogleGemini` | Inspect parameters |
| Gmail Report | `gmail` | Inspect parameters |
| Aggregate #damus Content | `aggregate` | Inspect parameters |
| Merge Themes and Content | `merge` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Telegram Themes | `telegram` | Inspect parameters |
| Telegram Themes & Threads | `telegram` | Inspect parameters |
| Nostr Read #damus | `nostrobotsread` | Inspect parameters |

## Connection map

- Get HTML → Gmail Themes (`main`, output 0, input 0)
- Get HTML Report → Gmail Report (`main`, output 0, input 0)
- Schedule Trigger → Nostr Read #damus (`main`, output 0, input 0)
- Nostr Read #damus → Aggregate #damus Content (`main`, output 0, input 0)
- #damus Themes List → Merge Themes and Content (`main`, output 0, input 0)
- #damus Thread Themes → Get HTML (`main`, output 0, input 0)
- #damus Thread Themes → #damus Themes List (`main`, output 0, input 0)
- #damus Thread Themes → Telegram Themes (`main`, output 0, input 0)
- Aggregate #damus Content → #damus Thread Themes (`main`, output 0, input 0)
- Aggregate #damus Content → Merge Themes and Content (`main`, output 0, input 1)
- Merge Themes and Content → #damus Themes & Threads Report (`main`, output 0, input 0)
- gemini-2.0-flash-lite-preview → #damus Thread Themes (`ai_languageModel`, output 0, input 0)
- #damus Themes & Threads Report → Get HTML Report (`main`, output 0, input 0)
- #damus Themes & Threads Report → Telegram Themes & Threads (`main`, output 0, input 0)
- gemini-2.0-flash-lite-preview1 → #damus Themes List (`ai_languageModel`, output 0, input 0)
- gemini-2.0-flash-lite-preview2 → #damus Themes & Threads Report (`ai_languageModel`, output 0, input 0)
- When clicking ‘Test workflow’ → Nostr Read #damus (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0001_Telegram_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0001_Telegram_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Stage annotation review

The sticky notes now explain collection, theme extraction, positional merging, report generation, and email/Telegram delivery. They also identify configuration gaps visible in the export: the manual-trigger connection key does not match its node name, the schedule interval is unspecified, preview model availability is unverified, and Telegram truncates model output while requesting HTML parsing. These are inspection findings, not runtime test results. Executable nodes and connections are unchanged.
