# fetch apple press releases1 and parse apple press xml1 and fetch google news rss1

This folder contains the **fetch apple press releases1 and parse apple press xml1 and fetch google news rss1** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `if`, `merge`, `openAi`, `respondToWebhook`, `splitInBatches`, `webhook`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-apple-press-releases1-and-parse-apple-press-xml1-and-fetch-google-news-rss1.json`](fetch-apple-press-releases1-and-parse-apple-press-xml1-and-fetch-google-news-rss1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Fetch Apple Press Releases1 | `httpRequest` | Inspect parameters |
| Parse Apple Press XML1 | `xml` | Inspect parameters |
| Extract Apple Press1 | `code` | Inspect parameters |
| Fetch Google News RSS1 | `httpRequest` | Inspect parameters |
| Parse Google News XML1 | `xml` | Inspect parameters |
| Extract Google News1 | `code` | Inspect parameters |
| Merge All News2 | `merge` | Inspect parameters |
| Read Processed Links1 | `googleSheets` | Inspect parameters |
| Combine Data1 | `merge` | Inspect parameters |
| Deduplicate with Sheets1 | `code` | Inspect parameters |
| Multi-Brand Config1 | `code` | Inspect parameters |
| Split In Batches1 | `splitInBatches` | Inspect parameters |
| Prepare Subreddits | `code` | Inspect parameters |
| Fetch Reddit Posts | `httpRequest` | Inspect parameters |
| Extract & Format Reddit Data | `code` | Inspect parameters |
| Split In Batches | `splitInBatches` | Inspect parameters |
| Webhook Trigger | `webhook` | Inspect parameters |
| Parse XML1 | `xml` | Inspect parameters |
| Filter Source Type | `if` | Inspect parameters |
| Fetch Regulatory News1 | `httpRequest` | Inspect parameters |
| Regulatory Sources Config1 | `code` | Inspect parameters |
| Merge Data Streams | `merge` | Inspect parameters |
| Save to Compliance Sheet | `googleSheets` | append |
| Extract Content1 | `code` | Inspect parameters |
| Read Existing Articles1 | `googleSheets` | Inspect parameters |
| Deduplicate Articles1 | `code` | Inspect parameters |
| Check New Articles1 | `if` | Inspect parameters |
| OpenAI Sentiment | `openAi` | chat |
| Merge Analysis Results1 | `code` | Inspect parameters |
| Calculate Baseline Metrics | `code` | Inspect parameters |
| Build Knowledge Graph | `code` | Inspect parameters |
| Multi-Brand Competitor Analysis | `code` | Inspect parameters |
| Detect Anomalies | `code` | Inspect parameters |
| Format Drift Metrics | `code` | Inspect parameters |
| Alert Trigger | `code` | Inspect parameters |
| Format Knowledge Graph for Sheets | `code` | Inspect parameters |
| Format Competitor Analysis for Sheets | `code` | Inspect parameters |
| Check New Items | `if` | Inspect parameters |
| OpenAI Sentiment2 | `openAi` | chat |
| Combine Data | `code` | Inspect parameters |
| Save Drift Metrics1 | `googleSheets` | append |
| Save to Google Sheets | `googleSheets` | append |
| Create JSON1 | `code` | Inspect parameters |
| Respond with JSON | `respondToWebhook` | Inspect parameters |
| Respond No New Items | `respondToWebhook` | Inspect parameters |
| Save Knowledge Graph to Sheets | `googleSheets` | append |
| Save Competitor Analysis to Sheets | `googleSheets` | append |

## Connection map

- Fetch Apple Press Releases1 → Parse Apple Press XML1 (`main`, output 0, input 0)
- Parse Apple Press XML1 → Extract Apple Press1 (`main`, output 0, input 0)
- Extract Apple Press1 → Merge All News2 (`main`, output 0, input 0)
- Fetch Google News RSS1 → Parse Google News XML1 (`main`, output 0, input 0)
- Parse Google News XML1 → Extract Google News1 (`main`, output 0, input 0)
- Extract Google News1 → Split In Batches1 (`main`, output 0, input 0)
- Merge All News2 → Combine Data1 (`main`, output 0, input 0)
- Merge All News2 → Read Processed Links1 (`main`, output 0, input 0)
- Read Processed Links1 → Combine Data1 (`main`, output 0, input 1)
- Combine Data1 → Deduplicate with Sheets1 (`main`, output 0, input 0)
- Deduplicate with Sheets1 → Check New Items (`main`, output 0, input 0)
- Multi-Brand Config1 → Split In Batches1 (`main`, output 0, input 0)
- Multi-Brand Config1 → Split In Batches (`main`, output 0, input 0)
- Multi-Brand Config1 → Fetch Apple Press Releases1 (`main`, output 0, input 0)
- Split In Batches1 → Merge All News2 (`main`, output 0, input 1)
- Split In Batches1 → Fetch Google News RSS1 (`main`, output 1, input 0)
- Prepare Subreddits → Fetch Reddit Posts (`main`, output 0, input 0)
- Fetch Reddit Posts → Extract & Format Reddit Data (`main`, output 0, input 0)
- Extract & Format Reddit Data → Split In Batches (`main`, output 0, input 0)
- Split In Batches → Merge All News2 (`main`, output 0, input 1)
- Split In Batches → Prepare Subreddits (`main`, output 1, input 0)
- Webhook Trigger → Regulatory Sources Config1 (`main`, output 0, input 0)
- Webhook Trigger → Read Existing Articles1 (`main`, output 0, input 0)
- Webhook Trigger → Multi-Brand Config1 (`main`, output 0, input 0)
- Parse XML1 → Extract Content1 (`main`, output 0, input 0)
- Filter Source Type → Fetch Regulatory News1 (`main`, output 1, input 0)
- Fetch Regulatory News1 → Parse XML1 (`main`, output 0, input 0)
- Regulatory Sources Config1 → Filter Source Type (`main`, output 0, input 0)
- Merge Data Streams → Deduplicate Articles1 (`main`, output 0, input 0)
- Extract Content1 → Merge Data Streams (`main`, output 0, input 0)
- Read Existing Articles1 → Merge Data Streams (`main`, output 0, input 1)
- Deduplicate Articles1 → Check New Articles1 (`main`, output 0, input 0)
- Check New Articles1 → OpenAI Sentiment (`main`, output 0, input 0)
- OpenAI Sentiment → Merge Analysis Results1 (`main`, output 0, input 0)
- Merge Analysis Results1 → Save to Compliance Sheet (`main`, output 0, input 0)
- Calculate Baseline Metrics → Detect Anomalies (`main`, output 0, input 0)
- Build Knowledge Graph → Format Knowledge Graph for Sheets (`main`, output 0, input 0)
- Multi-Brand Competitor Analysis → Format Competitor Analysis for Sheets (`main`, output 0, input 0)
- Detect Anomalies → Format Drift Metrics (`main`, output 0, input 0)
- Detect Anomalies → Alert Trigger (`main`, output 0, input 0)
- Format Drift Metrics → Save Drift Metrics1 (`main`, output 0, input 0)
- Format Knowledge Graph for Sheets → Save Knowledge Graph to Sheets (`main`, output 0, input 0)
- Format Competitor Analysis for Sheets → Save Competitor Analysis to Sheets (`main`, output 0, input 0)
- Check New Items → OpenAI Sentiment2 (`main`, output 0, input 0)
- Check New Items → Respond No New Items (`main`, output 1, input 0)
- OpenAI Sentiment2 → Combine Data (`main`, output 0, input 0)
- Combine Data → Calculate Baseline Metrics (`main`, output 0, input 0)
- Combine Data → Save to Google Sheets (`main`, output 0, input 0)
- Combine Data → Create JSON1 (`main`, output 0, input 0)
- Combine Data → Multi-Brand Competitor Analysis (`main`, output 0, input 0)
- Combine Data → Build Knowledge Graph (`main`, output 0, input 0)
- Create JSON1 → Respond with JSON (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Humanitariansai/Madison](https://github.com/Humanitariansai/Madison). License: **MIT**; preserve [the notice](../../licenses/humanitariansai-mit.txt) and embedded attribution. License included in local Madison source tree.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
