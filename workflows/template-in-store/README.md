# template in store

This folder contains the **template in store** workflow. Its executable nodes use `errorTrigger`, `googleDrive`, `googleDriveTrigger`, `httpRequest`, `if`, `openAi`, `readBinaryFile`, `telegram`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`template-in-store.json`](template-in-store.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Google Drive Trigger, Error Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Drive Trigger | `googleDriveTrigger` | Inspect parameters |
| Google Drive | `googleDrive` | download |
| Error Trigger | `errorTrigger` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| If | `if` | Inspect parameters |
| Get Audio from Video | `openAi` | audio / transcribe |
| Read video from Google Drive | `writeBinaryFile` | Inspect parameters |
| Generate Description for Videos in Tiktok and Instagram | `openAi` | Inspect parameters |
| Read Video from Google Drive | `readBinaryFile` | Inspect parameters |
| Read Video from Google Drive2 | `readBinaryFile` | Inspect parameters |
| Upload Video and Description to Tiktok | `httpRequest` | POST |
| Upload Video and Description to Instagram | `httpRequest` | POST |

## Connection map

- If → Telegram (`main`, output 0, input 0)
- Google Drive → Read video from Google Drive (`main`, output 0, input 0)
- Error Trigger → If (`main`, output 0, input 0)
- Get Audio from Video → Generate Description for Videos in Tiktok and Instagram (`main`, output 0, input 0)
- Google Drive Trigger → Google Drive (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Tiktok (`main`, output 0, input 0)
- Read video from Google Drive → Get Audio from Video (`main`, output 0, input 0)
- Read Video from Google Drive2 → Upload Video and Description to Instagram (`main`, output 0, input 0)
- Generate Description for Videos in Tiktok and Instagram → Read Video from Google Drive (`main`, output 0, input 0)
- Generate Description for Videos in Tiktok and Instagram → Read Video from Google Drive2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1715_Error_Telegram_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Error/1715_Error_Telegram_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
