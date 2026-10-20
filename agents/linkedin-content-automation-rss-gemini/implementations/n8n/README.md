# LinkedIn Content Automation (RSS + Gemini)

This folder contains the **LinkedIn Content Automation (RSS + Gemini)** workflow. Its executable nodes use `code`, `filter`, `googleSheets`, `httpRequest`, `merge`, `rssFeedRead`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-content-automation-rss-gemini.json`](linkedin-content-automation-rss-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `queryAuth`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| RSS Feed - TechCrunch | `rssFeedRead` | Inspect parameters |
| RSS Feed - The Verge | `rssFeedRead` | Inspect parameters |
| Merge RSS Feeds | `merge` | Inspect parameters |
| Filter Last 24hrs | `filter` | Inspect parameters |
| Extract Article Data | `set` | Inspect parameters |
| Gemini - Analyze Article | `httpRequest` | POST |
| Parse Analysis | `code` | Inspect parameters |
| Filter Recommended Only | `filter` | Inspect parameters |
| Gemini - Create LinkedIn Post | `httpRequest` | POST |
| Gemini - Suggest Schedule | `httpRequest` | POST |
| Prepare Calendar Entry | `code` | Inspect parameters |
| Add to Content Calendar | `googleSheets` | append |

## Connection map

- Schedule Trigger → RSS Feed - TechCrunch (`main`, output 0, input 0)
- Schedule Trigger → RSS Feed - The Verge (`main`, output 0, input 0)
- RSS Feed - TechCrunch → Merge RSS Feeds (`main`, output 0, input 0)
- RSS Feed - The Verge → Merge RSS Feeds (`main`, output 0, input 1)
- Merge RSS Feeds → Filter Last 24hrs (`main`, output 0, input 0)
- Filter Last 24hrs → Extract Article Data (`main`, output 0, input 0)
- Extract Article Data → Gemini - Analyze Article (`main`, output 0, input 0)
- Gemini - Analyze Article → Parse Analysis (`main`, output 0, input 0)
- Parse Analysis → Filter Recommended Only (`main`, output 0, input 0)
- Filter Recommended Only → Gemini - Create LinkedIn Post (`main`, output 0, input 0)
- Filter Recommended Only → Gemini - Suggest Schedule (`main`, output 0, input 0)
- Gemini - Create LinkedIn Post → Prepare Calendar Entry (`main`, output 0, input 0)
- Gemini - Suggest Schedule → Prepare Calendar Entry (`main`, output 0, input 0)
- Prepare Calendar Entry → Add to Content Calendar (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/skadaai/awesome-n8n-templates/blob/4eabc190bf6fac4073e3e1dcaabf0f72897770eb/li-post.json](https://github.com/skadaai/awesome-n8n-templates/blob/4eabc190bf6fac4073e3e1dcaabf0f72897770eb/li-post.json). License: **MIT**; preserve [the notice](../../../../licenses/skadaai--awesome-n8n-templates.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
