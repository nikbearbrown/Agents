# GitHub Commit Velocity Tracker

This folder contains the **GitHub Commit Velocity Tracker** workflow. Its executable nodes use `code`, `httpRequest`, `merge`, `respondToWebhook`, `scheduleTrigger`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`github-activity-monitor.json`](github-activity-monitor.json): sanitized, inactive import copy with an overview sticky note.
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
| Fetch NVIDIA GitHub | `httpRequest` | Inspect parameters |
| Fetch AMD GitHub | `httpRequest` | Inspect parameters |
| Fetch Intel GitHub | `httpRequest` | Inspect parameters |
| Fetch Google GitHub | `httpRequest` | Inspect parameters |
| Fetch Apple GitHub | `httpRequest` | Inspect parameters |
| Fetch Microsoft GitHub | `httpRequest` | Inspect parameters |
| Fetch Meta GitHub | `httpRequest` | Inspect parameters |
| Merge GitHub Results | `merge` | Inspect parameters |
| Parse & Calculate Velocity | `code` | Inspect parameters |
| Load Previous Run from Supabase | `code` | Inspect parameters |
| Calculate Week-over-Week Delta | `code` | Inspect parameters |
| Aggregate for Groq | `code` | Inspect parameters |
| Groq: Activity Classifier | `httpRequest` | POST |
| Parse Groq Response | `code` | Inspect parameters |
| Signal Assembler | `code` | Inspect parameters |
| Upsert to Supabase | `supabase` | upsert |
| Generate Report | `code` | Inspect parameters |
| Store Report in Supabase | `supabase` | insert |
| Pipeline Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Cron Trigger → Fetch Watchlist (`main`, output 0, input 0)
- Manual Pipeline Webhook → Fetch Watchlist (`main`, output 0, input 0)
- Fetch Watchlist → Fetch NVIDIA GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch AMD GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Intel GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Google GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Apple GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Microsoft GitHub (`main`, output 0, input 0)
- Fetch Watchlist → Fetch Meta GitHub (`main`, output 0, input 0)
- Fetch NVIDIA GitHub → Merge GitHub Results (`main`, output 0, input 0)
- Fetch AMD GitHub → Merge GitHub Results (`main`, output 0, input 1)
- Fetch Intel GitHub → Merge GitHub Results (`main`, output 0, input 2)
- Fetch Google GitHub → Merge GitHub Results (`main`, output 0, input 3)
- Fetch Apple GitHub → Merge GitHub Results (`main`, output 0, input 4)
- Fetch Microsoft GitHub → Merge GitHub Results (`main`, output 0, input 5)
- Fetch Meta GitHub → Merge GitHub Results (`main`, output 0, input 6)
- Merge GitHub Results → Parse & Calculate Velocity (`main`, output 0, input 0)
- Parse & Calculate Velocity → Load Previous Run from Supabase (`main`, output 0, input 0)
- Load Previous Run from Supabase → Calculate Week-over-Week Delta (`main`, output 0, input 0)
- Calculate Week-over-Week Delta → Aggregate for Groq (`main`, output 0, input 0)
- Aggregate for Groq → Groq: Activity Classifier (`main`, output 0, input 0)
- Groq: Activity Classifier → Parse Groq Response (`main`, output 0, input 0)
- Parse Groq Response → Signal Assembler (`main`, output 0, input 0)
- Signal Assembler → Upsert to Supabase (`main`, output 0, input 0)
- Upsert to Supabase → Generate Report (`main`, output 0, input 0)
- Generate Report → Store Report in Supabase (`main`, output 0, input 0)
- Store Report in Supabase → Pipeline Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 1 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
