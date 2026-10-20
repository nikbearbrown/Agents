# Business Canvas Generator

Adapt the published “Business Canvas Generator” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 42 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["Key Partners Generator"]
  n2["Key Activities Generator"]
  n3["Value Proposition Generator"]
  n4["Customer Relationship Generator"]
  n5["Customer Segments Generator"]
  n6["Ollama Chat Model"]
  n7["Key Resources Generator"]
  n8["Channels Generator"]
  n9["Cost Structure Generator"]
  n10["Title Generator"]
  n11["Revenue Streams Generator"]
  n12["Key Partners HTML Transformer"]
  n13["Key Activities HTML Transformer"]
  n14["Values proposition HTML Transformer"]
  n15["Customer Relationship HTML Transformer"]
  n16["Customer Segments HTML Transformer"]
  n17["Key Resources HTML Transformer"]
  n18["Channels HTML Transformer"]
  n19["Revenue streams HTML Transformer"]
  n20["Code1"]
  n21["Cost Structure HTML Transformer"]
  n22["Turn to HTML"]
  n23["HTML code to HTML file"]
  n24["Merge All Data"]
  n20 -->|"main out 0 to in 0"| n24
  n22 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n22
  n10 -->|"main out 0 to in 0"| n20
  n6 -->|"ai_languageModel out 0 to in 0"| n1
  n6 -->|"ai_languageModel out 0 to in 0"| n2
  n6 -->|"ai_languageModel out 0 to in 0"| n3
  n6 -->|"ai_languageModel out 0 to in 0"| n4
  n6 -->|"ai_languageModel out 0 to in 0"| n5
  n6 -->|"ai_languageModel out 0 to in 0"| n7
  n6 -->|"ai_languageModel out 0 to in 0"| n8
  n6 -->|"ai_languageModel out 0 to in 0"| n9
  n6 -->|"ai_languageModel out 0 to in 0"| n10
  n6 -->|"ai_languageModel out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 0 to in 7"| n24
  n11 -->|"main out 0 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 1"| n24
  n17 -->|"main out 0 to in 6"| n24
  n21 -->|"main out 0 to in 8"| n24
  n4 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 2"| n24
  n19 -->|"main out 0 to in 9"| n24
  n16 -->|"main out 0 to in 5"| n24
  n14 -->|"main out 0 to in 3"| n24
  n15 -->|"main out 0 to in 4"| n24
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
