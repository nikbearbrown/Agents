# AI-Powered WhatsApp Chatbot for Text, Voice, Images &amp; PDFs

Adapt the published “AI-Powered WhatsApp Chatbot for Text, Voice, Images &amp; PDFs” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["WhatsApp Trigger"]
  n1["Download Image"]
  n2["Analyze Image"]
  n3["Download Audio"]
  n4["Transcribe Audio"]
  n5["OpenAI Chat Model"]
  n6["AI Agent1"]
  n7["Download File"]
  n8["Extract from File"]
  n9["Simple Memory"]
  n10["Get File Url"]
  n11["Only PDF File"]
  n12["Fix mimeType for Audio"]
  n13["Send message"]
  n14["Send audio"]
  n15["Incorrect format"]
  n16["Text"]
  n17["Audio"]
  n18["Image"]
  n19["File"]
  n20["Not supported"]
  n21["Get Image Url"]
  n22["Get Audio Url"]
  n23["Generate Audio Response"]
  n24["From audio to audio#63;"]
  n25["Input type"]
  n19 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n6
  n18 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n24
  n25 -->|"main out 0 to in 0"| n16
  n25 -->|"main out 1 to in 0"| n22
  n25 -->|"main out 2 to in 0"| n21
  n25 -->|"main out 3 to in 0"| n11
  n25 -->|"main out 4 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n18
  n7 -->|"main out 0 to in 0"| n8
  n22 -->|"main out 0 to in 0"| n3
  n21 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 1 to in 0"| n15
  n9 -->|"ai_memory out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n25
  n8 -->|"main out 0 to in 0"| n19
  n5 -->|"ai_languageModel out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 1 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n12
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
