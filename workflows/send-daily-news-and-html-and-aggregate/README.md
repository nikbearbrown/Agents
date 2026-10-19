# send daily news and html and aggregate

This folder contains the **send daily news and html and aggregate** workflow. Its executable nodes use `aggregate`, `code`, `emailSend`, `filter`, `function`, `html`, `httpRequest`, `merge`, `openAi`, `rssFeedRead`, `scheduleTrigger`, `set`, `sort`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-daily-news-and-html-and-aggregate.json`](send-daily-news-and-html-and-aggregate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `smtp`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Send Daily News | `emailSend` | Inspect parameters |
| Get Date | `function` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Create HTML | `html` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Clean Text | `set` | Inspect parameters |
| Extract Text | `html` | extractHtmlContent |
| Fetch HTML | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| ChatGPT 4o | `openAi` | Inspect parameters |
| Clean List | `code` | Inspect parameters |
| Sort List | `sort` | Inspect parameters |
| Remove NaN | `filter` | Inspect parameters |
| Merged RSS | `merge` | Inspect parameters |
| Edit Fields - Mako | `set` | Inspect parameters |
| Edit Fields - Calcalist | `set` | Inspect parameters |
| RSS - Calcalist | `rssFeedRead` | Inspect parameters |
| RSS - Mako | `rssFeedRead` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |

## Connection map

- Merge → Send Daily News (`main`, output 0, input 0)
- Get Date → Merge (`main`, output 0, input 1)
- Aggregate → Create HTML (`main`, output 0, input 0)
- Sort List → Clean List (`main`, output 0, input 0)
- Split Out → Fetch HTML (`main`, output 0, input 0)
- ChatGPT 4o → Split Out (`main`, output 0, input 0)
- Clean List → ChatGPT 4o (`main`, output 0, input 0)
- Clean Text → Aggregate (`main`, output 0, input 0)
- Fetch HTML → Extract Text (`main`, output 0, input 0)
- Merged RSS → Remove NaN (`main`, output 0, input 0)
- RSS - Mako → Edit Fields - Mako (`main`, output 0, input 0)
- Remove NaN → Sort List (`main`, output 0, input 0)
- Create HTML → Merge (`main`, output 0, input 0)
- Extract Text → Clean Text (`main`, output 0, input 0)
- RSS - Calcalist → Edit Fields - Calcalist (`main`, output 0, input 0)
- Schedule Trigger → RSS - Mako (`main`, output 0, input 0)
- Schedule Trigger → Get Date (`main`, output 0, input 0)
- Schedule Trigger → RSS - Calcalist (`main`, output 0, input 0)
- Edit Fields - Mako → Merged RSS (`main`, output 0, input 0)
- Edit Fields - Calcalist → Merged RSS (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0859_Splitout_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0859_Splitout_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
