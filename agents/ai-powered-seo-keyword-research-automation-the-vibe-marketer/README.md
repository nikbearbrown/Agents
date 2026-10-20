# AI powered SEO Keyword Research Automation - The vibe Marketer

Adapt the published “AI powered SEO Keyword Research Automation - The vibe Marketer” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Structured Output Parser"]
  n2["Topic Expansion"]
  n3["Competitor Analysis"]
  n4["Keyword Difficulty"]
  n5["Search Volume #38; CPC"]
  n6["split primary keywords"]
  n7["OpenAI Chat Model2"]
  n8["Keyword Ranking per URL"]
  n9["Final Keyword Strategy"]
  n10["Get Input from NocoDB"]
  n11["Split the Competitor URLs"]
  n12["Set relevant fields"]
  n13["OpenAI Chat Model1"]
  n14["Format Json and add Competitor URLs"]
  n15["Aggregate SV #38; CPC"]
  n16["Aggregate KWD"]
  n17["Merge SV, CPC #38; KWD"]
  n18["Merge Topic Expansion, SV, CPC #38; KWD"]
  n19["Aggregate Competitor Analysis"]
  n20["Merge Everything"]
  n21["Write Content Brief"]
  n22["Update Status - Done"]
  n23["Send Notification"]
  n24["Start Notification"]
  n25["Update Status - Started"]
  n16 -->|"main out 0 to in 1"| n17
  n2 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 1"| n18
  n20 -->|"main out 0 to in 0"| n9
  n0 -->|"ai_languageModel out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n16
  n13 -->|"ai_languageModel out 0 to in 0"| n3
  n7 -->|"ai_languageModel out 0 to in 0"| n9
  n3 -->|"main out 0 to in 0"| n19
  n17 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 2"| n20
  n12 -->|"main out 0 to in 0"| n25
  n12 -->|"main out 0 to in 0"| n24
  n10 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n3
  n1 -->|"ai_outputParser out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n8
  n19 -->|"main out 0 to in 1"| n20
  n14 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n20
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
