# Keep discord clean

This folder contains the **Keep discord clean** workflow. Its executable nodes use `discord`, `filter`, `scheduleTrigger`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`keep-discord-clean.json`](keep-discord-clean.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Every day at 9pm

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Channels | `splitInBatches` | Inspect parameters |
| Loop Over Messages | `splitInBatches` | Inspect parameters |
| Every day at 9pm | `scheduleTrigger` | Inspect parameters |
| Cool down Discord API rate limits | `wait` | Inspect parameters |
| Get all Discord channels | `discord` | getAll |
| Cool down Message deletion API rate limits | `wait` | Inspect parameters |
| Cool down Get messages API rate limits | `wait` | Inspect parameters |
| Get messages from Channel | `discord` | message / getAll |
| Delete Message | `discord` | message / deleteMessage |
| Filter Messages older than 7 days | `filter` | Inspect parameters |

## Connection map

- Delete Message → Cool down Message deletion API rate limits (`main`, output 0, input 0)
- Every day at 9pm → Get all Discord channels (`main`, output 0, input 0)
- Loop Over Channels → Filter Messages older than 7 days (`main`, output 0, input 0)
- Loop Over Channels → Get messages from Channel (`main`, output 1, input 0)
- Loop Over Messages → Delete Message (`main`, output 1, input 0)
- Get all Discord channels → Cool down Discord API rate limits (`main`, output 0, input 0)
- Get messages from Channel → Cool down Get messages API rate limits (`main`, output 0, input 0)
- Cool down Discord API rate limits → Loop Over Channels (`main`, output 0, input 0)
- Filter Messages older than 7 days → Loop Over Messages (`main`, output 0, input 0)
- Cool down Get messages API rate limits → Loop Over Channels (`main`, output 0, input 0)
- Cool down Message deletion API rate limits → Loop Over Messages (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1609_Wait_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1609_Wait_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
