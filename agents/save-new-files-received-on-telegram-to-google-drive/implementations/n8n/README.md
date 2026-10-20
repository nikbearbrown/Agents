# Save new Files received on Telegram to Google Drive

This folder contains the **Save new Files received on Telegram to Google Drive** workflow. Its executable nodes use `googleDrive`, `if`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`save-new-files-received-on-telegram-to-google-drive.json`](save-new-files-received-on-telegram-to-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `telegramApi`

**Entry nodes:** On new Telegram Message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On new Telegram Message | `telegramTrigger` | Inspect parameters |
| If Message contains a File | `if` | Inspect parameters |
| Upload File to GDrive | `googleDrive` | Inspect parameters |

## Connection map

- On new Telegram Message → If Message contains a File (`main`, output 0, input 0)
- If Message contains a File → Upload File to GDrive (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1797_Telegram_GoogleDrive_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1797_Telegram_GoogleDrive_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
