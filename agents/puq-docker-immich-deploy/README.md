# puq-docker-immich-deploy

Adapt the published “puq-docker-immich-deploy” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 34 executable nodes and 54 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["If"]
  n1["Parametrs"]
  n2["API"]
  n3["422-Invalid server domain"]
  n4["Code1"]
  n5["SSH"]
  n6["Container Actions"]
  n7["Service Actions"]
  n8["API answer"]
  n9["Inspect"]
  n10["Stat"]
  n11["Start"]
  n12["Stop"]
  n13["Test Connection1"]
  n14["Deploy"]
  n15["Suspend"]
  n16["Terminated"]
  n17["Unsuspend"]
  n18["Mount Disk"]
  n19["Unmount Disk"]
  n20["Log"]
  n21["ChangePackage"]
  n22["Deploy-docker-compose"]
  n23["Version"]
  n24["Users"]
  n25["If1"]
  n26["nginx"]
  n27["Container Stat"]
  n28["GET ACL"]
  n29["SET ACL"]
  n30["GET NET"]
  n31["Dependent containers Stat"]
  n32["Change Password"]
  n33["Immich"]
  n0 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n33
  n0 -->|"main out 0 to in 0"| n25
  n0 -->|"main out 1 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n1
  n25 -->|"main out 0 to in 0"| n26
  n25 -->|"main out 1 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n4
  n5 -->|"main out 1 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n5
  n24 -->|"main out 0 to in 0"| n5
  n26 -->|"main out 0 to in 0"| n22
  n14 -->|"main out 0 to in 0"| n5
  n33 -->|"main out 0 to in 0"| n23
  n33 -->|"main out 1 to in 0"| n24
  n33 -->|"main out 2 to in 0"| n32
  n28 -->|"main out 0 to in 0"| n5
  n30 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n5
  n29 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n5
  n18 -->|"main out 0 to in 0"| n5
  n16 -->|"main out 0 to in 0"| n5
  n19 -->|"main out 0 to in 0"| n5
  n21 -->|"main out 0 to in 0"| n5
  n27 -->|"main out 0 to in 0"| n9
  n27 -->|"main out 1 to in 0"| n10
  n27 -->|"main out 2 to in 0"| n20
  n27 -->|"main out 3 to in 0"| n31
  n32 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 1 to in 0"| n14
  n7 -->|"main out 2 to in 0"| n15
  n7 -->|"main out 3 to in 0"| n17
  n7 -->|"main out 4 to in 0"| n16
  n7 -->|"main out 5 to in 0"| n21
  n13 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 1 to in 0"| n12
  n6 -->|"main out 2 to in 0"| n18
  n6 -->|"main out 3 to in 0"| n19
  n6 -->|"main out 4 to in 0"| n28
  n6 -->|"main out 5 to in 0"| n29
  n6 -->|"main out 6 to in 0"| n30
  n22 -->|"main out 0 to in 0"| n7
  n31 -->|"main out 0 to in 0"| n5
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
