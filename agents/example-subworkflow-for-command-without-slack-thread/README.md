# Example subworkflow for command WITHOUT Slack thread..

Adapt the published “Example subworkflow for command WITHOUT Slack thread..” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Start thread"]
  n1["send help"]
  n2["Validate Slack token"]
  n3["Reply to user that command was received"]
  n4["if has workflow"]
  n5["Set config"]
  n6["Send debug url"]
  n7["if create thread"]
  n8["Alert user that thread was created"]
  n9["Add debug info"]
  n10["Execute target workflow"]
  n11["Add thread info"]
  n12["Handle other commands"]
  n13["Set thread info"]
  n14["Unknown command"]
  n15["Set vars"]
  n16["Webhook to call for Slack command"]
  n17["Reply to user directly"]
  n18["Command workflow trigger"]
  n19["if has flag"]
  n20["If matches env variable"]
  n21["Found user"]
  n22["Format data into nice structure"]
  n23["REPLACE ME WITH TRIGGER"]
  n24["Delete user here for example"]
  n25["Get user here for example"]
  n26["Confirm user was deleted"]
  n27["Replying to thread"]
  n28["parse command"]
  n29["Validate webhook signature"]
  n15 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n29
  n19 -->|"main out 0 to in 0"| n20
  n0 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n13
  n28 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 1 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 1"| n11
  n7 -->|"main out 1 to in 0"| n6
  n7 -->|"main out 1 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n28
  n12 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 1 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n25
  n23 -->|"main out 0 to in 0"| n27
  n23 -->|"main out 0 to in 0"| n24
  n18 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n19
  n25 -->|"main out 0 to in 0"| n22
  n29 -->|"main out 0 to in 0"| n2
  n24 -->|"main out 0 to in 0"| n26
  n22 -->|"main out 0 to in 0"| n21
  n16 -->|"main out 0 to in 0"| n15
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
