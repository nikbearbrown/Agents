# HDW Lead Geländewagen

Adapt the published “HDW Lead Geländewagen” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 71 executable nodes and 78 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["OpenAI Chat Model"]
  n2["Simple Memory"]
  n3["Structured Output Parser"]
  n4["Google Sheets"]
  n5["Google Sheets1"]
  n6["Google Sheets2"]
  n7["Loop Over Items"]
  n8["HDW LinkedIn SN"]
  n9["HDW Get Company Website"]
  n10["Google Sheets3"]
  n11["Loop Over Items1"]
  n12["Google Sheets4"]
  n13["HDW Get User Posts"]
  n14["Aggregate"]
  n15["Loop Over Items2"]
  n16["Google Sheets5"]
  n17["Google Sheets6"]
  n18["Aggregate1"]
  n19["Loop Over Items3"]
  n20["Google Sheets7"]
  n21["Google Sheets8"]
  n22["Aggregate2"]
  n23["Loop Over Items4"]
  n24["Google Sheets9"]
  n25["HDW Get Company News"]
  n26["HDW Get Company Posts"]
  n27["Loop Over Items5"]
  n28["Split Out"]
  n29["OpenAI Chat Model1"]
  n30["Google Sheets10"]
  n31["HDW Site-map"]
  n32["HDW Parser"]
  n33["Summarise user posts"]
  n34["Summarise company news"]
  n35["Summarise company posts"]
  n36["Summarise company website"]
  n37["Google Sheets11"]
  n38["Loop Over Items6"]
  n39["Google Sheets12"]
  n40["Google Sheets13"]
  n41["Sort"]
  n42["If2"]
  n43["Limit"]
  n44["Loop Over Items7"]
  n45["Google Sheets14"]
  n46["Google Sheets15"]
  n47["Google Sheets16"]
  n48["Google Sheets17"]
  n49["Loop Over Items8"]
  n50["HDW LinkedIn Send Message"]
  n51["Schedule Trigger"]
  n52["Schedule Trigger1"]
  n53["When clicking #8216;Test workflow#8217;"]
  n54["HDW Get LinkedIn Profile Connections"]
  n55["HDW Send LinkedIn Connection"]
  n56["AI Agent: ICP -#62; LinkedIn search filters"]
  n57["Company name is not empty"]
  n58["Website is not empty"]
  n59["Post summary is empty"]
  n60["Company news is empty"]
  n61["Company post is empty"]
  n62["Lead Score is empty"]
  n63["Company Score Analysis"]
  n64["Split LinkedIn connections to items"]
  n65["5s"]
  n66["Company name is not empty1"]
  n67["Google Sheets18"]
  n68["Loop Over Items9"]
  n69["HDW Get Company Website1"]
  n70["Google Sheets19"]
  n65 -->|"main out 0 to in 0"| n50
  n42 -->|"main out 0 to in 0"| n43
  n41 -->|"main out 0 to in 0"| n42
  n43 -->|"main out 0 to in 0"| n44
  n14 -->|"main out 0 to in 0"| n33
  n28 -->|"main out 0 to in 0"| n27
  n18 -->|"main out 0 to in 0"| n34
  n22 -->|"main out 0 to in 0"| n35
  n32 -->|"ai_tool out 0 to in 0"| n36
  n31 -->|"ai_tool out 0 to in 0"| n36
  n4 -->|"main out 0 to in 0"| n5
  n2 -->|"ai_memory out 0 to in 0"| n56
  n5 -->|"main out 0 to in 0"| n57
  n6 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n58
  n12 -->|"main out 0 to in 0"| n59
  n16 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n60
  n20 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n61
  n24 -->|"main out 0 to in 0"| n23
  n30 -->|"main out 0 to in 0"| n11
  n37 -->|"main out 0 to in 0"| n62
  n39 -->|"main out 0 to in 0"| n38
  n40 -->|"main out 0 to in 0"| n41
  n45 -->|"main out 0 to in 0"| n44
  n46 -->|"main out 0 to in 0"| n47
  n47 -->|"main out 0 to in 0"| n49
  n48 -->|"main out 0 to in 0"| n49
  n67 -->|"main out 0 to in 0"| n68
  n70 -->|"main out 0 to in 0"| n66
  n8 -->|"main out 0 to in 0"| n27
  n7 -->|"main out 0 to in 0"| n70
  n7 -->|"main out 1 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 1 to in 0"| n36
  n15 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 1 to in 0"| n13
  n19 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 1 to in 0"| n25
  n23 -->|"main out 0 to in 0"| n37
  n23 -->|"main out 1 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n4
  n27 -->|"main out 1 to in 0"| n8
  n38 -->|"main out 0 to in 0"| n40
  n38 -->|"main out 1 to in 0"| n63
  n44 -->|"main out 1 to in 0"| n55
  n49 -->|"main out 1 to in 0"| n65
  n68 -->|"main out 0 to in 0"| n10
  n68 -->|"main out 1 to in 0"| n69
  n51 -->|"main out 0 to in 0"| n40
  n1 -->|"ai_languageModel out 0 to in 0"| n56
  n52 -->|"main out 0 to in 0"| n54
  n13 -->|"main out 0 to in 0"| n14
  n29 -->|"ai_languageModel out 0 to in 0"| n36
  n62 -->|"main out 0 to in 0"| n38
  n25 -->|"main out 0 to in 0"| n18
  n33 -->|"main out 0 to in 0"| n16
  n58 -->|"main out 0 to in 0"| n11
  n60 -->|"main out 0 to in 0"| n19
  n61 -->|"main out 0 to in 0"| n23
  n26 -->|"main out 0 to in 0"| n22
  n59 -->|"main out 0 to in 0"| n15
  n63 -->|"main out 0 to in 0"| n39
  n34 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n6
  n35 -->|"main out 0 to in 0"| n24
  n69 -->|"main out 0 to in 0"| n67
  n3 -->|"ai_outputParser out 0 to in 0"| n56
  n57 -->|"main out 0 to in 0"| n7
  n50 -->|"main out 0 to in 0"| n48
  n36 -->|"main out 0 to in 0"| n30
  n66 -->|"main out 0 to in 0"| n68
  n0 -->|"main out 0 to in 0"| n56
  n55 -->|"main out 0 to in 0"| n45
  n64 -->|"main out 0 to in 0"| n46
  n54 -->|"main out 0 to in 0"| n64
  n56 -->|"main out 0 to in 0"| n28
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
