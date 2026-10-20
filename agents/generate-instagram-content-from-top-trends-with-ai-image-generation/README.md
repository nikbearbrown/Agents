# Generate Instagram Content from Top Trends with AI Image Generation

Adapt the published “Generate Instagram Content from Top Trends with AI Image Generation” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["If media status is finished"]
  n1["If media status is finished1"]
  n2["Telegram"]
  n3["Telegram1"]
  n4["Telegram2"]
  n5["Loop Over Items"]
  n6["Schedule Trigger1"]
  n7["Telegram Params"]
  n8["Instagram params"]
  n9["Rapid Api params"]
  n10["filter the image content"]
  n11["get top trends on instagram #35;blender3d"]
  n12["get top trends on instagram #35;isometric"]
  n13["merge the array content"]
  n14["Check Data on Database Is Exist"]
  n15["If Data is Exist"]
  n16["send error message to telegram"]
  n17["insert data on db"]
  n18["Analyze Image and give the content"]
  n19["Analyze Content And Generate Instagram Caption"]
  n20["Prepare data on Instagram"]
  n21["Check Status Of Media Before Uploaded"]
  n22["Publish Media on Instagram"]
  n23["Check status of post"]
  n24["filter the image content-2"]
  n25["Replicate params"]
  n26["Generate image on flux"]
  n5 -->|"main out 1 to in 0"| n14
  n7 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 1 to in 0"| n17
  n8 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n11
  n25 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 0 to in 0"| n1
  n26 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 1"| n13
  n20 -->|"main out 0 to in 0"| n21
  n22 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n22
  n0 -->|"main out 1 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 1 to in 0"| n4
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n16
  n18 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n24
  n19 -->|"main out 0 to in 0"| n26
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
