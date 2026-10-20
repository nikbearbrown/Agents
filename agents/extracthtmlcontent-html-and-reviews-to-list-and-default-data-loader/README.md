# extracthtmlcontent html and reviews to list and default data loader

Adapt the published “extracthtmlcontent html and reviews to list and default data loader” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Zip Entries"]
  n2["Extract Reviews"]
  n3["Reviews to List"]
  n4["Default Data Loader"]
  n5["Recursive Character Text Splitter"]
  n6["Embeddings OpenAI"]
  n7["Set Variables"]
  n8["Get Payload of Points"]
  n9["Clusters To List"]
  n10["OpenAI Chat Model"]
  n11["Only Clusters With 3#43; points"]
  n12["Set Variables1"]
  n13["Find Reviews"]
  n14["Prep Output For Export"]
  n15["Export To Sheets"]
  n16["Clear Existing Reviews"]
  n17["Trigger Insights"]
  n18["Prep Values For Trigger"]
  n19["Execute Workflow Trigger"]
  n20["Get TrustPilot Page"]
  n21["Qdrant Vector Store"]
  n22["Apply K-means Clustering Algorithm"]
  n23["Customer Insights Agent"]
  n1 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n16
  n12 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n11
  n6 -->|"ai_embedding out 0 to in 0"| n21
  n10 -->|"ai_languageModel out 0 to in 0"| n23
  n4 -->|"ai_document out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n2
  n21 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n23
  n16 -->|"main out 0 to in 0"| n20
  n14 -->|"main out 0 to in 0"| n15
  n23 -->|"main out 0 to in 0"| n14
  n18 -->|"main out 0 to in 0"| n17
  n19 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n8
  n5 -->|"ai_textSplitter out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n7
  n22 -->|"main out 0 to in 0"| n9
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
