# text classifier and list message discord and removeitemsseeninpreviousexecutions remove duplicates

Adapt the published “text classifier and list message discord and removeitemsseeninpreviousexecutions remove duplicates” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Spam Detection"]
  n1["Get Recent Messages"]
  n2["Only Once"]
  n3["Model"]
  n4["Warn User"]
  n5["Warn User Only"]
  n6["Group By User"]
  n7["For Each User..."]
  n8["Split Out"]
  n9["Message to List"]
  n10["Notify Moderators with Send #38; Wait"]
  n11["Flag as Spam"]
  n12["Flag as Not Spam"]
  n13["Merge"]
  n14["Spam Messages Only"]
  n15["Has Flagged Messages#63;"]
  n16["Get Message IDs"]
  n17["Delete Messages"]
  n18["Receive Instructions"]
  n19["Moderation Subworkflow"]
  n20["When Executed by Another Workflow"]
  n21["No Action Taken"]
  n22["Schedule Trigger"]
  n13 -->|"main out 0 to in 0"| n14
  n3 -->|"ai_languageModel out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 1 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n4
  n16 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 1"| n13
  n7 -->|"main out 1 to in 0"| n9
  n22 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n2
  n18 -->|"main out 0 to in 0"| n16
  n18 -->|"main out 1 to in 0"| n5
  n18 -->|"main out 2 to in 0"| n21
  n15 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 1 to in 0"| n7
  n19 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n18
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
