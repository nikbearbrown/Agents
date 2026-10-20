# get last execution timestamp and set new last execution timestamp and list zendesk

Adapt the published “get last execution timestamp and set new last execution timestamp and list zendesk” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get last execution timestamp"]
  n1["Set new last execution timestamp"]
  n2["Get tickets created after last execution"]
  n3["Get requester information"]
  n4["Keep only needed requester information"]
  n5["Keep only requester owner email"]
  n6["Every 5 minutes"]
  n7["Add requester information to ticket data"]
  n8["Search requester in pipedrive"]
  n9["Get owner information of Pipedrive contact"]
  n10["Get agents and admins"]
  n11["Keep only email and Id"]
  n12["Add Pipedrive agent data to pipedrive contact information"]
  n13["Add contact owner to ticket data"]
  n14["Contact exists in Pipedrive"]
  n15["Change assignee to Pipedrive contact owner"]
  n16["Add a note requester not found"]
  n6 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 1"| n12
  n3 -->|"main out 0 to in 0"| n4
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n16
  n0 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 1"| n7
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 1"| n13
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
