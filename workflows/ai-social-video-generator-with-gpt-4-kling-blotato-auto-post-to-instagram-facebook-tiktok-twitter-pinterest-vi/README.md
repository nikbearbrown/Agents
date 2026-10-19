# 💥AI Social Video Generator with GPT-4, Kling & Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter & Pinterest - vide

This folder contains the **💥AI Social Video Generator with GPT-4, Kling & Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter & Pinterest - vide** workflow. Its executable nodes use `agent`, `code`, `googleSheets`, `httpRequest`, `lmChatOpenAi`, `openAi`, `set`, `telegram`, `telegramTrigger`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-social-video-generator-with-gpt-4-kling-blotato-auto-post-to-instagram-facebook-tiktok-twitter-pinterest-vi.json`](ai-social-video-generator-with-gpt-4-kling-blotato-auto-post-to-instagram-facebook-tiktok-twitter-pinterest-vi.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `httpBasicAuth`, `httpHeaderAuth`, `openAiApi`, `telegramApi`

**Entry nodes:** Trigger: Telegram Prompt

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Trigger: Telegram Prompt | `telegramTrigger` | Inspect parameters |
| Extract Prompt & Caption | `code` | Inspect parameters |
| Transform Prompt for Kling (GPT-4) | `agent` | Inspect parameters |
| OpenAI Model Bridge | `lmChatOpenAi` | Inspect parameters |
| Generate Video via Kling API | `httpRequest` | POST |
| Wait for Video Generation | `wait` | Inspect parameters |
| Get Generated Video URL | `httpRequest` | Inspect parameters |
| Generate Voice-Over Script | `openAi` | Inspect parameters |
| Convert Script to Audio (TTS) | `openAi` | audio |
| Upload Audio to Cloudinary | `httpRequest` | Inspect parameters |
| Merge Audio + Video | `httpRequest` | POST |
| Wait for Audio/Video Fusion | `wait` | Inspect parameters |
| Get Video URL with Audio | `httpRequest` | Inspect parameters |
| Wait Before Captioning | `wait` | Inspect parameters |
| Add Captions/Subtitles to Video | `httpRequest` | POST |
| Wait for Caption Render | `wait` | Inspect parameters |
| Get Final Video URL (Audio + Captions) | `httpRequest` | Inspect parameters |
| Generate Social Caption from Voiceover | `openAi` | Inspect parameters |
| Generate YouTube-Style Title | `openAi` | Inspect parameters |
| Save Video Metadata to Google Sheets | `googleSheets` | append |
| Send Final Video to Telegram | `telegram` | sendVideo |
| Send Caption Link via Telegram | `telegram` | Inspect parameters |
| Assign Social Media IDs | `set` | Inspect parameters |
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

## Connection map

- Merge Audio + Video → Wait for Audio/Video Fusion (`main`, output 0, input 0)
- OpenAI Model Bridge → Transform Prompt for Kling (GPT-4) (`ai_languageModel`, output 0, input 0)
- Wait Before Captioning → Add Captions/Subtitles to Video (`main`, output 0, input 0)
- Assign Social Media IDs → Upload Video to Blotato (`main`, output 0, input 0)
- Get Generated Video URL → Generate Voice-Over Script (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Instagram (`main`, output 0, input 0)
- Upload Video to Blotato → Post to YouTube (`main`, output 0, input 0)
- Upload Video to Blotato → Post to TikTok (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Facebook Page (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Threads (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Twitter (X) (`main`, output 0, input 0)
- Upload Video to Blotato → Post to LinkedIn (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Bluesky (`main`, output 0, input 0)
- Upload Video to Blotato → Post to Pinterest (`main`, output 0, input 0)
- Wait for Caption Render → Get Final Video URL (Audio + Captions) (`main`, output 0, input 0)
- Extract Prompt & Caption → Transform Prompt for Kling (GPT-4) (`main`, output 0, input 0)
- Get Video URL with Audio → Wait Before Captioning (`main`, output 0, input 0)
- Trigger: Telegram Prompt → Extract Prompt & Caption (`main`, output 0, input 0)
- Wait for Video Generation → Get Generated Video URL (`main`, output 0, input 0)
- Generate Voice-Over Script → Convert Script to Audio (TTS) (`main`, output 0, input 0)
- Upload Audio to Cloudinary → Merge Audio + Video (`main`, output 0, input 0)
- Wait for Audio/Video Fusion → Get Video URL with Audio (`main`, output 0, input 0)
- Generate Video via Kling API → Wait for Video Generation (`main`, output 0, input 0)
- Generate YouTube-Style Title → Save Video Metadata to Google Sheets (`main`, output 0, input 0)
- Send Final Video to Telegram → Send Caption Link via Telegram (`main`, output 0, input 0)
- Convert Script to Audio (TTS) → Upload Audio to Cloudinary (`main`, output 0, input 0)
- Send Caption Link via Telegram → Assign Social Media IDs (`main`, output 0, input 0)
- Add Captions/Subtitles to Video → Wait for Caption Render (`main`, output 0, input 0)
- Transform Prompt for Kling (GPT-4) → Generate Video via Kling API (`main`, output 0, input 0)
- Save Video Metadata to Google Sheets → Send Final Video to Telegram (`main`, output 0, input 0)
- Generate Social Caption from Voiceover → Generate YouTube-Style Title (`main`, output 0, input 0)
- Get Final Video URL (Audio + Captions) → Generate Social Caption from Voiceover (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1288_Telegram_Wait_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1288_Telegram_Wait_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
