# ai data extraction with dynamic prompts and airtable

Adapt the published “ai data extraction with dynamic prompts and airtable” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Baserow Event"]
  n1["Event Type"]
  n2["Table Fields API"]
  n3["Get Prompt Fields"]
  n4["Get Event Body"]
  n5["List Table API"]
  n6["Get Valid Rows"]
  n7["Get File Data"]
  n8["Extract from File"]
  n9["Update Row"]
  n10["Get Result"]
  n11["Loop Over Items"]
  n12["Row Reference"]
  n13["Generate Field Value"]
  n14["Get Row"]
  n15["Rows to List"]
  n16["Fields to Update"]
  n17["Loop Over Items1"]
  n18["Row Ref"]
  n19["Get File Data1"]
  n20["Extract from File1"]
  n21["Update Row1"]
  n22["Get Result1"]
  n23["Generate Field Value1"]
  n24["Filter Valid Rows"]
  n25["Filter Valid Fields"]
  n26["Event Ref"]
  n27["Event Ref1"]
  n28["OpenAI Chat Model"]
  n29["OpenAI Chat Model1"]
  n14 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n19
  n26 -->|"main out 0 to in 0"| n25
  n27 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n27
  n1 -->|"main out 1 to in 0"| n26
  n1 -->|"main out 2 to in 0"| n26
  n10 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n11
  n22 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n24
  n0 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n20
  n6 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 1 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n23
  n17 -->|"main out 1 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n4
  n28 -->|"ai_languageModel out 0 to in 0"| n23
  n20 -->|"main out 0 to in 0"| n16
  n29 -->|"ai_languageModel out 0 to in 0"| n13
  n25 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n22
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
