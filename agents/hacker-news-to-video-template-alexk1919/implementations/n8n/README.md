# Hacker News to Video Template - AlexK1919

This folder contains the **Hacker News to Video Template - AlexK1919** workflow. Its executable nodes use `agent`, `dropbox`, `googleDrive`, `hackerNews`, `httpRequest`, `if`, `limit`, `linkedIn`, `lmChatOpenAi`, `manualTrigger`, `microsoftOneDrive`, `openAi`, `outputParserStructured`, `s3`, `set`, `splitInBatches`, `toolHttpRequest`, `twitter`, `wait`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hacker-news-to-video-template-alexk1919.json`](hacker-news-to-video-template-alexk1919.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpCustomAuth`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Hacker News | `hackerNews` | all |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| HTTP Request1 | `toolHttpRequest` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Upload to Minio | `s3` | upload |
| News1 | `set` | Inspect parameters |
| Leo - Improve Prompt | `httpRequest` | POST |
| Leo - Get imageId | `httpRequest` | Inspect parameters |
| Runway - Create Video | `httpRequest` | POST |
| Runway - Get Video | `httpRequest` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| If Topic | `if` | Inspect parameters |
| Get Image | `httpRequest` | Inspect parameters |
| Prompt Settings1 | `set` | Inspect parameters |
| Leo - Generate Image | `httpRequest` | POST |
| Wait1 | `wait` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Image Analysis | `openAi` | image / analyze |
| Wait3 | `wait` | Inspect parameters |
| Article Analysis | `agent` | Inspect parameters |
| Dropbox | `dropbox` | Inspect parameters |
| Google Drive | `googleDrive` | update |
| Microsoft OneDrive | `microsoftOneDrive` | Inspect parameters |
| YouTube | `youTube` | video / upload |
| X | `twitter` | Inspect parameters |
| Instagram | `httpRequest` | Inspect parameters |
| LinkedIn | `linkedIn` | Inspect parameters |
| Leo - Improve Prompt2 | `httpRequest` | POST |
| Wait4 | `wait` | Inspect parameters |
| Wait6 | `wait` | Inspect parameters |
| Leo - Generate Image2 | `httpRequest` | POST |
| Leo - Get imageId2 | `httpRequest` | Inspect parameters |
| Runway - Create Video2 | `httpRequest` | POST |
| Runway - Get Video2 | `httpRequest` | Inspect parameters |
| Cre - Generate Video1 | `httpRequest` | POST |
| Cre - Get Video | `httpRequest` | Inspect parameters |
| Article Prep | `openAi` | Inspect parameters |

## Connection map

- X → LinkedIn (`main`, output 0, input 0)
- Limit → Loop Over Items (`main`, output 0, input 0)
- News1 → Prompt Settings1 (`main`, output 0, input 0)
- Wait1 → Leo - Get imageId (`main`, output 0, input 0)
- Wait2 → Runway - Get Video (`main`, output 0, input 0)
- Wait3 → Cre - Get Video (`main`, output 0, input 0)
- Wait4 → Runway - Get Video2 (`main`, output 0, input 0)
- Wait6 → Leo - Get imageId2 (`main`, output 0, input 0)
- Dropbox → Google Drive (`main`, output 0, input 0)
- YouTube → X (`main`, output 0, input 0)
- If Topic → Image Analysis (`main`, output 0, input 0)
- If Topic → Loop Over Items (`main`, output 1, input 0)
- LinkedIn → Instagram (`main`, output 0, input 0)
- Get Image → Article Prep (`main`, output 0, input 0)
- Hacker News → Limit (`main`, output 0, input 0)
- Article Prep → News1 (`main`, output 0, input 0)
- Google Drive → Microsoft OneDrive (`main`, output 0, input 0)
- HTTP Request1 → Article Analysis (`ai_tool`, output 0, input 0)
- Image Analysis → Get Image (`main`, output 0, input 0)
- Loop Over Items → Article Analysis (`main`, output 1, input 0)
- Article Analysis → If Topic (`main`, output 0, input 0)
- Article Analysis → Loop Over Items (`main`, output 1, input 0)
- Prompt Settings1 → Leo - Improve Prompt (`main`, output 0, input 0)
- Leo - Get imageId → Runway - Create Video (`main`, output 0, input 0)
- Leo - Get imageId2 → Runway - Create Video2 (`main`, output 0, input 0)
- Microsoft OneDrive → Upload to Minio (`main`, output 0, input 0)
- OpenAI Chat Model3 → Article Analysis (`ai_languageModel`, output 0, input 0)
- Runway - Get Video → Leo - Improve Prompt2 (`main`, output 0, input 0)
- Runway - Get Video2 → Cre - Generate Video1 (`main`, output 0, input 0)
- Leo - Generate Image → Wait1 (`main`, output 0, input 0)
- Leo - Improve Prompt → Leo - Generate Image (`main`, output 0, input 0)
- Cre - Generate Video1 → Wait3 (`main`, output 0, input 0)
- Leo - Generate Image2 → Wait6 (`main`, output 0, input 0)
- Leo - Improve Prompt2 → Leo - Generate Image2 (`main`, output 0, input 0)
- Runway - Create Video → Wait2 (`main`, output 0, input 0)
- Runway - Create Video2 → Wait4 (`main`, output 0, input 0)
- Structured Output Parser → Article Analysis (`ai_outputParser`, output 0, input 0)
- When clicking ‘Test workflow’ → Hacker News (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1491_Linkedin_Wait_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1491_Linkedin_Wait_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
