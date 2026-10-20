# Slack Modal Interface

Adapt the published “Slack Modal Interface” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Parse Webhook"]
  n1["Close Modal Popup"]
  n2["Route Message"]
  n3["ServiceNow Modal"]
  n4["Webhook"]
  n5["Send 200"]
  n6["ServiceNow"]
  n7["Channel - Notify User no Incidents Matched"]
  n8["DM - Notify User no Incidents Matched"]
  n9["Were Incidents Found#63;"]
  n10["No Matches - Was a Channel Selected#63;"]
  n11["Sort by Most Recent"]
  n12["Retain First 5 Incidents"]
  n13["Loop Over Items"]
  n14["Format Incident Details"]
  n15["Format Slack Message"]
  n16["Concatenate Incident Details"]
  n17["DM - Send Matching Incidents"]
  n18["Channel - Send Matching Incidents"]
  n19["Was a Channel Selected#63;"]
  n20["Respond to Slack Webhook"]
  n4 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n20
  n2 -->|"main out 1 to in 0"| n1
  n2 -->|"main out 2 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 1 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n19
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 1 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n13
  n19 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 1 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 1 to in 0"| n8
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
