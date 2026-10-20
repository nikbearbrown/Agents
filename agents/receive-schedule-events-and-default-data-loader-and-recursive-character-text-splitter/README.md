# receive schedule events and default data loader and recursive character text splitter

Adapt the published “receive schedule events and default data loader and recursive character text splitter” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Embeddings OpenAI"]
  n2["Default Data Loader"]
  n3["Recursive Character Text Splitter"]
  n4["Issues Similarity Database"]
  n5["Supabase Vector Store"]
  n6["Embeddings OpenAI1"]
  n7["OpenAI Chat Model"]
  n8["Find Similar Issues #43; Assignees"]
  n9["Check User Workflow"]
  n10["For Each User"]
  n11["Assign User to Ticket"]
  n12["Schedule Trigger1"]
  n13["Remove Duplicates"]
  n14["Collect Fields"]
  n15["Get Unassigned Tickets more than 5 days"]
  n16["For Each Issue"]
  n17["Issue Ref"]
  n18["Add Comment to Issue"]
  n19["Last 50 Resolved"]
  n20["OpenAI Chat Model1"]
  n21["Issues to Items"]
  n22["To Structured Output"]
  n23["Count Assigned Open Issues per User"]
  n24["Tally In-Progress Issues per User"]
  n25["Sort By Most Capacity"]
  n26["If has Items#63;"]
  n27["Skip"]
  n27 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n23
  n10 -->|"main out 1 to in 0"| n9
  n26 -->|"main out 0 to in 0"| n10
  n26 -->|"main out 1 to in 0"| n27
  n14 -->|"main out 0 to in 0"| n4
  n16 -->|"main out 1 to in 0"| n17
  n21 -->|"main out 0 to in 0"| n26
  n19 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n19
  n1 -->|"ai_embedding out 0 to in 0"| n4
  n7 -->|"ai_languageModel out 0 to in 0"| n8
  n13 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n15
  n6 -->|"ai_embedding out 0 to in 0"| n5
  n20 -->|"ai_languageModel out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n24
  n2 -->|"ai_document out 0 to in 0"| n4
  n18 -->|"main out 0 to in 0"| n16
  n22 -->|"main out 0 to in 0"| n21
  n11 -->|"main out 0 to in 0"| n18
  n25 -->|"main out 0 to in 0"| n11
  n5 -->|"ai_tool out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n22
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n24 -->|"main out 0 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n25
  n15 -->|"main out 0 to in 0"| n16
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
