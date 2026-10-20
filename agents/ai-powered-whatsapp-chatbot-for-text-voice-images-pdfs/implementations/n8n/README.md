# AI-Powered WhatsApp Chatbot for Text, Voice, Images & PDFs

This folder contains the **AI-Powered WhatsApp Chatbot for Text, Voice, Images & PDFs** workflow. Its executable nodes use `agent`, `code`, `extractFromFile`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `openAi`, `set`, `switch`, `whatsApp`, `whatsAppTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-whatsapp-chatbot-for-text-voice-images-pdfs.json`](ai-powered-whatsapp-chatbot-for-text-voice-images-pdfs.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `whatsAppApi`, `whatsAppTriggerApi`

**Entry nodes:** WhatsApp Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| WhatsApp Trigger | `whatsAppTrigger` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| Analyze Image | `openAi` | image / analyze |
| Download Audio | `httpRequest` | Inspect parameters |
| Transcribe Audio | `openAi` | audio / transcribe |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| Download File | `httpRequest` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Get File Url | `whatsApp` | media / mediaUrlGet |
| Only PDF File | `if` | Inspect parameters |
| Fix mimeType for Audio | `code` | Inspect parameters |
| Send message | `whatsApp` | send |
| Send audio | `whatsApp` | send |
| Incorrect format | `whatsApp` | send |
| Text | `set` | Inspect parameters |
| Audio | `set` | Inspect parameters |
| Image | `set` | Inspect parameters |
| File | `set` | Inspect parameters |
| Not supported | `whatsApp` | send |
| Get Image Url | `whatsApp` | media / mediaUrlGet |
| Get Audio Url | `whatsApp` | media / mediaUrlGet |
| Generate Audio Response | `openAi` | audio |
| From audio to audio? | `if` | Inspect parameters |
| Input type | `switch` | Inspect parameters |

## Connection map

- File → AI Agent1 (`main`, output 0, input 0)
- Text → AI Agent1 (`main`, output 0, input 0)
- Audio → AI Agent1 (`main`, output 0, input 0)
- Image → AI Agent1 (`main`, output 0, input 0)
- AI Agent1 → From audio to audio? (`main`, output 0, input 0)
- Input type → Text (`main`, output 0, input 0)
- Input type → Get Audio Url (`main`, output 1, input 0)
- Input type → Get Image Url (`main`, output 2, input 0)
- Input type → Only PDF File (`main`, output 3, input 0)
- Input type → Not supported (`main`, output 4, input 0)
- Get File Url → Download File (`main`, output 0, input 0)
- Analyze Image → Image (`main`, output 0, input 0)
- Download File → Extract from File (`main`, output 0, input 0)
- Get Audio Url → Download Audio (`main`, output 0, input 0)
- Get Image Url → Download Image (`main`, output 0, input 0)
- Only PDF File → Get File Url (`main`, output 0, input 0)
- Only PDF File → Incorrect format (`main`, output 1, input 0)
- Simple Memory → AI Agent1 (`ai_memory`, output 0, input 0)
- Download Audio → Transcribe Audio (`main`, output 0, input 0)
- Download Image → Analyze Image (`main`, output 0, input 0)
- Transcribe Audio → Audio (`main`, output 0, input 0)
- WhatsApp Trigger → Input type (`main`, output 0, input 0)
- Extract from File → File (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent1 (`ai_languageModel`, output 0, input 0)
- From audio to audio? → Generate Audio Response (`main`, output 0, input 0)
- From audio to audio? → Send message (`main`, output 1, input 0)
- Fix mimeType for Audio → Send audio (`main`, output 0, input 0)
- Generate Audio Response → Fix mimeType for Audio (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2033_Code_Extractfromfile_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2033_Code_Extractfromfile_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
