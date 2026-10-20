# Patent Filing Velocity Tracker — Mycroft Agent

This folder contains the **Patent Filing Velocity Tracker — Mycroft Agent** workflow. Its executable nodes use `chainLlm`, `code`, `emailSend`, `httpRequest`, `if`, `lmChatAnthropic`, `merge`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`patent-filing-velocity-tracker-mycroft-agent.json`](patent-filing-velocity-tracker-mycroft-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `smtp`

**Entry nodes:** Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook Trigger | `webhook` | Inspect parameters |
| Security Gate | `code` | Inspect parameters |
| IF Authorized | `if` | Inspect parameters |
| Unauthorized Response | `respondToWebhook` | Inspect parameters |
| Fetch Previous Run | `httpRequest` | GET |
| Fetch Patent Data | `code` | Inspect parameters |
| Merge Fetch Outputs | `merge` | Inspect parameters |
| 1A: Structural Clean | `code` | Inspect parameters |
| 1B: Classify + Quality Weight | `code` | Inspect parameters |
| Patent Count Gate | `code` | Inspect parameters |
| Aggregate for Claude | `code` | Inspect parameters |
| Anthropic Model 1 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 2 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 3 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 4 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 5 | `lmChatAnthropic` | Inspect parameters |
| Anthropic Model 6 | `lmChatAnthropic` | Inspect parameters |
| Claude 1: Velocity Score | `chainLlm` | Inspect parameters |
| Claude 2: Concept Novelty | `chainLlm` | Inspect parameters |
| Claude 3: Inventor Network | `chainLlm` | Inspect parameters |
| Claude 4: Cross-Company Convergence | `chainLlm` | Inspect parameters |
| Claude 5: Strategic Intent | `chainLlm` | Inspect parameters |
| Claude 6: Breakthrough Detection | `chainLlm` | Inspect parameters |
| Merge Claude Outputs | `merge` | Inspect parameters |
| Signal Aggregator | `code` | Inspect parameters |
| Insert to Supabase | `httpRequest` | POST |
| Parse Insert + Build Errors | `code` | Inspect parameters |
| Write Error Log | `httpRequest` | POST |
| Newsletter Gate | `if` | Inspect parameters |
| Log Newsletter Skipped | `httpRequest` | POST |
| Anthropic Model Newsletter | `lmChatAnthropic` | Inspect parameters |
| Generate Newsletter | `chainLlm` | Inspect parameters |
| Fetch Subscribers | `httpRequest` | GET |
| Send Email | `emailSend` | Inspect parameters |
| Insert Newsletter Run | `httpRequest` | POST |
| Mycroft Orchestration Emit | `httpRequest` | POST |
| Converge Outputs | `merge` | Inspect parameters |
| Webhook Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook Trigger → Security Gate (`main`, output 0, input 0)
- Security Gate → IF Authorized (`main`, output 0, input 0)
- IF Authorized → Fetch Previous Run (`main`, output 0, input 0)
- IF Authorized → Fetch Patent Data (`main`, output 0, input 0)
- IF Authorized → Unauthorized Response (`main`, output 1, input 0)
- Fetch Previous Run → Merge Fetch Outputs (`main`, output 0, input 0)
- Fetch Patent Data → Merge Fetch Outputs (`main`, output 0, input 1)
- Merge Fetch Outputs → 1A: Structural Clean (`main`, output 0, input 0)
- 1A: Structural Clean → 1B: Classify + Quality Weight (`main`, output 0, input 0)
- 1B: Classify + Quality Weight → Patent Count Gate (`main`, output 0, input 0)
- Patent Count Gate → Aggregate for Claude (`main`, output 0, input 0)
- Aggregate for Claude → Claude 1: Velocity Score (`main`, output 0, input 0)
- Aggregate for Claude → Claude 2: Concept Novelty (`main`, output 0, input 0)
- Aggregate for Claude → Claude 3: Inventor Network (`main`, output 0, input 0)
- Aggregate for Claude → Claude 4: Cross-Company Convergence (`main`, output 0, input 0)
- Aggregate for Claude → Claude 5: Strategic Intent (`main`, output 0, input 0)
- Aggregate for Claude → Claude 6: Breakthrough Detection (`main`, output 0, input 0)
- Anthropic Model 1 → Claude 1: Velocity Score (`ai_languageModel`, output 0, input 0)
- Anthropic Model 2 → Claude 2: Concept Novelty (`ai_languageModel`, output 0, input 0)
- Anthropic Model 3 → Claude 3: Inventor Network (`ai_languageModel`, output 0, input 0)
- Anthropic Model 4 → Claude 4: Cross-Company Convergence (`ai_languageModel`, output 0, input 0)
- Anthropic Model 5 → Claude 5: Strategic Intent (`ai_languageModel`, output 0, input 0)
- Anthropic Model 6 → Claude 6: Breakthrough Detection (`ai_languageModel`, output 0, input 0)
- Anthropic Model Newsletter → Generate Newsletter (`ai_languageModel`, output 0, input 0)
- Claude 1: Velocity Score → Merge Claude Outputs (`main`, output 0, input 0)
- Claude 2: Concept Novelty → Merge Claude Outputs (`main`, output 0, input 1)
- Claude 3: Inventor Network → Merge Claude Outputs (`main`, output 0, input 2)
- Claude 4: Cross-Company Convergence → Merge Claude Outputs (`main`, output 0, input 3)
- Claude 5: Strategic Intent → Merge Claude Outputs (`main`, output 0, input 4)
- Claude 6: Breakthrough Detection → Merge Claude Outputs (`main`, output 0, input 5)
- Merge Claude Outputs → Signal Aggregator (`main`, output 0, input 0)
- Signal Aggregator → Insert to Supabase (`main`, output 0, input 0)
- Signal Aggregator → Newsletter Gate (`main`, output 0, input 0)
- Signal Aggregator → Mycroft Orchestration Emit (`main`, output 0, input 0)
- Insert to Supabase → Parse Insert + Build Errors (`main`, output 0, input 0)
- Parse Insert + Build Errors → Write Error Log (`main`, output 0, input 0)
- Parse Insert + Build Errors → Converge Outputs (`main`, output 0, input 0)
- Newsletter Gate → Generate Newsletter (`main`, output 0, input 0)
- Newsletter Gate → Log Newsletter Skipped (`main`, output 1, input 0)
- Log Newsletter Skipped → Converge Outputs (`main`, output 0, input 1)
- Generate Newsletter → Fetch Subscribers (`main`, output 0, input 0)
- Fetch Subscribers → Send Email (`main`, output 0, input 0)
- Send Email → Insert Newsletter Run (`main`, output 0, input 0)
- Insert Newsletter Run → Converge Outputs (`main`, output 0, input 1)
- Mycroft Orchestration Emit → Converge Outputs (`main`, output 0, input 2)
- Converge Outputs → Webhook Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
