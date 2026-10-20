# All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem

Adapt the published “All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["gpt-4o-mini"]
  n1["Chat Response"]
  n2["Telegram Response"]
  n3["AI Tools Agent"]
  n4["Aggregate"]
  n5["Merge"]
  n6["Get Audio File"]
  n7["Analyze Image"]
  n8["Transcribe Recording"]
  n9["Edit Fields"]
  n10["Convert to Image File"]
  n11["Extract from File to Base64"]
  n12["Message Router"]
  n13["Image Schema1"]
  n14["caption"]
  n15["Merge1"]
  n16["Get Image"]
  n17["Edit Fields1"]
  n18["Postgres Chat Memory"]
  n19["Save Note Tool"]
  n20["Save Memory"]
  n21["Listen for Telegram Events"]
  n22["Validation"]
  n23["Check User #38; Chat ID"]
  n24["Error message"]
  n25["Baserow Retrieve Memories"]
  n26["Baserow Retrieve Notes"]
  n27["Window Memory #40;Easy Mode#41;"]
  n5 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n17
  n14 -->|"main out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n3
  n16 -->|"main out 0 to in 0"| n11
  n22 -->|"main out 0 to in 0"| n23
  n9 -->|"main out 0 to in 0"| n25
  n9 -->|"main out 0 to in 0"| n26
  n20 -->|"ai_tool out 0 to in 0"| n3
  n0 -->|"ai_languageModel out 0 to in 0"| n3
  n17 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 0 to in 0"| n26
  n7 -->|"main out 0 to in 1"| n15
  n13 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 1 to in 0"| n9
  n12 -->|"main out 2 to in 0"| n13
  n12 -->|"main out 3 to in 0"| n24
  n19 -->|"ai_tool out 0 to in 0"| n3
  n23 -->|"main out 0 to in 0"| n12
  n23 -->|"main out 1 to in 0"| n24
  n18 -->|"ai_memory out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n25
  n8 -->|"main out 0 to in 0"| n26
  n10 -->|"main out 0 to in 0"| n7
  n26 -->|"main out 0 to in 1"| n5
  n25 -->|"main out 0 to in 0"| n5
  n21 -->|"main out 0 to in 0"| n22
  n11 -->|"main out 0 to in 0"| n10
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
