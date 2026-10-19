# Email AI Auto-responder. Summerize and send email

This folder contains the **Email AI Auto-responder. Summerize and send email** workflow. Its executable nodes use `agent`, `chainLlm`, `chainSummarization`, `documentDefaultDataLoader`, `emailReadImap`, `emailSend`, `embeddingsOpenAi`, `googleDrive`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `noOp`, `textClassifier`, `textSplitterTokenSplitter`, `vectorStoreQdrant`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`email-ai-auto-responder-summerize-and-send-email.json`](email-ai-auto-responder-summerize-and-send-email.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `httpHeaderAuth`, `imap`, `openAiApi`, `qdrantApi`, `smtp`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| DeepSeek R1 | `lmChatOpenAi` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Email Classifier | `textClassifier` | Inspect parameters |
| Email Summarization Chain | `chainSummarization` | Inspect parameters |
| Write email | `agent` | Inspect parameters |
| Review email | `chainLlm` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Create collection | `httpRequest` | POST |
| Refresh collection | `httpRequest` | POST |
| Get folder | `googleDrive` | fileFolder |
| Download Files | `googleDrive` | download |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter | `textSplitterTokenSplitter` | Inspect parameters |
| Qdrant Vector Store1 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Do nothing | `noOp` | Inspect parameters |
| OpenAI | `lmChatOpenAi` | Inspect parameters |
| DeepSeek | `lmChatOpenAi` | Inspect parameters |
| OpenAI 4-o-mini | `lmChatOpenAi` | Inspect parameters |

## Connection map

- OpenAI → Write email (`ai_languageModel`, output 0, input 0)
- DeepSeek → Review email (`ai_languageModel`, output 0, input 0)
- Markdown → Email Summarization Chain (`main`, output 0, input 0)
- Get folder → Download Files (`main`, output 0, input 0)
- DeepSeek R1 → Email Summarization Chain (`ai_languageModel`, output 0, input 0)
- Write email → Review email (`main`, output 0, input 0)
- Review email → Send Email (`main`, output 0, input 0)
- Download Files → Qdrant Vector Store1 (`main`, output 0, input 0)
- Token Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- OpenAI 4-o-mini → Email Classifier (`ai_languageModel`, output 0, input 0)
- Email Classifier → Write email (`main`, output 0, input 0)
- Email Classifier → Do nothing (`main`, output 1, input 0)
- Embeddings OpenAI → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI1 → Qdrant Vector Store1 (`ai_embedding`, output 0, input 0)
- Refresh collection → Get folder (`main`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store1 (`ai_document`, output 0, input 0)
- Qdrant Vector Store → Write email (`ai_tool`, output 0, input 0)
- Email Trigger (IMAP) → Markdown (`main`, output 0, input 0)
- Email Summarization Chain → Email Classifier (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Create collection (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Refresh collection (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Emailreadimap/1277_Emailreadimap_Manual_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Emailreadimap/1277_Emailreadimap_Manual_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
