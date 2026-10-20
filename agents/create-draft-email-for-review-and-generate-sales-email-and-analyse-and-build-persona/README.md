# create draft email for review and generate sales email and analyse and build persona

Adapt the published “create draft email for review and generate sales email and analyse and build persona” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 11 executable nodes and 11 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Variables"]
  n2["Google Gemini Chat Model"]
  n3["Google Gemini Chat Model1"]
  n4["Create Draft Email For Review"]
  n5["Generate Sales Email"]
  n6["Analyse and Build Persona"]
  n7["Get All Customer#39;s Correspondence"]
  n8["Get Contacts"]
  n9["For Each Contact"]
  n10["Contact Ref"]
  n1 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 1 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n4
  n2 -->|"ai_languageModel out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n5
  n3 -->|"ai_languageModel out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n8
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
