# Dialpad to Syncro

Adapt the published “Dialpad to Syncro” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["GetCustomer"]
  n1["Webhook"]
  n2["CreateTicket"]
  n3["GetTicket"]
  n4["IFMoreThanOne"]
  n5["Google Sheets"]
  n6["ForGoogle"]
  n7["UpdateTicket"]
  n8["ForGoogle1"]
  n9["Google Sheets1"]
  n10["NoOp"]
  n11["Contacts"]
  n12["IFContacts"]
  n13["Customers"]
  n14["IFCustomers"]
  n15["NoOp1"]
  n16["CreateTicketForCustomer"]
  n17["ForGoogle2"]
  n18["Google Sheets2"]
  n19["EnvVariables"]
  n20["IF"]
  n21["NoOp2"]
  n20 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 1 to in 0"| n21
  n1 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n18
  n12 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 1 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 1 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n8
  n19 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 1 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n17
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
