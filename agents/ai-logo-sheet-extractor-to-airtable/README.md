# AI Logo Sheet Extractor to Airtable

Adapt the published “AI Logo Sheet Extractor to Airtable” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On form submission"]
  n1["Retrieve and Parser Agent"]
  n2["JSON it"]
  n3["Structured Output Parser"]
  n4["Check if Attribute exists"]
  n5["Merge"]
  n6["Map Attribute ID"]
  n7["Loop Over Attributes"]
  n8["All Attributes"]
  n9["Wait for Attribute Creation"]
  n10["Change each Attribute to the corresponding RecID"]
  n11["Split Out Tools"]
  n12["Split Out each Attribute String"]
  n13["Generate Unique Hash for Name"]
  n14["Create if not Exist"]
  n15["Merge Old Data #43; RecID"]
  n16["Only what we need"]
  n17["Determine Attributes we should save"]
  n18["Split Out similar"]
  n19["Merge1"]
  n20["Generate Unique Hash for Similar"]
  n21["It Should exists"]
  n22["All Similar"]
  n23["Merge2"]
  n24["Change each Smiliar to the corresponding RecID"]
  n25["Determine Similar we should save"]
  n26["Save all this juicy data"]
  n27["Map Agent Input"]
  n28["gpt-4o"]
  n29["Table: Tools"]
  n30["Table: Attributes"]
  n31["make it a readable list"]
  n32["Get Schema"]
  n5 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n24
  n28 -->|"ai_languageModel out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n11
  n32 -->|"main out 0 to in 0"| n31
  n22 -->|"main out 0 to in 1"| n23
  n29 -->|"main out 0 to in 0"| n29
  n29 -->|"main out 0 to in 0"| n30
  n8 -->|"main out 0 to in 1"| n9
  n27 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n9
  n21 -->|"main out 0 to in 0"| n19
  n6 -->|"main out 0 to in 0"| n7
  n16 -->|"main out 0 to in 1"| n15
  n18 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 1"| n19
  n0 -->|"main out 0 to in 0"| n27
  n14 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n17
  n3 -->|"ai_outputParser out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 1"| n5
  n25 -->|"main out 0 to in 0"| n26
  n20 -->|"main out 0 to in 0"| n21
  n17 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n25
  n10 -->|"main out 0 to in 0"| n13
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
