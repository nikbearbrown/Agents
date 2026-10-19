# search reddit and edit open ai and open ai 652cede2

This folder contains the **search reddit and edit open ai and open ai 652cede2** workflow. Its executable nodes use `if`, `manualTrigger`, `merge`, `openAi`, `reddit`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-reddit-and-edit-open-ai-and-open-ai-652cede2.json`](search-reddit-and-edit-open-ai-and-open-ai-652cede2.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking "Execute Workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| Reddit | `reddit` | search |
| Set | `set` | Inspect parameters |
| IF | `if` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| SetFinal | `set` | Inspect parameters |
| OpenAI Summary | `openAi` | edit |
| OpenAI Classify | `openAi` | Inspect parameters |
| OpenAI Summary Backup | `openAi` | Inspect parameters |

## Connection map

- IF → Set (`main`, output 0, input 0)
- IF1 → OpenAI Summary Backup (`main`, output 1, input 0)
- IF1 → Merge1 (`main`, output 1, input 1)
- Set → OpenAI Classify (`main`, output 0, input 0)
- Set → Merge (`main`, output 0, input 1)
- Merge → IF1 (`main`, output 0, input 0)
- Merge1 → SetFinal (`main`, output 0, input 0)
- Reddit → IF (`main`, output 0, input 0)
- OpenAI Classify → Merge (`main`, output 0, input 0)
- OpenAI Summary Backup → Merge1 (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Reddit (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1636_Manual_Openai_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1636_Manual_Openai_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
