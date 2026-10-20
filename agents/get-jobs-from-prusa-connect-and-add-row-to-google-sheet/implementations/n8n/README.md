# get jobs from prusa connect and add row to google sheet

This folder contains the **get jobs from prusa connect and add row to google sheet** workflow. Its executable nodes use `function`, `googleSheets`, `httpRequest`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-jobs-from-prusa-connect-and-add-row-to-google-sheet.json`](get-jobs-from-prusa-connect-and-add-row-to-google-sheet.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Jobs from Prusa Connect | `httpRequest` | Inspect parameters |
| Split Jobs | `function` | Inspect parameters |
| Add Row to Google Sheet | `googleSheets` | Inspect parameters |

## Connection map

- Get Jobs from Prusa Connect → Split Jobs (`main`, output 0, input 0)
- Split Jobs → Add Row to Google Sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/devopsmariocom/3D-Sopa/blob/c20a34ebe63911ce07f51e9c2bdbbde75c226e16/jobs.json](https://github.com/devopsmariocom/3D-Sopa/blob/c20a34ebe63911ce07f51e9c2bdbbde75c226e16/jobs.json). License: **MIT**; preserve [the notice](../../../../licenses/devopsmariocom--3D-Sopa.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
