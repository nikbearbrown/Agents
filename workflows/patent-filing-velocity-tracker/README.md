# Patent Filing Velocity Tracker

This folder contains the **Patent Filing Velocity Tracker** workflow. Its executable nodes use `chainLlm`, `code`, `httpRequest`, `if`, `lmChatAnthropic`, `merge`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`patent-filing-velocity-tracker.json`](patent-filing-velocity-tracker.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`

**Entry nodes:** Manual Run Trigger, Dashboard Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Run Trigger | `webhook` | Inspect parameters |
| Dashboard Webhook | `webhook` | Inspect parameters |
| Fetch Patent Data | `code` | Inspect parameters |
| 1A: Structural Clean | `code` | Inspect parameters |
| 1B: Category Classifier + Velocity Pre-Scorer | `code` | Inspect parameters |
| Aggregate for Claude | `code` | Inspect parameters |
| Claude 1: Velocity Score | `chainLlm` | Inspect parameters |
| Claude 2: Concept Novelty | `chainLlm` | Inspect parameters |
| Claude 3: Inventor Network | `chainLlm` | Inspect parameters |
| Claude 4: Cross-Company Convergence | `chainLlm` | Inspect parameters |
| Claude 5: Strategic Intent | `chainLlm` | Inspect parameters |
| Anthropic Model 1 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 2 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 3 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 4 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 5 | `lmChatAnthropic` | Inspect parameters |
| Merge Claude Outputs | `merge` | Inspect parameters |
| Signal Aggregator | `code` | Inspect parameters |
| Insert to Supabase | `httpRequest` | POST |
| Check Trigger Type | `code` | Inspect parameters |
| If Webhook | `if` | Inspect parameters |
| Pipeline Response | `respondToWebhook` | Inspect parameters |
| Build Dashboard HTML | `code` | Inspect parameters |
| Serve Dashboard HTML | `respondToWebhook` | Inspect parameters |

## Connection map

- Manual Run Trigger → Fetch Patent Data (`main`, output 0, input 0)
- Dashboard Webhook → Build Dashboard HTML (`main`, output 0, input 0)
- Fetch Patent Data → 1A: Structural Clean (`main`, output 0, input 0)
- 1A: Structural Clean → 1B: Category Classifier + Velocity Pre-Scorer (`main`, output 0, input 0)
- 1B: Category Classifier + Velocity Pre-Scorer → Aggregate for Claude (`main`, output 0, input 0)
- Aggregate for Claude → Claude 1: Velocity Score (`main`, output 0, input 0)
- Aggregate for Claude → Claude 2: Concept Novelty (`main`, output 0, input 0)
- Aggregate for Claude → Claude 3: Inventor Network (`main`, output 0, input 0)
- Aggregate for Claude → Claude 4: Cross-Company Convergence (`main`, output 0, input 0)
- Aggregate for Claude → Claude 5: Strategic Intent (`main`, output 0, input 0)
- Claude 1: Velocity Score → Merge Claude Outputs (`main`, output 0, input 0)
- Claude 2: Concept Novelty → Merge Claude Outputs (`main`, output 0, input 1)
- Claude 3: Inventor Network → Merge Claude Outputs (`main`, output 0, input 2)
- Claude 4: Cross-Company Convergence → Merge Claude Outputs (`main`, output 0, input 3)
- Claude 5: Strategic Intent → Merge Claude Outputs (`main`, output 0, input 4)
- Merge Claude Outputs → Signal Aggregator (`main`, output 0, input 0)
- Signal Aggregator → Insert to Supabase (`main`, output 0, input 0)
- Insert to Supabase → Check Trigger Type (`main`, output 0, input 0)
- Check Trigger Type → If Webhook (`main`, output 0, input 0)
- If Webhook → Pipeline Response (`main`, output 0, input 0)
- Build Dashboard HTML → Serve Dashboard HTML (`main`, output 0, input 0)
- Anthropic Model 1 → Claude 1: Velocity Score (`ai_languageModel`, output 0, input 0)
- Anthropic Model 2 → Claude 2: Concept Novelty (`ai_languageModel`, output 0, input 0)
- Anthropic Model 3 → Claude 3: Inventor Network (`ai_languageModel`, output 0, input 0)
- Anthropic Model 4 → Claude 4: Cross-Company Convergence (`ai_languageModel`, output 0, input 0)
- Anthropic Model 5 → Claude 5: Strategic Intent (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
