# receive telegram events and send next question and telegram

Adapt the published “receive telegram events and send next question and telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 34 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Send Next Question"]
  n2["Send Response"]
  n3["Has No Record#63;"]
  n4["Is Survey Continue#63;"]
  n5["Get State2"]
  n6["Get Columns1"]
  n7["Set Variables1"]
  n8["Message Type1"]
  n9["Get Command1"]
  n10["Bot Actions1"]
  n11["Memory3"]
  n12["Get Survey State1"]
  n13["Reset Agent Memory1"]
  n14["Memory4"]
  n15["Start Session1"]
  n16["Get State3"]
  n17["Increment Index1"]
  n18["Interview Agent1"]
  n19["Get Record1"]
  n20["Append Responses1"]
  n21["Update Answer2"]
  n22["Get Last Bot Message1"]
  n23["Update Answer3"]
  n24["Model2"]
  n25["Model3"]
  n26["Should Follow Up#63;1"]
  n27["Execution Data2"]
  n28["Create Record2"]
  n29["Send Start"]
  n30["Send Start1"]
  n31["Completed Survey"]
  n32["Create Record1"]
  n24 -->|"ai_languageModel out 0 to in 0"| n18
  n25 -->|"ai_languageModel out 0 to in 0"| n26
  n11 -->|"ai_memory out 0 to in 0"| n13
  n14 -->|"ai_memory out 0 to in 0"| n18
  n5 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n32
  n10 -->|"main out 1 to in 0"| n16
  n10 -->|"main out 2 to in 0"| n30
  n6 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 1 to in 0"| n19
  n32 -->|"main out 0 to in 0"| n15
  n28 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 0 to in 0"| n28
  n3 -->|"main out 1 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n27
  n15 -->|"main out 0 to in 0"| n29
  n21 -->|"main out 0 to in 0"| n2
  n23 -->|"main out 0 to in 0"| n16
  n27 -->|"main out 0 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n4
  n18 -->|"main out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n26
  n12 -->|"main out 0 to in 0"| n17
  n26 -->|"main out 0 to in 0"| n23
  n26 -->|"main out 1 to in 0"| n18
  n4 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 1 to in 0"| n31
  n13 -->|"main out 0 to in 0"| n1
  n22 -->|"main out 0 to in 0"| n20
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
