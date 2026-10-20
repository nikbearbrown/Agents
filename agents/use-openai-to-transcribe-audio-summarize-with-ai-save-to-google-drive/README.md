# 🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive

Adapt the published “🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Gmail User for Approval"]
  n1["Set Config"]
  n2["Transcribe with OpenAI"]
  n3["Filter by .m4a extension"]
  n4["Limit to last file"]
  n5["Download audio file"]
  n6["Search Google Drive"]
  n7["Send Telegram Message"]
  n8["Send Gmail Message"]
  n9["Email Content Formatter"]
  n10["Summarize to Structured JSON"]
  n11["Summarize to JSON"]
  n12["Convert JSON to Markdown"]
  n13["Get Filename for JSON"]
  n14["Get Filename for Markdown"]
  n15["Save JSON file to Google Drive"]
  n16["Save Markdown file to Google Drive"]
  n17["Get JSON File Meta"]
  n18["Get Markdown File Meta"]
  n19["Prepare Response JSON"]
  n20["Prepare Response Markdown"]
  n21["Merge All Paths"]
  n22["Save Raw Transcript to Google Drive"]
  n23["Start Workflow"]
  n24["On File Created Trigger"]
  n1 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n6
  n21 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n15
  n19 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n20
  n2 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n4
  n14 -->|"main out 0 to in 0"| n16
  n20 -->|"main out 0 to in 1"| n21
  n10 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n18
  n22 -->|"main out 0 to in 2"| n21
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
