# Mycroft - Financial Regulatory Intelligence System - Enhanced

This folder contains the **Mycroft - Financial Regulatory Intelligence System - Enhanced** workflow. Its executable nodes use `code`, `emailSend`, `if`, `merge`, `postgres`, `readWriteFile`, `rssFeedRead`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`mycroft-financial-regulatory-intelligence-system-enhanced.json`](mycroft-financial-regulatory-intelligence-system-enhanced.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `postgres`, `smtp`

**Entry nodes:** Schedule Every Day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Federal Register - Securities | `rssFeedRead` | Inspect parameters |
| SEC Press Releases | `rssFeedRead` | Inspect parameters |
| FINRA Enforcement News | `rssFeedRead` | Inspect parameters |
| CFTC Regulations | `rssFeedRead` | Inspect parameters |
| Investment Advisor Rules | `rssFeedRead` | Inspect parameters |
| Merge All Sources | `merge` | Inspect parameters |
| Normalize Data | `code` | Inspect parameters |
| Filter Valid Content | `if` | Inspect parameters |
| Generate HTML Report | `code` | Inspect parameters |
| High Priority Filter | `if` | Inspect parameters |
| Send Email Alert | `emailSend` | Inspect parameters |
| Read/Write Files from Disk | `readWriteFile` | write |
| If | `if` | Inspect parameters |
| Send email | `emailSend` | Inspect parameters |
| Schedule Every Day | `scheduleTrigger` | Inspect parameters |
| Generate Email | `code` | Inspect parameters |
| Mark email sent | `postgres` | executeQuery |
| Keyword Analysis & Urgency Scoring | `code` | Inspect parameters |
| Insert data into DB | `postgres` | executeQuery |
| Prepare Data | `code` | Inspect parameters |
| Code in JavaScript | `code` | Inspect parameters |
| If2 | `if` | Inspect parameters |

## Connection map

- Federal Register - Securities → Merge All Sources (`main`, output 0, input 0)
- SEC Press Releases → Merge All Sources (`main`, output 0, input 1)
- FINRA Enforcement News → Merge All Sources (`main`, output 0, input 2)
- CFTC Regulations → Merge All Sources (`main`, output 0, input 3)
- Investment Advisor Rules → Merge All Sources (`main`, output 0, input 4)
- Merge All Sources → Normalize Data (`main`, output 0, input 0)
- Normalize Data → Filter Valid Content (`main`, output 0, input 0)
- Filter Valid Content → Keyword Analysis & Urgency Scoring (`main`, output 0, input 0)
- High Priority Filter → Generate Email (`main`, output 0, input 0)
- Send Email Alert → Mark email sent (`main`, output 0, input 0)
- Generate HTML Report → Read/Write Files from Disk (`main`, output 0, input 0)
- If → Send Email Alert (`main`, output 1, input 0)
- Schedule Every Day → Federal Register - Securities (`main`, output 0, input 0)
- Schedule Every Day → SEC Press Releases (`main`, output 0, input 0)
- Schedule Every Day → FINRA Enforcement News (`main`, output 0, input 0)
- Schedule Every Day → CFTC Regulations (`main`, output 0, input 0)
- Schedule Every Day → Investment Advisor Rules (`main`, output 0, input 0)
- Generate Email → If (`main`, output 0, input 0)
- Keyword Analysis & Urgency Scoring → Prepare Data (`main`, output 0, input 0)
- Prepare Data → Insert data into DB (`main`, output 0, input 0)
- Insert data into DB → Code in JavaScript (`main`, output 0, input 0)
- Code in JavaScript → If2 (`main`, output 0, input 0)
- If2 → High Priority Filter (`main`, output 0, input 0)
- If2 → Generate HTML Report (`main`, output 0, input 0)
- If2 → Send email (`main`, output 1, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
