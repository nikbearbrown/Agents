# Group K

This folder contains the **Group K** workflow. Its executable nodes use `function`, `httpRequest`, `splitInBatches`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-extract-information-from-telegram-and-telegram.json`](receive-telegram-events-and-extract-information-from-telegram-and-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Extract information from Telegram | `httpRequest` | POST |
| Telegram1 | `telegram` | Inspect parameters |
| Scrape user reels | `httpRequest` | POST |
| Split Videos | `function` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Download each reel | `httpRequest` | POST |
| Strip metadata | `httpRequest` | POST |
| Transcribe the video | `httpRequest` | POST |
| Telegram | `telegram` | Inspect parameters |
| Upload to aws | `httpRequest` | POST |

## Connection map

- Telegram Trigger → Extract information from Telegram (`main`, output 0, input 0)
- Extract information from Telegram → Telegram1 (`main`, output 0, input 0)
- Telegram1 → Scrape user reels (`main`, output 0, input 0)
- Scrape user reels → Split Videos (`main`, output 0, input 0)
- Split Videos → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Telegram (`main`, output 0, input 0)
- Loop Over Items → Download each reel (`main`, output 1, input 0)
- Download each reel → Strip metadata (`main`, output 0, input 0)
- Strip metadata → Transcribe the video (`main`, output 0, input 0)
- Transcribe the video → Upload to aws (`main`, output 0, input 0)
- Upload to aws → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/1ordo/n8n-instagram-scrapper-with-transcription/blob/2a47dd0436e1beb9ca588b9faff95c4f3aa996b4/n8n.json](https://github.com/1ordo/n8n-instagram-scrapper-with-transcription/blob/2a47dd0436e1beb9ca588b9faff95c4f3aa996b4/n8n.json). License: **MIT**; preserve [the notice](../../../../licenses/1ordo--n8n-instagram-scrapper-with-transcription.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
