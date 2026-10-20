# notion knowledge base ai assistant

This folder contains the **notion knowledge base ai assistant** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `lmChatAnthropic`, `notion`, `outputParserAutofixing`, `outputParserStructured`, `set`, `switch`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`notion-knowledge-base-ai-assistant.json`](notion-knowledge-base-ai-assistant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `notionApi`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Notion | `notion` | database |
| Return success to chat | `set` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Set schema for eval | `set` | Inspect parameters |
| Return error to chat | `set` | Inspect parameters |
| Anthropic Chat Model1 | `lmChatAnthropic` | Inspect parameters |
| standardize schema | `set` | Inspect parameters |
| Simplify properties object | `code` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Set input data | `code` | Inspect parameters |
| Set schem for rerun | `set` | Inspect parameters |
| Add feedback prompt | `set` | Inspect parameters |
| Check for WF JSON errors | `switch` | Inspect parameters |
| Generate Workflow Agent | `agent` | Inspect parameters |
| Anthropic Chat Model2 | `lmChatAnthropic` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Valid n8n workflow JSON? | `textClassifier` | Inspect parameters |

## Connection map

- Notion → standardize schema (`main`, output 0, input 0)
- Notion → Return error to chat (`main`, output 1, input 0)
- Set input data → Generate Workflow Agent (`main`, output 0, input 0)
- standardize schema → Simplify properties object (`main`, output 0, input 0)
- Add feedback prompt → Set schem for rerun (`main`, output 0, input 0)
- Set schem for rerun → Set input data (`main`, output 0, input 0)
- Set schema for eval → Check for WF JSON errors (`main`, output 0, input 0)
- Anthropic Chat Model → Generate Workflow Agent (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model2 → Valid n8n workflow JSON? (`ai_languageModel`, output 0, input 0)
- Generate Workflow Agent → Set schema for eval (`main`, output 0, input 0)
- Check for WF JSON errors → Add feedback prompt (`main`, output 0, input 0)
- Check for WF JSON errors → Valid n8n workflow JSON? (`main`, output 1, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Valid n8n workflow JSON? → Set schem for rerun (`main`, output 0, input 0)
- Valid n8n workflow JSON? → Return success to chat (`main`, output 1, input 0)
- Auto-fixing Output Parser → Generate Workflow Agent (`ai_outputParser`, output 0, input 0)
- Simplify properties object → Set input data (`main`, output 0, input 0)
- When chat message received → Notion (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0574_Stickynote_Notion_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0574_Stickynote_Notion_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
