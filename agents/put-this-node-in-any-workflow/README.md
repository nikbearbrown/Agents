# Put this node in any workflow.

Adapt the published “Put this node in any workflow.” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["AI Agent"]
  n2["OpenAI Chat Model"]
  n3["Window Buffer Memory"]
  n4["Vector Store Retriever"]
  n5["In-Memory Vector Store"]
  n6["Embeddings OpenAI"]
  n7["Question and Answer Chain"]
  n8["Switch"]
  n9["IF"]
  n10["Dummy Node"]
  n11["Dummy Node #40;1#41;"]
  n12["Loop Over Items"]
  n13["Dummy Node #40;2#41;"]
  n14["Dummy Node #40;3#41;"]
  n15["Dummy Node #40;4#41;"]
  n16["Dummy Node #40;5#41;"]
  n17["Dummy Node #40;6#41;"]
  n18["Dummy Node #40;7#41;"]
  n19["Dummy Node #40;8#41;"]
  n20["Dummy Node #40;9#41;"]
  n21["Dummy Tool"]
  n22["Dummy Tool #40;1#41;"]
  n23["OpenAI Chat Model #40;1#41;"]
  n24["Update n8n Workflow"]
  n25["Magic Positioning IA2S"]
  n26["POST /workflow/magic/position/id"]
  n27["Get n8n Workflow"]
  n28["Simple Webhook Response"]
  n29["Schedule Trigger"]
  n30["Magic Positioning"]
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 1 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n17
  n8 -->|"main out 1 to in 0"| n18
  n8 -->|"main out 2 to in 0"| n19
  n8 -->|"main out 3 to in 0"| n20
  n8 -->|"main out 4 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n14
  n21 -->|"ai_tool out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n12
  n22 -->|"ai_tool out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 1 to in 0"| n16
  n27 -->|"main out 0 to in 0"| n25
  n29 -->|"main out 0 to in 0"| n9
  n6 -->|"ai_embedding out 0 to in 0"| n5
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n28
  n3 -->|"ai_memory out 0 to in 0"| n1
  n23 -->|"ai_languageModel out 0 to in 0"| n7
  n5 -->|"ai_vectorStore out 0 to in 0"| n4
  n25 -->|"main out 0 to in 0"| n24
  n4 -->|"ai_retriever out 0 to in 0"| n7
  n26 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n9
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
