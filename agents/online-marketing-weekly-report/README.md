# Online Marketing Weekly Report

Adapt the published “Online Marketing Weekly Report” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 46 executable nodes and 42 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["OpenAI Chat Model"]
  n2["Google_Ads"]
  n3["Meta_Ads"]
  n4["Analytics_Domain_1"]
  n5["Analytics_Domain_3"]
  n6["Analytics_Domain_2"]
  n7["Analytics_Domain_4"]
  n8["Analytics_Domain_5"]
  n9["Execute Workflow Trigger"]
  n10["Calculator"]
  n11["Calculator1"]
  n12["Calculator3"]
  n13["Call Google Analytics data: Last 7 days"]
  n14["Call Google Analytics data: Last 7 days #40;previous year#41;"]
  n15["Calculation same period previous year"]
  n16["Format data input #40;previous year#41;"]
  n17["Format data input #40;current year#41;"]
  n18["Assign data from input #40;current year#41;"]
  n19["Summarize input #40;current year#41;"]
  n20["Assign input #40;previous year#41;"]
  n21["Summarize input #40;previous year#41;"]
  n22["Calculate date format for Google Ads request #40;last 7 days#41;"]
  n23["Call Google Ads Data: Last 7 days"]
  n24["Call Google Ads Data: Last 7 days #40;previous year#41;"]
  n25["Call Meta Ads Data: Last 7 days"]
  n26["Call Meta Ads Data: Last 7 days #40;previous year#41;"]
  n27["Summarize Meta input #40;current year#41;"]
  n28["Assign Meta data from input #40;current year#41;"]
  n29["Assign Meta data input #40;previous year#41;"]
  n30["Summarize Meta data input #40;previous year#41;"]
  n31["Format all Meta data for LLM"]
  n32["Processing for Google Ads report"]
  n33["Format all Google data for LLM"]
  n34["Assign Google Analytics data input #40;current year#41;"]
  n35["Summarize Google Analytics input #40;current year#41;"]
  n36["Calculate date format for meta ads request s"]
  n37["Calculation same period previous year1"]
  n38["Assign Google Analytics data input #40;previous year#41;"]
  n39["Summarize Google Analytics input #40;previous year#41;"]
  n40["Send mail report"]
  n41["Processing for Meta Ads Report"]
  n42["Processing for Google Analytics Report"]
  n43["Processing for Telegram Report"]
  n44["Weekly Report Agent"]
  n45["Send Telegram report"]
  n3 -->|"ai_tool out 0 to in 0"| n44
  n10 -->|"ai_tool out 0 to in 0"| n42
  n2 -->|"ai_tool out 0 to in 0"| n44
  n11 -->|"ai_tool out 0 to in 0"| n32
  n12 -->|"ai_tool out 0 to in 0"| n41
  n0 -->|"main out 0 to in 0"| n44
  n1 -->|"ai_languageModel out 0 to in 0"| n44
  n4 -->|"ai_tool out 0 to in 0"| n44
  n6 -->|"ai_tool out 0 to in 0"| n44
  n5 -->|"ai_tool out 0 to in 0"| n44
  n7 -->|"ai_tool out 0 to in 0"| n44
  n8 -->|"ai_tool out 0 to in 0"| n44
  n44 -->|"main out 0 to in 0"| n43
  n44 -->|"main out 0 to in 0"| n40
  n9 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 0 to in 0"| n21
  n31 -->|"main out 0 to in 0"| n41
  n33 -->|"main out 0 to in 0"| n32
  n43 -->|"main out 0 to in 0"| n45
  n19 -->|"main out 0 to in 0"| n15
  n25 -->|"main out 0 to in 0"| n28
  n21 -->|"main out 0 to in 0"| n33
  n17 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n20
  n27 -->|"main out 0 to in 0"| n26
  n18 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 0 to in 0"| n24
  n29 -->|"main out 0 to in 0"| n30
  n37 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n34
  n30 -->|"main out 0 to in 0"| n31
  n28 -->|"main out 0 to in 0"| n27
  n36 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n29
  n35 -->|"main out 0 to in 0"| n37
  n39 -->|"main out 0 to in 0"| n42
  n34 -->|"main out 0 to in 0"| n35
  n24 -->|"main out 0 to in 0"| n16
  n38 -->|"main out 0 to in 0"| n39
  n14 -->|"main out 0 to in 0"| n38
  n22 -->|"main out 0 to in 0"| n23
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
