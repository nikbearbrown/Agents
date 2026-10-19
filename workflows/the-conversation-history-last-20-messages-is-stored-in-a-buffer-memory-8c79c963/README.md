# The conversation history(last 20 messages) is stored in a buffer memory

This folder contains the **The conversation history(last 20 messages) is stored in a buffer memory** workflow. Its executable nodes use `agent`, `lmChatOllama`, `manualChatTrigger`, `memoryBufferWindow`, `toolHttpRequest`, `toolWikipedia`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`the-conversation-history-last-20-messages-is-stored-in-a-buffer-memory-8c79c963.json`](the-conversation-history-last-20-messages-is-stored-in-a-buffer-memory-8c79c963.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ollamaApi`

**Entry nodes:** On new manual Chat Message

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On new manual Chat Message | `manualChatTrigger` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Weather HTTP Request | `toolHttpRequest` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |

## Connection map

- Wikipedia → AI Agent (`ai_tool`, output 0, input 0)
- Ollama Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Weather HTTP Request → AI Agent (`ai_tool`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- On new manual Chat Message → AI Agent (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0727_Stickynote_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0727_Stickynote_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
