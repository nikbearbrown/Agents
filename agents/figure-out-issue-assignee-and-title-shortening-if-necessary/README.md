# Figure out issue assignee and title (shortening if necessary)

Adapt the published “Figure out issue assignee and title (shortening if necessary)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Loop Over Items"]
  n1["Fetch Linear team details"]
  n2["Get issue contents"]
  n3["Aggregate"]
  n4["Prepare issue data"]
  n5["Create linear issue"]
  n6["Set assignee and title"]
  n7["Team missing#63;"]
  n8["Set page URL"]
  n9["Set team ID"]
  n10["Add link to Notion block"]
  n11["Get issue URL"]
  n12["Shorten title"]
  n13["Unimported, unchecked to_do blocks only"]
  n14["n8n Form Trigger"]
  n15["Get issues"]
  n16["Convert contents to Markdown"]
  n17["Respond with error"]
  n18["Respond with error1"]
  n3 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 1 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n16
  n11 -->|"main out 0 to in 0"| n10
  n12 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n18
  n7 -->|"main out 1 to in 0"| n9
  n0 -->|"main out 1 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n0
  n1 -->|"main out 0 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n0
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
