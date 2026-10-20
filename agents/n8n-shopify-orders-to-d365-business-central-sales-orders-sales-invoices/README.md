# &#91;n8n&#93; - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices

Adapt the published “&#91;n8n&#93; - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["GetFufillmentOrders"]
  n1["Shopify"]
  n2["Schedule Trigger"]
  n3["Loop Over Items"]
  n4["New Customer#63;"]
  n5["Lookup Customers"]
  n6["SelectFields"]
  n7["orderPreprocessing"]
  n8["Create Customer"]
  n9["Set Business Central Customer Id"]
  n10["Create Order Lines"]
  n11["End"]
  n12["Split Out"]
  n13["DELETE Sales Order"]
  n14["D365 BC Environment Settings"]
  n15["Create Sales Order"]
  n16["Set Lines Invoice"]
  n17["Set Lines SO"]
  n18["Split Out Invoice"]
  n19["Create Invoice Lines"]
  n20["Filter"]
  n21["Create Sales Invoice"]
  n22["End1"]
  n23["Sales Invoice"]
  n24["Lookup Sales Order"]
  n25["Sales Order Mapping"]
  n26["New SO#63;"]
  n27["Lookup Sales Invoice"]
  n28["New Invoice#63;"]
  n29["POS#63;"]
  n30["DELETE Sales Invoice"]
  n29 -->|"main out 0 to in 0"| n27
  n29 -->|"main out 1 to in 0"| n24
  n20 -->|"main out 0 to in 0"| n0
  n26 -->|"main out 0 to in 0"| n25
  n1 -->|"main out 0 to in 0"| n20
  n12 -->|"main out 0 to in 0"| n10
  n28 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 0 to in 0"| n7
  n17 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 1 to in 0"| n3
  n23 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 1 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n14
  n16 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n17
  n24 -->|"main out 0 to in 0"| n26
  n7 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n6
  n25 -->|"main out 0 to in 0"| n15
  n19 -->|"main out 0 to in 0"| n22
  n19 -->|"main out 1 to in 0"| n30
  n21 -->|"main out 0 to in 0"| n16
  n27 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n29
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
