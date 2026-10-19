# AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs and upload to all social networks

This folder contains the **AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs and upload to all social networks** workflow. Its executable nodes use `code`, `discord`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `merge`, `openAi`, `readBinaryFile`, `scheduleTrigger`, `set`, `wait`, `writeBinaryFile`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-short-form-video-generator-with-openai-flux-kling-and-elevenlabs-and-upload-to-all-social-networks.json`](ai-powered-short-form-video-generator-with-openai-flux-kling-and-elevenlabs-and-upload-to-all-social-networks.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `openAiApi`

**Entry nodes:** Once Per Day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get image | `httpRequest` | Inspect parameters |
| Generate Image | `httpRequest` | POST |
| Image-to-Video | `httpRequest` | POST |
| Get Video | `httpRequest` | Inspect parameters |
| List Elements | `code` | Inspect parameters |
| Wait 10min | `wait` | Inspect parameters |
| Wait 3min | `wait` | Inspect parameters |
| Wait 5min | `wait` | Inspect parameters |
| Generate voice | `httpRequest` | POST |
| List Elements1 | `code` | Inspect parameters |
| Fail check | `if` | Inspect parameters |
| Wait to retry | `wait` | Inspect parameters |
| Generate Image Prompts | `openAi` | Inspect parameters |
| Calculate Token Usage | `code` | Inspect parameters |
| Check for failures | `if` | Inspect parameters |
| Generate Video Captions | `openAi` | Inspect parameters |
| Match captions with videos | `merge` | Inspect parameters |
| Generate Script | `openAi` | Inspect parameters |
| Upload Voice Audio | `googleDrive` | Inspect parameters |
| Set Access Permissions | `googleDrive` | share |
| Pair Videos with Audio | `merge` | Inspect parameters |
| Render Final Video | `httpRequest` | POST |
| Notify me on Discord | `discord` | Inspect parameters |
| Once Per Day | `scheduleTrigger` | Inspect parameters |
| Load Google Sheet | `googleSheets` | Inspect parameters |
| Create List | `code` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Get Final Video | `httpRequest` | Inspect parameters |
| Upload Final Video | `googleDrive` | Inspect parameters |
| Get Raw File | `httpRequest` | Inspect parameters |
| Set Permissions | `googleDrive` | share |
| Update Google Sheet | `googleSheets` | update |
| Set API Keys | `set` | Inspect parameters |
| Validate list formatting | `if` | Inspect parameters |
| Get Audio from Video | `openAi` | audio / transcribe |
| Generate Description for Videos  in Tiktok and Instagram | `openAi` | Inspect parameters |
| Upload Video and Description to Tiktok | `httpRequest` | POST |
| Upload Video and Description to Instagram | `httpRequest` | POST |
| Upload Video and Description to Youtube | `httpRequest` | POST |
| Upload Video and Description to Facebook | `httpRequest` | POST |
| Upload Video and Description to Linkedin | `httpRequest` | POST |
| Read Video from Google Drive | `readBinaryFile` | Inspect parameters |
| Write video | `writeBinaryFile` | Inspect parameters |

## Connection map

- Wait1 → Get Final Video (`main`, output 0, input 0)
- Get Video → Fail check (`main`, output 0, input 0)
- Get image → Check for failures (`main`, output 0, input 0)
- Wait 3min → Get image (`main`, output 0, input 0)
- Wait 5min → Generate Image (`main`, output 0, input 0)
- Fail check → Wait to retry (`main`, output 0, input 0)
- Fail check → Match captions with videos (`main`, output 1, input 1)
- Wait 10min → Get Video (`main`, output 0, input 0)
- Create List → Validate list formatting (`main`, output 0, input 0)
- Write video → Get Audio from Video (`main`, output 0, input 0)
- Get Raw File → Upload Final Video (`main`, output 0, input 0)
- Get Raw File → Write video (`main`, output 0, input 0)
- Once Per Day → Set API Keys (`main`, output 0, input 0)
- Set API Keys → Load Google Sheet (`main`, output 0, input 0)
- List Elements → Pair Videos with Audio (`main`, output 0, input 0)
- Wait to retry → Image-to-Video (`main`, output 0, input 0)
- Generate Image → Wait 3min (`main`, output 0, input 0)
- Generate voice → Upload Voice Audio (`main`, output 0, input 0)
- Image-to-Video → Wait 10min (`main`, output 0, input 0)
- List Elements1 → Pair Videos with Audio (`main`, output 0, input 1)
- Generate Script → Generate voice (`main`, output 0, input 0)
- Get Final Video → Get Raw File (`main`, output 0, input 0)
- Set Permissions → Update Google Sheet (`main`, output 0, input 0)
- Load Google Sheet → Generate Video Captions (`main`, output 0, input 0)
- Check for failures → Wait 5min (`main`, output 0, input 0)
- Check for failures → Image-to-Video (`main`, output 1, input 0)
- Render Final Video → Wait1 (`main`, output 0, input 0)
- Upload Final Video → Set Permissions (`main`, output 0, input 0)
- Upload Voice Audio → Set Access Permissions (`main`, output 0, input 0)
- Update Google Sheet → Notify me on Discord (`main`, output 0, input 0)
- Get Audio from Video → Generate Description for Videos  in Tiktok and Instagram (`main`, output 0, input 0)
- Calculate Token Usage → Generate Image (`main`, output 0, input 0)
- Generate Image Prompts → Calculate Token Usage (`main`, output 0, input 0)
- Pair Videos with Audio → Render Final Video (`main`, output 0, input 0)
- Set Access Permissions → List Elements1 (`main`, output 0, input 0)
- Generate Video Captions → Create List (`main`, output 0, input 0)
- Validate list formatting → Generate Image Prompts (`main`, output 0, input 0)
- Validate list formatting → Match captions with videos (`main`, output 0, input 0)
- Validate list formatting → Generate Script (`main`, output 0, input 0)
- Validate list formatting → Generate Video Captions (`main`, output 1, input 0)
- Match captions with videos → List Elements (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Tiktok (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Instagram (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Youtube (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Facebook (`main`, output 0, input 0)
- Read Video from Google Drive → Upload Video and Description to Linkedin (`main`, output 0, input 0)
- Generate Description for Videos  in Tiktok and Instagram → Read Video from Google Drive (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1282_Wait_Code_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1282_Wait_Code_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
