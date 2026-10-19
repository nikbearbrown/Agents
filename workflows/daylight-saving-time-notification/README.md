# Daylight Saving Time Notification

This folder contains the **Daylight Saving Time Notification** workflow. Its executable nodes use `code`, `dateTime`, `emailSend`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `slack`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`daylight-saving-time-notification.json`](daylight-saving-time-notification.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `slackOAuth2Api`, `smtp`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Timezones List | `code` | Inspect parameters |
| Calculate Zone Date and Time | `set` | Inspect parameters |
| Check If Daylight Saving Time | `set` | Inspect parameters |
| Check If Change Tomorrow | `if` | Inspect parameters |
| Send Notification On Upcoming Change | `slack` | Inspect parameters |
| Calculate Tomorrow's Date | `dateTime` | addToDate |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Send Email On Upcoming Change | `emailSend` | Inspect parameters |

## Connection map

- Timezones List → Calculate Zone Date and Time (`main`, output 0, input 0)
- Schedule Trigger → Timezones List (`main`, output 0, input 0)
- Check If Change Tomorrow → Send Notification On Upcoming Change (`main`, output 0, input 0)
- Check If Change Tomorrow → Send Email On Upcoming Change (`main`, output 0, input 0)
- Calculate Tomorrow's Date → Check If Daylight Saving Time (`main`, output 0, input 0)
- Calculate Zone Date and Time → Calculate Tomorrow's Date (`main`, output 0, input 0)
- Check If Daylight Saving Time → Check If Change Tomorrow (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Timezones List (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1523_Datetime_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Datetime/1523_Datetime_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
