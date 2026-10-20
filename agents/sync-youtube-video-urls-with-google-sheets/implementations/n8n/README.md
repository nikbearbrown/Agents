# Sync Youtube Video Urls with Google Sheets

This folder contains the **Sync Youtube Video Urls with Google Sheets** workflow. Its executable nodes use `googleSheets`, `httpRequest`, `manualTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sync-youtube-video-urls-with-google-sheets.json`](sync-youtube-video-urls-with-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpQueryAuth`

**Entry nodes:** Manual Trigger (When Clicking 'Test workflow'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Manual Trigger (When Clicking 'Test workflow' | `manualTrigger` | Inspect parameters |
| Get Youtube Channel Ids from Google Sheet | `googleSheets` | Inspect parameters |
| Get Youtube Video Urls form specific channel | `httpRequest` | Inspect parameters |
| Format fields as required to save in google sheet | `set` | Inspect parameters |
| Insert & Update Youtube Urls in Google Sheet | `googleSheets` | appendOrUpdate |

## Connection map

- Split Out → Format fields as required to save in google sheet (`main`, output 0, input 0)
- Get Youtube Channel Ids from Google Sheet → Get Youtube Video Urls form specific channel (`main`, output 0, input 0)
- Get Youtube Video Urls form specific channel → Split Out (`main`, output 0, input 0)
- Manual Trigger (When Clicking 'Test workflow' → Get Youtube Channel Ids from Google Sheet (`main`, output 0, input 0)
- Format fields as required to save in google sheet → Insert & Update Youtube Urls in Google Sheet (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1970_Splitout_Manual_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1970_Splitout_Manual_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
