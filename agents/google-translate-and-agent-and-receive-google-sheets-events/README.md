# google translate and agent and receive google sheets events

Adapt the published “google translate and agent and receive google sheets events” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Google Translate"]
  n1["AI Agent"]
  n2["OpenAI Chat Model"]
  n3["Structured Output Parser"]
  n4["Merge"]
  n5["Trigger Added Row"]
  n6["No Operation, do nothing"]
  n7["Upload Picture"]
  n8["Get Picture"]
  n9["Call API Pexels"]
  n10["Take initialText"]
  n11["Extract Image Link"]
  n12["Final Merge"]
  n13["Extract Pinyin and Example"]
  n14["Extract Fields"]
  n15["initialText is empty#63;"]
  n16["Add Results in Sheet"]
  n4 -->|"main out 0 to in 0"| n12
  n1 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n16
  n8 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n9
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 1"| n12
  n15 -->|"main out 0 to in 0"| n0
  n15 -->|"main out 1 to in 0"| n6
  n3 -->|"ai_outputParser out 0 to in 0"| n1
  n13 -->|"main out 0 to in 1"| n4
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
