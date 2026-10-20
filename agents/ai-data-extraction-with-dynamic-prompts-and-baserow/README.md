# ai data extraction with dynamic prompts and baserow

Adapt the published “ai data extraction with dynamic prompts and baserow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 36 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Event Type"]
  n1["Get Prompt Fields"]
  n2["Get File Data"]
  n3["Extract from File"]
  n4["Get Result"]
  n5["Loop Over Items"]
  n6["Row Reference"]
  n7["Generate Field Value"]
  n8["Fields to Update"]
  n9["Loop Over Items1"]
  n10["Row Ref"]
  n11["Get File Data1"]
  n12["Extract from File1"]
  n13["Get Result1"]
  n14["Generate Field Value1"]
  n15["Filter Valid Rows"]
  n16["Filter Valid Fields"]
  n17["Event Ref"]
  n18["Event Ref1"]
  n19["OpenAI Chat Model"]
  n20["OpenAI Chat Model1"]
  n21["Get Webhook Payload"]
  n22["Parse Event"]
  n23["Get Table Schema"]
  n24["Fetch Records"]
  n25["Update Row"]
  n26["Get Row"]
  n27["Add Row ID to Payload"]
  n28["Update Record"]
  n29["Airtable Webhook"]
  n30["When clicking #8216;Test workflow#8217;"]
  n31["Set Airtable Vars"]
  n32["Get Table Schema1"]
  n33["Get #34;Input#34; Field"]
  n34["RecordsChanged Webhook"]
  n35["FieldsChanged Webhook"]
  n26 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n16
  n18 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n18
  n0 -->|"main out 1 to in 0"| n17
  n0 -->|"main out 2 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n27
  n22 -->|"main out 0 to in 0"| n0
  n24 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n2
  n28 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 1 to in 0"| n6
  n29 -->|"main out 0 to in 0"| n23
  n8 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 1 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n9
  n33 -->|"main out 0 to in 0"| n34
  n1 -->|"main out 0 to in 0"| n21
  n32 -->|"main out 0 to in 0"| n33
  n19 -->|"ai_languageModel out 0 to in 0"| n14
  n31 -->|"main out 0 to in 0"| n32
  n31 -->|"main out 0 to in 0"| n35
  n12 -->|"main out 0 to in 0"| n8
  n20 -->|"ai_languageModel out 0 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n24
  n21 -->|"main out 0 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n4
  n27 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n13
  n30 -->|"main out 0 to in 0"| n31
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
