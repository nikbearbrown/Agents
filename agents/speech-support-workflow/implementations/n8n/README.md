# Speech Support Workflow

This folder contains the **Speech Support Workflow** workflow. Its executable nodes use `agent`, `code`, `if`, `lmChatGoogleGemini`, `memoryBufferWindow`, `memoryManager`, `openAi`, `set`, `switch`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`speech-support-workflow.json`](speech-support-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `openAiApi`, `telegramApi`

**Entry nodes:** Recieve Telegram Message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Recieve Telegram Message | `telegramTrigger` | Inspect parameters |
| Check For Text or Voice Message | `set` | Inspect parameters |
| Download Audio File | `telegram` | file |
| Transcribe Audio File | `openAi` | audio / transcribe |
| If Voice Message | `if` | Inspect parameters |
| Code to remove unwanted characters from LLM response | `code` | Inspect parameters |
| Code to split output into chunks under 4000 characters | `code` | Inspect parameters |
| Respond to Telegram Message | `telegram` | Inspect parameters |
| Wipe Conversation Memory | `memoryManager` | Inspect parameters |
| Store Conversation Memory | `memoryBufferWindow` | Inspect parameters |
| Set prompt to start a new speech | `set` | Inspect parameters |
| Set prompt to generate a speech based on the feedback | `set` | Inspect parameters |
| Set prompt to provide feedback on speech | `set` | Inspect parameters |
| Route Flow Based on Message Content | `switch` | Inspect parameters |

## Connection map

- AI Agent → Code to remove unwanted characters from LLM response (`main`, output 0, input 0)
- If Voice Message → Download Audio File (`main`, output 0, input 0)
- If Voice Message → Route Flow Based on Message Content (`main`, output 1, input 0)
- Download Audio File → Transcribe Audio File (`main`, output 0, input 0)
- Transcribe Audio File → Route Flow Based on Message Content (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Recieve Telegram Message → Check For Text or Voice Message (`main`, output 0, input 0)
- Wipe Conversation Memory → Set prompt to start a new speech (`main`, output 0, input 0)
- Store Conversation Memory → AI Agent (`ai_memory`, output 0, input 0)
- Store Conversation Memory → Wipe Conversation Memory (`ai_memory`, output 0, input 0)
- Check For Text or Voice Message → If Voice Message (`main`, output 0, input 0)
- Set prompt to start a new speech → AI Agent (`main`, output 0, input 0)
- Route Flow Based on Message Content → Wipe Conversation Memory (`main`, output 0, input 0)
- Route Flow Based on Message Content → Set prompt to generate a speech based on the feedback (`main`, output 1, input 0)
- Route Flow Based on Message Content → Set prompt to provide feedback on speech (`main`, output 2, input 0)
- Set prompt to provide feedback on speech → AI Agent (`main`, output 0, input 0)
- Code to remove unwanted characters from LLM response → Code to split output into chunks under 4000 characters (`main`, output 0, input 0)
- Set prompt to generate a speech based on the feedback → AI Agent (`main`, output 0, input 0)
- Code to split output into chunks under 4000 characters → Respond to Telegram Message (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1452_Telegram_Stickynote_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1452_Telegram_Stickynote_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
