# receive telegram events and telegram and google drive

Adapt the published “receive telegram events and telegram and google drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 32 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Check State"]
  n2["Clear State"]
  n3["addGPS"]
  n4["Welcome Message"]
  n5["Command#63;"]
  n6["Store GPS Location"]
  n7["addGPS result"]
  n8["addShipmentNumber"]
  n9["Shipment Number"]
  n10["addShipmentNumber result"]
  n11["Store Shipment"]
  n12["Store GPS"]
  n13["Load Workspace Data"]
  n14["waitingShipmentNumber"]
  n15["waitingGPS"]
  n16["Instructions"]
  n17["waitingPhoto"]
  n18["Waiting Conditions"]
  n19["addPhoto result"]
  n20["sendPhoto"]
  n21["Upload Picture"]
  n22["Save Public Image Link"]
  n23["Confirmation Driver"]
  n24["Distribution Team Confirmation"]
  n25["Extract FileName"]
  n26["Store fileName"]
  n27["Get Picture"]
  n28["Share Picture"]
  n29["Initiate Workflow Data"]
  n30["Switch Command"]
  n31["Load Delivery Information"]
  n5 -->|"main out 0 to in 0"| n30
  n5 -->|"main out 1 to in 0"| n18
  n15 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 1 to in 0"| n6
  n1 -->|"main out 2 to in 0"| n27
  n1 -->|"main out 3 to in 0"| n16
  n27 -->|"main out 0 to in 0"| n21
  n27 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 0 to in 0"| n20
  n28 -->|"main out 0 to in 0"| n22
  n30 -->|"main out 0 to in 0"| n14
  n30 -->|"main out 1 to in 0"| n15
  n30 -->|"main out 2 to in 0"| n17
  n30 -->|"main out 3 to in 0"| n13
  n30 -->|"main out 4 to in 0"| n4
  n21 -->|"main out 0 to in 0"| n28
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n11
  n25 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n31
  n13 -->|"main out 0 to in 0"| n23
  n13 -->|"main out 0 to in 0"| n24
  n14 -->|"main out 0 to in 0"| n8
  n22 -->|"main out 0 to in 0"| n19
  n24 -->|"main out 0 to in 0"| n2
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
