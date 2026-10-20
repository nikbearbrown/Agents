# Workflow management

Adapt the published “Workflow management” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On clicking #39;execute#39;"]
  n1["Function"]
  n2["SplitInBatches"]
  n3["IF"]
  n4["NoOp"]
  n5["Airtable"]
  n6["Airtable1"]
  n7["Airtable2"]
  n8["Set"]
  n9["Set1"]
  n10["Get All Workflows"]
  n11["Prepare data"]
  n12["Prepare data1"]
  n13["Cron"]
  n14["Move Binary Data"]
  n15["Dropbox"]
  n16["Get Workflow Details"]
  n17["Get file link"]
  n18["IF Airtable record exists#63;"]
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n17
  n5 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n8
  n17 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n10
  n18 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 1 to in 0"| n12
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
