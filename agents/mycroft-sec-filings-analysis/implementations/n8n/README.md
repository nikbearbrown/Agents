# Mycroft - SEC_Filings_Analysis

This folder contains the **Mycroft - SEC_Filings_Analysis** workflow. Its executable nodes use `code`, `executeCommand`, `if`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-sec-filings-analysis.json`](mycroft-sec-filings-analysis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking 'Execute workflow'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking 'Execute workflow' | `manualTrigger` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Setup Github Repo | `executeCommand` | Inspect parameters |
| Set Path Variables | `code` | Inspect parameters |
| Setup Python Enviornment and Output Directories | `executeCommand` | Inspect parameters |
| Edgar_Fetcher | `executeCommand` | Inspect parameters |
| Validate Fetcher | `code` | Inspect parameters |
| Financial Analyzer | `executeCommand` | Inspect parameters |
| Narrative Parser | `executeCommand` | Inspect parameters |
| Validate Financial Metrics | `code` | Inspect parameters |
| Validate Narrative Content | `code` | Inspect parameters |
| Cleanup Temp Directories | `executeCommand` | Inspect parameters |
| Error Handling | `code` | Inspect parameters |
| Cleanup  | `executeCommand` | Inspect parameters |

## Connection map

- When clicking 'Execute workflow' → Set Variables (`main`, output 0, input 0)
- If → Financial Analyzer (`main`, output 0, input 0)
- If → Narrative Parser (`main`, output 0, input 0)
- If → Error Handling (`main`, output 1, input 0)
- Set Variables → Setup Github Repo (`main`, output 0, input 0)
- Setup Github Repo → Set Path Variables (`main`, output 0, input 0)
- Set Path Variables → Setup Python Enviornment and Output Directories (`main`, output 0, input 0)
- Set Path Variables → Edgar_Fetcher (`main`, output 0, input 0)
- Edgar_Fetcher → Validate Fetcher (`main`, output 0, input 0)
- Validate Fetcher → If (`main`, output 0, input 0)
- Financial Analyzer → Validate Financial Metrics (`main`, output 0, input 0)
- Narrative Parser → Validate Narrative Content (`main`, output 0, input 0)
- Validate Narrative Content → Cleanup Temp Directories (`main`, output 0, input 0)
- Error Handling → Cleanup  (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
