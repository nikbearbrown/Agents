# Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini

This folder contains the **Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini** workflow. Its executable nodes use `agent`, `chainLlm`, `googleSheets`, `httpRequest`, `lmChatGoogleGemini`, `memoryBufferWindow`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`line-chatbot-extract-text-from-pay-slip-with-gemini.json`](line-chatbot-extract-text-from-pay-slip-with-gemini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `googleSheetsOAuth2Api`, `httpHeaderAuth`

**Entry nodes:** Line: Messaging API

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Line: Get Image | `httpRequest` | Inspect parameters |
| Message Type | `set` | Inspect parameters |
| Message Classification | `switch` | Inspect parameters |
| Text Message Processing | `agent` | Inspect parameters |
| Image Message Processing | `chainLlm` | Inspect parameters |
| Line: Response to User | `httpRequest` | POST |
| Line: Text Response to User | `httpRequest` | POST |
| Text from Slip Result | `googleSheets` | append |
| Line: Messaging API | `webhook` | Inspect parameters |
| Google Gemini for Text | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini for Image | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Message Type → Message Classification (`main`, output 0, input 0)
- Line: Get Image → Image Message Processing (`main`, output 0, input 0)
- Line: Messaging API → Message Type (`main`, output 0, input 0)
- Window Buffer Memory → Text Message Processing (`ai_memory`, output 0, input 0)
- Google Gemini for Text → Text Message Processing (`ai_languageModel`, output 0, input 0)
- Line: Response to User → Text from Slip Result (`main`, output 0, input 0)
- Message Classification → Text Message Processing (`main`, output 0, input 0)
- Message Classification → Line: Get Image (`main`, output 1, input 0)
- Google Gemini for Image → Image Message Processing (`ai_languageModel`, output 0, input 0)
- Text Message Processing → Line: Text Response to User (`main`, output 0, input 0)
- Image Message Processing → Line: Response to User (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1811_HTTP_GoogleSheets_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/1811_HTTP_GoogleSheets_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
