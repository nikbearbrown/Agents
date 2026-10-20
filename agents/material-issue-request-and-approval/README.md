# Material Issue Request and Approval

Adapt the published “Material Issue Request and Approval” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 48 executable nodes and 48 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Append Material Request"]
  n1["Get Approvals"]
  n2["Standardize Data"]
  n3["Update Stock"]
  n4["Receive Issue Request"]
  n5["Send Approval Request"]
  n6["Prepare Approval"]
  n7["Create Record Issue"]
  n8["Search Product ID"]
  n9["Searck Issues"]
  n10["Update Current Stck"]
  n11["Merge Lookups"]
  n12["Update Current Stock1"]
  n13["LookUp Current stock1"]
  n14["Low stock Detection1"]
  n15["Merge1"]
  n16["Append Raw Materials"]
  n17["Calculate Total Price"]
  n18["Calculate Updated Current Stock"]
  n19["Validate Quantity Received"]
  n20["Initialize New Product stock"]
  n21["Update Current Stock"]
  n22["LookUp Current stock"]
  n23["New Row Current Stock"]
  n24["Current Stock Update"]
  n25["Search Current Stock"]
  n26["Format response"]
  n27["Merge"]
  n28["Low stock Detection2"]
  n29["Receive Raw Materials Webhook"]
  n30["Standardize Raw Material Data"]
  n31["Lookup Existing Stock"]
  n32["Check If Product ID Exists"]
  n33["New Record Row"]
  n34["Trigger Low Stock Alert"]
  n35["Send Low Stock Email Alert"]
  n36["Low Stock Email Alert"]
  n37["Validate Issue Request Data"]
  n38["Verify Requested Quantity"]
  n39["Check Available Stock for Issue"]
  n40["Format Approval Response"]
  n41["Verify Approval Data"]
  n42["Retrieve Issue Request Details"]
  n43["Process Approval Decision"]
  n44["Get Stock for Issue Update from Current"]
  n45["Update Stock After Issue"]
  n46["Materials Issue Table Update"]
  n47["Is Stock is Low"]
  n27 -->|"main out 0 to in 0"| n32
  n15 -->|"main out 0 to in 0"| n43
  n3 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n40
  n11 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 0 to in 1"| n15
  n33 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n20
  n26 -->|"main out 0 to in 0"| n23
  n47 -->|"main out 0 to in 0"| n36
  n6 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n37
  n8 -->|"main out 0 to in 1"| n11
  n7 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n19
  n22 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n47
  n28 -->|"main out 0 to in 0"| n34
  n25 -->|"main out 0 to in 0"| n27
  n21 -->|"main out 0 to in 0"| n22
  n41 -->|"main out 0 to in 0"| n42
  n41 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n33
  n13 -->|"main out 0 to in 0"| n14
  n31 -->|"main out 0 to in 0"| n27
  n4 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n39
  n34 -->|"main out 0 to in 0"| n35
  n40 -->|"main out 0 to in 0"| n41
  n43 -->|"main out 0 to in 0"| n45
  n43 -->|"main out 0 to in 0"| n46
  n43 -->|"main out 0 to in 0"| n44
  n38 -->|"main out 0 to in 0"| n0
  n38 -->|"main out 0 to in 0"| n7
  n32 -->|"main out 0 to in 0"| n18
  n32 -->|"main out 1 to in 0"| n26
  n19 -->|"main out 0 to in 0"| n31
  n37 -->|"main out 0 to in 0"| n38
  n29 -->|"main out 0 to in 0"| n30
  n30 -->|"main out 0 to in 0"| n17
  n42 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n24
  n39 -->|"main out 0 to in 0"| n11
  n44 -->|"main out 0 to in 0"| n3
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
