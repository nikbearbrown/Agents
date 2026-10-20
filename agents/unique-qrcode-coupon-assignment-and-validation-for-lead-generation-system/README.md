# Unique QRcode coupon assignment and validation for Lead Generation system

Adapt the published “Unique QRcode coupon assignment and validation for Lead Generation system” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["If"]
  n2["Token SuiteCRM"]
  n3["Create Lead SuiteCRM"]
  n4["On form submission"]
  n5["Duplicate Lead#63;"]
  n6["Form Fields"]
  n7["Get Coupon"]
  n8["Update Sheet"]
  n9["Is Duplicate#63;"]
  n10["Get QR"]
  n11["Send Email"]
  n12["Update Lead"]
  n13["Not used#63;"]
  n14["Coupon OK"]
  n15["No coupon"]
  n16["Coupon KO"]
  n17["Token SuiteCRM 1"]
  n18["Set coupon"]
  n19["Get Lead"]
  n20["Update coupon used"]
  n1 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 1 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 1 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n2
  n18 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n20
  n8 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 1 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n8
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
