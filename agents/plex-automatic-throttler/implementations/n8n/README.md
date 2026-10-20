# Plex Automatic Throttler

This folder contains the **Plex Automatic Throttler** workflow. Its executable nodes use `httpRequest`, `if`, `noOp`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`plex-automatic-throttler.json`](plex-automatic-throttler.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Resume | `noOp` | Inspect parameters |
| Check if Local | `if` | Inspect parameters |
| Play | `noOp` | Inspect parameters |
| Don't Do Anything | `noOp` | Inspect parameters |
| Pause | `noOp` | Inspect parameters |
| Stop | `noOp` | Inspect parameters |
| Get QB Cookie | `httpRequest` | Inspect parameters |
| Get QB Cookie1 | `httpRequest` | Inspect parameters |
| Global Variables | `set` | Inspect parameters |
| Check Throttle State | `httpRequest` | Inspect parameters |
| Check if Throttled | `if` | Inspect parameters |
| Do Nothing | `noOp` | Inspect parameters |
| Check Throttle State2 | `httpRequest` | Inspect parameters |
| Check if Throttled1 | `if` | Inspect parameters |
| Do Nothing1 | `noOp` | Inspect parameters |
| Throttle Connection | `noOp` | Inspect parameters |
| Resume Downloads | `noOp` | Inspect parameters |
| Disable Throttle | `httpRequest` | Inspect parameters |
| Enable Throttle | `httpRequest` | Inspect parameters |

## Connection map

- Play → Throttle Connection (`main`, output 0, input 0)
- Stop → Resume Downloads (`main`, output 0, input 0)
- Pause → Resume Downloads (`main`, output 0, input 0)
- Resume → Throttle Connection (`main`, output 0, input 0)
- Switch → Resume (`main`, output 0, input 0)
- Switch → Play (`main`, output 1, input 0)
- Switch → Pause (`main`, output 2, input 0)
- Switch → Stop (`main`, output 3, input 0)
- Webhook → Global Variables (`main`, output 0, input 0)
- Get QB Cookie → Check Throttle State (`main`, output 0, input 0)
- Check if Local → Don't Do Anything (`main`, output 0, input 0)
- Check if Local → Switch (`main`, output 1, input 0)
- Get QB Cookie1 → Check Throttle State2 (`main`, output 0, input 0)
- Global Variables → Check if Local (`main`, output 0, input 0)
- Resume Downloads → Get QB Cookie1 (`main`, output 0, input 0)
- Check if Throttled → Do Nothing (`main`, output 0, input 0)
- Check if Throttled → Enable Throttle (`main`, output 1, input 0)
- Check if Throttled1 → Disable Throttle (`main`, output 0, input 0)
- Check if Throttled1 → Do Nothing1 (`main`, output 1, input 0)
- Throttle Connection → Get QB Cookie (`main`, output 0, input 0)
- Check Throttle State → Check if Throttled (`main`, output 0, input 0)
- Check Throttle State2 → Check if Throttled1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0083_Noop_HTTP_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Noop/0083_Noop_HTTP_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
