# WooCommerce AI Chatbot Workflow for Post-Sales Support

Adapt the published “WooCommerce AI Chatbot Workflow for Post-Sales Support” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["Simple Memory"]
  n2["get_order"]
  n3["get_orders"]
  n4["get_user"]
  n5["Calculator"]
  n6["When clicking #8216;Test workflow#8217;"]
  n7["Create collection"]
  n8["Refresh collection"]
  n9["Get folder"]
  n10["Download Files"]
  n11["Default Data Loader"]
  n12["Token Splitter"]
  n13["Qdrant Vector Store1"]
  n14["Embeddings OpenAI1"]
  n15["Qdrant Vector Store"]
  n16["Embeddings OpenAI"]
  n17["OpenAI Chat Model"]
  n18["ToS"]
  n19["get_tracking"]
  n20["When Executed by Another Workflow"]
  n21["Post-Sales Agent"]
  n22["human_assistence"]
  n23["Get tracking"]
  n24["Set tracking code"]
  n25["GPT 4o-mini"]
  n18 -->|"ai_tool out 0 to in 0"| n21
  n4 -->|"ai_tool out 0 to in 0"| n21
  n2 -->|"ai_tool out 0 to in 0"| n21
  n5 -->|"ai_tool out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n10
  n3 -->|"ai_tool out 0 to in 0"| n21
  n25 -->|"ai_languageModel out 0 to in 0"| n21
  n23 -->|"main out 0 to in 0"| n24
  n19 -->|"ai_tool out 0 to in 0"| n21
  n1 -->|"ai_memory out 0 to in 0"| n21
  n10 -->|"main out 0 to in 0"| n13
  n12 -->|"ai_textSplitter out 0 to in 0"| n11
  n22 -->|"ai_tool out 0 to in 0"| n21
  n16 -->|"ai_embedding out 0 to in 0"| n15
  n17 -->|"ai_languageModel out 0 to in 0"| n18
  n14 -->|"ai_embedding out 0 to in 0"| n13
  n8 -->|"main out 0 to in 0"| n9
  n11 -->|"ai_document out 0 to in 0"| n13
  n15 -->|"ai_vectorStore out 0 to in 0"| n18
  n0 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n8
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
