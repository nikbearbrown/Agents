# Very simple Human in the loop system email with AI e IMAP

Adapt the published “Very simple Human in the loop system email with AI e IMAP” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 10 executable nodes and 9 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Email Trigger #40;IMAP#41;"]
  n1["Markdown"]
  n2["Send Email"]
  n3["Email Summarization Chain"]
  n4["Write email"]
  n5["OpenAI"]
  n6["Approve Email"]
  n7["OpenAI Chat Model"]
  n8["Set Email text"]
  n9["Approved#63;"]
  n5 -->|"ai_languageModel out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n6
  n7 -->|"ai_languageModel out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n4
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
