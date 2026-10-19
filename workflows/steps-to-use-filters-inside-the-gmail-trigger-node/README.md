# Steps to Use Filters Inside the Gmail Trigger Node:

This folder contains the **Steps to Use Filters Inside the Gmail Trigger Node:** workflow. Its executable nodes use `aggregate`, `chainSummarization`, `code`, `convertToFile`, `gmail`, `gmailTrigger`, `httpRequest`, `lmChatOpenAi`, `merge`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`steps-to-use-filters-inside-the-gmail-trigger-node.json`](steps-to-use-filters-inside-the-gmail-trigger-node.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`, `telegramApi`

**Entry nodes:** Gmail trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get message content1 | `gmail` | get |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Delete the unnecessary items | `code` | Inspect parameters |
| Aggregate in same cell | `aggregate` | Inspect parameters |
| Gmail trigger | `gmailTrigger` | Inspect parameters |
| Convert from base64 to File | `convertToFile` | toBinary |
| Merge Text with Audio | `merge` | Inspect parameters |
| Send Message to Telegram | `telegram` | sendAudio |
| Summarization Chain3 | `chainSummarization` | Inspect parameters |
| Text to  TTS | `httpRequest` | POST |

## Connection map

- Text to  TTS → Convert from base64 to File (`main`, output 0, input 0)
- Text to  TTS → Summarization Chain3 (`main`, output 1, input 0)
- Gmail trigger → Get message content1 (`main`, output 0, input 0)
- OpenAI Chat Model3 → Summarization Chain3 (`ai_languageModel`, output 0, input 0)
- Get message content1 → Delete the unnecessary items (`main`, output 0, input 0)
- Summarization Chain3 → Merge Text with Audio (`main`, output 0, input 1)
- Summarization Chain3 → Text to  TTS (`main`, output 0, input 0)
- Merge Text with Audio → Aggregate in same cell (`main`, output 0, input 0)
- Aggregate in same cell → Send Message to Telegram (`main`, output 0, input 0)
- Convert from base64 to File → Merge Text with Audio (`main`, output 0, input 0)
- Delete the unnecessary items → Summarization Chain3 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0481_Telegram_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0481_Telegram_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
