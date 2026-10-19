# Query List of Sign-in IPs

This folder contains the **Query List of Sign-in IPs** workflow. Its executable nodes use `convertToFile`, `formTrigger`, `httpRequest`, `merge`, `moveBinaryData`, `removeDuplicates`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`query-list-of-sign-in-ips.json`](query-list-of-sign-in-ips.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`

**Entry nodes:** Authentication Request Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| GET Events - Login Successful | `httpRequest` | Inspect parameters |
| Send Email Upon Completion (SMTP2Go) | `httpRequest` | POST |
| Remove Duplicate IPs | `removeDuplicates` | Inspect parameters |
| Convert CSV to Base64 | `moveBinaryData` | Inspect parameters |
| Convert to CSV | `convertToFile` | Inspect parameters |
| Filter IP Information | `set` | Inspect parameters |
| Combine all Authentication Events | `merge` | Inspect parameters |
| GET Events - OAuth Authentication | `httpRequest` | Inspect parameters |
| GET Events - Office365 Shell WCSS | `httpRequest` | Inspect parameters |
| Set Date and Form Variables | `set` | Inspect parameters |
| Authentication Request Form | `formTrigger` | Inspect parameters |

## Connection map

- Convert to CSV → Convert CSV to Base64 (`main`, output 0, input 0)
- Remove Duplicate IPs → Convert to CSV (`main`, output 0, input 0)
- Convert CSV to Base64 → Send Email Upon Completion (SMTP2Go) (`main`, output 0, input 0)
- Filter IP Information → Remove Duplicate IPs (`main`, output 0, input 0)
- Authentication Request Form → Set Date and Form Variables (`main`, output 0, input 0)
- Set Date and Form Variables → GET Events - Login Successful (`main`, output 0, input 0)
- Set Date and Form Variables → GET Events - OAuth Authentication (`main`, output 0, input 0)
- Set Date and Form Variables → GET Events - Office365 Shell WCSS (`main`, output 0, input 0)
- GET Events - Login Successful → Combine all Authentication Events (`main`, output 0, input 2)
- Combine all Authentication Events → Filter IP Information (`main`, output 0, input 0)
- GET Events - OAuth Authentication → Combine all Authentication Events (`main`, output 0, input 1)
- GET Events - Office365 Shell WCSS → Combine all Authentication Events (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Removeduplicates/1854_Removeduplicates_Converttofile_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Removeduplicates/1854_Removeduplicates_Converttofile_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
