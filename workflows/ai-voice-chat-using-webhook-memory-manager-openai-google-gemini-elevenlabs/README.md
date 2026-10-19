# AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs

This folder contains the **AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs** workflow. Its executable nodes use `aggregate`, `chainLlm`, `httpRequest`, `limit`, `lmChatGoogleGemini`, `memoryBufferWindow`, `memoryManager`, `openAi`, `respondToWebhook`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-voice-chat-using-webhook-memory-manager-openai-google-gemini-elevenlabs.json`](ai-voice-chat-using-webhook-memory-manager-openai-google-gemini-elevenlabs.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpCustomAuth`, `openAiApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Chat | `memoryManager` | Inspect parameters |
| Insert Chat | `memoryManager` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| ElevenLabs - Generate Audio | `httpRequest` | POST |
| Limit | `limit` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| OpenAI - Speech to Text | `openAi` | audio / transcribe |

## Connection map

- Limit → ElevenLabs - Generate Audio (`main`, output 0, input 0)
- Webhook → OpenAI - Speech to Text (`main`, output 0, input 0)
- Get Chat → Aggregate (`main`, output 0, input 0)
- Aggregate → Basic LLM Chain (`main`, output 0, input 0)
- Insert Chat → Limit (`main`, output 0, input 0)
- Basic LLM Chain → Insert Chat (`main`, output 0, input 0)
- Window Buffer Memory → Insert Chat (`ai_memory`, output 0, input 0)
- Window Buffer Memory → Get Chat (`ai_memory`, output 0, input 0)
- OpenAI - Speech to Text → Get Chat (`main`, output 0, input 0)
- Google Gemini Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- ElevenLabs - Generate Audio → Respond to Webhook (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1262_Limit_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1262_Limit_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
