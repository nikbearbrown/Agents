# Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI

Adapt the published “Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split Out"]
  n1["Information Extractor"]
  n2["If"]
  n3["When clicking #8216;Test workflow#8217;"]
  n4["Limit1"]
  n5["Set Parameters"]
  n6["Get reviews"]
  n7["Extract"]
  n8["Get rows"]
  n9["Get Google Sheets"]
  n10["Get Single review"]
  n11["Extract review"]
  n12["Update sheet"]
  n13["Sentiment Analysis"]
  n14["DeepSeek Chat Model"]
  n15["OpenAI Chat Model"]
  n2 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n0
  n8 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n11
  n15 -->|"ai_languageModel out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 1 to in 0"| n12
  n13 -->|"main out 2 to in 0"| n12
  n14 -->|"ai_languageModel out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n5
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
