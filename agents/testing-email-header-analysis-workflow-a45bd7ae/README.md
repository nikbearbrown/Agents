# Testing Email Header Analysis Workflow

Adapt the published “Testing Email Header Analysis Workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 39 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Gmail Trigger"]
  n1["Gmail - Extract Received Headers"]
  n2["Gmail - Extract Original From IP"]
  n3["Gmail - Original IP Found#63;"]
  n4["Gmail - Query IP Quality Score API"]
  n5["Gmail - Query IP API"]
  n6["Gmail - Authentication-Results Header#63;"]
  n7["Gmail - Received-SPF Header#63;"]
  n8["Gmail - Extract Authentication-Results Header"]
  n9["Gmail - Extract Received-SPF Header"]
  n10["Gmail - Determine Auth Values"]
  n11["Gmail - Set SPF Value"]
  n12["Gmail - No SPF Found"]
  n13["Gmail - Format Output"]
  n14["Gmail - DKIM Signature Found"]
  n15["Gmail - DKIM-Signature Header#63;"]
  n16["Gmail - No DKIM Signature Found"]
  n17["Gmail - Set DMARC Value"]
  n18["Gmail - Extract DMARC Header"]
  n19["Gmail - DMARC Header#63;"]
  n20["Gmail - No DMARC Header"]
  n21["Set Gmail Headers Here"]
  n22["Format Individual Auth Outputs1"]
  n23["Format Combined Auth Output1"]
  n24["Gmail - Webhook"]
  n25["Gmail - Remove Extra Received Headers"]
  n26["Gmail - Merge"]
  n27["Gmail - Aggregate"]
  n28["Gmail - Set Headers"]
  n29["Gmail - Respond to Webhook"]
  n30["Aggregate Received-SPF Headers1"]
  n31["Set Gmail Webhook Headers Here"]
  n32["Skip IP Check"]
  n26 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n21
  n32 -->|"main out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n31
  n27 -->|"main out 0 to in 0"| n22
  n28 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n26
  n5 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 1 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n29
  n11 -->|"main out 0 to in 0"| n26
  n21 -->|"main out 0 to in 0"| n28
  n20 -->|"main out 0 to in 2"| n26
  n17 -->|"main out 0 to in 2"| n26
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n32
  n23 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 1"| n26
  n18 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 1 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n23
  n15 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 1 to in 0"| n16
  n31 -->|"main out 0 to in 0"| n28
  n30 -->|"main out 0 to in 0"| n11
  n22 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 1"| n26
  n2 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n25
  n4 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n30
  n25 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 1 to in 0"| n7
  n6 -->|"main out 1 to in 0"| n15
  n6 -->|"main out 1 to in 0"| n19
  n8 -->|"main out 0 to in 0"| n10
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
