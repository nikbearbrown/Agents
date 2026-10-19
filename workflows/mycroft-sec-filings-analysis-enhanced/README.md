# Mycroft - SEC_Filings_Analysis_Enhanced

This folder contains the **Mycroft - SEC_Filings_Analysis_Enhanced** workflow. Its executable nodes use `code`, `executeCommand`, `if`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-sec-filings-analysis-enhanced.json`](mycroft-sec-filings-analysis-enhanced.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set Variables | `set` | Inspect parameters |
| Initialize Logging | `executeCommand` | Inspect parameters |
| Setup Github Repo | `executeCommand` | Inspect parameters |
| Log: Repo Cloned | `executeCommand` | Inspect parameters |
| Set Path Variables | `code` | Inspect parameters |
| Setup Python Enviornment and Output Directories | `executeCommand` | Inspect parameters |
| Log: Python Setup | `executeCommand` | Inspect parameters |
| Edgar_Fetcher | `executeCommand` | Inspect parameters |
| Validate Fetcher | `code` | Inspect parameters |
| Log: Fetcher Complete | `executeCommand` | Inspect parameters |
| If | `if` | Inspect parameters |
| Financial Analyzer | `executeCommand` | Inspect parameters |
| Narrative Parser | `executeCommand` | Inspect parameters |
| Validate Financial Metrics | `code` | Inspect parameters |
| Validate Narrative Content | `code` | Inspect parameters |
| Log: Financial Complete | `executeCommand` | Inspect parameters |
| Log: Narrative Complete | `executeCommand` | Inspect parameters |
| Merge Results | `code` | Inspect parameters |
| Log: Merge Complete | `executeCommand` | Inspect parameters |
| Save to Database | `executeCommand` | Inspect parameters |
| Log: Saved | `executeCommand` | Inspect parameters |
| Cleanup Temp Directories | `executeCommand` | Inspect parameters |
| Log Completion | `executeCommand` | Inspect parameters |
| Error Handling | `code` | Inspect parameters |
| Log Error | `executeCommand` | Inspect parameters |
| Cleanup On Error | `executeCommand` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Code in JavaScript | `code` | Inspect parameters |

## Connection map

- Set Variables → Initialize Logging (`main`, output 0, input 0)
- Initialize Logging → Setup Github Repo (`main`, output 0, input 0)
- Setup Github Repo → Log: Repo Cloned (`main`, output 0, input 0)
- Log: Repo Cloned → Set Path Variables (`main`, output 0, input 0)
- Set Path Variables → Setup Python Enviornment and Output Directories (`main`, output 0, input 0)
- Set Path Variables → Edgar_Fetcher (`main`, output 0, input 0)
- Setup Python Enviornment and Output Directories → Log: Python Setup (`main`, output 0, input 0)
- Edgar_Fetcher → Validate Fetcher (`main`, output 0, input 0)
- Validate Fetcher → Log: Fetcher Complete (`main`, output 0, input 0)
- Log: Fetcher Complete → If (`main`, output 0, input 0)
- If → Financial Analyzer (`main`, output 0, input 0)
- If → Error Handling (`main`, output 1, input 0)
- Financial Analyzer → Validate Financial Metrics (`main`, output 0, input 0)
- Narrative Parser → Validate Narrative Content (`main`, output 0, input 0)
- Validate Financial Metrics → Log: Financial Complete (`main`, output 0, input 0)
- Validate Narrative Content → Log: Narrative Complete (`main`, output 0, input 0)
- Log: Financial Complete → Narrative Parser (`main`, output 0, input 0)
- Log: Narrative Complete → Merge Results (`main`, output 0, input 0)
- Merge Results → Log: Merge Complete (`main`, output 0, input 0)
- Log: Merge Complete → Save to Database (`main`, output 0, input 0)
- Save to Database → Log: Saved (`main`, output 0, input 0)
- Log: Saved → Cleanup Temp Directories (`main`, output 0, input 0)
- Cleanup Temp Directories → Log Completion (`main`, output 0, input 0)
- Error Handling → Log Error (`main`, output 0, input 0)
- Log Error → Cleanup On Error (`main`, output 0, input 0)
- Webhook → Set Variables (`main`, output 0, input 0)
- Log Completion → Code in JavaScript (`main`, output 0, input 0)
- Code in JavaScript → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
