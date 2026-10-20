# Testing Email Header Analysis Workflow

Adapt the published “Testing Email Header Analysis Workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 34 executable nodes and 40 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Trigger on New Email"]
  n1["Retrieve Headers of Email"]
  n2["Extract Received Headers"]
  n3["Remove Extra Received Headers"]
  n4["Extract Original From IP"]
  n5["Query IP Quality Score API"]
  n6["Query IP API"]
  n7["Authentication-Results Header#63;"]
  n8["Extract Authentication-Results Header"]
  n9["Received-SPF Header#63;"]
  n10["DKIM-Signature Header#63;"]
  n11["Set SPF Value"]
  n12["Extract Received-SPF Header"]
  n13["DKIM Signature Found"]
  n14["DMARC Header#63;"]
  n15["No DMARC Header"]
  n16["Extract DMARC Header"]
  n17["Set DMARC Value"]
  n18["Original IP Found#63;"]
  n19["No DKIM Signature Found"]
  n20["Determine Auth Values"]
  n21["No SPF Found"]
  n22["Merge"]
  n23["Aggregate"]
  n24["No Operation, do nothing"]
  n25["Format Webhook Output"]
  n26["Format Individual Auth Outputs"]
  n27["Format Combined Auth Output"]
  n28["Respond to Webhook"]
  n29["Webhook1"]
  n30["Set Headers"]
  n31["Aggregate Received-SPF Headers"]
  n32["Set Headers Here"]
  n33["Set Webhook Headers Here"]
  n22 -->|"main out 0 to in 0"| n23
  n29 -->|"main out 0 to in 0"| n33
  n23 -->|"main out 0 to in 0"| n26
  n30 -->|"main out 0 to in 0"| n2
  n21 -->|"main out 0 to in 0"| n22
  n6 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 1 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n22
  n15 -->|"main out 0 to in 2"| n22
  n17 -->|"main out 0 to in 2"| n22
  n32 -->|"main out 0 to in 0"| n30
  n18 -->|"main out 0 to in 0"| n5
  n18 -->|"main out 1 to in 0"| n24
  n13 -->|"main out 0 to in 1"| n22
  n16 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 1 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n1
  n20 -->|"main out 0 to in 0"| n27
  n25 -->|"main out 0 to in 0"| n28
  n10 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 1 to in 0"| n19
  n19 -->|"main out 0 to in 1"| n22
  n4 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n3
  n24 -->|"main out 0 to in 0"| n7
  n33 -->|"main out 0 to in 0"| n30
  n1 -->|"main out 0 to in 0"| n32
  n5 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n31
  n27 -->|"main out 0 to in 0"| n25
  n3 -->|"main out 0 to in 0"| n4
  n31 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n9
  n7 -->|"main out 1 to in 0"| n10
  n7 -->|"main out 1 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n25
  n8 -->|"main out 0 to in 0"| n20
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
