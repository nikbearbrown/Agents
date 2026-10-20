# sendandwait telegram and set redis and get redis

Adapt the published “sendandwait telegram and set redis and get redis” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Human Handoff using Send and Wait"]
  n1["Set Interaction to Bot"]
  n2["Set Interaction to Human"]
  n3["Get Interaction State"]
  n4["Model"]
  n5["Memory"]
  n6["Handoff Subworkflow"]
  n7["Telegram Trigger"]
  n8["Send Response"]
  n9["Switch Interaction"]
  n10["Information Extractor"]
  n11["OpenAI Chat Model"]
  n12["With Defaults"]
  n13["Has All Criteria#63;"]
  n14["Onboarding Agent"]
  n15["Get Onboarding Chat History"]
  n16["After Sales Agent"]
  n17["Memory1"]
  n18["Model1"]
  n19["Handoff Tool"]
  n20["Handoff Subworkflow1"]
  n21["Send Response2"]
  n22["Memory2"]
  n23["Update Agent Memory"]
  n24["Send Response3"]
  n25["Get Canned Response"]
  n26["Notify user"]
  n27["Memory3"]
  n28["Update Agent Memory1"]
  n29["Continue Conversation"]
  n4 -->|"ai_languageModel out 0 to in 0"| n14
  n5 -->|"ai_memory out 0 to in 0"| n14
  n18 -->|"ai_languageModel out 0 to in 0"| n16
  n17 -->|"ai_memory out 0 to in 0"| n16
  n22 -->|"ai_memory out 0 to in 0"| n23
  n27 -->|"ai_memory out 0 to in 0"| n28
  n26 -->|"main out 0 to in 0"| n2
  n19 -->|"ai_tool out 0 to in 0"| n16
  n8 -->|"main out 0 to in 0"| n28
  n12 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n3
  n16 -->|"main out 0 to in 0"| n24
  n13 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 1 to in 0"| n29
  n11 -->|"ai_languageModel out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n25
  n9 -->|"main out 1 to in 0"| n16
  n9 -->|"main out 2 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n26
  n23 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n12
  n1 -->|"main out 0 to in 0"| n23
  n2 -->|"main out 0 to in 0"| n0
  n15 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n1
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
