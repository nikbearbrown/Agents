# Docsify example

Adapt the published “Docsify example” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 48 executable nodes and 71 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["CONFIG"]
  n1["Convert to File"]
  n2["HasFile#63;"]
  n3["Extract from File"]
  n4["Main Page"]
  n5["Instance overview"]
  n6["Sort-workflows"]
  n7["doc action"]
  n8["Empty Set"]
  n9["Load Doc File"]
  n10["Respond with markdown"]
  n11["Respond with HTML"]
  n12["Save New Doc File"]
  n13["Blank Doc File"]
  n14["Fetch Single Workflow1"]
  n15["Fill Workflow Table"]
  n16["Basic LLM Chain"]
  n17["OpenAI Chat Model"]
  n18["Structured Output Parser"]
  n19["Auto-fixing Output Parser"]
  n20["Respond with main page HTML"]
  n21["Workflow Tags"]
  n22["No Operation, do nothing"]
  n23["Merge"]
  n24["Fallback file name"]
  n25["mkdir"]
  n26["Merge1"]
  n27["Edit Page"]
  n28["Workflow md content"]
  n29["Is Action Edit#63;1"]
  n30["Is Action Edit#63;2"]
  n31["Generate Mermaid Chart"]
  n32["Merge2"]
  n33["Generated Doc"]
  n34["Passthrough"]
  n35["Merge3"]
  n36["Merge4"]
  n37["Merge5"]
  n38["Edit Fields"]
  n39["Is Action Save#63;"]
  n40["Merge6"]
  n41["Respond OK on Save"]
  n42["single workflow"]
  n43["file types"]
  n44["Get All Workflows"]
  n45["md files"]
  n46["Get Workflow tags"]
  n47["docsify"]
  n23 -->|"main out 0 to in 0"| n29
  n25 -->|"main out 0 to in 1"| n26
  n0 -->|"main out 0 to in 1"| n36
  n0 -->|"main out 0 to in 0"| n37
  n26 -->|"main out 0 to in 0"| n2
  n32 -->|"main out 0 to in 0"| n33
  n35 -->|"main out 0 to in 0"| n30
  n36 -->|"main out 0 to in 0"| n4
  n37 -->|"main out 0 to in 0"| n43
  n40 -->|"main out 0 to in 0"| n39
  n47 -->|"main out 0 to in 0"| n0
  n47 -->|"main out 0 to in 0"| n36
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n14
  n45 -->|"main out 0 to in 0"| n44
  n45 -->|"main out 1 to in 0"| n7
  n45 -->|"main out 2 to in 0"| n46
  n45 -->|"main out 3 to in 0"| n44
  n45 -->|"main out 4 to in 0"| n22
  n27 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n26
  n4 -->|"main out 0 to in 0"| n20
  n7 -->|"main out 0 to in 0"| n25
  n7 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n34
  n7 -->|"main out 1 to in 0"| n25
  n7 -->|"main out 1 to in 0"| n9
  n7 -->|"main out 1 to in 0"| n34
  n7 -->|"main out 2 to in 0"| n25
  n7 -->|"main out 2 to in 0"| n8
  n7 -->|"main out 2 to in 0"| n34
  n7 -->|"main out 3 to in 0"| n38
  n43 -->|"main out 0 to in 0"| n45
  n38 -->|"main out 0 to in 0"| n1
  n38 -->|"main out 0 to in 1"| n40
  n34 -->|"main out 0 to in 1"| n35
  n34 -->|"main out 0 to in 0"| n23
  n33 -->|"main out 0 to in 0"| n1
  n33 -->|"main out 0 to in 0"| n30
  n9 -->|"main out 0 to in 0"| n26
  n21 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n30
  n6 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 1"| n32
  n1 -->|"main out 0 to in 0"| n12
  n39 -->|"main out 0 to in 0"| n41
  n42 -->|"main out 0 to in 0"| n0
  n42 -->|"main out 0 to in 1"| n37
  n42 -->|"main out 1 to in 0"| n0
  n42 -->|"main out 1 to in 1"| n37
  n29 -->|"main out 0 to in 0"| n13
  n29 -->|"main out 1 to in 0"| n16
  n29 -->|"main out 1 to in 0"| n32
  n30 -->|"main out 0 to in 0"| n27
  n30 -->|"main out 1 to in 0"| n28
  n3 -->|"main out 0 to in 0"| n35
  n44 -->|"main out 0 to in 0"| n6
  n46 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n10
  n17 -->|"ai_languageModel out 0 to in 0"| n16
  n17 -->|"ai_languageModel out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n40
  n24 -->|"main out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n5
  n28 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n31
  n14 -->|"main out 0 to in 1"| n23
  n31 -->|"main out 0 to in 2"| n23
  n22 -->|"main out 0 to in 0"| n24
  n18 -->|"ai_outputParser out 0 to in 0"| n19
  n19 -->|"ai_outputParser out 0 to in 0"| n16
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
