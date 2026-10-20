# Suspicious_login_detection

Adapt the published “Suspicious_login_detection” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 40 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Extract relevant data"]
  n1["New /login event"]
  n2["Unknown threat#63;"]
  n3["Get last 10 logins from the same user"]
  n4["Query IP API1"]
  n5["New location#63;"]
  n6["Parse User Agent"]
  n7["Merge"]
  n8["New Device/Browser#63;"]
  n9["Complete login info"]
  n10["Query user by ID"]
  n11["New Location"]
  n12["New Device/Browser"]
  n13["User has email#63;"]
  n14["HTML"]
  n15["Inform user"]
  n16["noise#63;"]
  n17["Slack"]
  n18["Check trust level"]
  n19["Check classification"]
  n20["riot#63;"]
  n21["#128308; Priority: HIGH"]
  n22["#128993; Priority: MEDIUM"]
  n23["#128994; Priority: LOW"]
  n24["GreyNoise"]
  n25["IP API"]
  n26["UserParser"]
  n27["When clicking #34;Execute Workflow#34;"]
  n28["Example event"]
  n29["Known, Do Nothing"]
  n30["Known Location"]
  n31["Old Device/Browser"]
  n32["Not Riot"]
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 1"| n9
  n20 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 1 to in 0"| n32
  n25 -->|"main out 0 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n19
  n16 -->|"main out 1 to in 0"| n20
  n24 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n16
  n26 -->|"main out 0 to in 1"| n7
  n11 -->|"main out 0 to in 0"| n10
  n28 -->|"main out 0 to in 0"| n0
  n5 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 1 to in 0"| n30
  n4 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n29
  n13 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 1 to in 0"| n21
  n18 -->|"main out 2 to in 0"| n22
  n18 -->|"main out 3 to in 0"| n23
  n12 -->|"main out 0 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 1 to in 0"| n31
  n21 -->|"main out 0 to in 0"| n17
  n19 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 1 to in 0"| n22
  n19 -->|"main out 2 to in 0"| n23
  n0 -->|"main out 0 to in 0"| n24
  n0 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n25
  n22 -->|"main out 0 to in 0"| n17
  n27 -->|"main out 0 to in 0"| n28
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n6
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
