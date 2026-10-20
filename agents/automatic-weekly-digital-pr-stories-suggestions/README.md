# My workflow

Adapt the published “My workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split Topics into Items"]
  n1["Search Posts"]
  n2["Upvotes Requirement Filtering"]
  n3["Set Reddit Posts"]
  n4["Remove Duplicates"]
  n5["Loop Over Items"]
  n6["Get Comments"]
  n7["Extract Top Comments"]
  n8["Format Comments"]
  n9["Set for Loop"]
  n10["Get News Content"]
  n11["Set Final Report"]
  n12["Convert to File"]
  n13["Compress files"]
  n14["Merge Binary Files"]
  n15["Google Drive6"]
  n16["Google Drive7"]
  n17["Send files to Mattermost3"]
  n18["Aggregate"]
  n19["Schedule Trigger"]
  n20["Anthropic Chat Model"]
  n21["Anthropic Chat Model1"]
  n22["Keep Last"]
  n23["Anthropic Chat Model2"]
  n24["Comments Analysis"]
  n25["News Analysis"]
  n26["Stories Report"]
  n27["Set Data"]
  n27 -->|"main out 0 to in 0"| n0
  n18 -->|"main out 0 to in 0"| n14
  n22 -->|"main out 0 to in 0"| n25
  n6 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n25 -->|"main out 0 to in 0"| n26
  n13 -->|"main out 0 to in 0"| n15
  n26 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 0"| n24
  n5 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 1 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n22
  n19 -->|"main out 0 to in 0"| n27
  n11 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n4
  n24 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n13
  n20 -->|"ai_languageModel out 0 to in 0"| n24
  n7 -->|"main out 0 to in 0"| n8
  n21 -->|"ai_languageModel out 0 to in 0"| n25
  n23 -->|"ai_languageModel out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n3
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
