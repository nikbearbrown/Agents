# Analyze Reddit Posts with AI to Identify Business Opportunities

Adapt the published “Analyze Reddit Posts with AI to Identify Business Opportunities” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["OpenAI Chat Model"]
  n2["OpenAI Chat Model1"]
  n3["OpenAI Chat Model2"]
  n4["Post Sentiment Analysis"]
  n5["Positive Posts Draft"]
  n6["Neutral Posts Draft"]
  n7["Negative Posts Draft"]
  n8["Find Proper Solutions"]
  n9["Post Summarization"]
  n10["Merge Input"]
  n11["Output The Results"]
  n12["Merge 3 Inputs"]
  n13["Filter Posts By Features"]
  n14["Filter Posts By Content"]
  n15["Select Key Fields"]
  n16["Analysis Content By AI"]
  n17["Get Posts"]
  n17 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n11
  n1 -->|"ai_languageModel out 0 to in 0"| n16
  n15 -->|"main out 0 to in 1"| n10
  n15 -->|"main out 0 to in 0"| n16
  n2 -->|"ai_languageModel out 0 to in 0"| n9
  n3 -->|"ai_languageModel out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 1"| n12
  n16 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 2"| n12
  n14 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 1 to in 0"| n6
  n4 -->|"main out 2 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n17
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
