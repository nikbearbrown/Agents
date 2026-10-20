# PG&E Daily Cost Tracker

This folder contains the **PG&E Daily Cost Tracker** workflow. Its executable nodes use `airtop`, `gmail`, `scheduleTrigger`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pg-e-daily-cost-tracker.json`](pg-e-daily-cost-tracker.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Type password | `airtop` | interaction / type |
| Variables | `set` | Inspect parameters |
| Go to "Energy Costs" | `airtop` | interaction |
| Go to "Electricity and Gas" | `airtop` | interaction |
| Extract Costs | `airtop` | extraction / query |
| Go to "Energy Usage Details" | `airtop` | interaction |
| Wait 5 secs | `wait` | Inspect parameters |
| Close modal (if any) | `airtop` | interaction |
| Create session | `airtop` | Inspect parameters |
| Create browser window | `airtop` | window |
| Type username | `airtop` | interaction / type |
| Send email | `gmail` | Inspect parameters |
| End session | `airtop` | terminate |

## Connection map

- Variables → Create session (`main`, output 0, input 0)
- Wait 5 secs → Go to "Energy Usage Details" (`main`, output 0, input 0)
- Extract Costs → End session (`main`, output 0, input 0)
- Extract Costs → Send email (`main`, output 0, input 0)
- Type password → Close modal (if any) (`main`, output 0, input 0)
- Type username → Type password (`main`, output 0, input 0)
- Create session → Create browser window (`main`, output 0, input 0)
- Schedule Trigger → Variables (`main`, output 0, input 0)
- Close modal (if any) → Wait 5 secs (`main`, output 0, input 0)
- Go to "Energy Costs" → Go to "Electricity and Gas" (`main`, output 0, input 0)
- Create browser window → Type username (`main`, output 0, input 0)
- Go to "Electricity and Gas" → Extract Costs (`main`, output 0, input 0)
- Go to "Energy Usage Details" → Go to "Energy Costs" (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1563_Wait_Schedule_Monitor_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1563_Wait_Schedule_Monitor_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
