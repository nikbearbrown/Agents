# Check for Bot Responses

Adapt the published “Check for Bot Responses” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 11 executable nodes and 10 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Verify Webhook"]
  n1["OpenAI Chat Model"]
  n2["No Operation, do nothing"]
  n3["Window Buffer Memory"]
  n4["Check if Bot"]
  n5["Send Initial Message"]
  n6["Delete Initial Message"]
  n7["Send Message"]
  n8["Receive DMs"]
  n9["Call Confluence Workflow Tool"]
  n10["AI Agent"]
  n10 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n0
  n4 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 1 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"ai_languageModel out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n10
  n3 -->|"ai_memory out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"ai_tool out 0 to in 0"| n10
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
