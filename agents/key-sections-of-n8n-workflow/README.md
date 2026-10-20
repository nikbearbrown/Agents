# Key Sections of n8n Workflow

Adapt the published “Key Sections of n8n Workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["YTD vs Prevoius Month1"]
  n2["Loop Over Items"]
  n3["CostCentrs"]
  n4["Date #38; Time"]
  n5["PreviousMonth"]
  n6["Selected Cost Center"]
  n7["Get Cost Centers with Budgets"]
  n8["Filter"]
  n9["HTML"]
  n10["verticalPL"]
  n11["Merge"]
  n12["Code"]
  n13["Microsoft Outlook2"]
  n14["CostCenter"]
  n15["WIP1"]
  n16["Employees"]
  n17["Employees1"]
  n18["Wait"]
  n19["Financial Performance"]
  n20["Email Data"]
  n21["Calculator"]
  n22["Business Performance AI Agent #40;Analyst#41;"]
  n23["Think"]
  n24["Google Gemini Chat Model"]
  n25["Departments"]
  n26["Projects"]
  n12 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n22
  n15 -->|"main out 0 to in 2"| n11
  n18 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n12
  n23 -->|"ai_tool out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n2
  n26 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n17
  n21 -->|"ai_tool out 0 to in 0"| n22
  n14 -->|"main out 0 to in 0"| n11
  n3 -->|"main out 0 to in 0"| n8
  n20 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 3"| n11
  n10 -->|"main out 0 to in 1"| n11
  n4 -->|"main out 0 to in 0"| n5
  n25 -->|"main out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 1 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n25
  n6 -->|"main out 0 to in 0"| n26
  n6 -->|"main out 0 to in 0"| n16
  n19 -->|"main out 0 to in 0"| n20
  n1 -->|"main out 0 to in 0"| n14
  n24 -->|"ai_languageModel out 0 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n3
  n22 -->|"main out 0 to in 0"| n19
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
