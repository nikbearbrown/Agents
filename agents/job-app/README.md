# Job-App

Adapt the published “Job-App” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 32 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Frontend input"]
  n1["Extract data from pdf"]
  n2["Structured Output Parser"]
  n3["DeepSeek Chat Model"]
  n4["Personal Details Extract"]
  n5["Drive Details Set"]
  n6["Google Drive"]
  n7["Primary Details"]
  n8["Google Sheets"]
  n9["Sheets Title Set"]
  n10["Sheet Titles"]
  n11["Google Sheets2"]
  n12["URL Fields"]
  n13["Job Request URL"]
  n14["Job Details Set"]
  n15["Store Job details"]
  n16["Create Personal Sheet"]
  n17["Extract Job from Sheets"]
  n18["Code"]
  n19["Loop Over Items"]
  n20["AI Agent"]
  n21["DeepSeek Chat Model1"]
  n22["Think"]
  n23["Structured Output Parser1"]
  n24["Convert to File"]
  n25["Code1"]
  n26["HTTP Request"]
  n27["Edit Fields"]
  n28["Edit Fields1"]
  n29["Google Drive1"]
  n30["Edit Fields2"]
  n31["Google Sheets1"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n4
  n2 -->|"ai_outputParser out 0 to in 0"| n4
  n3 -->|"ai_languageModel out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n25
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 1 to in 0"| n28
  n20 -->|"main out 0 to in 0"| n24
  n21 -->|"ai_languageModel out 0 to in 0"| n20
  n22 -->|"ai_tool out 0 to in 0"| n20
  n23 -->|"ai_outputParser out 0 to in 0"| n20
  n24 -->|"main out 0 to in 0"| n27
  n25 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n29
  n27 -->|"main out 0 to in 0"| n26
  n28 -->|"main out 0 to in 0"| n20
  n29 -->|"main out 0 to in 0"| n30
  n30 -->|"main out 0 to in 0"| n31
  n31 -->|"main out 0 to in 0"| n19
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/AloysJehwin--job-app.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
