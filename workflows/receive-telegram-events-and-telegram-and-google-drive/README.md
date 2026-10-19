# receive telegram events and telegram and google drive

This folder contains the **receive telegram events and telegram and google drive** workflow. Its executable nodes use `code`, `gmail`, `googleDrive`, `googleSheets`, `if`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-telegram-and-google-drive.json`](receive-telegram-events-and-telegram-and-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Check State | `switch` | Inspect parameters |
| Clear State | `code` | Inspect parameters |
| addGPS | `telegram` | Inspect parameters |
| Welcome Message | `telegram` | Inspect parameters |
| Command? | `if` | Inspect parameters |
| Store GPS Location | `set` | Inspect parameters |
| addGPS result | `telegram` | Inspect parameters |
| addShipmentNumber | `telegram` | Inspect parameters |
| Shipment Number | `set` | Inspect parameters |
| addShipmentNumber result | `telegram` | Inspect parameters |
| Store Shipment | `code` | Inspect parameters |
| Store GPS | `code` | Inspect parameters |
| Load Workspace Data | `code` | Inspect parameters |
| waitingShipmentNumber | `code` | Inspect parameters |
| waitingGPS | `code` | Inspect parameters |
| Instructions | `telegram` | Inspect parameters |
| waitingPhoto | `code` | Inspect parameters |
| Waiting Conditions | `code` | Inspect parameters |
| addPhoto result | `telegram` | Inspect parameters |
| sendPhoto | `telegram` | Inspect parameters |
| Upload Picture | `googleDrive` | Inspect parameters |
| Save Public Image Link | `code` | Inspect parameters |
| Confirmation Driver | `telegram` | Inspect parameters |
| Distribution Team Confirmation | `gmail` | Inspect parameters |
| Extract FileName | `set` | Inspect parameters |
| Store fileName | `code` | Inspect parameters |
| Get Picture | `telegram` | file |
| Share Picture | `googleDrive` | share |
| Initiate Workflow Data | `code` | Inspect parameters |
| Switch Command | `switch` | Inspect parameters |
| Load Delivery Information | `googleSheets` | append |

## Connection map

- Command? → Switch Command (`main`, output 0, input 0)
- Command? → Waiting Conditions (`main`, output 1, input 0)
- waitingGPS → addGPS (`main`, output 0, input 0)
- Check State → Shipment Number (`main`, output 0, input 0)
- Check State → Store GPS Location (`main`, output 1, input 0)
- Check State → Get Picture (`main`, output 2, input 0)
- Check State → Instructions (`main`, output 3, input 0)
- Get Picture → Upload Picture (`main`, output 0, input 0)
- Get Picture → Extract FileName (`main`, output 0, input 0)
- waitingPhoto → sendPhoto (`main`, output 0, input 0)
- Share Picture → Save Public Image Link (`main`, output 0, input 0)
- Switch Command → waitingShipmentNumber (`main`, output 0, input 0)
- Switch Command → waitingGPS (`main`, output 1, input 0)
- Switch Command → waitingPhoto (`main`, output 2, input 0)
- Switch Command → Load Workspace Data (`main`, output 3, input 0)
- Switch Command → Welcome Message (`main`, output 4, input 0)
- Upload Picture → Share Picture (`main`, output 0, input 0)
- Shipment Number → addShipmentNumber result (`main`, output 0, input 0)
- Shipment Number → Store Shipment (`main`, output 0, input 0)
- Extract FileName → Store fileName (`main`, output 0, input 0)
- Telegram Trigger → Command? (`main`, output 0, input 0)
- Store GPS Location → addGPS result (`main`, output 0, input 0)
- Store GPS Location → Store GPS (`main`, output 0, input 0)
- Waiting Conditions → Check State (`main`, output 0, input 0)
- Load Workspace Data → Load Delivery Information (`main`, output 0, input 0)
- Load Workspace Data → Confirmation Driver (`main`, output 0, input 0)
- Load Workspace Data → Distribution Team Confirmation (`main`, output 0, input 0)
- waitingShipmentNumber → addShipmentNumber (`main`, output 0, input 0)
- Save Public Image Link → addPhoto result (`main`, output 0, input 0)
- Distribution Team Confirmation → Clear State (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0789_Telegram_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0789_Telegram_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
