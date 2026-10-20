# Delete NM of KV (By Name Serach)

Adapt the published “Delete NM of KV (By Name Serach)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Delete KV"]
  n1["Delete KV1"]
  n2["KV to Rename"]
  n3["Account Path"]
  n4["Delete KVs inside NM"]
  n5["Create KV-NM"]
  n6["Write KVs inside NM"]
  n7["-Get Keys inside NM"]
  n8["Delete KV inside NM"]
  n9["Read Value Of KV In NM"]
  n10["Manual Trigger"]
  n11["List KV-NMs #40;1#41;"]
  n12["Set KV-NM Name #40;2#41;"]
  n13["Set KV-NM Name #40;1#41;"]
  n14["Set KV-NM Name #40;3#41;"]
  n15["List KV-NMs #40;2#41;"]
  n16["List KV-NMs #40;3#41;"]
  n17["Set KV-NM Name #40;4#41;"]
  n18["Write V #38; MD of KV In NM"]
  n19["Set KV-NM Name #40;5#41;"]
  n20["Set KV-NM Name #40;6#41;"]
  n21["List KV-NMs #40;4#41;"]
  n22["List KV-NMs #40;5#41;"]
  n23["List KV-NMs #40;6#41;"]
  n24["List KV-NMs #40;7#41;"]
  n25["List KV-NMs #40;8#41;"]
  n26["List KV-NMs #40;9#41;"]
  n27["List KV-NMs #40;10#41;"]
  n28["Set KV-NM Name #40;7#41;"]
  n29["Set KV-NM Name #40;8#41;"]
  n30["Read MD from Key"]
  n3 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n20
  n3 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n28
  n3 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n19
  n3 -->|"main out 0 to in 0"| n29
  n2 -->|"main out 0 to in 0"| n22
  n10 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n8
  n15 -->|"main out 0 to in 0"| n0
  n16 -->|"main out 0 to in 0"| n4
  n21 -->|"main out 0 to in 0"| n18
  n22 -->|"main out 0 to in 0"| n1
  n23 -->|"main out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n9
  n25 -->|"main out 0 to in 0"| n30
  n26 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 0 to in 0"| n23
  n20 -->|"main out 0 to in 0"| n24
  n28 -->|"main out 0 to in 0"| n25
  n29 -->|"main out 0 to in 0"| n26
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
