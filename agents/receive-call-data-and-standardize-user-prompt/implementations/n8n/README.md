# Receive Call Data and standardize User Prompt

This folder contains the **Receive Call Data and standardize User Prompt** workflow. Its executable nodes use `agent`, `aggregate`, `executeWorkflow`, `executeWorkflowTrigger`, `lmChatAzureOpenAi`, `merge`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-call-data-and-standardize-user-prompt.json`](receive-call-data-and-standardize-user-prompt.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `azureOpenAiApi`

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Marketing AI Agent Processor | `agent` | Inspect parameters |
| Structured Output Parser2 | `outputParserStructured` | Inspect parameters |
| Product AI Agent Processor | `agent` | Inspect parameters |
| Sales Data Processor | `executeWorkflow` | Inspect parameters |
| Marketing Data Processor | `executeWorkflow` | Inspect parameters |
| Product AI Data Processor | `executeWorkflow` | Inspect parameters |
| Data Recall Sales | `set` | Inspect parameters |
| Data Recall Marketing | `set` | Inspect parameters |
| Data Recall Product | `set` | Inspect parameters |
| SF Sales Data Processor | `executeWorkflow` | Inspect parameters |
| Azure OpenAI Chat Model | `lmChatAzureOpenAi` | Inspect parameters |
| Azure OpenAI Chat Model1 | `lmChatAzureOpenAi` | Inspect parameters |
| Azure OpenAI Chat Model2 | `lmChatAzureOpenAi` | Inspect parameters |
| Create User Prompt | `set` | Inspect parameters |
| Success Status Generated | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Structured Output Parser3 | `outputParserStructured` | Inspect parameters |
| Merge all processed data | `merge` | Inspect parameters |
| Bundle processed Data | `aggregate` | Inspect parameters |

## Connection map

- AI Agent → Data Recall Sales (`main`, output 0, input 0)
- Data Recall Sales → Sales Data Processor (`main`, output 0, input 0)
- Data Recall Sales → SF Sales Data Processor (`main`, output 0, input 0)
- Create User Prompt → Marketing AI Agent Processor (`main`, output 0, input 0)
- Create User Prompt → Product AI Agent Processor (`main`, output 0, input 0)
- Create User Prompt → AI Agent (`main`, output 0, input 0)
- Data Recall Product → Product AI Data Processor (`main`, output 0, input 0)
- Sales Data Processor → Merge all processed data (`main`, output 0, input 0)
- Bundle processed Data → Success Status Generated (`main`, output 0, input 0)
- Data Recall Marketing → Marketing Data Processor (`main`, output 0, input 0)
- Azure OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model1 → Marketing AI Agent Processor (`ai_languageModel`, output 0, input 0)
- Azure OpenAI Chat Model2 → Product AI Agent Processor (`ai_languageModel`, output 0, input 0)
- Execute Workflow Trigger → Create User Prompt (`main`, output 0, input 0)
- Marketing Data Processor → Merge all processed data (`main`, output 0, input 1)
- Merge all processed data → Bundle processed Data (`main`, output 0, input 0)
- Product AI Data Processor → Merge all processed data (`main`, output 0, input 2)
- Structured Output Parser1 → Marketing AI Agent Processor (`ai_outputParser`, output 0, input 0)
- Structured Output Parser2 → Product AI Agent Processor (`ai_outputParser`, output 0, input 0)
- Structured Output Parser3 → AI Agent (`ai_outputParser`, output 0, input 0)
- Product AI Agent Processor → Data Recall Product (`main`, output 0, input 0)
- Marketing AI Agent Processor → Data Recall Marketing (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/0762_Aggregate_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Aggregate/0762_Aggregate_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
