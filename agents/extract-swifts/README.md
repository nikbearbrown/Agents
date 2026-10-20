# extract_swifts

Adapt the published “extract_swifts” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On clicking #39;execute#39;"]
  n1["HTTP Request"]
  n2["HTML Extract"]
  n3["SplitInBatches"]
  n4["HTTP Request1"]
  n5["HTML Extract1"]
  n6["MongoDB1"]
  n7["uProc"]
  n8["Prepare Documents"]
  n9["More Countries"]
  n10["Set Page to Scrape"]
  n11["More Pages"]
  n12["Set More Pages"]
  n13["Set"]
  n14["Generate filename"]
  n15["Read Binary File"]
  n16["File exists#63;"]
  n17["Write Binary File"]
  n18["Read Binary File1"]
  n19["Wait"]
  n20["Prepare countries"]
  n21["Create Directory"]
  n22["MongoDB"]
  n13 -->|"main out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 1 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 1 to in 0"| n19
  n2 -->|"main out 0 to in 0"| n20
  n1 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 1 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n11
  n3 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n1
  n15 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n3
  n18 -->|"main out 0 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n18
  n10 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n21
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
