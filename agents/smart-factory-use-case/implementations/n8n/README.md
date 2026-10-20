# Smart Factory Use Case

This folder contains the **Smart Factory Use Case** workflow. Its executable nodes use `amqpTrigger`, `crateDb`, `function`, `if`, `noOp`, `pagerDuty`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`smart-factory-use-case.json`](smart-factory-use-case.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `amqp`, `crateDb`, `pagerDutyApi`

**Entry nodes:** Data from factory sensors

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Values higher than 50°C | `if` | Inspect parameters |
| Data from factory sensors | `amqpTrigger` | Inspect parameters |
| Set sensor data | `set` | Inspect parameters |
| Ingest machine data | `crateDb` | Inspect parameters |
| Ingest incident data | `crateDb` | Inspect parameters |
| Set incident info | `set` | Inspect parameters |
| Create an incident | `pagerDuty` | Inspect parameters |
| Data enrichment (°C to °F) | `function` | Inspect parameters |
| Do  nothing | `noOp` | Inspect parameters |

## Connection map

- Set sensor data → Ingest machine data (`main`, output 0, input 0)
- Set incident info → Ingest incident data (`main`, output 0, input 0)
- Create an incident → Set incident info (`main`, output 0, input 0)
- Values higher than 50°C → Create an incident (`main`, output 0, input 0)
- Values higher than 50°C → Do  nothing (`main`, output 1, input 0)
- Data from factory sensors → Data enrichment (°C to °F) (`main`, output 0, input 0)
- Data from factory sensors → Values higher than 50°C (`main`, output 0, input 0)
- Data enrichment (°C to °F) → Set sensor data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0212_Noop_Cratedb_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0212_Noop_Cratedb_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
