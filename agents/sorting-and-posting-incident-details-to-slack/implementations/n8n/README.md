# Sorting and Posting Incident Details to Slack

This folder contains the **Sorting and Posting Incident Details to Slack** workflow. Its executable nodes use `dateTime`, `if`, `manualTrigger`, `noOp`, `scheduleTrigger`, `serviceNow`, `slack`, `sort`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`sorting-and-posting-incident-details-to-slack.json`](sorting-and-posting-incident-details-to-slack.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `serviceNowBasicApi`, `slackApi`

**Entry nodes:** When clicking ‘Test workflow’, Run Every 5 Minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Run Every 5 Minutes | `scheduleTrigger` | Inspect parameters |
| Get 5 Minute Ago Timestamp | `dateTime` | subtractFromDate |
| Get Incidents from ServiceNow | `serviceNow` | incident / getAll |
| Check if New Incidents | `if` | Inspect parameters |
| Post Error Message if Error with ServiceNow | `slack` | Inspect parameters |
| Sort Incidents in Ascending Order | `sort` | Inspect parameters |
| Post Incident Details to Slack Channel | `slack` | Inspect parameters |
| No Incidents, Do Nothing | `noOp` | Inspect parameters |

## Connection map

- Run Every 5 Minutes → Get 5 Minute Ago Timestamp (`main`, output 0, input 0)
- Check if New Incidents → Sort Incidents in Ascending Order (`main`, output 0, input 0)
- Check if New Incidents → No Incidents, Do Nothing (`main`, output 1, input 0)
- Get 5 Minute Ago Timestamp → Get Incidents from ServiceNow (`main`, output 0, input 0)
- Get Incidents from ServiceNow → Check if New Incidents (`main`, output 0, input 0)
- Get Incidents from ServiceNow → Post Error Message if Error with ServiceNow (`main`, output 1, input 0)
- Sort Incidents in Ascending Order → Post Incident Details to Slack Channel (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get 5 Minute Ago Timestamp (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0682_Datetime_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/0682_Datetime_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
