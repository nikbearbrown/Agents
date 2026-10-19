# Mycroft — Signal Contradiction Detector (Agent 6)

This folder contains the **Mycroft — Signal Contradiction Detector (Agent 6)** workflow. Its executable nodes use `code`, `httpRequest`, `merge`, `respondToWebhook`, `scheduleTrigger`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-signal-contradiction-detector-agent-6.json`](mycroft-signal-contradiction-detector-agent-6.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Cron Trigger, Manual Pipeline Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Cron Trigger | `scheduleTrigger` | Inspect parameters |
| Manual Pipeline Webhook | `webhook` | Inspect parameters |
| Fetch Watchlist | `code` | Inspect parameters |
| Read anxiety_runs | `supabase` | getAll |
| Read patent_runs | `supabase` | getAll |
| Read media_narratives_raw | `supabase` | getAll |
| Read github_signals | `supabase` | getAll |
| Read mindshare_signals | `supabase` | getAll |
| Merge All Signals | `merge` | Inspect parameters |
| Normalize Signal Data | `code` | Inspect parameters |
| Detect Contradiction Patterns | `code` | Inspect parameters |
| Score Contradictions | `code` | Inspect parameters |
| Aggregate for Groq | `code` | Inspect parameters |
| Groq: Contradiction Analyst | `httpRequest` | POST |
| Parse Groq Response | `code` | Inspect parameters |
| Assemble Contradiction Report Data | `code` | Inspect parameters |
| Insert to Supabase | `supabase` | upsert |
| Generate Report | `code` | Inspect parameters |
| Store Full Report | `supabase` | insert |
| Pipeline Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Cron Trigger → Fetch Watchlist (`main`, output 0, input 0)
- Manual Pipeline Webhook → Fetch Watchlist (`main`, output 0, input 0)
- Fetch Watchlist → Read anxiety_runs (`main`, output 0, input 0)
- Fetch Watchlist → Read patent_runs (`main`, output 0, input 0)
- Fetch Watchlist → Read media_narratives_raw (`main`, output 0, input 0)
- Fetch Watchlist → Read github_signals (`main`, output 0, input 0)
- Fetch Watchlist → Read mindshare_signals (`main`, output 0, input 0)
- Read anxiety_runs → Merge All Signals (`main`, output 0, input 0)
- Read patent_runs → Merge All Signals (`main`, output 0, input 1)
- Merge All Signals → Normalize Signal Data (`main`, output 0, input 0)
- Normalize Signal Data → Detect Contradiction Patterns (`main`, output 0, input 0)
- Detect Contradiction Patterns → Score Contradictions (`main`, output 0, input 0)
- Score Contradictions → Aggregate for Groq (`main`, output 0, input 0)
- Aggregate for Groq → Groq: Contradiction Analyst (`main`, output 0, input 0)
- Groq: Contradiction Analyst → Parse Groq Response (`main`, output 0, input 0)
- Parse Groq Response → Assemble Contradiction Report Data (`main`, output 0, input 0)
- Assemble Contradiction Report Data → Insert to Supabase (`main`, output 0, input 0)
- Insert to Supabase → Generate Report (`main`, output 0, input 0)
- Generate Report → Store Full Report (`main`, output 0, input 0)
- Store Full Report → Pipeline Response (`main`, output 0, input 0)
- Read media_narratives_raw → Merge All Signals (`main`, output 0, input 2)
- Read github_signals → Merge All Signals (`main`, output 0, input 3)
- Read mindshare_signals → Merge All Signals (`main`, output 0, input 4)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
