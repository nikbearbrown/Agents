# AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs and upload to all social networks

Adapt the published “AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs and upload to all social networks” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 43 executable nodes and 47 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get image"]
  n1["Generate Image"]
  n2["Image-to-Video"]
  n3["Get Video"]
  n4["List Elements"]
  n5["Wait 10min"]
  n6["Wait 3min"]
  n7["Wait 5min"]
  n8["Generate voice"]
  n9["List Elements1"]
  n10["Fail check"]
  n11["Wait to retry"]
  n12["Generate Image Prompts"]
  n13["Calculate Token Usage"]
  n14["Check for failures"]
  n15["Generate Video Captions"]
  n16["Match captions with videos"]
  n17["Generate Script"]
  n18["Upload Voice Audio"]
  n19["Set Access Permissions"]
  n20["Pair Videos with Audio"]
  n21["Render Final Video"]
  n22["Notify me on Discord"]
  n23["Once Per Day"]
  n24["Load Google Sheet"]
  n25["Create List"]
  n26["Wait1"]
  n27["Get Final Video"]
  n28["Upload Final Video"]
  n29["Get Raw File"]
  n30["Set Permissions"]
  n31["Update Google Sheet"]
  n32["Set API Keys"]
  n33["Validate list formatting"]
  n34["Get Audio from Video"]
  n35["Generate Description for Videos in Tiktok and Instagram"]
  n36["Upload Video and Description to Tiktok"]
  n37["Upload Video and Description to Instagram"]
  n38["Upload Video and Description to Youtube"]
  n39["Upload Video and Description to Facebook"]
  n40["Upload Video and Description to Linkedin"]
  n41["Read Video from Google Drive"]
  n42["Write video"]
  n26 -->|"main out 0 to in 0"| n27
  n3 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 1"| n16
  n5 -->|"main out 0 to in 0"| n3
  n25 -->|"main out 0 to in 0"| n33
  n42 -->|"main out 0 to in 0"| n34
  n29 -->|"main out 0 to in 0"| n28
  n29 -->|"main out 0 to in 0"| n42
  n23 -->|"main out 0 to in 0"| n32
  n32 -->|"main out 0 to in 0"| n24
  n4 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 1"| n20
  n17 -->|"main out 0 to in 0"| n8
  n27 -->|"main out 0 to in 0"| n29
  n30 -->|"main out 0 to in 0"| n31
  n24 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 1 to in 0"| n2
  n21 -->|"main out 0 to in 0"| n26
  n28 -->|"main out 0 to in 0"| n30
  n18 -->|"main out 0 to in 0"| n19
  n31 -->|"main out 0 to in 0"| n22
  n34 -->|"main out 0 to in 0"| n35
  n13 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n25
  n33 -->|"main out 0 to in 0"| n12
  n33 -->|"main out 0 to in 0"| n16
  n33 -->|"main out 0 to in 0"| n17
  n33 -->|"main out 1 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n4
  n41 -->|"main out 0 to in 0"| n36
  n41 -->|"main out 0 to in 0"| n37
  n41 -->|"main out 0 to in 0"| n38
  n41 -->|"main out 0 to in 0"| n39
  n41 -->|"main out 0 to in 0"| n40
  n35 -->|"main out 0 to in 0"| n41
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
