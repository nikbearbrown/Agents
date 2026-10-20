# Embed your Vector Store

This folder contains the **Embed your Vector Store** workflow. Its executable nodes use `agent`, `chatTrigger`, `documentDefaultDataLoader`, `embeddingsOpenAi`, `extractFromFile`, `googleDrive`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `noOp`, `outputParserStructured`, `splitInBatches`, `splitOut`, `textSplitterTokenSplitter`, `vectorStoreQdrant`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`embed-your-vector-store.json`](embed-your-vector-store.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `qdrantApi`, `zendeskApi`

**Entry nodes:** When chat message received, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Embeddings OpenAI1 | `embeddingsOpenAi` | Inspect parameters |
| Default Data Loader | `documentDefaultDataLoader` | Inspect parameters |
| Token Splitter1 | `textSplitterTokenSplitter` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Embeddings OpenAI2 | `embeddingsOpenAi` | Inspect parameters |
| Extract from File | `extractFromFile` | fromJson |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| AI Agent1 | `agent` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Embeddings OpenAI | `embeddingsOpenAi` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Pull Mitre Data From Gdrive | `googleDrive` | download |
| Embed JSON in Qdrant Collection | `vectorStoreQdrant` | Inspect parameters |
| Query Qdrant Vector Store | `vectorStoreQdrant` | Inspect parameters |
| Qdrant Vector Store query | `vectorStoreQdrant` | Inspect parameters |
| Get all Zendesk Tickets | `zendesk` | getAll |
| Update Zendesk with Mitre Data | `zendesk` | update |
| Move on to next ticket | `noOp` | Inspect parameters |

## Connection map

- AI Agent1 → Update Zendesk with Mitre Data (`main`, output 0, input 0)
- Split Out → Embed JSON in Qdrant Collection (`main`, output 0, input 0)
- Loop Over Items → AI Agent1 (`main`, output 1, input 0)
- Token Splitter1 → Default Data Loader (`ai_textSplitter`, output 0, input 0)
- Embeddings OpenAI → Qdrant Vector Store query (`ai_embedding`, output 0, input 0)
- Extract from File → Split Out (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Embeddings OpenAI1 → Embed JSON in Qdrant Collection (`ai_embedding`, output 0, input 0)
- Embeddings OpenAI2 → Query Qdrant Vector Store (`ai_embedding`, output 0, input 0)
- OpenAI Chat Model1 → AI Agent1 (`ai_languageModel`, output 0, input 0)
- Default Data Loader → Embed JSON in Qdrant Collection (`ai_document`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Move on to next ticket → Loop Over Items (`main`, output 0, input 0)
- Get all Zendesk Tickets → Loop Over Items (`main`, output 0, input 0)
- Structured Output Parser → AI Agent1 (`ai_outputParser`, output 0, input 0)
- Qdrant Vector Store query → AI Agent1 (`ai_tool`, output 0, input 0)
- Query Qdrant Vector Store → AI Agent (`ai_tool`, output 0, input 0)
- When chat message received → AI Agent (`main`, output 0, input 0)
- Pull Mitre Data From Gdrive → Extract from File (`main`, output 0, input 0)
- Update Zendesk with Mitre Data → Move on to next ticket (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Pull Mitre Data From Gdrive (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1332_Splitout_Zendesk_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1332_Splitout_Zendesk_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
