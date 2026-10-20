# Data Standardization &amp; Google DNS Integration

Adapt the published “Data Standardization &amp; Google DNS Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["VirusTotal result"]
  n1["DNS Lookup"]
  n2["Set IP From Lookup"]
  n3["Set IP"]
  n4["Merge VirusTotal #38; Greynoise results"]
  n5["Is IP#63;"]
  n6["Start VirusTotal Scan"]
  n7["VirusTotal Summary"]
  n8["VirusTotal ready#63;"]
  n9["Wait 5s"]
  n10["Webhook"]
  n11["Get List of URLs"]
  n12["Set Email"]
  n13["Merge Greynoise results"]
  n14["Send Report Slack"]
  n15["Send Report Email"]
  n16["Greynoise Summary"]
  n17["Merge"]
  n18["Combine looped items"]
  n19["Filter"]
  n20["GreyNoise RIOT lookup"]
  n21["GreyNoise IP Check"]
  n22["Form Trigger"]
  n17 -->|"main out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n21
  n17 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 1 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n2
  n22 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 1 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 1"| n13
  n2 -->|"main out 0 to in 1"| n17
  n7 -->|"main out 0 to in 1"| n4
  n18 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n16
  n4 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n15
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
