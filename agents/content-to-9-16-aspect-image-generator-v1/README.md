# Content to 9:16 Aspect Image Generator v1

Adapt the published “Content to 9:16 Aspect Image Generator v1” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Set Guidelines"]
  n2["Get Brand Guidelines"]
  n3["Get SEO Keywords"]
  n4["Remove Duplicates"]
  n5["Keyword Filter"]
  n6["Get Content"]
  n7["Split Out Content"]
  n8["Split Out Keywords"]
  n9["Limit"]
  n10["Script Prep"]
  n11["Split Out Scenes"]
  n12["Split Out TN Prompt"]
  n13["Leo - Improve Prompt1"]
  n14["Leo - Get imageId1"]
  n15["Prompt Settings"]
  n16["Leo - Generate Image1"]
  n17["Wait 30 Seconds"]
  n18["Leo - Improve Prompt"]
  n19["Leo - Get imageId"]
  n20["Prompt Settings1"]
  n21["Leo - Generate Image"]
  n22["Wait 30 Seconds1"]
  n23["Loop Over Items"]
  n24["Add Asset Info"]
  n25["Add Asset Info1"]
  n26["Wikipedia"]
  n9 -->|"main out 0 to in 0"| n10
  n26 -->|"ai_tool out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n3
  n25 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 1 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n5
  n20 -->|"main out 0 to in 0"| n18
  n11 -->|"main out 0 to in 0"| n23
  n22 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n25
  n4 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n1
  n21 -->|"main out 0 to in 0"| n22
  n18 -->|"main out 0 to in 0"| n21
  n16 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n16
  n0 -->|"main out 0 to in 0"| n2
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
