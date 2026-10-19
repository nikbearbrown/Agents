# News Extraction

This folder contains the **News Extraction** workflow. Its executable nodes use `code`, `html`, `httpRequest`, `itemLists`, `merge`, `nocoDb`, `openAi`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`news-extraction.json`](news-extraction.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `nocoDbApiToken`, `openAiApi`

**Entry nodes:** Schedule Trigger each week

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract the HTML with the right css class | `html` | extractHtmlContent |
| Summary | `openAi` | chat |
| Keywords | `openAi` | chat |
| Rename keywords | `set` | Inspect parameters |
| Rename Summary | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Extract date | `html` | extractHtmlContent |
| Select posts of last 7 days | `code` | Inspect parameters |
| Merge date & links | `merge` | Inspect parameters |
| HTTP Request1 | `httpRequest` | Inspect parameters |
| Merge Content with Date & Link | `merge` | Inspect parameters |
| Extract individual posts | `html` | extractHtmlContent |
| Merge ChatGPT output with Date & Link | `merge` | Inspect parameters |
| Retrieve the web page for further processsing | `httpRequest` | Inspect parameters |
| Schedule Trigger each week | `scheduleTrigger` | Inspect parameters |
| NocoDB news database | `nocoDb` | create |
| Create single link items | `itemLists` | Inspect parameters |
| Create single date items | `itemLists` | Inspect parameters |

## Connection map

- Merge → Merge ChatGPT output with Date & Link (`main`, output 0, input 1)
- Summary → Rename Summary (`main`, output 0, input 0)
- Keywords → Rename keywords (`main`, output 0, input 0)
- Extract date → Create single date items (`main`, output 0, input 0)
- HTTP Request1 → Extract individual posts (`main`, output 0, input 0)
- Rename Summary → Merge (`main`, output 0, input 0)
- Rename keywords → Merge (`main`, output 0, input 1)
- Merge date & links → Select posts of last 7 days (`main`, output 0, input 0)
- Create single date items → Merge date & links (`main`, output 0, input 0)
- Create single link items → Merge date & links (`main`, output 0, input 1)
- Extract individual posts → Merge Content with Date & Link (`main`, output 0, input 0)
- Schedule Trigger each week → Retrieve the web page for further processsing (`main`, output 0, input 0)
- Select posts of last 7 days → Merge Content with Date & Link (`main`, output 0, input 1)
- Select posts of last 7 days → HTTP Request1 (`main`, output 0, input 0)
- Merge Content with Date & Link → Summary (`main`, output 0, input 0)
- Merge Content with Date & Link → Keywords (`main`, output 0, input 0)
- Merge Content with Date & Link → Merge ChatGPT output with Date & Link (`main`, output 0, input 0)
- Merge ChatGPT output with Date & Link → NocoDB news database (`main`, output 0, input 0)
- Extract the HTML with the right css class → Create single link items (`main`, output 0, input 0)
- Retrieve the web page for further processsing → Extract the HTML with the right css class (`main`, output 0, input 0)
- Retrieve the web page for further processsing → Extract date (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1646_Code_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1646_Code_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
