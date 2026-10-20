# Get Gong Transcript and Call Details

This folder contains the **Get Gong Transcript and Call Details** workflow. Its executable nodes use `executeWorkflow`, `gong`, `if`, `manualTrigger`, `salesforce`, `scheduleTrigger`, `set`, `sort`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-gong-transcript-and-call-details.json`](get-gong-transcript-and-call-details.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gongApi`, `salesforceOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Run Hourly

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Check if Primary Opportunity Contains Value | `if` | Inspect parameters |
| Check if Opportunity Stage is Meeting Booked or Discovery | `if` | Inspect parameters |
| Format call into correct JSON Object | `set` | Inspect parameters |
| Pass to Gong Call Preprocessor | `executeWorkflow` | Inspect parameters |
| Get Gong Call | `gong` | get |
| Sort by date | `sort` | Inspect parameters |
| Get all custom Salesforce Gong Objects | `salesforce` | customObject / getAll |
| Run Hourly | `scheduleTrigger` | Inspect parameters |

## Connection map

- Run Hourly → Get all custom Salesforce Gong Objects (`main`, output 0, input 0)
- Sort by date → Check if Opportunity Stage is Meeting Booked or Discovery (`main`, output 0, input 0)
- Get Gong Call → Format call into correct JSON Object (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all custom Salesforce Gong Objects (`main`, output 0, input 0)
- Format call into correct JSON Object → Pass to Gong Call Preprocessor (`main`, output 0, input 0)
- Get all custom Salesforce Gong Objects → Sort by date (`main`, output 0, input 0)
- Check if Primary Opportunity Contains Value → Get Gong Call (`main`, output 0, input 0)
- Check if Opportunity Stage is Meeting Booked or Discovery → Check if Primary Opportunity Contains Value (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0758_Schedule_Manual_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0758_Schedule_Manual_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
