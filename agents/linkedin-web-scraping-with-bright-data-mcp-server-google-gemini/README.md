# LinkedIn Web Scraping with Bright Data MCP Server &amp; Google Gemini

Adapt the published “LinkedIn Web Scraping with Bright Data MCP Server &amp; Google Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Set the URLs"]
  n2["Bright Data MCP Client For LinkedIn Person"]
  n3["List all tools for Bright Data"]
  n4["Bright Data MCP Client For LinkedIn Company"]
  n5["Set the LinkedIn Company URL"]
  n6["Webhook for LinkedIn Company Web Scraper"]
  n7["LinkedIn Data Extractor"]
  n8["Google Gemini Chat Model"]
  n9["List all available tools for Bright Data"]
  n10["Code"]
  n11["Merge"]
  n12["Aggregate"]
  n13["Create a binary data for LinkedIn person info extract"]
  n14["Write the LinkedIn person info to disk"]
  n15["Create a binary data for LinkedIn company info extract"]
  n16["Write the LinkedIn company info to disk"]
  n17["Webhook for LinkedIn Person Web Scraper"]
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 1"| n11
  n8 -->|"ai_languageModel out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n17
  n2 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n16
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
