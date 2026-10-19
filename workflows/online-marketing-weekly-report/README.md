# Online Marketing Weekly Report

This folder contains the **Online Marketing Weekly Report** workflow. Its executable nodes use `agent`, `code`, `emailSend`, `executeWorkflowTrigger`, `facebookGraphApi`, `googleAnalytics`, `httpRequest`, `lmChatOpenAi`, `openAi`, `scheduleTrigger`, `set`, `summarize`, `telegram`, `toolCalculator`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`online-marketing-weekly-report.json`](online-marketing-weekly-report.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `googleAdsOAuth2Api`, `googleAnalyticsOAuth2`, `googleOAuth2Api`, `openAiApi`, `smtp`, `telegramApi`

**Entry nodes:** Schedule Trigger, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Google_Ads | `toolWorkflow` | Inspect parameters |
| Meta_Ads | `toolWorkflow` | Inspect parameters |
| Analytics_Domain_1 | `toolWorkflow` | Inspect parameters |
| Analytics_Domain_3 | `toolWorkflow` | Inspect parameters |
| Analytics_Domain_2 | `toolWorkflow` | Inspect parameters |
| Analytics_Domain_4 | `toolWorkflow` | Inspect parameters |
| Analytics_Domain_5 | `toolWorkflow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Calculator1 | `toolCalculator` | Inspect parameters |
| Calculator3 | `toolCalculator` | Inspect parameters |
| Call Google Analytics data: Last 7 days | `googleAnalytics` | Inspect parameters |
| Call Google Analytics data: Last 7 days (previous year) | `googleAnalytics` | Inspect parameters |
| Calculation same period previous year | `code` | Inspect parameters |
| Format data input (previous year) | `code` | Inspect parameters |
| Format data input (current year) | `code` | Inspect parameters |
| Assign data from input (current year) | `set` | Inspect parameters |
| Summarize input (current year) | `summarize` | Inspect parameters |
| Assign input (previous year) | `set` | Inspect parameters |
| Summarize input (previous year) | `summarize` | Inspect parameters |
| Calculate date format for Google Ads request (last 7 days) | `code` | Inspect parameters |
| Call Google Ads Data: Last 7 days | `httpRequest` | POST |
| Call Google Ads Data: Last 7 days (previous year) | `httpRequest` | POST |
| Call Meta Ads Data: Last 7 days | `facebookGraphApi` | Inspect parameters |
| Call Meta Ads Data: Last 7 days (previous year) | `facebookGraphApi` | Inspect parameters |
| Summarize Meta input (current year) | `summarize` | Inspect parameters |
| Assign Meta data from input (current year) | `set` | Inspect parameters |
| Assign Meta data input (previous year) | `set` | Inspect parameters |
| Summarize Meta data input (previous year) | `summarize` | Inspect parameters |
| Format all Meta data for LLM | `code` | Inspect parameters |
| Processing for Google Ads report | `openAi` | Inspect parameters |
| Format all Google data for LLM | `code` | Inspect parameters |
| Assign Google Analytics data input (current year) | `set` | Inspect parameters |
| Summarize Google Analytics input (current year) | `summarize` | Inspect parameters |
| Calculate date format for meta ads request s | `code` | Inspect parameters |
| Calculation same period previous year1 | `code` | Inspect parameters |
| Assign Google Analytics data input (previous year) | `set` | Inspect parameters |
| Summarize Google Analytics input (previous year) | `summarize` | Inspect parameters |
| Send mail report | `emailSend` | Inspect parameters |
| Processing for Meta Ads Report | `openAi` | Inspect parameters |
| Processing for Google Analytics Report | `openAi` | Inspect parameters |
| Processing for Telegram Report | `openAi` | Inspect parameters |
| Weekly Report Agent | `agent` | Inspect parameters |
| Send Telegram report | `telegram` | Inspect parameters |

## Connection map

- Meta_Ads → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Calculator → Processing for Google Analytics Report (`ai_tool`, output 0, input 0)
- Google_Ads → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Calculator1 → Processing for Google Ads report (`ai_tool`, output 0, input 0)
- Calculator3 → Processing for Meta Ads Report (`ai_tool`, output 0, input 0)
- Schedule Trigger → Weekly Report Agent (`main`, output 0, input 0)
- OpenAI Chat Model → Weekly Report Agent (`ai_languageModel`, output 0, input 0)
- Analytics_Domain_1 → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Analytics_Domain_2 → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Analytics_Domain_3 → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Analytics_Domain_4 → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Analytics_Domain_5 → Weekly Report Agent (`ai_tool`, output 0, input 0)
- Weekly Report Agent → Processing for Telegram Report (`main`, output 0, input 0)
- Weekly Report Agent → Send mail report (`main`, output 0, input 0)
- Execute Workflow Trigger → Call Google Analytics data: Last 7 days (`main`, output 0, input 0)
- Assign input (previous year) → Summarize input (previous year) (`main`, output 0, input 0)
- Format all Meta data for LLM → Processing for Meta Ads Report (`main`, output 0, input 0)
- Format all Google data for LLM → Processing for Google Ads report (`main`, output 0, input 0)
- Processing for Telegram Report → Send Telegram report (`main`, output 0, input 0)
- Summarize input (current year) → Calculation same period previous year (`main`, output 0, input 0)
- Call Meta Ads Data: Last 7 days → Assign Meta data from input (current year) (`main`, output 0, input 0)
- Summarize input (previous year) → Format all Google data for LLM (`main`, output 0, input 0)
- Format data input (current year) → Assign data from input (current year) (`main`, output 0, input 0)
- Call Google Ads Data: Last 7 days → Format data input (current year) (`main`, output 0, input 0)
- Format data input (previous year) → Assign input (previous year) (`main`, output 0, input 0)
- Summarize Meta input (current year) → Call Meta Ads Data: Last 7 days (previous year) (`main`, output 0, input 0)
- Assign data from input (current year) → Summarize input (current year) (`main`, output 0, input 0)
- Calculation same period previous year → Call Google Ads Data: Last 7 days (previous year) (`main`, output 0, input 0)
- Assign Meta data input (previous year) → Summarize Meta data input (previous year) (`main`, output 0, input 0)
- Calculation same period previous year1 → Call Google Analytics data: Last 7 days (previous year) (`main`, output 0, input 0)
- Call Google Analytics data: Last 7 days → Assign Google Analytics data input (current year) (`main`, output 0, input 0)
- Summarize Meta data input (previous year) → Format all Meta data for LLM (`main`, output 0, input 0)
- Assign Meta data from input (current year) → Summarize Meta input (current year) (`main`, output 0, input 0)
- Calculate date format for meta ads request s → Call Meta Ads Data: Last 7 days (`main`, output 0, input 0)
- Call Meta Ads Data: Last 7 days (previous year) → Assign Meta data input (previous year) (`main`, output 0, input 0)
- Summarize Google Analytics input (current year) → Calculation same period previous year1 (`main`, output 0, input 0)
- Summarize Google Analytics input (previous year) → Processing for Google Analytics Report (`main`, output 0, input 0)
- Assign Google Analytics data input (current year) → Summarize Google Analytics input (current year) (`main`, output 0, input 0)
- Call Google Ads Data: Last 7 days (previous year) → Format data input (previous year) (`main`, output 0, input 0)
- Assign Google Analytics data input (previous year) → Summarize Google Analytics input (previous year) (`main`, output 0, input 0)
- Call Google Analytics data: Last 7 days (previous year) → Assign Google Analytics data input (previous year) (`main`, output 0, input 0)
- Calculate date format for Google Ads request (last 7 days) → Call Google Ads Data: Last 7 days (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1905_Telegram_Googleanalytics_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1905_Telegram_Googleanalytics_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
