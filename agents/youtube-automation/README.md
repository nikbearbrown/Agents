# Youtube_Automation

Adapt the published “Youtube_Automation” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Fetch Latest Videos"]
  n1["Loop Over Items"]
  n2["YT Title"]
  n3["Create Description"]
  n4["When clicking #8216;Test workflow#8217;"]
  n5["2.5FlashPrev"]
  n6["YT Tags"]
  n7["3s"]
  n8["gettitle"]
  n9["Set Publish Date"]
  n10["Every Day"]
  n11["Get Videos to reschedule"]
  n12["Get video Ids seperated"]
  n13["Loop over Video IDs"]
  n14["Get Video Data"]
  n15["Return Private Videos"]
  n16["4s"]
  n17["Loop over All Videos not Published"]
  n18["get video id"]
  n19["Remove Duplicates from previous Runs"]
  n20["new video#63;"]
  n21["getLatestVideoID"]
  n22["Get Transcript"]
  n23["Adjust Transcript Format"]
  n24["Update Video#39;s Metadata"]
  n7 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n11
  n20 -->|"main out 1 to in 0"| n21
  n5 -->|"ai_languageModel out 0 to in 0"| n6
  n18 -->|"main out 0 to in 0"| n19
  n22 -->|"main out 0 to in 0"| n23
  n14 -->|"main out 0 to in 0"| n13
  n1 -->|"main out 1 to in 0"| n18
  n9 -->|"main out 0 to in 0"| n17
  n21 -->|"main out 0 to in 0"| n22
  n3 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 1 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n17
  n12 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 1 to in 0"| n8
  n19 -->|"main out 0 to in 0"| n20
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
