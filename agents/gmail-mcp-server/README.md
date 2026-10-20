# Gmail MCP Server

Adapt the published “Gmail MCP Server” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["addLabels"]
  n1["delete"]
  n2["get"]
  n3["search"]
  n4["markAsRead"]
  n5["markAsUnread"]
  n6["reply"]
  n7["removeLabels"]
  n8["getLabels"]
  n9["getLabel"]
  n10["deleteLabel"]
  n11["createLabel"]
  n12["deleteDraft"]
  n13["createDraft"]
  n14["getDraft"]
  n15["getManyDrafts"]
  n16["getManyThreads"]
  n17["getThread"]
  n18["addLabelThread"]
  n19["removeLabelThread"]
  n20["replyThread"]
  n21["Gmail MCP Server"]
  n2 -->|"ai_tool out 0 to in 0"| n21
  n6 -->|"ai_tool out 0 to in 0"| n21
  n1 -->|"ai_tool out 0 to in 0"| n21
  n3 -->|"ai_tool out 0 to in 0"| n21
  n14 -->|"ai_tool out 0 to in 0"| n21
  n9 -->|"ai_tool out 0 to in 0"| n21
  n0 -->|"ai_tool out 0 to in 0"| n21
  n8 -->|"ai_tool out 0 to in 0"| n21
  n17 -->|"ai_tool out 0 to in 0"| n21
  n4 -->|"ai_tool out 0 to in 0"| n21
  n13 -->|"ai_tool out 0 to in 0"| n21
  n11 -->|"ai_tool out 0 to in 0"| n21
  n12 -->|"ai_tool out 0 to in 0"| n21
  n10 -->|"ai_tool out 0 to in 0"| n21
  n20 -->|"ai_tool out 0 to in 0"| n21
  n5 -->|"ai_tool out 0 to in 0"| n21
  n7 -->|"ai_tool out 0 to in 0"| n21
  n15 -->|"ai_tool out 0 to in 0"| n21
  n18 -->|"ai_tool out 0 to in 0"| n21
  n16 -->|"ai_tool out 0 to in 0"| n21
  n19 -->|"ai_tool out 0 to in 0"| n21
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
