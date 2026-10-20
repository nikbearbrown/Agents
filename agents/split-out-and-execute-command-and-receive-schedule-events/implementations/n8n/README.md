# split out and execute command and receive schedule events

This folder contains the **split out and execute command and receive schedule events** workflow. Its executable nodes use `executeCommand`, `manualTrigger`, `n8nTrigger`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`split-out-and-execute-command-and-receive-schedule-events.json`](split-out-and-execute-command-and-receive-schedule-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** trigger_manual, trigger_schedule, trigger_instance

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| libraries_set | `set` | Inspect parameters |
| trigger_manual | `manualTrigger` | Inspect parameters |
| libraries_array | `set` | Inspect parameters |
| libraries_split | `splitOut` | Inspect parameters |
| library_install | `executeCommand` | Inspect parameters |
| trigger_schedule | `scheduleTrigger` | Inspect parameters |
| trigger_instance | `n8nTrigger` | Inspect parameters |

## Connection map

- libraries_set → libraries_array (`main`, output 0, input 0)
- trigger_manual → libraries_set (`main`, output 0, input 0)
- libraries_array → libraries_split (`main`, output 0, input 0)
- libraries_split → library_install (`main`, output 0, input 0)
- trigger_instance → libraries_set (`main`, output 0, input 0)
- trigger_schedule → libraries_set (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0799_Splitout_Executecommand_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0799_Splitout_Executecommand_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
