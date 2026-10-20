# Publish Videos &amp; Images - Blotato

Adapt the published “Publish Videos &amp; Images - Blotato” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["#91;Instagram#93; Publish via Blotato"]
  n1["#91;Facebook#93; Publish via Blotato"]
  n2["#91;Linkedin#93; Publish via Blotato"]
  n3["#91;Tiktok#93; Publish via Blotato"]
  n4["#91;Pinterest#93; Publish via Blotato"]
  n5["#91;Youtube#93; Publish via Blotato"]
  n6["#91;Threads#93; Publish via Blotato"]
  n7["#91;Twitter#93; Publish via Blotato"]
  n8["#91;Bluesky#93; Publish via Blotato"]
  n9["Prepare for Publish"]
  n10["Airtable"]
  n11["Upload Video to Blotato"]
  n12["Upload Image to Blotato"]
  n13["Ensure Valid YouTube Title"]
  n14["Airtable: Posted Instagram"]
  n15["Airtable: Posted Instagram1"]
  n16["When clicking #8216;Test workflow#8217;"]
  n17["Airtable Record ID"]
  n18["Pinterest System #40;tm#41;"]
  n19["Grab Pinterest Board Page"]
  n20["Pinterest Page Sleuth"]
  n10 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 1 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n17
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
