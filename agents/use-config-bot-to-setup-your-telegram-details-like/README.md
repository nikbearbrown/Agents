# Use Config Bot to setup your telegram details, like:

Adapt the published “Use Config Bot to setup your telegram details, like:” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 38 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["New User #63;"]
  n1["Format"]
  n2["Bot-Fields"]
  n3["Create Topic #40;Chat Ticket#41;"]
  n4["Save Topic ID"]
  n5["Get User Chat Topic"]
  n6["Forward New Message"]
  n7["IF No Topic Created"]
  n8["ReCreate Topic #40;Chat Ticket#41;"]
  n9["ReSave Topic ID"]
  n10["Update User Data"]
  n11["Save User Data"]
  n12["Support Forum"]
  n13["From Ticket"]
  n14["Forward Support Reply To User"]
  n15["IF Topic Created"]
  n16["Forward New Message to the recrated topic"]
  n17["No Operation, do nothing"]
  n18["Check User in Database"]
  n19["Send User Ticket Created Notification"]
  n20["Bot-Config"]
  n21["Telegram-Bot"]
  n22["1st"]
  n23["Split In Batches1"]
  n24["Wait1"]
  n25["Format Users"]
  n26["Broadcast Channel Post into Users"]
  n27["Set Blocked Member"]
  n28["IF Verified Channel"]
  n29["Filter Blocked Users"]
  n30["Retrieve all users in DB"]
  n22 -->|"main out 1 to in 0"| n18
  n22 -->|"main out 2 to in 0"| n12
  n22 -->|"main out 3 to in 0"| n28
  n24 -->|"main out 0 to in 0"| n23
  n1 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n22
  n0 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 1 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 1 to in 0"| n15
  n25 -->|"main out 0 to in 0"| n29
  n21 -->|"main out 0 to in 0"| n20
  n4 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 0 to in 0"| n17
  n6 -->|"main out 1 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n17
  n28 -->|"main out 0 to in 0"| n30
  n28 -->|"main out 1 to in 0"| n17
  n29 -->|"main out 0 to in 0"| n23
  n18 -->|"main out 0 to in 0"| n0
  n30 -->|"main out 0 to in 0"| n25
  n3 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n17
  n26 -->|"main out 0 to in 0"| n24
  n26 -->|"main out 1 to in 0"| n27
  n19 -->|"main out 0 to in 0"| n17
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
