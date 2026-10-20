# Q. Do I need to analyse Brand Voice for every article?

Adapt the published “Q. Do I need to analyse Brand Voice for every article?” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["OpenAI Chat Model"]
  n2["OpenAI Chat Model1"]
  n3["OpenAI Chat Model2"]
  n4["Extract Voice Characteristics"]
  n5["Get Blog"]
  n6["Get Article"]
  n7["Extract Article URLs"]
  n8["Split Out URLs"]
  n9["Latest Articles"]
  n10["Extract Article Content"]
  n11["Combine Articles"]
  n12["Article Style #38; Brand Voice"]
  n13["Save as Draft"]
  n14["Capture Existing Article Structure"]
  n15["Markdown"]
  n16["Content Generation Agent"]
  n17["New Article Instruction"]
  n5 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n4
  n1 -->|"ai_languageModel out 0 to in 0"| n4
  n2 -->|"ai_languageModel out 0 to in 0"| n16
  n3 -->|"ai_languageModel out 0 to in 0"| n14
  n7 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n17
  n4 -->|"main out 0 to in 1"| n12
  n0 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n12
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
