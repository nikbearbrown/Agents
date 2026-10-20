# Spot Workplace Discrimination Patterns with AI

Adapt the published “Spot Workplace Discrimination Patterns with AI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["OpenAI Chat Model1"]
  n2["OpenAI Chat Model2"]
  n3["Merge"]
  n4["OpenAI Chat Model"]
  n5["SET company_name"]
  n6["Define dictionary of demographic keys"]
  n7["ScrapingBee Search Glassdoor"]
  n8["Extract company url path"]
  n9["ScrapingBee GET company page contents"]
  n10["Extract reviews page url path"]
  n11["ScrapingBee GET Glassdoor Reviews Content"]
  n12["Extract Overall Review Summary"]
  n13["Extract Demographics Module"]
  n14["Extract overall ratings and distribution percentages"]
  n15["Extract demographic distributions"]
  n16["Define contributions to variance"]
  n17["Set variance and std_dev"]
  n18["Calculate P-Scores"]
  n19["Sort Effect Sizes"]
  n20["Calculate Z-Scores and Effect Sizes"]
  n21["Format dataset for scatterplot"]
  n22["Specify additional parameters for scatterplot"]
  n23["Quickchart Scatterplot"]
  n24["QuickChart Bar Chart"]
  n25["Text Analysis of Bias Data"]
  n3 -->|"main out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n6
  n4 -->|"ai_languageModel out 0 to in 0"| n25
  n19 -->|"main out 0 to in 0"| n24
  n19 -->|"main out 0 to in 0"| n25
  n18 -->|"main out 0 to in 0"| n19
  n1 -->|"ai_languageModel out 0 to in 0"| n15
  n2 -->|"ai_languageModel out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n14
  n21 -->|"main out 0 to in 0"| n22
  n16 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 1"| n3
  n0 -->|"main out 0 to in 0"| n5
  n20 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n12
  n22 -->|"main out 0 to in 0"| n23
  n14 -->|"main out 0 to in 0"| n16
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
