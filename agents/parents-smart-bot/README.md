# Parents smart bot

Adapt the published “Parents smart bot” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Ultimate Assistant"]
  n2["Email Agent"]
  n3["Contact Agent"]
  n4["Content Creator Agent"]
  n5["Tavily"]
  n6["Calendar Agent"]
  n7["Download File"]
  n8["Transcribe"]
  n9["Calculator1"]
  n10["Set #39;Text#39;1"]
  n11["Switch1"]
  n12["Response1"]
  n13["Wikipedia"]
  n14["Qdrant Vector Store"]
  n15["Default Data Loader"]
  n16["Recursive Character Text Splitter"]
  n17["OpenAI Chat Model"]
  n18["Embeddings OpenAI1"]
  n19["Qdrant Vector Store1"]
  n20["Embeddings OpenAI"]
  n21["Window Buffer Memory"]
  n22["Download File1"]
  n23["Code"]
  n24["If"]
  n25["Edit Fields"]
  n26["Edit Fields1"]
  n2 -->|"ai_tool out 0 to in 0"| n1
  n3 -->|"ai_tool out 0 to in 0"| n1
  n4 -->|"ai_tool out 0 to in 0"| n1
  n5 -->|"ai_tool out 0 to in 0"| n1
  n6 -->|"ai_tool out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n1
  n9 -->|"ai_tool out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n24
  n11 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 1 to in 0"| n10
  n11 -->|"main out 2 to in 0"| n22
  n13 -->|"ai_tool out 0 to in 0"| n1
  n15 -->|"ai_document out 0 to in 0"| n14
  n16 -->|"ai_textSplitter out 0 to in 0"| n15
  n17 -->|"ai_languageModel out 0 to in 0"| n1
  n18 -->|"ai_embedding out 0 to in 0"| n14
  n19 -->|"ai_tool out 0 to in 0"| n1
  n20 -->|"ai_embedding out 0 to in 0"| n19
  n21 -->|"ai_memory out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n11
  n22 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 1 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n25
  n24 -->|"main out 1 to in 0"| n1
  n25 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n1
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
