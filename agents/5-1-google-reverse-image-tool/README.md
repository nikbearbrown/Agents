# 5.1 Google Reverse Image Tool

Adapt the published “5.1 Google Reverse Image Tool” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Test workflow#34;"]
  n1["OpenAI Chat Model1"]
  n2["Get Applicable Rows"]
  n3["Execute Workflow Trigger"]
  n4["Edit Fields"]
  n5["Fallback Response"]
  n6["SERP Google Reverse Image API"]
  n7["Reverse Image Search Response"]
  n8["Reverse Image Search Tool"]
  n9["Firecrawl Scrape API"]
  n10["Scrape Success#63;"]
  n11["Firecrawl Scrape Success Response"]
  n12["Firecrawl scrape Error Response"]
  n13["Firecrawl Web Scaper Tool"]
  n14["Structured Output Parser"]
  n15["Enrich Product Rows"]
  n16["Analyse Image"]
  n17["Object Identifier Agent"]
  n18["Actions Router"]
  n4 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n6
  n18 -->|"main out 1 to in 0"| n9
  n18 -->|"main out 2 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n12
  n1 -->|"ai_languageModel out 0 to in 0"| n17
  n2 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n4
  n14 -->|"ai_outputParser out 0 to in 0"| n17
  n13 -->|"ai_tool out 0 to in 0"| n17
  n8 -->|"ai_tool out 0 to in 0"| n17
  n6 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n2
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
