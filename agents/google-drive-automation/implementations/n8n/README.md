# Google Drive Automation

This folder contains the **Google Drive Automation** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `extractFromFile`, `googleDrive`, `googleDriveTrigger`, `lmChatOpenRouter`, `textSplitterRecursiveCharacterTextSplitter`, `vectorStorePinecone`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`google-drive-automation.json`](google-drive-automation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `openRouterApi`, `pineconeApi`

**Entry nodes:** Monitor Google Drive for New Files, Chat Message Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| AI Agent | `agent` | Inspect parameters |
| Monitor Google Drive for New Files | `googleDriveTrigger` | Inspect parameters |
| Download File from Google Drive | `googleDrive` | download |
| Extract PDF Content | `extractFromFile` | pdf |
| Insert Document into Pinecone Vector Store | `vectorStorePinecone` | Inspect parameters |
| Generate Document Embeddings (Google Gemini) | `embeddingsGoogleGemini` | Inspect parameters |
| Clean and Normalize PDF Text | `code` | Inspect parameters |
| Load Document Data for Processing | `documentDefaultDataLoader` | Inspect parameters |
| Split Document Text into Chunks | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Chat Message Trigger | `chatTrigger` | Inspect parameters |
| Retrieve Relevant Documents from Pinecone | `vectorStorePinecone` | Inspect parameters |
| Generate Query Embeddings (Google Gemini) | `embeddingsGoogleGemini` | Inspect parameters |
| Generate Chat Prompt with Context | `code` | Inspect parameters |
| OpenRouter Chat Model Interface | `lmChatOpenRouter` | Inspect parameters |

## Connection map

- Extract PDF Content → Clean and Normalize PDF Text (`main`, output 0, input 0)
- Chat Message Trigger → Retrieve Relevant Documents from Pinecone (`main`, output 0, input 0)
- Clean and Normalize PDF Text → Insert Document into Pinecone Vector Store (`main`, output 0, input 0)
- Download File from Google Drive → Extract PDF Content (`main`, output 0, input 0)
- OpenRouter Chat Model Interface → AI Agent (`ai_languageModel`, output 0, input 0)
- Split Document Text into Chunks → Load Document Data for Processing (`ai_textSplitter`, output 0, input 0)
- Generate Chat Prompt with Context → AI Agent (`main`, output 0, input 0)
- Load Document Data for Processing → Insert Document into Pinecone Vector Store (`ai_document`, output 0, input 0)
- Monitor Google Drive for New Files → Download File from Google Drive (`main`, output 0, input 0)
- Generate Query Embeddings (Google Gemini) → Retrieve Relevant Documents from Pinecone (`ai_embedding`, output 0, input 0)
- Retrieve Relevant Documents from Pinecone → Generate Chat Prompt with Context (`main`, output 0, input 0)
- Generate Document Embeddings (Google Gemini) → Insert Document into Pinecone Vector Store (`ai_embedding`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1906_Code_Extractfromfile_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1906_Code_Extractfromfile_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
