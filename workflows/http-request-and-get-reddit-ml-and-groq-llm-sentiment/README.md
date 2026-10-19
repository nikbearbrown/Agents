# http request and get reddit ml and groq llm sentiment

This folder contains the **http request and get reddit ml and groq llm sentiment** workflow. Its executable nodes use `function`, `googleSheets`, `httpRequest`, `manualTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-get-reddit-ml-and-groq-llm-sentiment.json`](http-request-and-get-reddit-ml-and-groq-llm-sentiment.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `groqApi`

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Process StackOverflow | `function` | Inspect parameters |
| Get StackOverflow | `httpRequest` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| Combine All Data | `function` | Inspect parameters |
| Process Reddit ML | `function` | Inspect parameters |
| Get Reddit ML | `httpRequest` | Inspect parameters |
| Process GitHub | `function` | Inspect parameters |
| Get GitHub | `httpRequest` | Inspect parameters |
| Groq LLM Sentiment | `httpRequest` | POST |
| Process Groq Sentiment | `function` | Inspect parameters |
| Groq Topic Classification | `httpRequest` | POST |
| Topic Clustering Engine | `function` | Inspect parameters |
| Signal-to-Noise Filter | `function` | Inspect parameters |
| Social Sentiment Output | `function` | Inspect parameters |
| Enhanced Data Export | `function` | Inspect parameters |
| Prepare for Google Sheets | `function` | Inspect parameters |
| Store in Google Sheets | `googleSheets` | appendOrUpdate |

## Connection map

- Process StackOverflow → Combine All Data (`main`, output 0, input 0)
- Get StackOverflow → Process StackOverflow (`main`, output 0, input 0)
- Manual Trigger → Get StackOverflow (`main`, output 0, input 0)
- Manual Trigger → Get Reddit ML (`main`, output 0, input 0)
- Manual Trigger → Get GitHub (`main`, output 0, input 0)
- Combine All Data → Groq LLM Sentiment (`main`, output 0, input 0)
- Process Reddit ML → Combine All Data (`main`, output 0, input 0)
- Get Reddit ML → Process Reddit ML (`main`, output 0, input 0)
- Process GitHub → Combine All Data (`main`, output 0, input 0)
- Get GitHub → Process GitHub (`main`, output 0, input 0)
- Groq LLM Sentiment → Process Groq Sentiment (`main`, output 0, input 0)
- Process Groq Sentiment → Groq Topic Classification (`main`, output 0, input 0)
- Groq Topic Classification → Topic Clustering Engine (`main`, output 0, input 0)
- Topic Clustering Engine → Signal-to-Noise Filter (`main`, output 0, input 0)
- Signal-to-Noise Filter → Social Sentiment Output (`main`, output 0, input 0)
- Social Sentiment Output → Enhanced Data Export (`main`, output 0, input 0)
- Enhanced Data Export → Prepare for Google Sheets (`main`, output 0, input 0)
- Prepare for Google Sheets → Store in Google Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
