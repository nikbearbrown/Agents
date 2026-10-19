# Portfolio Intelligence Agent - Complete with RAG

This folder contains the **Portfolio Intelligence Agent - Complete with RAG** workflow. Its executable nodes use `code`, `convertToFile`, `gmail`, `httpRequest`, `manualTrigger`, `readBinaryFile`, `readWriteFile`, `scheduleTrigger`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`portfolio-intelligence-agent-complete-with-rag.json`](portfolio-intelligence-agent-complete-with-rag.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** Manual Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Read Holdings File | `readBinaryFile` | Inspect parameters |
| Parse JSON Holdings | `code` | Inspect parameters |
| Calculate Portfolio Metrics | `code` | Inspect parameters |
| Read Previous Summaries | `readBinaryFile` | Inspect parameters |
| Fetch & Extract Stock Prices | `code` | Inspect parameters |
| Parse Summaries CSV | `code` | Inspect parameters |
| Calculate Daily Return | `code` | Inspect parameters |
| Read Knowledge Base1 | `readWriteFile` | Inspect parameters |
| Parse Knowledge Base CSV | `code` | Inspect parameters |
| Read Portfolio History CSV | `readWriteFile` | Inspect parameters |
| Parse Portfolio History Data | `code` | Inspect parameters |
| Build Portfolio Analysis | `code` | Inspect parameters |
| RAG-Retrieve Context | `code` | Inspect parameters |
| Extract AI Summary | `code` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Generate AI Summary (Groq) | `httpRequest` | POST |
| Send a message | `gmail` | Inspect parameters |
| Append Portfolio History1 | `readWriteFile` | write |
| Convert Holdings to CSV | `convertToFile` | Inspect parameters |
| Convert Summary to CSV | `convertToFile` | Inspect parameters |
| Append Daily Summary | `readWriteFile` | write |

## Connection map

- Manual Trigger → Read Holdings File (`main`, output 0, input 0)
- Schedule Trigger → Read Holdings File (`main`, output 0, input 0)
- Read Holdings File → Parse JSON Holdings (`main`, output 0, input 0)
- Parse JSON Holdings → Fetch & Extract Stock Prices (`main`, output 0, input 0)
- Calculate Portfolio Metrics → Read Portfolio History CSV (`main`, output 0, input 0)
- Read Previous Summaries → Parse Summaries CSV (`main`, output 0, input 0)
- Fetch & Extract Stock Prices → Calculate Portfolio Metrics (`main`, output 0, input 0)
- Parse Summaries CSV → Calculate Daily Return (`main`, output 0, input 0)
- Calculate Daily Return → Read Knowledge Base1 (`main`, output 0, input 0)
- Read Knowledge Base1 → Parse Knowledge Base CSV (`main`, output 0, input 0)
- Read Portfolio History CSV → Parse Portfolio History Data (`main`, output 0, input 0)
- Parse Portfolio History Data → Build Portfolio Analysis (`main`, output 0, input 0)
- Build Portfolio Analysis → Read Previous Summaries (`main`, output 0, input 0)
- Parse Knowledge Base CSV → RAG-Retrieve Context (`main`, output 0, input 0)
- RAG-Retrieve Context → Generate AI Summary (Groq) (`main`, output 0, input 0)
- Extract AI Summary → Split Out (`main`, output 0, input 0)
- Extract AI Summary → Convert Summary to CSV (`main`, output 0, input 0)
- Extract AI Summary → Send a message (`main`, output 0, input 0)
- Generate AI Summary (Groq) → Extract AI Summary (`main`, output 0, input 0)
- Split Out → Convert Holdings to CSV (`main`, output 0, input 0)
- Convert Holdings to CSV → Append Portfolio History1 (`main`, output 0, input 0)
- Convert Summary to CSV → Append Daily Summary (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
