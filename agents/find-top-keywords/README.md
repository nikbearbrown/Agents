# Find Top Keywords

Adapt the published “Find Top Keywords” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 31 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Schedule Trigger"]
  n2["Gen Time"]
  n3["NocoDB"]
  n4["Second Order Google Autocomplete Keywords"]
  n5["Google Search Volume"]
  n6["Split Out Google Search"]
  n7["YouTube Search Volume"]
  n8["Second Order YouTube Autocomplete Keywords"]
  n9["Split Out YT Search"]
  n10["Google Filter"]
  n11["YT Filter"]
  n12["Add Second Tier YT Keyword Data"]
  n13["Add Second Tier G Keyword Data"]
  n14["Format G Data"]
  n15["Format YT Data"]
  n16["Bulk Import G Monthly Search Volume"]
  n17["Bulk Import YT Monthly Search Volume"]
  n18["Is Google Keyword Available"]
  n19["Is YT Keyword Avaliable"]
  n20["Check for Google Keyword"]
  n21["Check for YT Keyword"]
  n22["Loop Over YT Keywords"]
  n23["Update Second Tier G Keyword Data"]
  n24["Update Second Tier YT Keyword Data"]
  n25["Loop Over Google Keywords"]
  n26["Combine G Keywords and Filter"]
  n27["Combine YT Keywords and Filter"]
  n3 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n22
  n14 -->|"main out 0 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n25
  n15 -->|"main out 0 to in 0"| n17
  n1 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n11
  n21 -->|"main out 0 to in 0"| n19
  n5 -->|"main out 0 to in 0"| n6
  n22 -->|"main out 1 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n9
  n19 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 1 to in 0"| n24
  n6 -->|"main out 0 to in 0"| n10
  n20 -->|"main out 0 to in 0"| n18
  n25 -->|"main out 1 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 1 to in 0"| n23
  n26 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n14
  n27 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n15
  n23 -->|"main out 0 to in 0"| n25
  n0 -->|"main out 0 to in 0"| n2
  n24 -->|"main out 0 to in 0"| n22
  n16 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 0 to in 0"| n22
  n4 -->|"main out 0 to in 0"| n26
  n8 -->|"main out 0 to in 0"| n27
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
