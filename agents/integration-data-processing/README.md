# Integration Data Processing

Adapt the published “Integration Data Processing” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Check if Competitor Data Found"]
  n1["Check if Integration Data Found"]
  n2["Execute Workflow Trigger"]
  n3["Check if objection found"]
  n4["Create Competitors in DB"]
  n5["Create Integrations"]
  n6["Update Call with Objection Summary"]
  n7["Check for use cases"]
  n8["Update Notion Call object with AI data"]
  n9["Split Out all objections"]
  n10["Format Tag Data for notion"]
  n11["Bundle all Tags"]
  n12["Add Objection Tag to Notion"]
  n13["Wait for rate limiting again"]
  n14["Merge Objection Threads"]
  n15["Wait for rate limiting - Integration"]
  n16["Split Out Integration data"]
  n17["Bundle Integration Data to 1 object"]
  n18["Merge Integration Thread"]
  n19["Wait for rate limiting - Competitors"]
  n20["Wait for rate limiting - Objection"]
  n21["Wait for rate limiting - Use Cases"]
  n22["Split Out Use Cases"]
  n23["Create Use Cases"]
  n24["Bundle Use Case Data to 1 object"]
  n25["Bundle Competitor Data to 1 object"]
  n26["Split Out Competitor Data"]
  n27["Get AI Response - Competitors"]
  n28["Merge Competitor Thread"]
  n29["Merge Use Case Thread"]
  n11 -->|"main out 0 to in 0"| n12
  n23 -->|"main out 0 to in 0"| n24
  n7 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 1 to in 0"| n29
  n5 -->|"main out 0 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n23
  n3 -->|"main out 0 to in 0"| n20
  n3 -->|"main out 1 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n25
  n2 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n10
  n26 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n6
  n27 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n19
  n0 -->|"main out 1 to in 0"| n28
  n1 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 1 to in 0"| n18
  n24 -->|"main out 0 to in 0"| n29
  n25 -->|"main out 0 to in 0"| n28
  n6 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n9
  n21 -->|"main out 0 to in 0"| n22
  n17 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n27
  n15 -->|"main out 0 to in 0"| n16
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
