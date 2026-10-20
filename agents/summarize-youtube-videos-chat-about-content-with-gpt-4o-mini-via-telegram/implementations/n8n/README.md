# Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram

This folder contains the **Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram** workflow. Its executable nodes use `agent`, `chainLlm`, `chatTrigger`, `code`, `googleDocs`, `googleDocsTool`, `lmChatOpenAi`, `memoryBufferWindow`, `respondToWebhook`, `set`, `splitOut`, `summarize`, `telegram`, `telegramTrigger`, `webhook`, `youtubeTranscripter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`summarize-youtube-videos-chat-about-content-with-gpt-4o-mini-via-telegram.json`](summarize-youtube-videos-chat-about-content-with-gpt-4o-mini-via-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDocsOAuth2Api`, `openAiApi`, `telegramApi`

**Entry nodes:** Trigger on Telegram Message, Receive YouTube URL via Webhook, Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Transcript into Segments | `splitOut` | Inspect parameters |
| Extract YouTube URL from Input | `set` | Inspect parameters |
| Extract Video ID from URL | `code` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Generate Summary with GPT-4o-mini | `chainLlm` | Inspect parameters |
| Concatenate Transcript Segments | `summarize` | Inspect parameters |
| Trigger on Telegram Message | `chatTrigger` | Inspect parameters |
| Extract YouTube Transcript | `youtubeTranscripter` | Inspect parameters |
| Send Summary via Telegram | `telegram` | Inspect parameters |
| Receive YouTube URL via Webhook | `webhook` | Inspect parameters |
| Send Response to Webhook | `respondToWebhook` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Retrieve Transcript from Google Docs | `googleDocs` | get |
| Update Transcript in Google Docs | `googleDocs` | update |
| Handle User Questions via AI | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Google Docs2 | `googleDocsTool` | get |
| Send AI Response via Telegram | `telegram` | Inspect parameters |

## Connection map

- gpt-4o-mini → Generate Summary with GPT-4o-mini (`ai_languageModel`, output 0, input 0)
- Google Docs2 → Handle User Questions via AI (`ai_tool`, output 0, input 0)
- Telegram Trigger → Handle User Questions via AI (`main`, output 0, input 0)
- OpenAI Chat Model → Handle User Questions via AI (`ai_languageModel`, output 0, input 0)
- Extract Video ID from URL → Extract YouTube Transcript (`main`, output 0, input 0)
- Send Summary via Telegram → Send Response to Webhook (`main`, output 0, input 0)
- Extract YouTube Transcript → Split Transcript into Segments (`main`, output 0, input 0)
- Trigger on Telegram Message → Extract YouTube URL from Input (`main`, output 0, input 0)
- Handle User Questions via AI → Send AI Response via Telegram (`main`, output 0, input 0)
- Extract YouTube URL from Input → Extract Video ID from URL (`main`, output 0, input 0)
- Split Transcript into Segments → Concatenate Transcript Segments (`main`, output 0, input 0)
- Concatenate Transcript Segments → Generate Summary with GPT-4o-mini (`main`, output 0, input 0)
- Concatenate Transcript Segments → Retrieve Transcript from Google Docs (`main`, output 0, input 0)
- Receive YouTube URL via Webhook → Extract YouTube URL from Input (`main`, output 0, input 0)
- Generate Summary with GPT-4o-mini → Send Summary via Telegram (`main`, output 0, input 0)
- Retrieve Transcript from Google Docs → Update Transcript in Google Docs (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1533_Telegram_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1533_Telegram_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
