# Crypto News & Sentiment

This folder contains the **Crypto News & Sentiment** workflow. Its executable nodes use `agent`, `code`, `lmChatOpenAi`, `merge`, `openAi`, `rssFeedRead`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`crypto-news-sentiment.json`](crypto-news-sentiment.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Send Crypto or Company Name for Analysis

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Set Query | `set` | Inspect parameters |
| Crypto News & Sentiment Agent | `agent` | Inspect parameters |
| RSS Cointelegraph | `rssFeedRead` | Inspect parameters |
| RSS Bitcoinmagazine | `rssFeedRead` | Inspect parameters |
| RSS Coindesk | `rssFeedRead` | Inspect parameters |
| RSS Bitcoinist | `rssFeedRead` | Inspect parameters |
| RSS Newsbtc | `rssFeedRead` | Inspect parameters |
| RSS Cryptopotato | `rssFeedRead` | Inspect parameters |
| RSS 99bitcoins | `rssFeedRead` | Inspect parameters |
| RSS Cryptobriefing | `rssFeedRead` | Inspect parameters |
| RSS Crypto.news | `rssFeedRead` | Inspect parameters |
| Merge All Articles | `merge` | Inspect parameters |
| Filter by Query | `code` | Inspect parameters |
| Build Prompt | `code` | Inspect parameters |
| Adds the sessionId | `set` | Inspect parameters |
| Summarize News & Sentiment (GPT-4o) | `openAi` | Inspect parameters |
| Prepare Telegram Message | `set` | Inspect parameters |
| Sends Response | `telegram` | Inspect parameters |
| Send Crypto or Company Name for Analysis | `telegramTrigger` | Inspect parameters |

## Connection map

- Set Query → RSS Cointelegraph (`main`, output 0, input 0)
- Set Query → RSS Bitcoinmagazine (`main`, output 0, input 0)
- Set Query → RSS Coindesk (`main`, output 0, input 0)
- Set Query → RSS Bitcoinist (`main`, output 0, input 0)
- Set Query → RSS Newsbtc (`main`, output 0, input 0)
- Set Query → RSS Cryptopotato (`main`, output 0, input 0)
- Set Query → RSS 99bitcoins (`main`, output 0, input 0)
- Set Query → RSS Cryptobriefing (`main`, output 0, input 0)
- Set Query → RSS Crypto.news (`main`, output 0, input 0)
- RSS Newsbtc → Merge All Articles (`main`, output 0, input 4)
- Build Prompt → Summarize News & Sentiment (GPT-4o) (`main`, output 0, input 0)
- RSS Coindesk → Merge All Articles (`main`, output 0, input 2)
- RSS 99bitcoins → Merge All Articles (`main`, output 0, input 7)
- RSS Bitcoinist → Merge All Articles (`main`, output 0, input 3)
- Filter by Query → Build Prompt (`main`, output 0, input 0)
- RSS Crypto.news → Merge All Articles (`main`, output 0, input 9)
- RSS Cryptopotato → Merge All Articles (`main`, output 0, input 6)
- OpenAI Chat Model → Crypto News & Sentiment Agent (`ai_languageModel`, output 0, input 0)
- RSS Cointelegraph → Merge All Articles (`main`, output 0, input 0)
- Adds the sessionId → Crypto News & Sentiment Agent (`main`, output 0, input 0)
- Merge All Articles → Filter by Query (`main`, output 0, input 0)
- RSS Cryptobriefing → Merge All Articles (`main`, output 0, input 8)
- RSS Bitcoinmagazine → Merge All Articles (`main`, output 0, input 1)
- Prepare Telegram Message → Sends Response (`main`, output 0, input 0)
- Crypto News & Sentiment Agent → Set Query (`main`, output 0, input 0)
- Summarize News & Sentiment (GPT-4o) → Prepare Telegram Message (`main`, output 0, input 0)
- Send Crypto or Company Name for Analysis → Adds the sessionId (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1186_Rssfeedread_Telegram_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1186_Rssfeedread_Telegram_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
