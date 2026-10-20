# InstaTest

This folder contains the **InstaTest** workflow. Its executable nodes use `agent`, `lmChatOpenAi`, `memoryBufferWindow`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`easy-instagram-via-manychat-bot.json`](easy-instagram-via-manychat-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Getting message from Instagram

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Set your system promt for AI | `set` | Inspect parameters |
| Local n8n memory | `memoryBufferWindow` | Inspect parameters |
| ChatGPT model | `lmChatOpenAi` | Inspect parameters |
| Send respond  | `respondToWebhook` | Inspect parameters |
| Getting message from Instagram | `webhook` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |

## Connection map

- AI Agent → Send respond  (`main`, output 0, input 0)
- ChatGPT model → AI Agent (`ai_languageModel`, output 0, input 0)
- Local n8n memory → AI Agent (`ai_memory`, output 0, input 0)
- Set your system promt for AI → AI Agent (`main`, output 0, input 0)
- Getting message from Instagram → Set your system promt for AI (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/1967_Respondtowebhook_Stickynote_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Respondtowebhook/1967_Respondtowebhook_Stickynote_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
