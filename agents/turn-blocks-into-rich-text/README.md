# ⚙️ Turn blocks into rich text

Adapt the published “⚙️ Turn blocks into rich text” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get simple page data"]
  n1["Get all page data"]
  n2["Take cover url"]
  n3["Merge1"]
  n4["Data transporter1"]
  n5["Get all blog posts1"]
  n6["Is sync checked#63;1"]
  n7["For each blog post1"]
  n8["Create post1"]
  n9["Update slug on posts1"]
  n10["Slug uniqueness checker and differentiator1"]
  n11["Success message1"]
  n12["Merge2"]
  n13["Compare by slug1"]
  n14["Add slug to posts1"]
  n15["Get all collection posts1"]
  n16["Data transporter, Notion posts to sync1"]
  n17["Craft the rich text element1"]
  n18["Turn blocks into HTML1"]
  n19["Get blocks1"]
  n20["Update in #34;Blog Posts#34;"]
  n21["Add Webflow item id to Notion data"]
  n22["Final Notion post data"]
  n23["Schedule Trigger"]
  n3 -->|"main out 0 to in 0"| n22
  n3 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 1"| n3
  n13 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 0 to in 1"| n12
  n13 -->|"main out 2 to in 0"| n21
  n23 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 1 to in 0"| n0
  n7 -->|"main out 1 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n4
  n22 -->|"main out 0 to in 0"| n16
  n22 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 1"| n13
  n17 -->|"main out 0 to in 1"| n22
  n21 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n7
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
