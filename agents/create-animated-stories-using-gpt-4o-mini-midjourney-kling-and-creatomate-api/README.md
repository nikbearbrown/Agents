# Create Animated Stories using GPT-4o-mini, Midjourney, Kling and Creatomate API

Adapt the published “Create Animated Stories using GPT-4o-mini, Midjourney, Kling and Creatomate API” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 45 executable nodes and 50 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["output1"]
  n1["output2"]
  n2["Get Prompt"]
  n3["Basic Params"]
  n4["Get Task ID of the First Image"]
  n5["Midjourney Generator of the First Image"]
  n6["Wait for the First Image Generation"]
  n7["Verify the first image generation status"]
  n8["Get the First Image URL"]
  n9["Midjourney Generator of the Second Image"]
  n10["Midjourney Generator of the Third Image"]
  n11["Get the First Image Generation Status"]
  n12["Get the Second Image Generation Status"]
  n13["Get the Third Image Generation Status"]
  n14["Get the Second Image URL"]
  n15["Get the Third Image URL"]
  n16["Wait for the Second Image Generation"]
  n17["Get Task of the First Image"]
  n18["Get Task of the Second Image"]
  n19["Verify the second image generation status"]
  n20["Verify the third image generation status"]
  n21["Get Task of the Third Image"]
  n22["Wait for the Third Image Generation"]
  n23["Get three Image URLs"]
  n24["Generate the First Video"]
  n25["Generate the Second Video"]
  n26["Generate the Third Video"]
  n27["Final Video Combination"]
  n28["Get the Third Video URL"]
  n29["Get Video Task IDs"]
  n30["Get the First Video Task"]
  n31["Verify the First Video Generation"]
  n32["Verify the Second Video Generation"]
  n33["Verify the Third Video Generation"]
  n34["Wait for Video Generation for at Least 4 min"]
  n35["Wait for the First Video Generation"]
  n36["Wait for the Second Video Generation"]
  n37["Wait for the Third Video Generation"]
  n38["Get the First Video Generation"]
  n39["Get the Second Video Generation"]
  n40["Get the Third Video Generation"]
  n41["Get the Second Video Task"]
  n42["Get the Third Video Task"]
  n43["When clicking Test workflow"]
  n44["GPT-4o-mini Generate Image Scenario Prompt"]
  n0 -->|"main out 0 to in 0"| n41
  n1 -->|"main out 0 to in 0"| n42
  n2 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n44
  n29 -->|"main out 0 to in 0"| n34
  n23 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n23
  n28 -->|"main out 0 to in 0"| n27
  n24 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n29
  n30 -->|"main out 0 to in 0"| n31
  n14 -->|"main out 0 to in 0"| n10
  n42 -->|"main out 0 to in 0"| n33
  n25 -->|"main out 0 to in 0"| n26
  n41 -->|"main out 0 to in 0"| n32
  n17 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n20
  n43 -->|"main out 0 to in 0"| n3
  n18 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n6
  n38 -->|"main out 0 to in 0"| n0
  n40 -->|"main out 0 to in 0"| n28
  n39 -->|"main out 0 to in 0"| n1
  n31 -->|"main out 0 to in 0"| n38
  n31 -->|"main out 1 to in 0"| n35
  n33 -->|"main out 0 to in 0"| n40
  n33 -->|"main out 1 to in 0"| n37
  n32 -->|"main out 0 to in 0"| n39
  n32 -->|"main out 1 to in 0"| n36
  n6 -->|"main out 0 to in 0"| n17
  n35 -->|"main out 0 to in 0"| n30
  n22 -->|"main out 0 to in 0"| n21
  n37 -->|"main out 0 to in 0"| n42
  n16 -->|"main out 0 to in 0"| n18
  n36 -->|"main out 0 to in 0"| n41
  n11 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n14
  n5 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 1 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 1 to in 0"| n22
  n19 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 1 to in 0"| n16
  n44 -->|"main out 0 to in 0"| n2
  n34 -->|"main out 0 to in 0"| n30
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
