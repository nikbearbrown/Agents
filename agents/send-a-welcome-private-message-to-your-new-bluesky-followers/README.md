# Send a welcome private message to your new BlueSky followers

Adapt the published “Send a welcome private message to your new BlueSky followers” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Create Session"]
  n1["List followers"]
  n2["Convert to File"]
  n3["Extract from File"]
  n4["Split Out"]
  n5["Loop Over Items"]
  n6["Wait"]
  n7["Find new followers"]
  n8["Read followers from file"]
  n9["Save followers to file"]
  n10["Define welcome message"]
  n11["Send message"]
  n12["Get conversation ID"]
  n13["Each 60 minutes"]
  n14["No Operation, do nothing"]
  n6 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n0
  n5 -->|"main out 1 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n3
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
