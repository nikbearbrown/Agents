# telegram and receive telegram events and sendphoto telegram

Adapt the published “telegram and receive telegram events and sendphoto telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Switch"]
  n1["msg_greet"]
  n2["msg_wrongcommand"]
  n3["Telegram Trigger"]
  n4["msg_getweather"]
  n5["City List"]
  n6["Convert API response"]
  n7["Get weather data"]
  n8["Spreadsheet File"]
  n9["Write csv"]
  n10["Filename"]
  n11["msg_errorAPI"]
  n12["Any errors API#63;"]
  n13["msg_errorR"]
  n14["Read Binary File"]
  n15["R successful#63;"]
  n16["Merge"]
  n17["Merge1"]
  n18["msg_pleasewait"]
  n19["Merge2"]
  n20["Run R script"]
  n16 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 1 to in 0"| n18
  n0 -->|"main out 1 to in 0"| n19
  n0 -->|"main out 3 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 1 to in 0"| n13
  n18 -->|"main out 0 to in 1"| n19
  n12 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 1 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n8
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
