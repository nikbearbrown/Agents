# Retail Investor Anxiety Index

This folder contains the **Retail Investor Anxiety Index** workflow. Its executable nodes use `chainLlm`, `code`, `httpRequest`, `lmChatAnthropic`, `merge`, `respondToWebhook`, `scheduleTrigger`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`investor-sentiment-dashboard.json`](investor-sentiment-dashboard.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`

**Entry nodes:** Schedule Trigger, Manual Run Trigger, Dashboard Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Manual Run Trigger | `webhook` | Inspect parameters |
| Fetch WSB | `httpRequest` | Inspect parameters |
| Fetch Investing | `httpRequest` | Inspect parameters |
| Fetch Stocks | `httpRequest` | Inspect parameters |
| Merge Reddit Feeds | `merge` | Inspect parameters |
| 1A: Raw Merge & Structural Clean | `code` | Inspect parameters |
| 1B: Linguistic & Relevance Filter | `code` | Inspect parameters |
| Keyword Pre-Scorer | `code` | Inspect parameters |
| Aggregate for Claude | `code` | Inspect parameters |
| Claude 1: Anxiety Score | `chainLlm` | Inspect parameters |
| Claude 2: Narrative Velocity | `chainLlm` | Inspect parameters |
| Claude 3: Herd Detection | `chainLlm` | Inspect parameters |
| Claude 4: Conviction vs Uncertainty | `chainLlm` | Inspect parameters |
| Claude 5: Crowd Cycle Stage | `chainLlm` | Inspect parameters |
| Anthropic Model 1 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 2 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 3 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 4 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 5 | `lmChatAnthropic` | Inspect parameters |
| Merge Claude Outputs | `merge` | Inspect parameters |
| Signal Aggregator | `code` | Inspect parameters |
| Persist to File | `code` | Inspect parameters |
| Generate Quickchart URLs | `code` | Inspect parameters |
| Write output.json | `code` | Inspect parameters |
| Insert to Supabase | `httpRequest` | POST |
| Pipeline Response | `respondToWebhook` | Inspect parameters |
| Dashboard Webhook | `webhook` | Inspect parameters |
| Build Dashboard Response | `code` | Inspect parameters |
| Serve Dashboard HTML | `respondToWebhook` | Inspect parameters |

## Connection map

- Schedule Trigger → Fetch WSB (`main`, output 0, input 0)
- Schedule Trigger → Fetch Investing (`main`, output 0, input 0)
- Schedule Trigger → Fetch Stocks (`main`, output 0, input 0)
- Manual Run Trigger → Fetch WSB (`main`, output 0, input 0)
- Manual Run Trigger → Fetch Investing (`main`, output 0, input 0)
- Manual Run Trigger → Fetch Stocks (`main`, output 0, input 0)
- Fetch WSB → Merge Reddit Feeds (`main`, output 0, input 0)
- Fetch Investing → Merge Reddit Feeds (`main`, output 0, input 1)
- Fetch Stocks → Merge Reddit Feeds (`main`, output 0, input 2)
- Merge Reddit Feeds → 1A: Raw Merge & Structural Clean (`main`, output 0, input 0)
- 1A: Raw Merge & Structural Clean → 1B: Linguistic & Relevance Filter (`main`, output 0, input 0)
- 1B: Linguistic & Relevance Filter → Keyword Pre-Scorer (`main`, output 0, input 0)
- Keyword Pre-Scorer → Aggregate for Claude (`main`, output 0, input 0)
- Aggregate for Claude → Claude 1: Anxiety Score (`main`, output 0, input 0)
- Aggregate for Claude → Claude 2: Narrative Velocity (`main`, output 0, input 0)
- Aggregate for Claude → Claude 3: Herd Detection (`main`, output 0, input 0)
- Aggregate for Claude → Claude 4: Conviction vs Uncertainty (`main`, output 0, input 0)
- Aggregate for Claude → Claude 5: Crowd Cycle Stage (`main`, output 0, input 0)
- Claude 1: Anxiety Score → Merge Claude Outputs (`main`, output 0, input 0)
- Claude 2: Narrative Velocity → Merge Claude Outputs (`main`, output 0, input 1)
- Claude 3: Herd Detection → Merge Claude Outputs (`main`, output 0, input 2)
- Claude 4: Conviction vs Uncertainty → Merge Claude Outputs (`main`, output 0, input 3)
- Claude 5: Crowd Cycle Stage → Merge Claude Outputs (`main`, output 0, input 4)
- Merge Claude Outputs → Signal Aggregator (`main`, output 0, input 0)
- Signal Aggregator → Persist to File (`main`, output 0, input 0)
- Persist to File → Generate Quickchart URLs (`main`, output 0, input 0)
- Generate Quickchart URLs → Write output.json (`main`, output 0, input 0)
- Write output.json → Insert to Supabase (`main`, output 0, input 0)
- Insert to Supabase → Pipeline Response (`main`, output 0, input 0)
- Anthropic Model 1 → Claude 1: Anxiety Score (`ai_languageModel`, output 0, input 0)
- Anthropic Model 2 → Claude 2: Narrative Velocity (`ai_languageModel`, output 0, input 0)
- Anthropic Model 3 → Claude 3: Herd Detection (`ai_languageModel`, output 0, input 0)
- Anthropic Model 4 → Claude 4: Conviction vs Uncertainty (`ai_languageModel`, output 0, input 0)
- Anthropic Model 5 → Claude 5: Crowd Cycle Stage (`ai_languageModel`, output 0, input 0)
- Dashboard Webhook → Build Dashboard Response (`main`, output 0, input 0)
- Build Dashboard Response → Serve Dashboard HTML (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
