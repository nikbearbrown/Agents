# Automate Etsy Data Mining with Bright Data Scrape &amp; Google Gemini

Adapt the published “Automate Etsy Data Mining with Bright Data Scrape &amp; Google Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Set Esty Search Query"]
  n2["Perform Esty Web Request"]
  n3["Google Gemini Chat Model"]
  n4["Loop Over Items"]
  n5["Perform Esty web request over the loop"]
  n6["Initiate a Webhook Notification for the extracted data"]
  n7["Extract Item List with the Product Info"]
  n8["Google Gemini Chat Model for product info"]
  n9["Extract Paginated Resultset"]
  n10["Write the scraped content to disk"]
  n11["Create a binary data"]
  n12["Split Out"]
  n13["Extract Paginated Resultset With OpenAI"]
  n14["OpenAI Chat Model"]
  n12 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 1 to in 0"| n5
  n14 -->|"ai_languageModel out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n2
  n3 -->|"ai_languageModel out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n11
  n8 -->|"ai_languageModel out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n4
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
