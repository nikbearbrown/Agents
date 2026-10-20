# list gmail and split out and extract news items

This folder contains the **list gmail and split out and extract news items** workflow. Its executable nodes use `gmail`, `linkedIn`, `manualTrigger`, `openAi`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-gmail-and-split-out-and-extract-news-items.json`](list-gmail-and-split-out-and-extract-news-items.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `linkedInOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Gmail | `gmail` | getAll |
| Split Out | `splitOut` | Inspect parameters |
| Extract News Items | `openAi` | Inspect parameters |
| Create LinkedIn Posts | `openAi` | Inspect parameters |
| LinkedIn | `linkedIn` | Inspect parameters |

## Connection map

- Gmail → Extract News Items (`main`, output 0, input 0)
- Split Out → Create LinkedIn Posts (`main`, output 0, input 0)
- Extract News Items → Split Out (`main`, output 0, input 0)
- Create LinkedIn Posts → LinkedIn (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Gmail (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/0847_Linkedin_Splitout_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/0847_Linkedin_Splitout_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
