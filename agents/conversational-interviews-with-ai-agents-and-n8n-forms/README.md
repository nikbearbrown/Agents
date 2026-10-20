# conversational interviews with ai agents and n8n forms

Adapt the published “conversational interviews with ai agents and n8n forms” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 64 executable nodes and 68 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Structured Output Parser"]
  n1["Set Variables"]
  n2["OpenAI Chat Model"]
  n3["OpenAI Chat Model1"]
  n4["OpenAI Chat Model2"]
  n5["Structured Output Parser1"]
  n6["On form submission"]
  n7["Generate SERP Queries"]
  n8["Structured Output Parser2"]
  n9["OpenAI Chat Model3"]
  n10["Set Initial Query"]
  n11["SERP to Items"]
  n12["Item Ref"]
  n13["Research Goal #43; Learnings"]
  n14["Accumulate Results"]
  n15["DeepResearch Results"]
  n16["Results to Items"]
  n17["Set Next Queries"]
  n18["For Each Query..."]
  n19["Feedback to Items"]
  n20["Ask Clarity Questions"]
  n21["For Each Question..."]
  n22["DeepResearch Subworkflow"]
  n23["Clarifying Questions"]
  n24["End Form"]
  n25["Initiate DeepResearch"]
  n26["Execution Data"]
  n27["JobType Router"]
  n28["OpenAI Chat Model4"]
  n29["Get Initial Query"]
  n30["Structured Output Parser4"]
  n31["Create Row"]
  n32["Report Page Generator"]
  n33["Is Depth Reached#63;"]
  n34["Get Research Results"]
  n35["Get Existing Row"]
  n36["Set In-Progress"]
  n37["Set Done"]
  n38["Tags to Items"]
  n39["Convert to HTML"]
  n40["HTML to Array"]
  n41["Notion Block Generator"]
  n42["Google Gemini Chat Model"]
  n43["Parse JSON blocks"]
  n44["Upload to Notion Page"]
  n45["Get Existing Row1"]
  n46["DeepResearch Report"]
  n47["DeepResearch Learnings"]
  n48["Generate Report"]
  n49["Generate Learnings"]
  n50["Confirmation"]
  n51["Research Request"]
  n52["Valid Blocks"]
  n53["Append Blocks"]
  n54["URL Sources to Lists"]
  n55["Empty Response"]
  n56["Has Content#63;"]
  n57["Combine #38; Send back to Loop"]
  n58["For Each Block..."]
  n59["Valid Results"]
  n60["RAG Web Browser"]
  n61["Get Markdown #43; URL"]
  n62["Is Apify Auth Error#63;"]
  n63["Stop and Error"]
  n12 -->|"main out 0 to in 0"| n60
  n31 -->|"main out 0 to in 0"| n25
  n50 -->|"main out 0 to in 0"| n24
  n56 -->|"main out 0 to in 0"| n61
  n56 -->|"main out 1 to in 0"| n55
  n52 -->|"main out 0 to in 0"| n53
  n53 -->|"main out 0 to in 0"| n58
  n40 -->|"main out 0 to in 0"| n38
  n11 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n23
  n38 -->|"main out 0 to in 0"| n41
  n59 -->|"main out 0 to in 0"| n56
  n55 -->|"main out 0 to in 0"| n18
  n26 -->|"main out 0 to in 0"| n27
  n27 -->|"main out 0 to in 0"| n35
  n27 -->|"main out 1 to in 0"| n7
  n27 -->|"main out 2 to in 0"| n45
  n39 -->|"main out 0 to in 0"| n40
  n60 -->|"main out 0 to in 0"| n62
  n36 -->|"main out 0 to in 0"| n10
  n35 -->|"main out 0 to in 0"| n36
  n51 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n49
  n19 -->|"main out 0 to in 0"| n21
  n58 -->|"main out 0 to in 0"| n37
  n58 -->|"main out 1 to in 0"| n44
  n18 -->|"main out 0 to in 0"| n57
  n18 -->|"main out 1 to in 0"| n12
  n45 -->|"main out 0 to in 0"| n46
  n29 -->|"main out 0 to in 0"| n32
  n33 -->|"main out 0 to in 0"| n34
  n33 -->|"main out 1 to in 0"| n15
  n2 -->|"ai_languageModel out 0 to in 0"| n47
  n43 -->|"main out 0 to in 0"| n52
  n43 -->|"main out 0 to in 0"| n54
  n10 -->|"main out 0 to in 0"| n49
  n14 -->|"main out 0 to in 0"| n33
  n49 -->|"main out 0 to in 0"| n14
  n61 -->|"main out 0 to in 0"| n47
  n6 -->|"main out 0 to in 0"| n51
  n3 -->|"ai_languageModel out 0 to in 0"| n46
  n4 -->|"ai_languageModel out 0 to in 0"| n23
  n9 -->|"ai_languageModel out 0 to in 0"| n7
  n28 -->|"ai_languageModel out 0 to in 0"| n32
  n46 -->|"main out 0 to in 0"| n39
  n23 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 0 to in 0"| n16
  n21 -->|"main out 0 to in 0"| n29
  n21 -->|"main out 1 to in 0"| n20
  n34 -->|"main out 0 to in 0"| n48
  n62 -->|"main out 0 to in 0"| n63
  n62 -->|"main out 1 to in 0"| n59
  n54 -->|"main out 0 to in 1"| n53
  n20 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n11
  n25 -->|"main out 0 to in 0"| n50
  n32 -->|"main out 0 to in 0"| n31
  n44 -->|"main out 0 to in 0"| n58
  n47 -->|"main out 0 to in 0"| n13
  n41 -->|"main out 0 to in 0"| n43
  n22 -->|"main out 0 to in 0"| n26
  n42 -->|"ai_languageModel out 0 to in 0"| n41
  n0 -->|"ai_outputParser out 0 to in 0"| n47
  n13 -->|"main out 0 to in 0"| n18
  n5 -->|"ai_outputParser out 0 to in 0"| n23
  n8 -->|"ai_outputParser out 0 to in 0"| n7
  n30 -->|"ai_outputParser out 0 to in 0"| n32
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
