# Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)

Adapt the published “Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 36 executable nodes and 0 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Start"]
  n1["Webhook Trigger"]
  n2["Check DB Connection"]
  n3["Meta-Orchestrator"]
  n4["Parse Orchestration Plan"]
  n5["More Agents to Run#63;"]
  n6["Prepare Agent Input"]
  n7["Route Agents with Switch"]
  n8["Summarizer Agent"]
  n9["Synthesizer Agent"]
  n10["Peer Reviewer Agent"]
  n11["Sensemaking Agent"]
  n12["Prompt Engineer Agent"]
  n13["Onboarding/Explainer Agent"]
  n14["Add Handbook Metadata"]
  n15["Generate Content for Review"]
  n16["Generate Review ID"]
  n17["Send Review Request Email"]
  n18["Wait for Human Approval"]
  n19["Human Decision Split"]
  n20["Save to handbook_entries"]
  n21["Prepare Approved Contribution Data"]
  n22["Save Agent Contribution #40;Approved#41;"]
  n23["Generate GitHub File Path"]
  n24["GitHub Enabled#63;"]
  n25["Commit to GitHub #40;Approved#41;"]
  n26["Log Human Rejection"]
  n27["Merge Archivist Paths"]
  n28["Evaluate Board Consensus"]
  n29["Check Redraft Needed"]
  n30["Handle Redraft"]
  n31["Process Agent Output"]
  n32["Slack Enabled#63;"]
  n33["Notify Slack"]
  n34["Final Response"]
  n35["Error Handler"]
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
