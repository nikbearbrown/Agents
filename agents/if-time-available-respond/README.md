# If time available Respond

Adapt the published “If time available Respond” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 55 executable nodes and 53 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Input Arguments"]
  n1["Format response"]
  n2["Sort"]
  n3["Available Start Times #38; Ranges"]
  n4["Flatten Slots"]
  n5["Enrich Date"]
  n6["Build Response Payload"]
  n7["Booking Payload"]
  n8["Success Response"]
  n9["Add Friendly Error"]
  n10["Error Response"]
  n11["Escape Json"]
  n12["Has all information"]
  n13["Respond with Error"]
  n14["Build Error Response Payload"]
  n15["Build Error Response Payload2"]
  n16["Getslot_tool"]
  n17["Check Availability"]
  n18["Response"]
  n19["Check if time is available or not"]
  n20["Time available #40;true#41; #38; Call_id"]
  n21["Get All Calendar Events"]
  n22["Extract start, end and name"]
  n23["Convert into Json format for Vapi"]
  n24["Response to Vapi"]
  n25["bookslots_tool"]
  n26["Input Arguments from booking tools"]
  n27["Convert time to CST America / Chicago"]
  n28["Create Event"]
  n29["Respond to Vapi"]
  n30["If the booking is confirmed then true"]
  n31["Information to be Saved in Airtable"]
  n32["Logs the confirmed booking details"]
  n33["Updateslots_tool"]
  n34["Input Arguments from updateslot tool"]
  n35["Checks if required info is provided."]
  n36["Finds original appointment"]
  n37["Response with Error"]
  n38["Update Event"]
  n39["Updates Airtable record"]
  n40["Response #38; call_id"]
  n41["Respond to Vapi about Updating slots"]
  n42["CancelSlots_tool"]
  n43["Input Arguments from cancelslot tool"]
  n44["Checks if required info is provided for cancelation"]
  n45["Finds the appointment record"]
  n46["Build Error Response"]
  n47["Respond with Error to Vapi"]
  n48["Delete Event"]
  n49["Update Airtable record"]
  n50["Call_id #38; Response"]
  n51["Respond to Vapi about cancelation"]
  n52["call_results"]
  n53["All Input Arguments"]
  n54["Save all information"]
  n2 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n27
  n28 -->|"main out 0 to in 0"| n7
  n28 -->|"main out 1 to in 0"| n9
  n48 -->|"main out 0 to in 0"| n49
  n48 -->|"main out 1 to in 0"| n50
  n16 -->|"main out 0 to in 0"| n0
  n38 -->|"main out 0 to in 0"| n39
  n38 -->|"main out 1 to in 0"| n40
  n52 -->|"main out 0 to in 0"| n53
  n4 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n29
  n25 -->|"main out 0 to in 0"| n26
  n7 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n17
  n29 -->|"main out 0 to in 0"| n30
  n42 -->|"main out 0 to in 0"| n43
  n8 -->|"main out 0 to in 0"| n29
  n33 -->|"main out 0 to in 0"| n34
  n9 -->|"main out 0 to in 0"| n10
  n50 -->|"main out 0 to in 0"| n51
  n17 -->|"main out 0 to in 0"| n19
  n40 -->|"main out 0 to in 0"| n41
  n53 -->|"main out 0 to in 0"| n54
  n12 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 1 to in 0"| n14
  n46 -->|"main out 0 to in 0"| n47
  n6 -->|"main out 0 to in 0"| n23
  n49 -->|"main out 0 to in 0"| n50
  n21 -->|"main out 0 to in 0"| n22
  n39 -->|"main out 0 to in 0"| n40
  n36 -->|"main out 0 to in 0"| n38
  n22 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n13
  n45 -->|"main out 0 to in 0"| n48
  n15 -->|"main out 0 to in 0"| n37
  n3 -->|"main out 0 to in 0"| n4
  n20 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 1 to in 0"| n21
  n23 -->|"main out 0 to in 0"| n24
  n26 -->|"main out 0 to in 0"| n12
  n31 -->|"main out 0 to in 0"| n32
  n35 -->|"main out 0 to in 0"| n36
  n35 -->|"main out 1 to in 0"| n15
  n43 -->|"main out 0 to in 0"| n44
  n34 -->|"main out 0 to in 0"| n35
  n27 -->|"main out 0 to in 0"| n28
  n30 -->|"main out 0 to in 0"| n31
  n44 -->|"main out 0 to in 0"| n45
  n44 -->|"main out 1 to in 0"| n46
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
