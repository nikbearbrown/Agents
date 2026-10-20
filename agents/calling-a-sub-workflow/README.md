# Calling a Sub-workflow

Adapt the published “Calling a Sub-workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 36 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Get list of owners"]
  n2["Get list of clients for owner"]
  n3["If"]
  n4["Edit"]
  n5["Increment Page"]
  n6["Split Out1"]
  n7["Merge al the entries"]
  n8["If linkedin url is empty"]
  n9["if new post"]
  n10["Get list of clients"]
  n11["When Executed by Another Workflow"]
  n12["Get last post"]
  n13["Gmail"]
  n14["Search for user by link"]
  n15["Do nothing"]
  n16["Merge profileURL"]
  n17["Set last_post"]
  n18["Set last_position"]
  n19["if new position"]
  n20["Set data here"]
  n21["Change this for testing"]
  n22["Create entry with email"]
  n23["Get rows from document"]
  n24["Search for user profile by names"]
  n25["Profile URL not found#63;"]
  n26["Set the profile URL"]
  n27["Set the profile URL1"]
  n28["Update last post"]
  n29["Updates last position"]
  n30["Set post_updated"]
  n31["Set position_updated"]
  n32["Generate the email text"]
  n33["Merge on email"]
  n34["Split Out owners"]
  n35["Get current owner"]
  n3 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 1 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n28
  n12 -->|"main out 0 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n1
  n17 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 0 to in 0"| n3
  n33 -->|"main out 0 to in 0"| n32
  n19 -->|"main out 0 to in 0"| n29
  n16 -->|"main out 0 to in 0"| n14
  n30 -->|"main out 0 to in 0"| n33
  n34 -->|"main out 0 to in 0"| n35
  n28 -->|"main out 0 to in 0"| n30
  n35 -->|"main out 0 to in 0"| n10
  n18 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n34
  n10 -->|"main out 0 to in 0"| n21
  n26 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n6
  n31 -->|"main out 0 to in 1"| n33
  n27 -->|"main out 0 to in 0"| n16
  n29 -->|"main out 0 to in 0"| n31
  n23 -->|"main out 0 to in 0"| n8
  n25 -->|"main out 0 to in 0"| n15
  n25 -->|"main out 1 to in 0"| n26
  n21 -->|"main out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n23
  n32 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 1 to in 0"| n27
  n2 -->|"main out 0 to in 0"| n5
  n24 -->|"main out 0 to in 0"| n25
  n11 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n20
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
