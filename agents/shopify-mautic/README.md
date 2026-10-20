# Shopify + Mautic

Adapt the published “Shopify + Mautic” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Shopify Trigger"]
  n1["Accepts Marketing#63;"]
  n2["Accepts Marketing#63;1"]
  n3["No Operation, do nothing"]
  n4["Add to confirmed segment"]
  n5["Remove from confirmed segment"]
  n6["Webhook"]
  n7["Crypto"]
  n8["If"]
  n9["No Operation, do nothing1"]
  n10["GraphQL"]
  n11["Marketing Consent - subscribed"]
  n12["Marketing Consent - unsubscribed"]
  n13["Mautic - Accepts Marketing#63;"]
  n14["Customer exists#63;"]
  n15["No Operation, do nothing2"]
  n16["Set Shopify Subdomain"]
  n17["Search for Contact by Email"]
  n18["Contact exists#63;"]
  n19["Create a new contact"]
  n8 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 1 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n16
  n18 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 1 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n17
  n14 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 1 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 1 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n19
  n2 -->|"main out 1 to in 0"| n3
  n19 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 1 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n18
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
