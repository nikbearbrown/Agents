# n8n and http request and create new file 53093cc6

Adapt the published “n8n and http request and create new file 53093cc6” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On clicking #39;execute#39;"]
  n1["n8n"]
  n2["Return"]
  n3["Get File"]
  n4["If file too large"]
  n5["Merge Items"]
  n6["isDiffOrNew"]
  n7["Check Status"]
  n8["Same file - Do nothing"]
  n9["File is different"]
  n10["File is new"]
  n11["Create new file"]
  n12["Edit existing file"]
  n13["Loop Over Items"]
  n14["Schedule Trigger"]
  n15["Get file data"]
  n16["Globals"]
  n17["Execute Workflow Trigger"]
  n18["Execute Workflow"]
  n19["/"]
  n20["tag#63;"]
  n19 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 1 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n9
  n7 -->|"main out 2 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n2
  n13 -->|"main out 1 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n3
  n4 -->|"main out 1 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 1"| n5
  n17 -->|"main out 0 to in 0"| n20
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
