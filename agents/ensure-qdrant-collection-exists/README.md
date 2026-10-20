# 🚨Ensure Qdrant collection exists!

Adapt the published “🚨Ensure Qdrant collection exists!” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Test workflow#34;"]
  n1["Get This Week#39;s Menu"]
  n2["Extract Available Courses"]
  n3["Extract Server Data"]
  n4["Get Course Metadata"]
  n5["Get Recipe"]
  n6["Embeddings Mistral Cloud"]
  n7["Default Data Loader"]
  n8["Merge Course #38; Recipe"]
  n9["Prepare Documents"]
  n10["Recursive Character Text Splitter"]
  n11["Chat Trigger"]
  n12["Extract Recipe Details"]
  n13["Qdrant Recommend API"]
  n14["Execute Workflow Trigger"]
  n15["Mistral Cloud Chat Model"]
  n16["Get Tool Response"]
  n17["Wait for Rate Limits"]
  n18["Get Mistral Embeddings"]
  n19["Use Qdrant Recommend API"]
  n20["Get Recipes From DB"]
  n21["Save Recipes to DB"]
  n22["AI Agent"]
  n23["Qdrant Vector Store"]
  n5 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n23
  n9 -->|"main out 0 to in 0"| n21
  n7 -->|"ai_document out 0 to in 0"| n23
  n3 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n8
  n20 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n3
  n13 -->|"ai_tool out 0 to in 0"| n22
  n17 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 1"| n8
  n18 -->|"main out 0 to in 0"| n19
  n6 -->|"ai_embedding out 0 to in 0"| n23
  n14 -->|"main out 0 to in 0"| n17
  n15 -->|"ai_languageModel out 0 to in 0"| n22
  n19 -->|"main out 0 to in 0"| n20
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n10 -->|"ai_textSplitter out 0 to in 0"| n7
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
