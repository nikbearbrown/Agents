# Local chatbot with retrieval augmented generation (RAG) Gemini

Adapt the published “Local chatbot with retrieval augmented generation (RAG) Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Embeddings Ollama"]
  n1["Default Data Loader"]
  n2["Recursive Character Text Splitter"]
  n3["When chat message received"]
  n4["On form submission1"]
  n5["Qdrant Vector Store"]
  n6["AI Agent1"]
  n7["Simple Memory1"]
  n8["Embeddings Ollama2"]
  n9["Qdrant Vector Store2"]
  n10["Google Gemini Chat Model"]
  n11["HTTP Request"]
  n12["Merge"]
  n0 -->|"ai_embedding out 0 to in 0"| n5
  n1 -->|"ai_document out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n12
  n2 -->|"ai_textSplitter out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n5
  n7 -->|"ai_memory out 0 to in 0"| n6
  n9 -->|"ai_tool out 0 to in 0"| n6
  n8 -->|"ai_embedding out 0 to in 0"| n9
  n10 -->|"ai_languageModel out 0 to in 0"| n6
  n6 -->|"main out 0 to in 1"| n12
  n12 -->|"main out 0 to in 0"| n11
```

[Diagram source](workflow.mmd)

## Implementations

| Implementation | Status |
|---|---|
| [n8n](implementations/n8n/README.md) | Sanitized source available; not runtime-tested |
| [Plain Python](implementations/python/README.md) | Planned |
| [Pydantic AI](implementations/pydantic-ai/README.md) | Planned |
| [CrewAI Flow](implementations/crewai-flow/README.md) | Planned |
| [CrewAI Crew](implementations/crewai-crew/README.md) | Planned |
| [LangGraph](implementations/langgraph/README.md) | Planned |

## Build or operate with an assistant

[Claude](prompts/claude.md) · [Codex](prompts/codex.md) · [Grok Bot](prompts/grok-bot.md) · [Muse](prompts/muse.md) · [Dots](prompts/dots.md)

Build instructions and operating instructions are separate. These are untested prompts, not additional working implementations.

## Attribution

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/algonacci--rag-evaluation.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
