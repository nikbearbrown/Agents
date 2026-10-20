# Track Working Time and Pauses

This folder contains the **Track Working Time and Pauses** workflow. Its executable nodes use `if`, `notion`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`track-working-time-and-pauses.json`](track-working-time-and-pauses.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`

**Entry nodes:** Webhook - Track Time

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create new page | `notion` | databasePage |
| Update page with end date | `notion` | databasePage / update |
| If pause_in_minuten is empty | `if` | Inspect parameters |
| If page responded | `if` | Inspect parameters |
| If page exist | `if` | Inspect parameters |
| If page exist1 | `if` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Break Duration | `set` | Inspect parameters |
| Update break duration for current day | `notion` | databasePage / update |
| Set break duration for current day | `notion` | databasePage / update |
| Get notion page by date | `notion` | databasePage / getAll |
| Set Message - End time already tracked | `set` | Inspect parameters |
| Set Message - End time tracked | `set` | Inspect parameters |
| Set Message - Start time not yet tracked | `set` | Inspect parameters |
| Set Message - Start not yet tracked | `set` | Inspect parameters |
| Set Message - Break time tracked | `set` | Inspect parameters |
| Set Message - Break time updated | `set` | Inspect parameters |
| Set Message - Start time already tracked | `set` | Inspect parameters |
| Set Message - Start time already tracked1 | `set` | Inspect parameters |
| Get notion page with todays date | `notion` | databasePage / getAll |
| Switch | `switch` | Inspect parameters |
| Get notion page with todays date1 | `notion` | databasePage / getAll |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Webhook - Track Time | `webhook` | Inspect parameters |

## Connection map

- If → Update page with end date (`main`, output 0, input 0)
- If → Set Message - End time already tracked (`main`, output 1, input 0)
- Switch → Get notion page with todays date (`main`, output 0, input 0)
- Switch → Set Break Duration (`main`, output 1, input 0)
- Switch → Get notion page with todays date1 (`main`, output 2, input 0)
- If page exist → Set Message - Start time already tracked (`main`, output 0, input 0)
- If page exist → Create new page (`main`, output 1, input 0)
- If page exist1 → If (`main`, output 0, input 0)
- If page exist1 → Set Message - Start time not yet tracked (`main`, output 1, input 0)
- Create new page → Set Message - Start time already tracked1 (`main`, output 0, input 0)
- If page responded → If pause_in_minuten is empty (`main`, output 0, input 0)
- If page responded → Set Message - Start not yet tracked (`main`, output 1, input 0)
- Set Break Duration → Get notion page by date (`main`, output 0, input 0)
- Webhook - Track Time → Switch (`main`, output 0, input 0)
- Get notion page by date → If page responded (`main`, output 0, input 0)
- Update page with end date → Set Message - End time tracked (`main`, output 0, input 0)
- If pause_in_minuten is empty → Set break duration for current day (`main`, output 0, input 0)
- If pause_in_minuten is empty → Update break duration for current day (`main`, output 1, input 0)
- Set Message - End time tracked → Respond to Webhook (`main`, output 0, input 0)
- Get notion page with todays date → If page exist (`main`, output 0, input 0)
- Set Message - Break time tracked → Respond to Webhook (`main`, output 0, input 0)
- Set Message - Break time updated → Respond to Webhook (`main`, output 0, input 0)
- Get notion page with todays date1 → If page exist1 (`main`, output 0, input 0)
- Set break duration for current day → Set Message - Break time tracked (`main`, output 0, input 0)
- Set Message - Start not yet tracked → Respond to Webhook (`main`, output 0, input 0)
- Update break duration for current day → Set Message - Break time updated (`main`, output 0, input 0)
- Set Message - End time already tracked → Respond to Webhook (`main`, output 0, input 0)
- Set Message - Start time already tracked → Respond to Webhook (`main`, output 0, input 0)
- Set Message - Start time not yet tracked → Respond to Webhook (`main`, output 0, input 0)
- Set Message - Start time already tracked1 → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/1953_Respondtowebhook_Stickynote_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/1953_Respondtowebhook_Stickynote_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
