# YouTube Comment Sentiment Analyzer

This folder contains the **YouTube Comment Sentiment Analyzer** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `noOp`, `sentimentAnalysis`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-comment-sentiment-analyzer.json`](youtube-comment-sentiment-analyzer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpQueryAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Get Video Urls from Google Sheet | `googleSheets` | Inspect parameters |
| check next fetch time is available or not | `if` | Inspect parameters |
| check next fetch time is before the current time | `if` | Inspect parameters |
| Get Comments for video urls | `httpRequest` | Inspect parameters |
| Analyze sentiment of every comment | `sentimentAnalysis` | Inspect parameters |
| Format fields as required to save in google sheet | `set` | Inspect parameters |
| Insert and update comment in google sheet | `googleSheets` | appendOrUpdate |
| Update last fetched time and next_fetch_time | `googleSheets` | appendOrUpdate |
| No Operation, do nothing1 | `noOp` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Check Success Response | `if` | Inspect parameters |

## Connection map

- Split Out → Analyze sentiment of every comment (`main`, output 0, input 0)
- OpenAI Chat Model → Analyze sentiment of every comment (`ai_languageModel`, output 0, input 0)
- Check Success Response → Split Out (`main`, output 0, input 0)
- Check Success Response → No Operation, do nothing1 (`main`, output 1, input 0)
- Get Comments for video urls → Check Success Response (`main`, output 0, input 0)
- Get Video Urls from Google Sheet → check next fetch time is available or not (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Video Urls from Google Sheet (`main`, output 0, input 0)
- Analyze sentiment of every comment → Format fields as required to save in google sheet (`main`, output 0, input 0)
- Analyze sentiment of every comment → Format fields as required to save in google sheet (`main`, output 1, input 0)
- Analyze sentiment of every comment → Format fields as required to save in google sheet (`main`, output 2, input 0)
- Insert and update comment in google sheet → Update last fetched time and next_fetch_time (`main`, output 0, input 0)
- check next fetch time is available or not → Get Comments for video urls (`main`, output 0, input 0)
- check next fetch time is available or not → check next fetch time is before the current time (`main`, output 1, input 0)
- check next fetch time is before the current time → Get Comments for video urls (`main`, output 0, input 0)
- check next fetch time is before the current time → No Operation, do nothing (`main`, output 1, input 0)
- Format fields as required to save in google sheet → Insert and update comment in google sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2016_Splitout_Noop_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/2016_Splitout_Noop_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
