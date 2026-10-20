# Get companies from database

Adapt the published “Get companies from database” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Text"]
  n1["URLs"]
  n2["OpenAI Chat Model"]
  n3["JSON Parser"]
  n4["Map company name and website"]
  n5["Execute workflow"]
  n6["Get companies"]
  n7["Select company name and website"]
  n8["Set social media array"]
  n9["Merge all data"]
  n10["Insert new row"]
  n11["Convert HTML to Markdown"]
  n12["Retrieve URLs"]
  n13["Split out URLs"]
  n14["Remove duplicated"]
  n15["Set domain to path"]
  n16["Filter out invalid URLs"]
  n17["Aggregate URLs"]
  n18["Filter out empty hrefs"]
  n19["Set domain #40;text#41;"]
  n20["Add protocool to domain #40;text#41;"]
  n21["Get website #40;text#41;"]
  n22["Set response #40;text#41;"]
  n23["Set domain #40;URL#41;"]
  n24["Get website #40;URL#41;"]
  n25["Set response #40;URL#41;"]
  n26["Add protocool to domain #40;URL#41;"]
  n27["Crawl website"]
  n0 -->|"ai_tool out 0 to in 0"| n27
  n1 -->|"ai_tool out 0 to in 0"| n27
  n3 -->|"ai_outputParser out 0 to in 0"| n27
  n27 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n25
  n9 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 0 to in 0"| n6
  n23 -->|"main out 0 to in 0"| n26
  n24 -->|"main out 0 to in 0"| n12
  n2 -->|"ai_languageModel out 0 to in 0"| n27
  n14 -->|"main out 0 to in 0"| n15
  n19 -->|"main out 0 to in 0"| n20
  n21 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n16
  n18 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 1"| n9
  n16 -->|"main out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n22
  n4 -->|"main out 0 to in 0"| n9
  n26 -->|"main out 0 to in 0"| n24
  n20 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n27
  n7 -->|"main out 0 to in 0"| n4
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
