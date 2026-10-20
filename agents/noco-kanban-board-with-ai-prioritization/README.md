# Noco Kanban Board with AI Prioritization

Adapt the published “Noco Kanban Board with AI Prioritization” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Incident Form"]
  n1["Assign Category"]
  n2["OpenAI Chat Model1"]
  n3["Structure Output Todoist Ready1"]
  n4["Get incident definitions"]
  n5["Insert Incident"]
  n6["Aggregate for AI parsing"]
  n7["On schedule or during flow"]
  n8["When clicking #8216;Test workflow#8217;"]
  n9["Task is not picked up after expected response"]
  n10["Send email to client"]
  n11["Check status every day"]
  n12["Send email to asignee"]
  n13["Get Unpicked Tasks"]
  n14["Get Unfinished Tasks"]
  n15["Task is not complete in expected time"]
  n16["Send email to client1"]
  n17["If there is asignee email"]
  n18["If there is assignee slack"]
  n19["Slack to assignee"]
  n20["Send another email to asignee"]
  n21["Format for Noco"]
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n9
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 1 to in 0"| n20
  n7 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n14
  n3 -->|"ai_outputParser out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 1 to in 0"| n18
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n17
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
