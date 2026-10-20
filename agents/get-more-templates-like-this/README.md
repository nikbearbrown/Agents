# Get More Templates Like This 👇

Adapt the published “Get More Templates Like This 👇” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get advice articles from a Google search"]
  n1["When clicking #8216;Test workflow#8217;"]
  n2["Merge data and keep unique google search results"]
  n3["Extract Article links for LinkedIn advice articles"]
  n4["Split Out all links for LinkedIn advice articles"]
  n5["Schedule Trigger Every Monday, #64; 08:00am"]
  n6["LinkedIn Contribution Writer"]
  n7["Post new LinkedIn contributions to NocoDB #40;CreateRows#41;"]
  n8["Post new LinkedIn contributions to Slack channel"]
  n9["Get all LinkedIn contributions from database NocoDB #40;GetRows#41;"]
  n10["HTML extract LinkedIn article #38; other users contributions"]
  n11["HTTP Request to get LinkedIn advice articles"]
  n12["Airtable"]
  n13["Google Sheets"]
  n14["Get all LinkedIn contributions from database NocoDB #40;GetRows#41;1"]
  n15["Set Topic for Google search"]
  n15 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 1"| n2
  n3 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 0 to in 0"| n2
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
