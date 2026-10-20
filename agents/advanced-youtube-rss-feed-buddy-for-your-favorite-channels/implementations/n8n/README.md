# 🎦💌Advanced YouTube RSS Feed Buddy for Your Favorite Channels

This folder contains the **🎦💌Advanced YouTube RSS Feed Buddy for Your Favorite Channels** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `filter`, `formTrigger`, `gmail`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `merge`, `rssFeedRead`, `scheduleTrigger`, `set`, `splitOut`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`advanced-youtube-rss-feed-buddy-for-your-favorite-channels.json`](advanced-youtube-rss-feed-buddy-for-your-favorite-channels.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`, `telegramApi`

**Entry nodes:** On form submission, Every Day, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Create RSS Feed URLs1 | `set` | Inspect parameters |
| Get Channel Ids | `set` | Inspect parameters |
| Create YouTube API URL | `code` | Inspect parameters |
| Get YouTube Video Details | `httpRequest` | Inspect parameters |
| Workflow Variables | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Default YouTube Channel Ids | `set` | Inspect parameters |
| YouTube Channel Ids | `set` | Inspect parameters |
| RSS Read  - Max 15 Latest Videos per Channel | `rssFeedRead` | Inspect parameters |
| Label New Videos | `code` | Inspect parameters |
| Get New Videos | `filter` | Inspect parameters |
| Prepare For Telegram Message | `set` | Inspect parameters |
| One List Object | `aggregate` | Inspect parameters |
| Prepare YouTube Data | `set` | Inspect parameters |
| Create List of Channel Ids | `splitOut` | Inspect parameters |
| Every Day | `scheduleTrigger` | Inspect parameters |
| Multiple Emails | `gmail` | Inspect parameters |
| Single Email | `gmail` | Inspect parameters |
| Create Email per Video | `chainLlm` | Inspect parameters |
| Create One Email for All Videos | `chainLlm` | Inspect parameters |
| Telegram | `telegram` | sendPhoto |
| Create RSS Feed URLs | `set` | Inspect parameters |
| RSS Read  - Max 15 Latest Videos per Channel1 | `rssFeedRead` | Inspect parameters |
| Create List of Channel Ids1 | `splitOut` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| YouTube Channel Ids1 | `set` | Inspect parameters |

## Connection map

- Merge → Create Email per Video (`main`, output 0, input 0)
- Merge → One List Object (`main`, output 0, input 0)
- Merge → Prepare For Telegram Message (`main`, output 0, input 0)
- Every Day → YouTube Channel Ids (`main`, output 0, input 0)
- Get New Videos → Workflow Variables (`main`, output 0, input 0)
- Get New Videos → Merge (`main`, output 0, input 1)
- Get Channel Ids → Create List of Channel Ids (`main`, output 0, input 0)
- One List Object → Create One Email for All Videos (`main`, output 0, input 0)
- Label New Videos → Get New Videos (`main`, output 0, input 0)
- OpenAI Chat Model → Create Email per Video (`ai_languageModel`, output 0, input 0)
- On form submission → Default YouTube Channel Ids (`main`, output 0, input 0)
- OpenAI Chat Model1 → Create One Email for All Videos (`ai_languageModel`, output 0, input 0)
- Workflow Variables → Create YouTube API URL (`main`, output 0, input 0)
- YouTube Channel Ids → Default YouTube Channel Ids (`main`, output 0, input 0)
- Create RSS Feed URLs → RSS Read  - Max 15 Latest Videos per Channel1 (`main`, output 0, input 0)
- Prepare YouTube Data → Merge (`main`, output 0, input 0)
- YouTube Channel Ids1 → Create List of Channel Ids1 (`main`, output 0, input 0)
- Create RSS Feed URLs1 → RSS Read  - Max 15 Latest Videos per Channel (`main`, output 0, input 0)
- Create Email per Video → Multiple Emails (`main`, output 0, input 0)
- Create YouTube API URL → Get YouTube Video Details (`main`, output 0, input 0)
- Get YouTube Video Details → Prepare YouTube Data (`main`, output 0, input 0)
- Create List of Channel Ids → Create RSS Feed URLs1 (`main`, output 0, input 0)
- Create List of Channel Ids1 → Create RSS Feed URLs (`main`, output 0, input 0)
- Default YouTube Channel Ids → Get Channel Ids (`main`, output 0, input 0)
- Prepare For Telegram Message → Telegram (`main`, output 0, input 0)
- Create One Email for All Videos → Single Email (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → YouTube Channel Ids1 (`main`, output 0, input 0)
- RSS Read  - Max 15 Latest Videos per Channel → Label New Videos (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1982_Telegram_Splitout_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1982_Telegram_Splitout_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
