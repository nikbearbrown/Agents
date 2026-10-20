# Mycroft Agent 5 — Research Footprint Monitor

This folder contains the **Mycroft Agent 5 — Research Footprint Monitor** workflow. Its executable nodes use `code`, `httpRequest`, `merge`, `respondToWebhook`, `scheduleTrigger`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`research-footprint-monitor.json`](research-footprint-monitor.json): sanitized, inactive import copy with an overview sticky note.
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
| Scholar: NVIDIA | `httpRequest` | Inspect parameters |
| Scholar: AMD | `httpRequest` | Inspect parameters |
| Scholar: Intel | `httpRequest` | Inspect parameters |
| Scholar: Google | `httpRequest` | Inspect parameters |
| Scholar: Apple | `httpRequest` | Inspect parameters |
| Scholar: Microsoft | `httpRequest` | Inspect parameters |
| Scholar: Meta | `httpRequest` | Inspect parameters |
| Merge Scholar Results | `merge` | Inspect parameters |
| Parse Scholar Data | `code` | Inspect parameters |
| Wikipedia: NVIDIA | `httpRequest` | Inspect parameters |
| Wikipedia: AMD | `httpRequest` | Inspect parameters |
| Wikipedia: Intel | `httpRequest` | Inspect parameters |
| Wikipedia: Google | `httpRequest` | Inspect parameters |
| Wikipedia: Apple | `httpRequest` | Inspect parameters |
| Wikipedia: Microsoft | `httpRequest` | Inspect parameters |
| Wikipedia: Meta | `httpRequest` | Inspect parameters |
| Merge Wikipedia Results | `merge` | Inspect parameters |
| Parse Wikipedia Data | `code` | Inspect parameters |
| Combine Signals | `merge` | Inspect parameters |
| Calculate Footprint Scores | `code` | Inspect parameters |
| Aggregate for Groq | `code` | Inspect parameters |
| Groq: Footprint Analyst | `httpRequest` | POST |
| Parse Groq Response | `code` | Inspect parameters |
| Signal Assembler | `code` | Inspect parameters |
| Upsert to Supabase | `supabase` | upsert |
| Generate Report | `code` | Inspect parameters |
| Store Report in Supabase | `supabase` | Inspect parameters |
| Pipeline Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Cron Trigger → Fetch Watchlist (`main`, output 0, input 0)
- Manual Pipeline Webhook → Fetch Watchlist (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: NVIDIA (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: AMD (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: Intel (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: Google (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: Apple (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: Microsoft (`main`, output 0, input 0)
- Fetch Watchlist → Scholar: Meta (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: NVIDIA (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: AMD (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: Intel (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: Google (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: Apple (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: Microsoft (`main`, output 0, input 0)
- Fetch Watchlist → Wikipedia: Meta (`main`, output 0, input 0)
- Scholar: NVIDIA → Merge Scholar Results (`main`, output 0, input 0)
- Scholar: AMD → Merge Scholar Results (`main`, output 0, input 1)
- Scholar: Intel → Merge Scholar Results (`main`, output 0, input 2)
- Scholar: Google → Merge Scholar Results (`main`, output 0, input 3)
- Scholar: Apple → Merge Scholar Results (`main`, output 0, input 4)
- Scholar: Microsoft → Merge Scholar Results (`main`, output 0, input 5)
- Scholar: Meta → Merge Scholar Results (`main`, output 0, input 6)
- Merge Scholar Results → Parse Scholar Data (`main`, output 0, input 0)
- Wikipedia: NVIDIA → Merge Wikipedia Results (`main`, output 0, input 0)
- Wikipedia: AMD → Merge Wikipedia Results (`main`, output 0, input 1)
- Wikipedia: Intel → Merge Wikipedia Results (`main`, output 0, input 2)
- Wikipedia: Google → Merge Wikipedia Results (`main`, output 0, input 3)
- Wikipedia: Apple → Merge Wikipedia Results (`main`, output 0, input 4)
- Wikipedia: Microsoft → Merge Wikipedia Results (`main`, output 0, input 5)
- Wikipedia: Meta → Merge Wikipedia Results (`main`, output 0, input 6)
- Merge Wikipedia Results → Parse Wikipedia Data (`main`, output 0, input 0)
- Parse Scholar Data → Combine Signals (`main`, output 0, input 0)
- Parse Wikipedia Data → Combine Signals (`main`, output 0, input 1)
- Combine Signals → Calculate Footprint Scores (`main`, output 0, input 0)
- Calculate Footprint Scores → Aggregate for Groq (`main`, output 0, input 0)
- Aggregate for Groq → Groq: Footprint Analyst (`main`, output 0, input 0)
- Groq: Footprint Analyst → Parse Groq Response (`main`, output 0, input 0)
- Parse Groq Response → Signal Assembler (`main`, output 0, input 0)
- Signal Assembler → Upsert to Supabase (`main`, output 0, input 0)
- Upsert to Supabase → Generate Report (`main`, output 0, input 0)
- Generate Report → Store Report in Supabase (`main`, output 0, input 0)
- Store Report in Supabase → Pipeline Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
