# Adaptive RAG

Adapt the published “Adaptive RAG” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Query Classification"]
  n1["Switch"]
  n2["Factual Strategy - Focus on Precision"]
  n3["Analytical Strategy - Comprehensive Coverage"]
  n4["Opinion Strategy - Diverse Perspectives"]
  n5["Contextual Strategy - User Context Integration"]
  n6["Chat"]
  n7["Factual Prompt and Output"]
  n8["Contextual Prompt and Output"]
  n9["Opinion Prompt and Output"]
  n10["Analytical Prompt and Output"]
  n11["Gemini Classification"]
  n12["Gemini Factual"]
  n13["Gemini Analytical"]
  n14["Chat Buffer Memory Analytical"]
  n15["Chat Buffer Memory Factual"]
  n16["Gemini Opinion"]
  n17["Chat Buffer Memory Opinion"]
  n18["Gemini Contextual"]
  n19["Chat Buffer Memory Contextual"]
  n20["Embeddings"]
  n21["Concatenate Context"]
  n22["Retrieve Documents from Vector Store"]
  n23["Set Prompt and Output"]
  n24["Gemini Answer"]
  n25["Answer"]
  n26["Chat Buffer Memory"]
  n27["Respond to Webhook"]
  n28["When Executed by Another Workflow"]
  n29["Combined Fields"]
  n6 -->|"main out 0 to in 0"| n29
  n25 -->|"main out 0 to in 0"| n27
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 1 to in 0"| n3
  n1 -->|"main out 2 to in 0"| n4
  n1 -->|"main out 3 to in 0"| n5
  n20 -->|"ai_embedding out 0 to in 0"| n22
  n24 -->|"ai_languageModel out 0 to in 0"| n25
  n12 -->|"ai_languageModel out 0 to in 0"| n2
  n16 -->|"ai_languageModel out 0 to in 0"| n4
  n29 -->|"main out 0 to in 0"| n0
  n13 -->|"ai_languageModel out 0 to in 0"| n3
  n18 -->|"ai_languageModel out 0 to in 0"| n5
  n26 -->|"ai_memory out 0 to in 0"| n25
  n21 -->|"main out 0 to in 0"| n25
  n0 -->|"main out 0 to in 0"| n1
  n11 -->|"ai_languageModel out 0 to in 0"| n0
  n23 -->|"main out 0 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n23
  n9 -->|"main out 0 to in 0"| n23
  n15 -->|"ai_memory out 0 to in 0"| n2
  n17 -->|"ai_memory out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n23
  n8 -->|"main out 0 to in 0"| n23
  n14 -->|"ai_memory out 0 to in 0"| n3
  n19 -->|"ai_memory out 0 to in 0"| n5
  n28 -->|"main out 0 to in 0"| n29
  n22 -->|"main out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n8
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
