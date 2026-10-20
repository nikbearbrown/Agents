# PUQ Docker NextCloud deploy

Adapt the published “PUQ Docker NextCloud deploy” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 43 executable nodes and 68 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["If"]
  n1["Parametrs"]
  n2["API"]
  n3["422-Invalid server domain"]
  n4["Container Actions"]
  n5["Container Stats"]
  n6["Inspect"]
  n7["Stat"]
  n8["Start"]
  n9["Stop"]
  n10["Mount Disk"]
  n11["Unmount Disk"]
  n12["Log"]
  n13["Deploy-docker-compose"]
  n14["Version"]
  n15["Users"]
  n16["Change Password"]
  n17["NextCloud"]
  n18["nginx"]
  n19["Test Connection"]
  n20["ChangePackage"]
  n21["Terminated"]
  n22["Unsuspend"]
  n23["Suspend"]
  n24["Deploy"]
  n25["Service Actions"]
  n26["If1"]
  n27["Dependent containers Stat"]
  n28["GET ACL"]
  n29["SET ACL"]
  n30["GET NET"]
  n31["If2"]
  n32["Split domain"]
  n33["DNS Service Actions"]
  n34["DNS Parametrs"]
  n35["Add record"]
  n36["Delete record"]
  n37["API answer1"]
  n38["REPLACE_WITH_CREDENTIAL"]
  n39["REPLACE_WITH_CREDENTIAL"]
  n40["Servers Switch"]
  n41["Code"]
  n42["API answer2"]
  n0 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 1 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n1
  n26 -->|"main out 0 to in 0"| n18
  n26 -->|"main out 1 to in 0"| n25
  n31 -->|"main out 0 to in 0"| n33
  n12 -->|"main out 0 to in 0"| n40
  n41 -->|"main out 0 to in 0"| n42
  n7 -->|"main out 0 to in 0"| n40
  n9 -->|"main out 0 to in 0"| n40
  n8 -->|"main out 0 to in 0"| n40
  n15 -->|"main out 0 to in 0"| n40
  n18 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n40
  n28 -->|"main out 0 to in 0"| n40
  n30 -->|"main out 0 to in 0"| n40
  n6 -->|"main out 0 to in 0"| n40
  n29 -->|"main out 0 to in 0"| n40
  n23 -->|"main out 0 to in 0"| n40
  n14 -->|"main out 0 to in 0"| n40
  n17 -->|"main out 0 to in 0"| n14
  n17 -->|"main out 1 to in 0"| n15
  n17 -->|"main out 2 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n0
  n22 -->|"main out 0 to in 0"| n40
  n10 -->|"main out 0 to in 0"| n40
  n21 -->|"main out 0 to in 0"| n40
  n32 -->|"main out 0 to in 0"| n34
  n11 -->|"main out 0 to in 0"| n40
  n20 -->|"main out 0 to in 0"| n40
  n34 -->|"main out 0 to in 0"| n31
  n40 -->|"main out 0 to in 0"| n39
  n40 -->|"main out 1 to in 0"| n39
  n16 -->|"main out 0 to in 0"| n40
  n5 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 1 to in 0"| n7
  n5 -->|"main out 2 to in 0"| n12
  n5 -->|"main out 3 to in 0"| n27
  n5 -->|"main out 4 to in 0"| n32
  n25 -->|"main out 0 to in 0"| n19
  n25 -->|"main out 1 to in 0"| n24
  n25 -->|"main out 1 to in 0"| n32
  n25 -->|"main out 2 to in 0"| n23
  n25 -->|"main out 3 to in 0"| n22
  n25 -->|"main out 4 to in 0"| n21
  n25 -->|"main out 4 to in 0"| n32
  n25 -->|"main out 5 to in 0"| n20
  n25 -->|"main out 5 to in 0"| n32
  n19 -->|"main out 0 to in 0"| n40
  n4 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 1 to in 0"| n9
  n4 -->|"main out 2 to in 0"| n10
  n4 -->|"main out 3 to in 0"| n11
  n4 -->|"main out 4 to in 0"| n28
  n4 -->|"main out 5 to in 0"| n29
  n4 -->|"main out 6 to in 0"| n30
  n33 -->|"main out 0 to in 0"| n35
  n33 -->|"main out 0 to in 0"| n37
  n33 -->|"main out 1 to in 0"| n35
  n33 -->|"main out 2 to in 0"| n36
  n33 -->|"main out 3 to in 0"| n35
  n33 -->|"main out 4 to in 0"| n36
  n33 -->|"main out 5 to in 0"| n35
  n13 -->|"main out 0 to in 0"| n25
  n27 -->|"main out 0 to in 0"| n40
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
