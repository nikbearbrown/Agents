# Send follow-up emails if appropriate

Adapt the published “Send follow-up emails if appropriate” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Update last contacted time"]
  n1["Set message template"]
  n2["Email sequence"]
  n3["Fill message placeholders"]
  n4["Compose message"]
  n5["Get previous message threads"]
  n6["Get thread details"]
  n7["Classify threads"]
  n8["Next message due#63;"]
  n9["Execute Workflow Trigger"]
  n10["Replying#63;"]
  n11["Send new message"]
  n12["Call message send sub-workflow"]
  n13["Prepare reply params"]
  n14["Prepare first message params"]
  n15["Call message send sub-workflow1"]
  n16["To email#63;"]
  n17["Decode messages"]
  n18["Decode placeholder values"]
  n19["Package placeholder values"]
  n20["Settings"]
  n21["Reply to message"]
  n22["Get emails"]
  n23["Every hour"]
  n24["Don#39;t email on weekends"]
  n20 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n21
  n10 -->|"main out 1 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n24
  n22 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n22
  n4 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n3
  n24 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 0 to in 0"| n0
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
