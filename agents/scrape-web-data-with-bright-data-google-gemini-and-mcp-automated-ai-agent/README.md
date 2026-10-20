# Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent

Adapt the published “Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["When clicking #8216;Test workflow#8217;"]
  n2["MCP Client list all tools for Bright Data"]
  n3["MCP Client List all tools"]
  n4["MCP Client Bright Data Web Scraper"]
  n5["Webhook for web scraper"]
  n6["Set the URLs"]
  n7["MCP Client to Scrape as Markdown"]
  n8["MCP Client to Scrape as HTML"]
  n9["Google Gemini Chat Model for AI Agent"]
  n10["Simple Memory"]
  n11["Webhook for Web Scraper AI Agent"]
  n12["Set the URL with the Webhook URL and data format"]
  n13["Create a binary data"]
  n14["Write the scraped content to disk"]
  n0 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n4
  n10 -->|"ai_memory out 0 to in 0"| n0
  n13 -->|"main out 0 to in 0"| n14
  n3 -->|"ai_tool out 0 to in 0"| n0
  n8 -->|"ai_tool out 0 to in 0"| n0
  n7 -->|"ai_tool out 0 to in 0"| n0
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n5
  n9 -->|"ai_languageModel out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n0
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
