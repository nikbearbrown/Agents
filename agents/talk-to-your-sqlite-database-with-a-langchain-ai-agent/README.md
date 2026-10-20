# talk to your sqlite database with a langchain ai agent

Adapt the published “talk to your sqlite database with a langchain ai agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Execute Workflow"]
  n2["Execute #34;Generate a chart#34; tool"]
  n3["OpenAI - Generate Chart definition with Structured Output"]
  n4["Set response"]
  n5["When chat message received"]
  n6["Set Text output"]
  n7["Set Text #43; Chart output"]
  n8["AI Agent"]
  n9["Window Buffer Memory"]
  n10["OpenAI Chat Model Classifier"]
  n11["Text Classifier - Chart required#63;"]
  n12["User question #43; Agent initial response"]
  n13["Information Extractor - User question"]
  n8 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n7
  n0 -->|"ai_languageModel out 0 to in 0"| n8
  n0 -->|"ai_languageModel out 0 to in 0"| n13
  n9 -->|"ai_memory out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n13
  n10 -->|"ai_languageModel out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 1 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n4
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
