# Latest company news before a call

This folder contains the **Latest company news before a call** workflow. Its executable nodes use `code`, `gmail`, `googleCalendar`, `httpRequest`, `if`, `noOp`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`latest-company-news-before-a-call.json`](latest-company-news-before-a-call.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`

**Entry nodes:** Every morning @ 7

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Setup | `set` | Inspect parameters |
| Extract company name | `set` | Inspect parameters |
| Every morning @ 7 | `scheduleTrigger` | Inspect parameters |
| Filter meetings | `if` | Inspect parameters |
| Get latest news | `httpRequest` | Inspect parameters |
| Format for email | `code` | Inspect parameters |
| Send news | `gmail` | Inspect parameters |
| No meetings today | `noOp` | Inspect parameters |
| Get meetings for today | `googleCalendar` | getAll |

## Connection map

- Setup → Get meetings for today (`main`, output 0, input 0)
- Filter meetings → Extract company name (`main`, output 0, input 0)
- Filter meetings → No meetings today (`main`, output 1, input 0)
- Get latest news → Format for email (`main`, output 0, input 0)
- Format for email → Send news (`main`, output 0, input 0)
- Every morning @ 7 → Setup (`main`, output 0, input 0)
- Extract company name → Get latest news (`main`, output 0, input 0)
- Get meetings for today → Filter meetings (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0415_Code_GoogleCalendar_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0415_Code_GoogleCalendar_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
