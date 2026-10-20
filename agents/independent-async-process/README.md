# Independent "Async" Process

Adapt the published “Independent "Async" Process” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 10 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Wait"]
  n2["HTTP Request - Initiate Independent Process"]
  n3["HTTP Request - Resume Other Workflow Execution"]
  n4["This Node Can Access Primary and Secondary"]
  n5["Set Primary Execution Context"]
  n6["Receive Input from External, Independent Process"]
  n7["Respond to Webhook"]
  n8["Simulate Event that Hits the 2nd Trigger/Flow"]
  n9["Simulate some Consumed Service Time"]
  n10["HTTP Request - Get A Random Joke"]
  n11["Demo #34;Trigger#34; Callback Setup"]
  n12["Webhook"]
  n1 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n3
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
