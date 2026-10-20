# 💥AI Social Video Generator with GPT-4, Kling &amp; Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter &amp; Pinterest - vide

Adapt the published “💥AI Social Video Generator with GPT-4, Kling &amp; Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter &amp; Pinterest - vide” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Trigger: Telegram Prompt"]
  n1["Extract Prompt #38; Caption"]
  n2["Transform Prompt for Kling #40;GPT-4#41;"]
  n3["OpenAI Model Bridge"]
  n4["Generate Video via Kling API"]
  n5["Wait for Video Generation"]
  n6["Get Generated Video URL"]
  n7["Generate Voice-Over Script"]
  n8["Convert Script to Audio #40;TTS#41;"]
  n9["Upload Audio to Cloudinary"]
  n10["Merge Audio #43; Video"]
  n11["Wait for Audio/Video Fusion"]
  n12["Get Video URL with Audio"]
  n13["Wait Before Captioning"]
  n14["Add Captions/Subtitles to Video"]
  n15["Wait for Caption Render"]
  n16["Get Final Video URL #40;Audio #43; Captions#41;"]
  n17["Generate Social Caption from Voiceover"]
  n18["Generate YouTube-Style Title"]
  n19["Save Video Metadata to Google Sheets"]
  n20["Send Final Video to Telegram"]
  n21["Send Caption Link via Telegram"]
  n22["Assign Social Media IDs"]
  n23["Upload Video to Blotato"]
  n24["Post to Instagram"]
  n25["Post to YouTube"]
  n26["Post to TikTok"]
  n27["Post to Facebook Page"]
  n28["Post to Threads"]
  n29["Post to Twitter #40;X#41;"]
  n30["Post to LinkedIn"]
  n31["Post to Bluesky"]
  n32["Post to Pinterest"]
  n10 -->|"main out 0 to in 0"| n11
  n3 -->|"ai_languageModel out 0 to in 0"| n2
  n13 -->|"main out 0 to in 0"| n14
  n22 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n24
  n23 -->|"main out 0 to in 0"| n25
  n23 -->|"main out 0 to in 0"| n26
  n23 -->|"main out 0 to in 0"| n27
  n23 -->|"main out 0 to in 0"| n28
  n23 -->|"main out 0 to in 0"| n29
  n23 -->|"main out 0 to in 0"| n30
  n23 -->|"main out 0 to in 0"| n31
  n23 -->|"main out 0 to in 0"| n32
  n15 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
  n9 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n5
  n18 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n9
  n21 -->|"main out 0 to in 0"| n22
  n14 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 0"| n20
  n17 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 0 to in 0"| n17
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
