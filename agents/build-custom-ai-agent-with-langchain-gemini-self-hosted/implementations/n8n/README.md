# Build Custom AI Agent with LangChain & Gemini (Self-Hosted)

This folder contains the **Build Custom AI Agent with LangChain & Gemini (Self-Hosted)** workflow. Its executable nodes use `chatTrigger`, `code`, `lmChatGoogleGemini`, `memoryBufferWindow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`build-custom-ai-agent-with-langchain-gemini-self-hosted.json`](build-custom-ai-agent-with-langchain-gemini-self-hosted.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Store conversation history | `memoryBufferWindow` | Inspect parameters |
| Construct & Execute LLM Prompt | `code` | Inspect parameters |

## Connection map

- Google Gemini Chat Model → Construct & Execute LLM Prompt (`ai_languageModel`, output 0, input 0)
- Store conversation history → Construct & Execute LLM Prompt (`ai_memory`, output 0, input 0)
- Store conversation history → When chat message received (`ai_memory`, output 0, input 0)
- When chat message received → Construct & Execute LLM Prompt (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2023_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/2023_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
