# Get all scaleway server info copy

Adapt the published “Get all scaleway server info copy” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Code"]
  n1["Edit Fields"]
  n2["Switch"]
  n3["Code search Tags"]
  n4["Code search Name"]
  n5["Code search public_ip"]
  n6["Code search zone"]
  n7["Webhook"]
  n8["Respond Error"]
  n9["Respond to Webhook1"]
  n10["Respond to Webhook2"]
  n11["Respond to Webhook3"]
  n12["Respond to Webhook"]
  n13["Get Scalway Machines"]
  n14["Loop Over Items"]
  n15["Respond to Webhook4"]
  n16["Get scw instance by zone"]
  n17["Loop Over Zone Instance"]
  n18["Get scw baremetal by zone"]
  n19["Split Out ZONE_INSTANCE"]
  n20["If ZONE_BAREMETAL in ZONE_INSTANCE"]
  n0 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n4
  n2 -->|"main out 2 to in 0"| n5
  n2 -->|"main out 3 to in 0"| n6
  n2 -->|"main out 4 to in 0"| n15
  n2 -->|"main out 5 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n14
  n5 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 1 to in 0"| n16
  n19 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 1 to in 0"| n17
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
