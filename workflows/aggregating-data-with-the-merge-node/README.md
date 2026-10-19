# Aggregating data with the Merge node

This folder contains the **Aggregating data with the Merge node** workflow. Its executable nodes use `code`, `manualTrigger`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`aggregating-data-with-the-merge-node.json`](aggregating-data-with-the-merge-node.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Ingredients in stock from recipe | `merge` | Inspect parameters |
| Super Band | `merge` | Inspect parameters |
| A. Ingredients Needed | `code` | Inspect parameters |
| B. Ingredients in stock | `code` | Inspect parameters |
| Merge recipe | `merge` | Inspect parameters |
| A. Ingredients | `code` | Inspect parameters |
| B. Recipe quantities | `code` | Inspect parameters |
| A. Queen | `code` | Inspect parameters |
| B. Led Zeppelin | `code` | Inspect parameters |

## Connection map

- A. Queen → Super Band (`main`, output 0, input 0)
- A. Ingredients → Merge recipe (`main`, output 0, input 0)
- B. Led Zeppelin → Super Band (`main`, output 0, input 1)
- B. Recipe quantities → Merge recipe (`main`, output 0, input 1)
- A. Ingredients Needed → Ingredients in stock from recipe (`main`, output 0, input 0)
- On clicking 'execute' → A. Ingredients Needed (`main`, output 0, input 0)
- On clicking 'execute' → B. Ingredients in stock (`main`, output 0, input 0)
- On clicking 'execute' → A. Ingredients (`main`, output 0, input 0)
- On clicking 'execute' → B. Recipe quantities (`main`, output 0, input 0)
- On clicking 'execute' → A. Queen (`main`, output 0, input 0)
- On clicking 'execute' → B. Led Zeppelin (`main`, output 0, input 0)
- B. Ingredients in stock → Ingredients in stock from recipe (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0228_Manual_Stickynote_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0228_Manual_Stickynote_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
