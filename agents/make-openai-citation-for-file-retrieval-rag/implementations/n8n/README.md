# Make OpenAI Citation for File Retrieval RAG

This folder contains the **Make OpenAI Citation for File Retrieval RAG** workflow. Its executable nodes use `aggregate`, `chatTrigger`, `code`, `httpRequest`, `markdown`, `memoryBufferWindow`, `openAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`make-openai-citation-for-file-retrieval-rag.json`](make-openai-citation-for-file-retrieval-rag.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`

**Entry nodes:** Create a simple Trigger to have the Chat button within N8N

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Aggregate | `aggregate` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Create a simple Trigger to have the Chat button within N8N | `chatTrigger` | Inspect parameters |
| OpenAI Assistant with Vector Store | `openAi` | assistant |
| Get ALL Thread Content | `httpRequest` | Inspect parameters |
| Split all message iterations from a thread | `splitOut` | Inspect parameters |
| Split all content from a single message | `splitOut` | Inspect parameters |
| Split all citations from a single message | `splitOut` | Inspect parameters |
| Retrieve file name from a file ID | `httpRequest` | Inspect parameters |
| Regularize output | `set` | Inspect parameters |
| Optional Markdown to HTML | `markdown` | Inspect parameters |
| Finnaly format the output | `code` | Inspect parameters |

## Connection map

- Aggregate → Finnaly format the output (`main`, output 0, input 0)
- Regularize output → Aggregate (`main`, output 0, input 0)
- Window Buffer Memory → OpenAI Assistant with Vector Store (`ai_memory`, output 0, input 0)
- Get ALL Thread Content → Split all message iterations from a thread (`main`, output 0, input 0)
- Finnaly format the output → Optional Markdown to HTML (`main`, output 0, input 0)
- Retrieve file name from a file ID → Regularize output (`main`, output 0, input 0)
- OpenAI Assistant with Vector Store → Get ALL Thread Content (`main`, output 0, input 0)
- Split all content from a single message → Split all citations from a single message (`main`, output 0, input 0)
- Split all citations from a single message → Retrieve file name from a file ID (`main`, output 0, input 0)
- Split all message iterations from a thread → Split all content from a single message (`main`, output 0, input 0)
- Create a simple Trigger to have the Chat button within N8N → OpenAI Assistant with Vector Store (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1059_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1059_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
