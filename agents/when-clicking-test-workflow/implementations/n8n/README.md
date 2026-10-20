# when clicking test workflow

This folder contains the **when clicking test workflow** workflow. Its executable nodes use `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`when-clicking-test-workflow.json`](when-clicking-test-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `httpHeaderAuth`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set Params | `set` | Inspect parameters |
| Clean Output | `set` | Inspect parameters |
| Perplexity Request | `httpRequest` | POST |

## Connection map

- Set Params → Perplexity Request (`main`, output 0, input 0)
- Perplexity Request → Clean Output (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Params (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0710_Manual_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0710_Manual_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `when-clicking-test-workflow-abe079dd` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
