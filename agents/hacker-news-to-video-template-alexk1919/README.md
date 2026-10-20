# Hacker News to Video Template - AlexK1919

Adapt the published “Hacker News to Video Template - AlexK1919” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 39 executable nodes and 38 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Hacker News"]
  n2["Loop Over Items"]
  n3["OpenAI Chat Model3"]
  n4["HTTP Request1"]
  n5["Structured Output Parser"]
  n6["Upload to Minio"]
  n7["News1"]
  n8["Leo - Improve Prompt"]
  n9["Leo - Get imageId"]
  n10["Runway - Create Video"]
  n11["Runway - Get Video"]
  n12["Wait2"]
  n13["If Topic"]
  n14["Get Image"]
  n15["Prompt Settings1"]
  n16["Leo - Generate Image"]
  n17["Wait1"]
  n18["Limit"]
  n19["Image Analysis"]
  n20["Wait3"]
  n21["Article Analysis"]
  n22["Dropbox"]
  n23["Google Drive"]
  n24["Microsoft OneDrive"]
  n25["YouTube"]
  n26["X"]
  n27["Instagram"]
  n28["LinkedIn"]
  n29["Leo - Improve Prompt2"]
  n30["Wait4"]
  n31["Wait6"]
  n32["Leo - Generate Image2"]
  n33["Leo - Get imageId2"]
  n34["Runway - Create Video2"]
  n35["Runway - Get Video2"]
  n36["Cre - Generate Video1"]
  n37["Cre - Get Video"]
  n38["Article Prep"]
  n26 -->|"main out 0 to in 0"| n28
  n18 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n11
  n20 -->|"main out 0 to in 0"| n37
  n30 -->|"main out 0 to in 0"| n35
  n31 -->|"main out 0 to in 0"| n33
  n22 -->|"main out 0 to in 0"| n23
  n25 -->|"main out 0 to in 0"| n26
  n13 -->|"main out 0 to in 0"| n19
  n13 -->|"main out 1 to in 0"| n2
  n28 -->|"main out 0 to in 0"| n27
  n14 -->|"main out 0 to in 0"| n38
  n1 -->|"main out 0 to in 0"| n18
  n38 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n24
  n4 -->|"ai_tool out 0 to in 0"| n21
  n19 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 1 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n13
  n21 -->|"main out 1 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n8
  n9 -->|"main out 0 to in 0"| n10
  n33 -->|"main out 0 to in 0"| n34
  n24 -->|"main out 0 to in 0"| n6
  n3 -->|"ai_languageModel out 0 to in 0"| n21
  n11 -->|"main out 0 to in 0"| n29
  n35 -->|"main out 0 to in 0"| n36
  n16 -->|"main out 0 to in 0"| n17
  n8 -->|"main out 0 to in 0"| n16
  n36 -->|"main out 0 to in 0"| n20
  n32 -->|"main out 0 to in 0"| n31
  n29 -->|"main out 0 to in 0"| n32
  n10 -->|"main out 0 to in 0"| n12
  n34 -->|"main out 0 to in 0"| n30
  n5 -->|"ai_outputParser out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n1
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
