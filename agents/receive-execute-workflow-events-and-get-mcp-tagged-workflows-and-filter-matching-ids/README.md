# receive execute workflow events and get mcp tagged workflows and filter matching ids

Adapt the published “receive execute workflow events and get mcp tagged workflows and filter matching ids” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 38 executable nodes and 36 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Simplify Workflows"]
  n1["When Executed by Another Workflow"]
  n2["Operations"]
  n3["Get MCP-tagged Workflows"]
  n4["Filter Matching Ids"]
  n5["Store In Memory"]
  n6["AddTool Success"]
  n7["AddTool Error"]
  n8["Get Memory"]
  n9["Split Out"]
  n10["Filter Matching IDs"]
  n11["Store In Memory1"]
  n12["Remove Tool Success"]
  n13["Convert to JSON"]
  n14["listTools Success"]
  n15["Get MCP-tagged Workflows1"]
  n16["Simplify Workflows1"]
  n17["listTools Success1"]
  n18["Get Parameters"]
  n19["executeTool Result"]
  n20["AI Agent"]
  n21["When chat message received"]
  n22["MCP Client"]
  n23["Simple Memory"]
  n24["Convert to JSON1"]
  n25["Has Workflow Available#63;"]
  n26["ExecuteTool Error"]
  n27["Workflow Exists#63;"]
  n28["N8N Workflows MCP Server"]
  n29["Add Workflow"]
  n30["RemoveWorkflow"]
  n31["List Workflows"]
  n32["SearchWorkflows"]
  n33["ExecuteWorkflow"]
  n34["Execute Workflow with PassThrough Variables"]
  n35["OpenAI Chat Model"]
  n36["Is Empty Array#63;"]
  n37["Delete Key"]
  n9 -->|"main out 0 to in 0"| n10
  n37 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n2
  n22 -->|"ai_tool out 0 to in 0"| n20
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n13
  n2 -->|"main out 2 to in 0"| n14
  n2 -->|"main out 3 to in 0"| n15
  n2 -->|"main out 4 to in 0"| n24
  n29 -->|"ai_tool out 0 to in 0"| n28
  n23 -->|"ai_memory out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n34
  n31 -->|"ai_tool out 0 to in 0"| n28
  n30 -->|"ai_tool out 0 to in 0"| n28
  n13 -->|"main out 0 to in 0"| n9
  n33 -->|"ai_tool out 0 to in 0"| n28
  n36 -->|"main out 0 to in 0"| n37
  n36 -->|"main out 1 to in 0"| n11
  n32 -->|"ai_tool out 0 to in 0"| n28
  n5 -->|"main out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n25
  n11 -->|"main out 0 to in 0"| n12
  n27 -->|"main out 0 to in 0"| n0
  n27 -->|"main out 1 to in 0"| n7
  n35 -->|"ai_languageModel out 0 to in 0"| n20
  n0 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n36
  n4 -->|"main out 0 to in 0"| n27
  n16 -->|"main out 0 to in 0"| n17
  n25 -->|"main out 0 to in 0"| n18
  n25 -->|"main out 1 to in 0"| n26
  n3 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n16
  n21 -->|"main out 0 to in 0"| n20
  n1 -->|"main out 0 to in 0"| n8
  n34 -->|"main out 0 to in 0"| n19
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
