# webhook and crypto and append airtable

Adapt the published “webhook and crypto and append airtable” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["Extract URL"]
  n2["Check URL"]
  n3["Crypto"]
  n4["Airtable"]
  n5["Set ID,shortUrl,longUrl"]
  n6["Find by ID"]
  n7["Already exists #63;"]
  n8["Set Output"]
  n9["Set Error output"]
  n10["Set Output1"]
  n11["Set input"]
  n12["Webhook1"]
  n13["Set Error output1"]
  n14["Check Id"]
  n15["Find by ID1"]
  n16["Already exists #63;1"]
  n17["Set Output2"]
  n18["Extract Id"]
  n19["404 Error"]
  n20["Update clicks"]
  n21["Prepare clicks count"]
  n22["Webhook2"]
  n23["Find by ID2"]
  n24["Extract stats"]
  n25["Set dashboard"]
  n3 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n18
  n14 -->|"main out 1 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n14
  n22 -->|"main out 0 to in 0"| n23
  n2 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 1 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n4
  n18 -->|"main out 0 to in 0"| n15
  n6 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 0"| n16
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n20 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n21
  n16 -->|"main out 1 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n6
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
