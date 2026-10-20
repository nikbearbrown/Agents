# history channel slack and split out and slack

Adapt the published “history channel slack and split out and slack” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 40 executable nodes and 40 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get Last Week#39;s Messages"]
  n1["Simplify Message"]
  n2["Group By User"]
  n3["Split Out"]
  n4["Messages to Items"]
  n5["Get User"]
  n6["Aggregate"]
  n7["Split Out1"]
  n8["Get Thread"]
  n9["Aggregate1"]
  n10["Simplify Thread Comments"]
  n11["Filter"]
  n12["Message Ref"]
  n13["Split Out2"]
  n14["Map Reply UserIds"]
  n15["Get Reply Users"]
  n16["Google Gemini Chat Model"]
  n17["Summarise Threads"]
  n18["Aggregate2"]
  n19["Aggregate Reply Users"]
  n20["Reply Users"]
  n21["Google Gemini Chat Model1"]
  n22["Loop Over Items"]
  n23["Aggregate3"]
  n24["Aggregate4"]
  n25["When Executed by Another Workflow"]
  n26["Switch"]
  n27["Map Users to Messages"]
  n28["Get User Info"]
  n29["Fetch Message Replies"]
  n30["Has ReplyUsers#63;"]
  n31["Messages to Items1"]
  n32["Aggregate Results"]
  n33["Team Member Weekly Report Agent"]
  n34["Merge with Results"]
  n35["Team Weekly Report Agent"]
  n36["Google Gemini Chat Model2"]
  n37["Post Report in Team Channel"]
  n38["Summarize Message Threads"]
  n39["Monday #64; 6am"]
  n11 -->|"main out 0 to in 0"| n10
  n26 -->|"main out 0 to in 0"| n5
  n26 -->|"main out 1 to in 0"| n7
  n26 -->|"main out 2 to in 0"| n14
  n5 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n28
  n3 -->|"main out 0 to in 0"| n27
  n9 -->|"main out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n22
  n13 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n8
  n20 -->|"main out 0 to in 0"| n31
  n39 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 0"| n19
  n30 -->|"main out 0 to in 0"| n13
  n30 -->|"main out 1 to in 0"| n20
  n22 -->|"main out 0 to in 0"| n23
  n22 -->|"main out 1 to in 0"| n12
  n1 -->|"main out 0 to in 0"| n6
  n32 -->|"main out 0 to in 0"| n33
  n14 -->|"main out 0 to in 0"| n30
  n4 -->|"main out 0 to in 0"| n1
  n17 -->|"main out 0 to in 0"| n18
  n34 -->|"main out 0 to in 0"| n35
  n31 -->|"main out 0 to in 0"| n17
  n19 -->|"main out 0 to in 0"| n20
  n29 -->|"main out 0 to in 0"| n38
  n27 -->|"main out 0 to in 0"| n29
  n0 -->|"main out 0 to in 0"| n2
  n16 -->|"ai_languageModel out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n9
  n35 -->|"main out 0 to in 0"| n37
  n21 -->|"ai_languageModel out 0 to in 0"| n33
  n36 -->|"ai_languageModel out 0 to in 0"| n35
  n38 -->|"main out 0 to in 0"| n32
  n33 -->|"main out 0 to in 0"| n34
  n25 -->|"main out 0 to in 0"| n26
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
