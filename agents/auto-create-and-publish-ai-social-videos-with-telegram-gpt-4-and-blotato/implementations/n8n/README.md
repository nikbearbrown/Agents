# Auto-create and publish AI social videos with Telegram, GPT-4 and Blotato

This folder contains the **Auto-create and publish AI social videos with Telegram, GPT-4 and Blotato** workflow. Its executable nodes use `code`, `googleSheets`, `httpRequest`, `if`, `openAi`, `set`, `telegram`, `telegramTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auto-create-and-publish-ai-social-videos-with-telegram-gpt-4-and-blotato.json`](auto-create-and-publish-ai-social-videos-with-telegram-gpt-4-and-blotato.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpBasicAuth`, `httpCustomAuth`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Trigger Telegram Prompt or Image

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Upload Video to Blotato | `httpRequest` | POST |
| Post to Instagram | `httpRequest` | POST |
| Post to YouTube | `httpRequest` | POST |
| Post to TikTok | `httpRequest` | POST |
| Post to Facebook Page | `httpRequest` | POST |
| Post to Threads | `httpRequest` | POST |
| Post to Twitter (X) | `httpRequest` | POST |
| Post to LinkedIn | `httpRequest` | POST |
| Post to Bluesky | `httpRequest` | POST |
| Post to Pinterest | `httpRequest` | POST |
| Trigger Telegram Prompt or Image | `telegramTrigger` | Inspect parameters |
| Split Prompt or Image Input | `code` | Inspect parameters |
| Condition Input Type (Image or Text) | `if` | Inspect parameters |
| Download Image from Telegram | `telegram` | file |
| Extract Image File URL | `httpRequest` | Inspect parameters |
| Upload Image to Cloudinary | `httpRequest` | POST |
| Convert Image to Video | `httpRequest` | POST |
| Wait for Image-to-Video Rendering | `wait` | Inspect parameters |
| Get Image-Based Video URL | `httpRequest` | Inspect parameters |
| Generate Video with blotato | `httpRequest` | POST |
| Wait for blotato Video Rendering | `wait` | Inspect parameters |
| Get blotato Video URL | `httpRequest` | Inspect parameters |
| Merge Video Data (Image or Prompt) | `set` | Inspect parameters |
| Generate Music with Piapi | `httpRequest` | POST |
| Wait for Music Generation | `wait` | Inspect parameters |
| Get Music File URL | `httpRequest` | Inspect parameters |
| Generate Script (GPT-4o-mini) | `openAi` | Inspect parameters |
| Split Script | `code` | Inspect parameters |
| Merge Video + Music | `httpRequest` | POST |
| Wait for Fusion Completion | `wait` | Inspect parameters |
| Get Final Video URL | `httpRequest` | Inspect parameters |
| Generate Social Caption (GPT-4) | `openAi` | Inspect parameters |
| Generate SEO Title (GPT-4) | `openAi` | Inspect parameters |
| Append Video Data to Google Sheet | `googleSheets` | append |
| Send Final Video to Telegram | `telegram` | Inspect parameters |
| Send Caption to Telegram | `telegram` | sendVideo |
| Assign Platform IDs for Blotato | `set` | Inspect parameters |

## Connection map

- Split Script → Merge Video + Music (`main`, output 0, input 0)
- Get Music File URL → Generate Script (GPT-4o-mini) (`main`, output 0, input 0)
- Get Final Video URL → Generate Social Caption (GPT-4) (`main`, output 0, input 0)
- Merge Video + Music → Wait for Fusion Completion (`main`, output 0, input 0)
- Get blotato Video URL → Merge Video Data (Image or Prompt) (`main`, output 0, input 0)
- Convert Image to Video → Wait for Image-to-Video Rendering (`main`, output 0, input 0)
- Extract Image File URL → Upload Image to Cloudinary (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Instagram (`main`, output 0, input 0)
- Upload Video to Blotato → Post to YouTube (`main`, output 0, input 0)
- Upload Video to Blotato → Post to TikTok (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Facebook Page (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Threads (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Twitter (X) (`main`, output 0, input 0)
- Upload Video to Blotato → Post to LinkedIn (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Bluesky (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Pinterest (`main`, output 0, input 0)
- Send Caption to Telegram → Assign Platform IDs for Blotato (`main`, output 0, input 0)
- Generate Music with Piapi → Wait for Music Generation (`main`, output 0, input 0)
- Get Image-Based Video URL → Merge Video Data (Image or Prompt) (`main`, output 0, input 0)
- Wait for Music Generation → Get Music File URL (`main`, output 0, input 0)
- Generate SEO Title (GPT-4) → Append Video Data to Google Sheet (`main`, output 0, input 0)
- Upload Image to Cloudinary → Convert Image to Video (`main`, output 0, input 0)
- Wait for Fusion Completion → Get Final Video URL (`main`, output 0, input 0)
- Generate Video with blotato → Wait for blotato Video Rendering (`main`, output 0, input 0)
- Split Prompt or Image Input → Condition Input Type (Image or Text) (`main`, output 0, input 0)
- Download Image from Telegram → Extract Image File URL (`main`, output 0, input 0)
- Send Final Video to Telegram → Send Caption to Telegram (`main`, output 0, input 0)
- Generate Script (GPT-4o-mini) → Split Script (`main`, output 0, input 0)
- Assign Platform IDs for Blotato → Upload Video to Blotato (`main`, output 0, input 0)
- Generate Social Caption (GPT-4) → Generate SEO Title (GPT-4) (`main`, output 0, input 0)
- Trigger Telegram Prompt or Image → Split Prompt or Image Input (`main`, output 0, input 0)
- Wait for blotato Video Rendering → Get blotato Video URL (`main`, output 0, input 0)
- Append Video Data to Google Sheet → Send Final Video to Telegram (`main`, output 0, input 0)
- Wait for Image-to-Video Rendering → Get Image-Based Video URL (`main`, output 0, input 0)
- Merge Video Data (Image or Prompt) → Generate Music with Piapi (`main`, output 0, input 0)
- Condition Input Type (Image or Text) → Generate Video with blotato (`main`, output 0, input 0)
- Condition Input Type (Image or Text) → Download Image from Telegram (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1878_Telegram_Wait_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1878_Telegram_Wait_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
