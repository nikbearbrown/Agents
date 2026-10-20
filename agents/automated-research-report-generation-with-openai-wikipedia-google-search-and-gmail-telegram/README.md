# Automated Research Report Generation with OpenAI, Wikipedia, Google Search, and Gmail/Telegram

Adapt the published “Automated Research Report Generation with OpenAI, Wikipedia, Google Search, and Gmail/Telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Simple Memory"]
  n2["Search News"]
  n3["Wikipedia"]
  n4["OpenAI Chat Model1"]
  n5["Query Refiner"]
  n6["Research AI Agent"]
  n7["Google Search Web"]
  n8["SerpApi"]
  n9["Structured Output Parser"]
  n10["Split Out"]
  n11["Input Validation"]
  n12["Parse Research Output"]
  n13["Merge Split Items"]
  n14["Store Research Metadata"]
  n15["Generate PDF HTML"]
  n16["Convert HTML to PDF"]
  n17["Aggregate"]
  n18["Download PDF"]
  n19["Send Research to Gmail"]
  n20["When clicking #8216;Test workflow#8217;"]
  n21["Send PDF"]
  n22["Executed by Main AI Agent"]
  n23["Search Folder"]
  n24["If"]
  n8 -->|"ai_tool out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n14
  n17 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n13
  n3 -->|"ai_tool out 0 to in 0"| n6
  n2 -->|"ai_tool out 0 to in 0"| n6
  n18 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n6
  n23 -->|"main out 0 to in 0"| n24
  n1 -->|"ai_memory out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n16
  n7 -->|"ai_tool out 0 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n17
  n0 -->|"ai_languageModel out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n12
  n4 -->|"ai_languageModel out 0 to in 0"| n5
  n16 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 0 to in 0"| n23
  n12 -->|"main out 0 to in 0"| n10
  n9 -->|"ai_outputParser out 0 to in 0"| n5
  n20 -->|"main out 0 to in 0"| n11
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
