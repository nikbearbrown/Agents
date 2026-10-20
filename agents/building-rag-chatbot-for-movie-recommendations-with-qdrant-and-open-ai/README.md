# Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

Adapt the published “Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["GitHub"]
  n2["Extract from File"]
  n3["Embeddings OpenAI"]
  n4["Default Data Loader"]
  n5["Token Splitter"]
  n6["Qdrant Vector Store"]
  n7["When chat message received"]
  n8["OpenAI Chat Model"]
  n9["Call n8n Workflow Tool"]
  n10["Window Buffer Memory"]
  n11["Execute Workflow Trigger"]
  n12["Merge"]
  n13["Split Out"]
  n14["Split Out1"]
  n15["Merge1"]
  n16["Aggregate"]
  n17["AI Agent"]
  n18["Embedding Recommendation Request with Open AI"]
  n19["Embedding Anti-Recommendation Request with Open AI"]
  n20["Extracting Embedding"]
  n21["Extracting Embedding1"]
  n22["Calling Qdrant Recommendation API"]
  n23["Retrieving Recommended Movies Meta Data"]
  n24["Selecting Fields Relevant for Agent"]
  n12 -->|"main out 0 to in 0"| n22
  n1 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n24
  n13 -->|"main out 0 to in 1"| n15
  n14 -->|"main out 0 to in 0"| n15
  n5 -->|"ai_textSplitter out 0 to in 0"| n4
  n3 -->|"ai_embedding out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n6
  n8 -->|"ai_languageModel out 0 to in 0"| n17
  n4 -->|"ai_document out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n12
  n10 -->|"ai_memory out 0 to in 0"| n17
  n21 -->|"main out 0 to in 1"| n12
  n9 -->|"ai_tool out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n18
  n11 -->|"main out 0 to in 0"| n19
  n7 -->|"main out 0 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n23
  n22 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n16
  n23 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n21
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/zie619-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
