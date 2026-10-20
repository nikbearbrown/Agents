# Trigger scan on Qualys agent

Adapt the published “Trigger scan on Qualys agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Start VM Scan in Qualys"]
  n1["Convert XML to JSON"]
  n2["Fetch Scan Results"]
  n3["Loop Over Items"]
  n4["Wait 5 Min"]
  n5["Convert XML to JSON1"]
  n6["Check if Scan Finished"]
  n7["Execute Workflow Trigger"]
  n8["Post Receipt"]
  n9["Confirm Waiting"]
  n10["Delete Receipt"]
  n11["Demo Data"]
  n12["Merge"]
  n13["Post Vulnerability Scan Summary to Slack"]
  n14["When clicking #34;Test workflow#34;"]
  n15["Begin Wait Loop"]
  n16["Merge1"]
  n17["Save receipt message timestamp"]
  n18["Global Variables #38; Slack Channel"]
  n12 -->|"main out 0 to in 0"| n0
  n16 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 1"| n12
  n4 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 1"| n16
  n3 -->|"main out 1 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 1 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n18
  n14 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n8
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
