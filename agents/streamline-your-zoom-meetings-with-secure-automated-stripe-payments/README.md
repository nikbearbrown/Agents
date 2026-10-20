# Streamline Your Zoom Meetings with Secure, Automated Stripe Payments

Adapt the published “Streamline Your Zoom Meetings with Secure, Automated Stripe Payments” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Create Zoom meeting"]
  n1["Create Stripe Product"]
  n2["Config"]
  n3["Send email to teacher"]
  n4["Create participant list"]
  n5["Add participant to list"]
  n6["Send confirmation to participant"]
  n7["Notify teacher"]
  n8["Create payment link"]
  n9["Format participant"]
  n10["Format event"]
  n11["Store event"]
  n12["Creation Form"]
  n13["On payment"]
  n14["if is creation flow"]
  n15["the end"]
  n2 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n0
  n14 -->|"main out 1 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n7
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
