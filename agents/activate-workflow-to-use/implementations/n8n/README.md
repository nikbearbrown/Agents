# Activate workflow to use!

This folder contains the **Activate workflow to use!** workflow. Its executable nodes use `agent`, `chainLlm`, `httpRequest`, `lmChatGoogleGemini`, `memoryBufferWindow`, `set`, `splitOut`, `switch`, `toolWikipedia`, `wait`, `whatsApp`, `whatsAppTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`activate-workflow-to-use.json`](activate-workflow-to-use.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `whatsAppApi`, `whatsAppTriggerApi`

**Entry nodes:** WhatsApp Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| WhatsApp Trigger | `whatsAppTrigger` | Inspect parameters |
| Get Audio URL | `whatsApp` | media / mediaUrlGet |
| Get Video URL | `whatsApp` | media / mediaUrlGet |
| Get Image URL | `whatsApp` | media / mediaUrlGet |
| Download Video | `httpRequest` | Inspect parameters |
| Download Audio | `httpRequest` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Get User's Message | `set` | Inspect parameters |
| Split Out Message Parts | `splitOut` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Redirect Message Types | `switch` | Inspect parameters |
| Get Text | `wait` | Inspect parameters |
| Respond to User | `whatsApp` | send |
| Image Explainer | `chainLlm` | Inspect parameters |
| Format Response | `set` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Audio | `httpRequest` | POST |
| Google Gemini Video | `httpRequest` | POST |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Format Response1 | `set` | Inspect parameters |
| Text Summarizer | `chainLlm` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- AI Agent → Respond to User (`main`, output 0, input 0)
- Get Text → Text Summarizer (`main`, output 0, input 0)
- Wikipedia → AI Agent (`ai_tool`, output 0, input 0)
- Get Audio URL → Download Audio (`main`, output 0, input 0)
- Get Image URL → Download Image (`main`, output 0, input 0)
- Get Video URL → Download Video (`main`, output 0, input 0)
- Download Audio → Google Gemini Audio (`main`, output 0, input 0)
- Download Image → Image Explainer (`main`, output 0, input 0)
- Download Video → Google Gemini Video (`main`, output 0, input 0)
- Format Response → Get User's Message (`main`, output 0, input 0)
- Image Explainer → Get User's Message (`main`, output 0, input 0)
- Text Summarizer → Get User's Message (`main`, output 0, input 0)
- Format Response1 → Get User's Message (`main`, output 0, input 0)
- WhatsApp Trigger → Split Out Message Parts (`main`, output 0, input 0)
- Get User's Message → AI Agent (`main`, output 0, input 0)
- Google Gemini Audio → Format Response1 (`main`, output 0, input 0)
- Google Gemini Video → Format Response (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Redirect Message Types → Get Audio URL (`main`, output 0, input 0)
- Redirect Message Types → Get Video URL (`main`, output 1, input 0)
- Redirect Message Types → Get Image URL (`main`, output 2, input 0)
- Redirect Message Types → Get Text (`main`, output 3, input 0)
- Split Out Message Parts → Redirect Message Types (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model1 → Image Explainer (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Text Summarizer (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0602_Wait_Splitout_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0602_Wait_Splitout_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
