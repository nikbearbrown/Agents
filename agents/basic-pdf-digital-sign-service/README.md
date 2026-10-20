# Basic PDF Digital Sign Service

Adapt the published “Basic PDF Digital Sign Service” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Validate Key Gen Params"]
  n1["Validate PDF Sign Params"]
  n2["Validate PDF Upload"]
  n3["Validate Key Upload"]
  n4["Generate Keys"]
  n5["Sign PDF"]
  n6["Prepare Success Response"]
  n7["Switch Operation"]
  n8["Switch Upload Type"]
  n9["Prepare input params"]
  n10["set file path"]
  n11["Convert PDF to File"]
  n12["Write PDF File to Disk"]
  n13["Read PDF File from Disk"]
  n14["Convert PFX to File"]
  n15["Write PFX File to Disk"]
  n16["Read PFX File from Disk"]
  n17["Check PDF file is OK"]
  n18["Check PFX file is OK"]
  n19["check success"]
  n20["set downlowd file info"]
  n21["Read download file from Disk"]
  n22["API POST Endpoint"]
  n23["API GET Endpoint"]
  n24["POST Success Response"]
  n25["POST Error Response"]
  n26["GET Respond to Webhook"]
  n5 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 1 to in 0"| n25
  n10 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 1 to in 0"| n0
  n7 -->|"main out 2 to in 0"| n1
  n7 -->|"main out 3 to in 0"| n20
  n22 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 1 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n19
  n9 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n16
  n20 -->|"main out 0 to in 0"| n21
  n13 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n18
  n0 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n24
  n1 -->|"main out 0 to in 0"| n5
  n21 -->|"main out 0 to in 0"| n26
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
