# TechCrunch &amp; VentureBeat

Adapt the published “TechCrunch &amp; VentureBeat” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 35 executable nodes and 34 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Filter"]
  n2["Structured Output Parser"]
  n3["Perplexity"]
  n4["Filter1"]
  n5["Extract Structured Data"]
  n6["Research URL"]
  n7["Extract URL"]
  n8["Merge Extracted Data"]
  n9["Split TC Articles"]
  n10["TC HTML Parser"]
  n11["Split VB Articles"]
  n12["VB HTML Parser"]
  n13["Venturebeat #40;VB#41;"]
  n14["Techcrunch #40;TC#41;"]
  n15["Claude 3.5 Sonnet"]
  n16["Claude 3.5 Haiku"]
  n17["Collect Data"]
  n18["Airtable"]
  n19["Auto-fixing Output Parser"]
  n20["Extract Structured JSON"]
  n21["Prompts"]
  n22["Deep Research"]
  n23["Pick data #40;Perplexity#41;"]
  n24["Pick data #40;jina#41;"]
  n25["When Executed by Another Workflow"]
  n26["JINA Deep Search"]
  n27["Write Results to Airtable"]
  n28["Extract Structured Data"]
  n29["Route to Deep Research"]
  n30["Parse TC XML"]
  n31["Parse VB XML"]
  n32["Claude 3.5 Sonnet"]
  n33["Get Funding Article HTML for scraping #40;TC#41;"]
  n34["Get Funding Article HTML for scraping #40;VB#41;"]
  n1 -->|"main out 0 to in 0"| n33
  n4 -->|"main out 0 to in 0"| n34
  n21 -->|"main out 0 to in 0"| n22
  n3 -->|"ai_languageModel out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n29
  n17 -->|"main out 0 to in 0"| n18
  n30 -->|"main out 0 to in 0"| n9
  n31 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 0 to in 0"| n7
  n22 -->|"main out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 1"| n8
  n14 -->|"main out 0 to in 0"| n30
  n16 -->|"ai_languageModel out 0 to in 0"| n7
  n26 -->|"main out 0 to in 0"| n24
  n13 -->|"main out 0 to in 0"| n31
  n15 -->|"ai_languageModel out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n4
  n32 -->|"ai_languageModel out 0 to in 0"| n28
  n32 -->|"ai_languageModel out 0 to in 0"| n19
  n8 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n27
  n5 -->|"main out 0 to in 0"| n6
  n20 -->|"ai_outputParser out 0 to in 0"| n19
  n2 -->|"ai_outputParser out 0 to in 0"| n7
  n19 -->|"ai_outputParser out 0 to in 0"| n28
  n25 -->|"main out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n13
  n33 -->|"main out 0 to in 0"| n10
  n34 -->|"main out 0 to in 0"| n12
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
