# n8n Subworkflow Dependency Graph &amp; Auto-Tagging

Adapt the published “n8n Subworkflow Dependency Graph &amp; Auto-Tagging” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Update workflow tags"]
  n1["GET all workflows"]
  n2["List callers of subworkflows"]
  n3["Exclude uncalled workflows"]
  n4["Exclude missing workflows"]
  n5["And every Sunday"]
  n6["When this workflow is activated"]
  n7["GET workflow#40;s#41;"]
  n8["Count callers and identify new callers"]
  n9["Loop through workflows"]
  n10["GET all tags"]
  n11["Remove existing tags from new_callers list"]
  n12["If any new callers"]
  n13["Split out new callers as new tags"]
  n14["Create new tags"]
  n15["Return original pass through values"]
  n16["Merge"]
  n17["GET all tags again"]
  n18["Create tag id:name dictionary"]
  n19["Retrieve tag ids and names from dictionary"]
  n20["Return dependency graph data"]
  n21["Combine dependency graph values into labels"]
  n22["Visualize subworkflow dependency graph"]
  n23["SET instance_url"]
  n24["When viewed in a browser"]
  n25["Format workflow relationship data for rendering"]
  n26["Visualize dependency graph with MermaidJS"]
  n16 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n4
  n5 -->|"main out 0 to in 0"| n1
  n23 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n18
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 1 to in 1"| n16
  n0 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n25
  n9 -->|"main out 1 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n3
  n20 -->|"main out 0 to in 0"| n9
  n18 -->|"main out 0 to in 0"| n19
  n6 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n16
  n8 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 0 to in 0"| n0
  n21 -->|"main out 0 to in 0"| n22
  n25 -->|"main out 0 to in 0"| n26
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
