# ⚡AI-Powered YouTube Playlist & Video Summarization and Analysis v2

This folder contains the **⚡AI-Powered YouTube Playlist & Video Summarization and Analysis v2** workflow. Its executable nodes use `agent`, `chainLlm`, `chatTrigger`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `httpRequest`, `if`, `limit`, `lmChatGoogleGemini`, `memoryBufferWindow`, `merge`, `outputParserStructured`, `redis`, `set`, `splitOut`, `summarize`, `switch`, `textSplitterRecursiveCharacterTextSplitter`, `toolVectorStore`, `vectorStoreQdrant`, `youtubeTranscripter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-youtube-playlist-video-summarization-and-analysis-v2.json`](ai-powered-youtube-playlist-video-summarization-and-analysis-v2.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `qdrantApi`, `redis`

**Entry nodes:** Chat

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Handle Queries | `agent` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Summarize & Analyze Transcript | `chainLlm` | Inspect parameters |
| Concatenate | `summarize` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Embeddings Google Gemini1 | `embeddingsGoogleGemini` | Inspect parameters |
| Chat | `chatTrigger` | Inspect parameters |
| Video Titles | `splitOut` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Google Gemini Chat Model4 | `lmChatGoogleGemini` | Inspect parameters |
| Delete Collection | `httpRequest` | POST |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Chat Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Full Summary | `summarize` | Inspect parameters |
| Chat Buffer Memory1 | `memoryBufferWindow` | Inspect parameters |
| YouTube Transcript | `youtubeTranscripter` | Inspect parameters |
| Message Intent | `agent` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Update Context Intent | `redis` | set |
| Get Previous Context Intent | `redis` | get |
| Route Message Intent | `switch` | Inspect parameters |
| Process Status | `code` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Simple Memory3 | `memoryBufferWindow` | Inspect parameters |
| Google Gemini Chat Model6 | `lmChatGoogleGemini` | Inspect parameters |
| Numb of Videos | `agent` | Inspect parameters |
| Default Intent | `code` | Inspect parameters |
| Playlist Limit | `if` | Inspect parameters |
| Playlist or Video | `switch` | Inspect parameters |
| Get Fields for Summary | `code` | Inspect parameters |
| Update Context Process Done1 | `redis` | set |
| Google Gemini Chat Model8 | `lmChatGoogleGemini` | Inspect parameters |
| Playlist HTTP Request | `httpRequest` | Inspect parameters |
| YouTube Transcript1 | `youtubeTranscripter` | Inspect parameters |
| Video HTTP Request | `httpRequest` | Inspect parameters |
| Get Title and Desc | `code` | Inspect parameters |
| Split Out2 | `splitOut` | Inspect parameters |
| Concatenate1 | `summarize` | Inspect parameters |
| Get Videos | `code` | Inspect parameters |
| Get Playlist Videos Data | `code` | Inspect parameters |
| Embeddings Google Gemini2 | `embeddingsGoogleGemini` | Inspect parameters |
| Qdrant Vector Store3 | `vectorStoreQdrant` | Inspect parameters |
| Answer questions with a vector store | `toolVectorStore` | Inspect parameters |
| Qdrant Vector Store4 | `vectorStoreQdrant` | Inspect parameters |
| Answer questions with a vector store1 | `toolVectorStore` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Qdrant Vector Store2 | `vectorStoreQdrant` | Inspect parameters |
| Embeddings Google Gemini4 | `embeddingsGoogleGemini` | Inspect parameters |
| If | `if` | Inspect parameters |
| Count Content | `summarize` | Inspect parameters |
| Update Context Intent1 | `redis` | set |

## Connection map

- If → Update Context Intent1 (`main`, output 0, input 0)
- If → Playlist Limit (`main`, output 1, input 0)
- Chat → Get Previous Context Intent (`main`, output 0, input 0)
- Limit → YouTube Transcript (`main`, output 0, input 0)
- Limit → Video Titles (`main`, output 0, input 0)
- Merge → Summarize & Analyze Transcript (`main`, output 0, input 0)
- Split Out → Concatenate (`main`, output 0, input 0)
- Get Videos → Qdrant Vector Store (`main`, output 0, input 0)
- Split Out1 → Limit (`main`, output 0, input 0)
- Split Out2 → Concatenate1 (`main`, output 0, input 0)
- Concatenate → Merge (`main`, output 0, input 0)
- Edit Fields → Delete Collection (`main`, output 0, input 0)
- Concatenate1 → Merge (`main`, output 0, input 0)
- Full Summary → AI Agent (`main`, output 0, input 0)
- Video Titles → Merge (`main`, output 0, input 1)
- Count Content → If (`main`, output 0, input 0)
- Simple Memory → Message Intent (`ai_memory`, output 0, input 0)
- Default Intent → Route Message Intent (`main`, output 0, input 0)
- Message Intent → Default Intent (`main`, output 0, input 0)
- Playlist Limit → Numb of Videos (`main`, output 0, input 0)
- Playlist Limit → Playlist or Video (`main`, output 1, input 0)
- Process Status → Update Context Intent (`main`, output 0, input 0)
- Simple Memory3 → Numb of Videos (`ai_memory`, output 0, input 0)
- Delete Collection → Get Videos (`main`, output 0, input 0)
- Playlist or Video → Video HTTP Request (`main`, output 0, input 0)
- Playlist or Video → Playlist HTTP Request (`main`, output 1, input 0)
- Chat Buffer Memory → Handle Queries (`ai_memory`, output 0, input 0)
- Get Title and Desc → Merge (`main`, output 0, input 1)
- Video HTTP Request → YouTube Transcript1 (`main`, output 0, input 0)
- Video HTTP Request → Get Title and Desc (`main`, output 0, input 0)
- YouTube Transcript → Split Out (`main`, output 0, input 0)
- Chat Buffer Memory1 → AI Agent (`ai_memory`, output 0, input 0)
- Default Data Loader → Qdrant Vector Store (`ai_document`, output 0, input 0)
- Qdrant Vector Store → Update Context Process Done1 (`main`, output 0, input 0)
- YouTube Transcript1 → Split Out2 (`main`, output 0, input 0)
- Qdrant Vector Store2 → Count Content (`main`, output 0, input 0)
- Qdrant Vector Store3 → Answer questions with a vector store (`ai_vectorStore`, output 0, input 0)
- Qdrant Vector Store4 → Answer questions with a vector store1 (`ai_vectorStore`, output 0, input 0)
- Route Message Intent → Process Status (`main`, output 0, input 0)
- Route Message Intent → Handle Queries (`main`, output 1, input 0)
- Route Message Intent → Handle Queries (`main`, output 2, input 0)
- Playlist HTTP Request → Get Playlist Videos Data (`main`, output 0, input 0)
- Update Context Intent → Qdrant Vector Store2 (`main`, output 0, input 0)
- Get Fields for Summary → Full Summary (`main`, output 0, input 0)
- Update Context Intent1 → Handle Queries (`main`, output 0, input 0)
- Embeddings Google Gemini → Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- Get Playlist Videos Data → Split Out1 (`main`, output 0, input 0)
- Google Gemini Chat Model → Answer questions with a vector store1 (`ai_languageModel`, output 0, input 0)
- Embeddings Google Gemini1 → Qdrant Vector Store3 (`ai_embedding`, output 0, input 0)
- Embeddings Google Gemini2 → Qdrant Vector Store4 (`ai_embedding`, output 0, input 0)
- Embeddings Google Gemini4 → Qdrant Vector Store2 (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model1 → Handle Queries (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Summarize & Analyze Transcript (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model3 → Answer questions with a vector store (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model4 → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model6 → Message Intent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model8 → Numb of Videos (`ai_languageModel`, output 0, input 0)
- Structured Output Parser1 → Message Intent (`ai_outputParser`, output 0, input 0)
- Get Previous Context Intent → Message Intent (`main`, output 0, input 0)
- Update Context Process Done1 → Get Fields for Summary (`main`, output 0, input 0)
- Summarize & Analyze Transcript → Edit Fields (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Answer questions with a vector store → Handle Queries (`ai_tool`, output 0, input 0)
- Answer questions with a vector store1 → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0971_Limit_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/0971_Limit_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
