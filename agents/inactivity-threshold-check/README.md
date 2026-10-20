# ⏳ Inactivity &amp; Threshold Check

Adapt the published “⏳ Inactivity &amp; Threshold Check” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 31 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["No Operation, do nothing1"]
  n2["Information Extractor"]
  n3["OpenAI Chat Model"]
  n4["get wait seconds"]
  n5["Set last_seen"]
  n6["Get waiting_reply"]
  n7["Mod input"]
  n8["waiting_reply#63;"]
  n9["When chat message received"]
  n10["Set waiting_reply"]
  n11["Get buffer"]
  n12["Delete buffer_in"]
  n13["Delete waiting_reply"]
  n14["WaitSeconds"]
  n15["Buffer messages"]
  n16["Set buffer_count increment"]
  n17["Get last_seen"]
  n18["Get buffer_count"]
  n19["Map ouput"]
  n20["Check Inactivity #43; Count"]
  n21["Delete waiting_reply1"]
  n22["No Operation, do nothing2"]
  n23["Wait"]
  n24["When Executed by Another Workflow"]
  n25["Mock input data"]
  n26["No Operation, do nothing3"]
  n23 -->|"main out 0 to in 0"| n20
  n7 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 1 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n6
  n25 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n26
  n18 -->|"main out 0 to in 0"| n20
  n4 -->|"main out 0 to in 0"| n15
  n6 -->|"main out 0 to in 0"| n7
  n3 -->|"ai_languageModel out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n26
  n21 -->|"main out 0 to in 0"| n26
  n2 -->|"main out 0 to in 0"| n19
  n2 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n11
  n20 -->|"main out 1 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n23
  n16 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n25
  n24 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n25
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
