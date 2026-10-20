# YogiAI

Adapt the published “YogiAI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Azure OpenAI Chat Model2"]
  n1["YogaLog"]
  n2["Azure OpenAI Chat Model3"]
  n3["Auto-fixing Output Parser"]
  n4["Azure OpenAI Chat Model1"]
  n5["Structured Output Parser"]
  n6["AI Agent"]
  n7["PosesDatabase1"]
  n8["YogaLog2"]
  n9["Split Out"]
  n10["Trigger 2130 YogaPosesToday"]
  n11["Azure OpenAI Chat Model5"]
  n12["Get PoseName"]
  n13["WritePosesToday"]
  n14["RewritePosesToday"]
  n15["Azure OpenAI Chat Model"]
  n16["WriteJSONflex"]
  n17["Structured Output Parser1"]
  n18["Auto-fixing Output Parser1"]
  n19["Azure OpenAI Chat Model6"]
  n20["Azure OpenAI Chat Model4"]
  n21["Code"]
  n22["Line Push with Flex Bubble"]
  n23["CombineAll"]
  n24["Fix JSON"]
  n21 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n8
  n23 -->|"main out 0 to in 0"| n24
  n12 -->|"main out 0 to in 0"| n21
  n16 -->|"main out 0 to in 0"| n13
  n7 -->|"ai_tool out 0 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n23
  n15 -->|"ai_languageModel out 0 to in 0"| n16
  n4 -->|"ai_languageModel out 0 to in 0"| n3
  n0 -->|"ai_languageModel out 0 to in 0"| n13
  n2 -->|"ai_languageModel out 0 to in 0"| n6
  n20 -->|"ai_languageModel out 0 to in 0"| n24
  n11 -->|"ai_languageModel out 0 to in 0"| n14
  n19 -->|"ai_languageModel out 0 to in 0"| n18
  n5 -->|"ai_outputParser out 0 to in 0"| n3
  n3 -->|"ai_outputParser out 0 to in 0"| n6
  n17 -->|"ai_outputParser out 0 to in 0"| n18
  n18 -->|"ai_outputParser out 0 to in 0"| n16
  n22 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n12
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
