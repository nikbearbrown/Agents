# Amazon keywords

This folder contains the **Amazon keywords** workflow. Its executable nodes use `aggregate`, `airtable`, `code`, `httpRequest`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`amazon-keywords.json`](amazon-keywords.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`

**Entry nodes:** Receive Keyword

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Clean Keywords | `set` | Inspect parameters |
| Get airtable data | `airtable` | Inspect parameters |
| Get Amazon keywords | `httpRequest` | Inspect parameters |
| Format output | `splitOut` | Inspect parameters |
| Aggregate keywords | `aggregate` | Inspect parameters |
| Combine into string | `code` | Inspect parameters |
| Save keywords | `airtable` | update |
| Receive Keyword | `webhook` | Inspect parameters |

## Connection map

- Format output → Clean Keywords (`main`, output 0, input 0)
- Clean Keywords → Aggregate keywords (`main`, output 0, input 0)
- Receive Keyword → Get airtable data (`main`, output 0, input 0)
- Get airtable data → Get Amazon keywords (`main`, output 0, input 0)
- Aggregate keywords → Combine into string (`main`, output 0, input 0)
- Combine into string → Save keywords (`main`, output 0, input 0)
- Get Amazon keywords → Format output (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1898_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1898_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
