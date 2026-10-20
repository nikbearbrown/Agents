# download google drive and http request and upload to drive

Adapt the published “download google drive and http request and upload to drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Base Image"]
  n1["Google Gemini Chat Model"]
  n2["Structured Output Parser"]
  n3["Loop Over Items"]
  n4["Wait"]
  n5["Download Screenshot"]
  n6["Upload to Drive"]
  n7["Update Base Image"]
  n8["Merge"]
  n9["Schedule Trigger"]
  n10["Get URLs with Missing Base Images"]
  n11["Run Webpage Screenshot"]
  n12["Run Webpage Screenshot1"]
  n13["Has Changes"]
  n14["Combine Row and Result"]
  n15["Wait1"]
  n16["Aggregate"]
  n17["Create Report"]
  n18["When clicking #8216;Test workflow#8217;"]
  n19["Get Webpages List"]
  n20["For Each Webpage..."]
  n21["Download New Screenshot"]
  n22["Combine Screenshots"]
  n23["Visual Regression Agent"]
  n4 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n22
  n13 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 0 to in 1"| n8
  n3 -->|"main out 1 to in 0"| n11
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n20
  n22 -->|"main out 0 to in 0"| n23
  n5 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 1 to in 0"| n0
  n20 -->|"main out 1 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n4
  n21 -->|"main out 0 to in 1"| n22
  n12 -->|"main out 0 to in 0"| n21
  n23 -->|"main out 0 to in 0"| n15
  n1 -->|"ai_languageModel out 0 to in 0"| n23
  n2 -->|"ai_outputParser out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n8
  n18 -->|"main out 0 to in 0"| n10
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
