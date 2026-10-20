# 🔗 1. Webhook Entry &amp; Initial Decryption Block

Adapt the published “🔗 1. Webhook Entry &amp; Initial Decryption Block” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 11 executable nodes and 10 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook1"]
  n1["Json Parser"]
  n2["Switch"]
  n3["Respond to Webhook1"]
  n4["Data Extraction Code"]
  n5["Respond to Webhook2"]
  n6["Data Extraction Code1"]
  n7["move to base64"]
  n8["Decryption Code"]
  n9["Encrypt Return"]
  n10["Encrypt Return1"]
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 1 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n9
  n6 -->|"main out 0 to in 0"| n10
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
