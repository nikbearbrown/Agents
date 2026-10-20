# Replace Mapbox public key - &lt;your_public_key&gt; in code

Adapt the published “Replace Mapbox public key - &lt;your_public_key&gt; in code” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["AI Agent"]
  n2["Window Buffer Memory"]
  n3["When chat message received"]
  n4["Execute Workflow Trigger"]
  n5["Response"]
  n6["Switch"]
  n7["Aggregate"]
  n8["Aggregate1"]
  n9["Merge"]
  n10["Aggregate2"]
  n11["If1"]
  n12["Response1"]
  n13["Search records"]
  n14["Process data with code"]
  n15["Create map image"]
  n16["Get list of bases"]
  n17["Get base schema"]
  n18["Get Bases"]
  n19["Get Base/Tables schema"]
  n20["If filter description exists"]
  n21["Airtable - Search records"]
  n22["OpenAI - Generate search filter"]
  n23["Set schema and prompt"]
  n24["Upload file to get link"]
  n25["OpenAI - Download File"]
  n26["OpenAI - Get messages"]
  n27["OpenAI - Run assistant"]
  n28["OpenAI - Send message"]
  n29["OpenAI - Create thread"]
  n11 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 1 to in 0"| n25
  n9 -->|"main out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 1 to in 0"| n19
  n6 -->|"main out 2 to in 0"| n20
  n6 -->|"main out 3 to in 0"| n29
  n7 -->|"main out 0 to in 0"| n5
  n18 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n5
  n13 -->|"ai_tool out 0 to in 0"| n1
  n17 -->|"ai_tool out 0 to in 0"| n1
  n15 -->|"ai_tool out 0 to in 0"| n1
  n16 -->|"ai_tool out 0 to in 0"| n1
  n0 -->|"ai_languageModel out 0 to in 0"| n1
  n2 -->|"ai_memory out 0 to in 0"| n1
  n26 -->|"main out 0 to in 0"| n11
  n28 -->|"main out 0 to in 0"| n27
  n23 -->|"main out 0 to in 0"| n22
  n19 -->|"main out 0 to in 0"| n8
  n29 -->|"main out 0 to in 0"| n28
  n25 -->|"main out 0 to in 0"| n24
  n27 -->|"main out 0 to in 0"| n26
  n14 -->|"ai_tool out 0 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n6
  n21 -->|"main out 0 to in 0"| n10
  n21 -->|"main out 1 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n1
  n20 -->|"main out 0 to in 0"| n9
  n20 -->|"main out 1 to in 0"| n23
  n22 -->|"main out 0 to in 1"| n9
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
