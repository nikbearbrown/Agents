# Age and number of the news

This folder contains the **Age and number of the news** workflow. Its executable nodes use `code`, `filter`, `gmail`, `limit`, `merge`, `rssFeedRead`, `scheduleTrigger`, `set`, `sort`, `trello`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`age-and-number-of-the-news.json`](age-and-number-of-the-news.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `trelloApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| RSS Read Testing Catalog | `rssFeedRead` | Inspect parameters |
| Transform date | `set` | Inspect parameters |
| Filter by date (more than 7 days) | `filter` | Inspect parameters |
| Sort by date | `sort` | Inspect parameters |
| Limit news to x | `limit` | Inspect parameters |
| Transform new to MD | `code` | Inspect parameters |
| Publish comment | `trello` | cardComment |
| Send revision email | `gmail` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| RSS Read marktechpost | `rssFeedRead` | Inspect parameters |
| RSS Read | `rssFeedRead` | Inspect parameters |

## Connection map

- Merge → Transform date (`main`, output 0, input 0)
- RSS Read → Merge (`main`, output 0, input 0)
- Sort by date → Limit news to x (`main`, output 0, input 0)
- Transform date → Filter by date (more than 7 days) (`main`, output 0, input 0)
- Limit news to x → Transform new to MD (`main`, output 0, input 0)
- Publish comment → Send revision email (`main`, output 0, input 0)
- Schedule Trigger → RSS Read Testing Catalog (`main`, output 0, input 0)
- Schedule Trigger → RSS Read marktechpost (`main`, output 0, input 0)
- Schedule Trigger → RSS Read (`main`, output 0, input 0)
- Transform new to MD → Publish comment (`main`, output 0, input 0)
- RSS Read marktechpost → Merge (`main`, output 0, input 1)
- RSS Read Testing Catalog → Merge (`main`, output 0, input 2)
- Filter by date (more than 7 days) → Sort by date (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/1302_Trello_Limit_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Trello/1302_Trello_Limit_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
