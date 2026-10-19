# upload ftp and receive schedule events and send zigbee2mqtt backup request

This folder contains the **upload ftp and receive schedule events and send zigbee2mqtt backup request** workflow. Its executable nodes use `code`, `convertToFile`, `ftp`, `mqtt`, `mqttTrigger`, `scheduleTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`upload-ftp-and-receive-schedule-events-and-send-zigbee2mqtt-backup-request.json`](upload-ftp-and-receive-schedule-events-and-send-zigbee2mqtt-backup-request.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mqtt`, `sftp`

**Entry nodes:** CRON Monday 2:45 am, MQTT Trigger - Backup Response

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| SFTP zip file content | `ftp` | upload |
| CRON Monday 2:45 am | `scheduleTrigger` | Inspect parameters |
| Send Zigbee2MQTT backup request | `mqtt` | Inspect parameters |
| MQTT Trigger - Backup Response | `mqttTrigger` | Inspect parameters |
| Parse JSON Object from Message Text | `code` | Inspect parameters |
| Convert to File - base64 to binary | `convertToFile` | toBinary |

## Connection map

- CRON Monday 2:45 am → Send Zigbee2MQTT backup request (`main`, output 0, input 0)
- MQTT Trigger - Backup Response → Parse JSON Object from Message Text (`main`, output 0, input 0)
- Convert to File - base64 to binary → SFTP zip file content (`main`, output 0, input 0)
- Parse JSON Object from Message Text → Convert to File - base64 to binary (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0553_Code_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0553_Code_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
