# Media Narrative Tracker — Mycroft Agent 3 (Groq)

This folder contains the **Media Narrative Tracker — Mycroft Agent 3 (Groq)** workflow. Its executable nodes use `code`, `httpRequest`, `merge`, `respondToWebhook`, `scheduleTrigger`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`media-narrative-novelty.json`](media-narrative-novelty.json): sanitized, inactive import copy with an overview sticky note.
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
| Fetch FT RSS | `httpRequest` | Inspect parameters |
| Fetch Reuters RSS | `httpRequest` | Inspect parameters |
| Fetch Seeking Alpha RSS | `httpRequest` | Inspect parameters |
| Fetch CNBC RSS | `httpRequest` | Inspect parameters |
| Fetch Yahoo Finance RSS | `httpRequest` | Inspect parameters |
| Parse & Clean Articles | `code` | Inspect parameters |
| Deduplicate Against Supabase | `code` | Inspect parameters |
| Aggregate for Groq | `code` | Inspect parameters |
| Groq 1: Core Claim Extractor | `httpRequest` | POST |
| Groq 2: Information Age Scorer | `httpRequest` | POST |
| Groq 3: Company Mention Extractor | `httpRequest` | POST |
| Signal Assembler | `code` | Inspect parameters |
| Insert to Supabase | `supabase` | upsert |
| Generate Report | `code` | Inspect parameters |
| Store Report in Supabase | `supabase` | insert |
| Pipeline Response | `respondToWebhook` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |

## Connection map

- Cron Trigger → Fetch Watchlist (`main`, output 0, input 0)
- Manual Pipeline Webhook → Fetch Watchlist (`main`, output 0, input 0)
- Fetch Watchlist → Fetch FT RSS (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Reuters RSS (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Seeking Alpha RSS (`main`, output 0, input 0)
- Fetch Watchlist → Fetch CNBC RSS (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Yahoo Finance RSS (`main`, output 0, input 0)
- Fetch FT RSS → Merge (`main`, output 0, input 0)
- Fetch Reuters RSS → Merge (`main`, output 0, input 1)
- Parse & Clean Articles → Deduplicate Against Supabase (`main`, output 0, input 0)
- Deduplicate Against Supabase → Aggregate for Groq (`main`, output 0, input 0)
- Aggregate for Groq → Groq 1: Core Claim Extractor (`main`, output 0, input 0)
- Aggregate for Groq → Groq 2: Information Age Scorer (`main`, output 0, input 0)
- Aggregate for Groq → Groq 3: Company Mention Extractor (`main`, output 0, input 0)
- Groq 1: Core Claim Extractor → Merge1 (`main`, output 0, input 0)
- Groq 2: Information Age Scorer → Merge1 (`main`, output 0, input 1)
- Signal Assembler → Insert to Supabase (`main`, output 0, input 0)
- Insert to Supabase → Generate Report (`main`, output 0, input 0)
- Generate Report → Store Report in Supabase (`main`, output 0, input 0)
- Store Report in Supabase → Pipeline Response (`main`, output 0, input 0)
- Groq 3: Company Mention Extractor → Merge1 (`main`, output 0, input 2)
- Fetch Seeking Alpha RSS → Merge (`main`, output 0, input 2)
- Merge → Parse & Clean Articles (`main`, output 0, input 0)
- Fetch CNBC RSS → Merge (`main`, output 0, input 3)
- Fetch Yahoo Finance RSS → Merge (`main`, output 0, input 4)
- Merge1 → Signal Assembler (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
