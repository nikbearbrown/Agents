# YT AI News Playlist Creator/AI News Form Updater

This folder contains the **YT AI News Playlist Creator/AI News Form Updater** workflow. Its executable nodes use `filter`, `googleSheets`, `httpRequest`, `manualTrigger`, `scheduleTrigger`, `splitOut`, `telegram`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`yt-ai-news-playlist-creator-ai-news-form-updater.json`](yt-ai-news-playlist-creator-ai-news-form-updater.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `telegramApi`, `youTubeOAuth2Api`

**Entry nodes:** 0715 Trigger, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Read Channel Names | `googleSheets` | Inspect parameters |
| Get Videos | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Create Playlist | `youTube` | playlist / create |
| Delete Old Playlist | `youTube` | playlist / delete |
| YouTube | `youTube` | playlistItem |
| Filter Out Upcoming | `filter` | Inspect parameters |
| Save Playlist ID | `googleSheets` | update |
| Google Sheets | `googleSheets` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| 0715 Trigger | `scheduleTrigger` | Inspect parameters |
| Get Channels | `httpRequest` | Inspect parameters |
| Update Google Sheet | `googleSheets` | update |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Read Channel Names1 | `googleSheets` | Inspect parameters |

## Connection map

- YouTube → Telegram (`main`, output 0, input 0)
- Split Out → Filter Out Upcoming (`main`, output 0, input 0)
- Get Videos → Split Out (`main`, output 0, input 0)
- 0715 Trigger → Create Playlist (`main`, output 0, input 0)
- 0715 Trigger → Google Sheets (`main`, output 0, input 0)
- Get Channels → Update Google Sheet (`main`, output 0, input 0)
- Google Sheets → Delete Old Playlist (`main`, output 0, input 0)
- Create Playlist → Save Playlist ID (`main`, output 0, input 0)
- Save Playlist ID → Read Channel Names (`main`, output 0, input 0)
- Read Channel Names → Get Videos (`main`, output 0, input 0)
- Filter Out Upcoming → YouTube (`main`, output 0, input 0)
- Read Channel Names1 → Get Channels (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Read Channel Names1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0742_Telegram_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0742_Telegram_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
