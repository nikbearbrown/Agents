# Google Analytics: Weekly Report

This folder contains the **Google Analytics: Weekly Report** workflow. Its executable nodes use `code`, `emailSend`, `googleAnalytics`, `openAi`, `scheduleTrigger`, `set`, `summarize`, `telegram`, `toolCalculator`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-analytics-weekly-report.json`](google-analytics-weekly-report.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleAnalyticsOAuth2`, `openAiApi`, `smtp`, `telegramApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Google Analytics Letzte 7 Tage | `googleAnalytics` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Processing for Telegram | `openAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Google Analytics: Past 7 days of the previous year | `googleAnalytics` | Inspect parameters |
| Summarize Data | `summarize` | Inspect parameters |
| Summarize Data1 | `summarize` | Inspect parameters |
| Calculation same period previous year | `code` | Inspect parameters |
| Assign data | `set` | Inspect parameters |
| Assign data1 | `set` | Inspect parameters |
| Processing for email | `openAi` | Inspect parameters |

## Connection map

- Calculator → Processing for email (`ai_tool`, output 0, input 0)
- Assign data → Summarize Data (`main`, output 0, input 0)
- Assign data1 → Summarize Data1 (`main`, output 0, input 0)
- Summarize Data → Calculation same period previous year (`main`, output 0, input 0)
- Summarize Data1 → Processing for email (`main`, output 0, input 0)
- Schedule Trigger → Google Analytics Letzte 7 Tage (`main`, output 0, input 0)
- Processing for email → Send Email (`main`, output 0, input 0)
- Processing for email → Processing for Telegram (`main`, output 0, input 0)
- Processing for Telegram → Telegram (`main`, output 0, input 0)
- Google Analytics Letzte 7 Tage → Assign data (`main`, output 0, input 0)
- Calculation same period previous year → Google Analytics: Past 7 days of the previous year (`main`, output 0, input 0)
- Google Analytics: Past 7 days of the previous year → Assign data1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1392_Telegram_Googleanalytics_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1392_Telegram_Googleanalytics_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
