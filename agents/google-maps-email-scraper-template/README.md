# Google Maps Email Scraper Template

Adapt the published “Google Maps Email Scraper Template” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Remove Duplicate URLs"]
  n1["Loop over queries"]
  n2["Search Google Maps with query"]
  n3["Scrape URLs from results"]
  n4["Filter irrelevant URLs"]
  n5["Request web page for URL"]
  n6["Loop over URLs"]
  n7["Loop over pages"]
  n8["Scrape emails from page"]
  n9["Aggregate arrays of emails"]
  n10["Split out into default data structure"]
  n11["Remove duplicate emails"]
  n12["Filter irrelevant emails"]
  n13["Save emails to Google Sheet"]
  n14["Starts scraper workflow"]
  n15["Run workflow"]
  n16["Wait between executions"]
  n17["Execute scraper for query"]
  n15 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 1 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 1 to in 0"| n8
  n1 -->|"main out 1 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n4
  n17 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n11
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
