# Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool

Adapt the published “Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 12 executable nodes and 11 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Structured Output Parser"]
  n1["OpenAI Chat Model"]
  n2["Get rows from Google Sheet"]
  n3["Call n8n workflow : Scrape companies homepage content"]
  n4["Update Company#39;s Row on Google Sheet"]
  n5["ScrapingBee : Scrape company#39;s homepage data"]
  n6["Tool called from Agent"]
  n7["Loop Over Items"]
  n8["AI Agent"]
  n9["Set company url"]
  n10["HTML to Markdown"]
  n11["Webhook"]
  n11 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 1 to in 0"| n8
  n9 -->|"main out 0 to in 0"| n5
  n1 -->|"ai_languageModel out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n9
  n0 -->|"ai_outputParser out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n10
  n3 -->|"ai_tool out 0 to in 0"| n8
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
