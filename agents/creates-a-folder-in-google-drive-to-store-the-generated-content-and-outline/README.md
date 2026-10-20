# Creates a folder in Google Drive to store the generated content and outline

Adapt the published “Creates a folder in Google Drive to store the generated content and outline” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["create_folder"]
  n1["input_brief"]
  n2["new_lines"]
  n3["input_sections"]
  n4["section_text"]
  n5["Merge"]
  n6["Sort"]
  n7["Aggregate"]
  n8["final_article"]
  n9["set_introduction"]
  n10["Merge1"]
  n11["receive_topic"]
  n12["add_row"]
  n13["topic_variables"]
  n14["markdown_to_file"]
  n15["split_out"]
  n16["section_starts_with_#35;"]
  n17["25_percent_chance"]
  n18["set_section_content"]
  n19["add_2_new_lines"]
  n20["final_article_file"]
  n21["upload_fiinalArticle"]
  n22["update_article_link"]
  n23["upload_outline_file"]
  n24["section_paragraphs"]
  n25["change_section_format"]
  n26["create_outline"]
  n6 -->|"main out 0 to in 0"| n19
  n5 -->|"main out 0 to in 0"| n6
  n10 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n26
  n8 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n12
  n26 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n24
  n19 -->|"main out 0 to in 1"| n10
  n13 -->|"main out 0 to in 0"| n0
  n14 -->|"main out 0 to in 0"| n23
  n9 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 1 to in 1"| n5
  n20 -->|"main out 0 to in 0"| n21
  n24 -->|"main out 0 to in 0"| n4
  n18 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n1
  n21 -->|"main out 0 to in 0"| n22
  n25 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 0 to in 0"| n9
  n16 -->|"main out 1 to in 0"| n3
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
