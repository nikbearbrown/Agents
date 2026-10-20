# Mycroft - Patent Intelligence System Enhanced

This folder contains the **Mycroft - Patent Intelligence System Enhanced** workflow. Its executable nodes use `code`, `emailSend`, `executeCommand`, `if`, `readBinaryFile`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-patent-intelligence-system-enhanced.json`](mycroft-patent-intelligence-system-enhanced.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set Variables | `set` | Inspect parameters |
| Initialize Logging | `executeCommand` | Inspect parameters |
| Setup Github Repo | `executeCommand` | Inspect parameters |
| Log: Repo Cloned | `executeCommand` | Inspect parameters |
| Set Path Variables | `code` | Inspect parameters |
| Setup Environment and Output Directories | `executeCommand` | Inspect parameters |
| Log: Environment Setup | `executeCommand` | Inspect parameters |
| Extract Patents | `executeCommand` | Inspect parameters |
| Log: Patents Extracted | `executeCommand` | Inspect parameters |
| Check Extraction Success | `if` | Inspect parameters |
| Process Patents | `executeCommand` | Inspect parameters |
| Log: Processing Complete | `executeCommand` | Inspect parameters |
| Read Processed Data | `readBinaryFile` | Inspect parameters |
| Read Metrics | `readBinaryFile` | Inspect parameters |
| Log: Results Loaded | `executeCommand` | Inspect parameters |
| Send Report Email | `emailSend` | Inspect parameters |
| Cleanup and Save Data | `executeCommand` | Inspect parameters |
| Log Completion | `executeCommand` | Inspect parameters |
| Error Notification | `emailSend` | Inspect parameters |
| Log Error | `executeCommand` | Inspect parameters |
| Cleanup Repository Error | `executeCommand` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |

## Connection map

- Set Variables → Initialize Logging (`main`, output 0, input 0)
- Initialize Logging → Setup Github Repo (`main`, output 0, input 0)
- Setup Github Repo → Log: Repo Cloned (`main`, output 0, input 0)
- Log: Repo Cloned → Set Path Variables (`main`, output 0, input 0)
- Set Path Variables → Setup Environment and Output Directories (`main`, output 0, input 0)
- Set Path Variables → Extract Patents (`main`, output 0, input 0)
- Setup Environment and Output Directories → Log: Environment Setup (`main`, output 0, input 0)
- Extract Patents → Log: Patents Extracted (`main`, output 0, input 0)
- Log: Patents Extracted → Check Extraction Success (`main`, output 0, input 0)
- Check Extraction Success → Process Patents (`main`, output 0, input 0)
- Check Extraction Success → Error Notification (`main`, output 1, input 0)
- Process Patents → Log: Processing Complete (`main`, output 0, input 0)
- Log: Processing Complete → Read Metrics (`main`, output 0, input 0)
- Read Processed Data → Log: Results Loaded (`main`, output 0, input 0)
- Read Metrics → Read Processed Data (`main`, output 0, input 0)
- Log: Results Loaded → Send Report Email (`main`, output 0, input 0)
- Send Report Email → Cleanup and Save Data (`main`, output 0, input 0)
- Cleanup and Save Data → Log Completion (`main`, output 0, input 0)
- Error Notification → Log Error (`main`, output 0, input 0)
- Log Error → Cleanup Repository Error (`main`, output 0, input 0)
- Webhook → Set Variables (`main`, output 0, input 0)
- Log Completion → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
