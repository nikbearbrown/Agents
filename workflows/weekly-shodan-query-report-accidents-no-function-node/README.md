# Weekly_Shodan_Query___Report_Accidents__no_function_node_

This folder contains the **Weekly_Shodan_Query___Report_Accidents__no_function_node_** workflow. Its executable nodes use `filter`, `html`, `httpRequest`, `itemLists`, `markdown`, `scheduleTrigger`, `set`, `splitInBatches`, `theHive`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`weekly-shodan-query-report-accidents-no-function-node.json`](weekly-shodan-query-report-accidents-no-function-node.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpQueryAuth`, `theHiveApi`

**Entry nodes:** Every Monday

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Scan each IP | `httpRequest` | Inspect parameters |
| Get watched IPs & Ports | `httpRequest` | Inspect parameters |
| Split out services | `itemLists` | Inspect parameters |
| Unexpected port? | `filter` | Inspect parameters |
| Set data to post for each port | `set` | Inspect parameters |
| Convert to table | `html` | convertToHtmlTable |
| Convert to Markdown | `markdown` | Inspect parameters |
| For each IP | `splitInBatches` | Inspect parameters |
| Every Monday | `scheduleTrigger` | Inspect parameters |
| Create TheHive alert | `theHive` | Inspect parameters |

## Connection map

- For each IP → Scan each IP (`main`, output 0, input 0)
- Every Monday → Get watched IPs & Ports (`main`, output 0, input 0)
- Scan each IP → Split out services (`main`, output 0, input 0)
- Convert to table → Convert to Markdown (`main`, output 0, input 0)
- Unexpected port? → Set data to post for each port (`main`, output 0, input 0)
- Split out services → Unexpected port? (`main`, output 0, input 0)
- Convert to Markdown → Create TheHive alert (`main`, output 0, input 0)
- Create TheHive alert → For each IP (`main`, output 0, input 0)
- Get watched IPs & Ports → For each IP (`main`, output 0, input 0)
- Set data to post for each port → Convert to table (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1751_Filter_Schedule_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1751_Filter_Schedule_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
