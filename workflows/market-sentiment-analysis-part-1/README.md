# Market Sentiment Analysis - Part 1

This folder contains the **Market Sentiment Analysis - Part 1** workflow. Its executable nodes use `code`, `emailSend`, `httpRequest`, `lmChatAnthropic`, `respondToWebhook`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`market-sentiment-analysis-part-1.json`](market-sentiment-analysis-part-1.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackApi`, `smtp`

**Entry nodes:** Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook Trigger | `webhook` | Inspect parameters |
| Parse Question & Extract Tickers | `code` | Inspect parameters |
| Fetch Price Data | `httpRequest` | GET |
| Fetch News Headlines | `httpRequest` | GET |
| Fetch Reddit Mentions | `httpRequest` | GET |
| Aggregate & Calculate Sentiment | `code` | Inspect parameters |
| AI Analysis & Synthesis | `lmChatAnthropic` | Inspect parameters |
| Format Response | `code` | Inspect parameters |
| Send to Slack | `slack` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Webhook Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook Trigger → Parse Question & Extract Tickers (`main`, output 0, input 0)
- Parse Question & Extract Tickers → Fetch Price Data (`main`, output 0, input 0)
- Parse Question & Extract Tickers → Fetch News Headlines (`main`, output 0, input 0)
- Parse Question & Extract Tickers → Fetch Reddit Mentions (`main`, output 0, input 0)
- Fetch Price Data → Aggregate & Calculate Sentiment (`main`, output 0, input 0)
- Fetch News Headlines → Aggregate & Calculate Sentiment (`main`, output 0, input 0)
- Fetch Reddit Mentions → Aggregate & Calculate Sentiment (`main`, output 0, input 0)
- Aggregate & Calculate Sentiment → AI Analysis & Synthesis (`main`, output 0, input 0)
- AI Analysis & Synthesis → Format Response (`main`, output 0, input 0)
- Format Response → Send to Slack (`main`, output 0, input 0)
- Format Response → Send Email (`main`, output 0, input 0)
- Format Response → Webhook Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
