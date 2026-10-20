# AI Document Assistant via Telegram + Supabase

This folder contains the **AI Document Assistant via Telegram + Supabase** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `documentDefaultDataLoader`, `embeddingsGoogleGemini`, `extractFromFile`, `lmChatGoogleGemini`, `memoryBufferWindow`, `openWeatherMapTool`, `set`, `splitOut`, `switch`, `telegram`, `telegramTrigger`, `textSplitterRecursiveCharacterTextSplitter`, `toolThink`, `toolVectorStore`, `vectorStoreSupabase`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-document-assistant-via-telegram-supabase.json`](ai-document-assistant-via-telegram-supabase.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `openWeatherMapApi`, `supabaseApi`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| OpenWeatherMap | `openWeatherMapTool` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Think | `toolThink` | Inspect parameters |
| Embeddings Google Gemini | `embeddingsGoogleGemini` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Recursive Character Text Splitter | `textSplitterRecursiveCharacterTextSplitter` | Inspect parameters |
| Extract from File | `extractFromFile` | pdf |
| Answer questions with a vector store | `toolVectorStore` | Inspect parameters |
| Supabase Vector Store | `vectorStoreSupabase` | Inspect parameters |
| Telegram - Embedding Complete | `telegram` | Inspect parameters |
| Supabase - Save Embeddings | `vectorStoreSupabase` | Inspect parameters |
| Command Router | `switch` | Inspect parameters |
| Telegram - Download file | `telegram` | file |
| Aggregate | `aggregate` | Inspect parameters |
| Fallback- No formatting | `telegram` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Handle formatting and split | `code` | Inspect parameters |
| Manual Mapping | `set` | Inspect parameters |
| Unsupported message | `telegram` | Inspect parameters |
| Send processing document message | `telegram` | Inspect parameters |
| Send embedding Started message | `telegram` | Inspect parameters |

## Connection map

- Think → AI Agent (`ai_tool`, output 0, input 0)
- AI Agent → Handle formatting and split (`main`, output 0, input 0)
- Telegram → Fallback- No formatting (`main`, output 1, input 0)
- Aggregate → Telegram - Embedding Complete (`main`, output 0, input 0)
- Split Out → Manual Mapping (`main`, output 0, input 0)
- Simple Memory → AI Agent (`ai_memory`, output 0, input 0)
- Command Router → Telegram - Download file (`main`, output 0, input 0)
- Command Router → AI Agent (`main`, output 1, input 0)
- Command Router → Unsupported message (`main`, output 2, input 0)
- Manual Mapping → Telegram (`main`, output 0, input 0)
- OpenWeatherMap → AI Agent (`ai_tool`, output 0, input 0)
- Telegram Trigger → Command Router (`main`, output 0, input 0)
- Extract from File → Supabase - Save Embeddings (`main`, output 0, input 0)
- Extract from File → Send embedding Started message (`main`, output 0, input 0)
- Default Data Loader → Supabase - Save Embeddings (`ai_document`, output 0, input 0)
- Supabase Vector Store → Answer questions with a vector store (`ai_vectorStore`, output 0, input 0)
- Embeddings Google Gemini → Supabase - Save Embeddings (`ai_embedding`, output 0, input 0)
- Embeddings Google Gemini → Supabase Vector Store (`ai_embedding`, output 0, input 0)
- Google Gemini Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model → Answer questions with a vector store (`ai_languageModel`, output 0, input 0)
- Telegram - Download file → Extract from File (`main`, output 0, input 0)
- Telegram - Download file → Send processing document message (`main`, output 0, input 0)
- Supabase - Save Embeddings → Aggregate (`main`, output 0, input 0)
- Handle formatting and split → Split Out (`main`, output 0, input 0)
- Recursive Character Text Splitter → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Answer questions with a vector store → AI Agent (`ai_tool`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1539_Telegram_Splitout_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1539_Telegram_Splitout_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
