# Contradiction_detection_agent

This folder contains the **Contradiction_detection_agent** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `manualTrigger`, `merge`, `postgres`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`contradiction-detection.json`](contradiction-detection.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Set Company Input | `set` | Inspect parameters |
| DB: Fetch Earnings Guidance Signals | `postgres` | executeQuery |
| DB: Fetch Risk Admissions | `postgres` | executeQuery |
| DB: Fetch QA Pressure Map | `postgres` | executeQuery |
| DB: Fetch News Signals | `postgres` | executeQuery |
| DB: Fetch Tech Stack Signals | `postgres` | executeQuery |
| Aggregate All Signals | `code` | Inspect parameters |
| Run Pattern Detection Engine | `code` | Inspect parameters |
| Build Groq Prompt | `code` | Inspect parameters |
| LLM Needed? | `if` | Inspect parameters |
| Groq: Analyse Contradictions | `httpRequest` | POST |
| Process Groq Response | `code` | Inspect parameters |
| No-Flag Passthrough | `code` | Inspect parameters |
| DB: Insert Contradiction Report | `postgres` | executeQuery |
| Fan Out Flags | `code` | Inspect parameters |
| DB: Insert Contradiction Flag | `postgres` | executeQuery |
| Build Final Report | `code` | Inspect parameters |
| Execute a SQL query | `postgres` | executeQuery |
| Execute a SQL query1 | `postgres` | executeQuery |
| Execute a SQL query2 | `postgres` | executeQuery |
| Execute a SQL query3 | `postgres` | executeQuery |
| HTTP Request | `httpRequest` | Inspect parameters |
| Process News Response | `code` | Inspect parameters |
| DB: Save News Signals | `postgres` | executeQuery |
| Merge | `merge` | Inspect parameters |

## Connection map

- Manual Trigger → Set Company Input (`main`, output 0, input 0)
- Set Company Input → HTTP Request (`main`, output 0, input 0)
- Set Company Input → DB: Fetch Earnings Guidance Signals (`main`, output 0, input 0)
- Set Company Input → DB: Fetch Tech Stack Signals (`main`, output 0, input 0)
- Set Company Input → DB: Fetch Risk Admissions (`main`, output 0, input 0)
- Set Company Input → DB: Fetch QA Pressure Map (`main`, output 0, input 0)
- DB: Fetch Earnings Guidance Signals → Merge (`main`, output 0, input 1)
- DB: Fetch Risk Admissions → Merge (`main`, output 0, input 4)
- DB: Fetch QA Pressure Map → Merge (`main`, output 0, input 0)
- DB: Fetch News Signals → Merge (`main`, output 0, input 3)
- DB: Fetch Tech Stack Signals → Merge (`main`, output 0, input 2)
- Aggregate All Signals → Run Pattern Detection Engine (`main`, output 0, input 0)
- Run Pattern Detection Engine → Build Groq Prompt (`main`, output 0, input 0)
- Build Groq Prompt → LLM Needed? (`main`, output 0, input 0)
- LLM Needed? → Groq: Analyse Contradictions (`main`, output 0, input 0)
- LLM Needed? → No-Flag Passthrough (`main`, output 1, input 0)
- Groq: Analyse Contradictions → Process Groq Response (`main`, output 0, input 0)
- Process Groq Response → DB: Insert Contradiction Report (`main`, output 0, input 0)
- No-Flag Passthrough → DB: Insert Contradiction Report (`main`, output 0, input 0)
- DB: Insert Contradiction Report → Fan Out Flags (`main`, output 0, input 0)
- Fan Out Flags → DB: Insert Contradiction Flag (`main`, output 0, input 0)
- DB: Insert Contradiction Flag → Build Final Report (`main`, output 0, input 0)
- HTTP Request → Process News Response (`main`, output 0, input 0)
- Process News Response → DB: Save News Signals (`main`, output 0, input 0)
- DB: Save News Signals → DB: Fetch News Signals (`main`, output 0, input 0)
- Merge → Aggregate All Signals (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
