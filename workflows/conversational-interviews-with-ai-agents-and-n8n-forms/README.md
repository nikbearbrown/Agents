# conversational interviews with ai agents and n8n forms

This folder contains the **conversational interviews with ai agents and n8n forms** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `filter`, `form`, `formTrigger`, `httpRequest`, `if`, `lmChatGoogleGemini`, `lmChatOpenAi`, `markdown`, `merge`, `noOp`, `notion`, `outputParserStructured`, `set`, `splitInBatches`, `splitOut`, `stopAndError`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`conversational-interviews-with-ai-agents-and-n8n-forms.json`](conversational-interviews-with-ai-agents-and-n8n-forms.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `httpHeaderAuth`, `httpQueryAuth`, `notionApi`, `openAiApi`

**Entry nodes:** On form submission, DeepResearch Subworkflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Generate SERP Queries | `chainLlm` | Inspect parameters |
| Structured Output Parser2 | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| Set Initial Query | `set` | Inspect parameters |
| SERP to Items | `splitOut` | Inspect parameters |
| Item Ref | `noOp` | Inspect parameters |
| Research Goal + Learnings | `set` | Inspect parameters |
| Accumulate Results | `set` | Inspect parameters |
| DeepResearch Results | `set` | Inspect parameters |
| Results to Items | `splitOut` | Inspect parameters |
| Set Next Queries | `set` | Inspect parameters |
| For Each Query... | `splitInBatches` | Inspect parameters |
| Feedback to Items | `splitOut` | Inspect parameters |
| Ask Clarity Questions | `form` | Inspect parameters |
| For Each Question... | `splitInBatches` | Inspect parameters |
| DeepResearch Subworkflow | `executeWorkflowTrigger` | Inspect parameters |
| Clarifying Questions | `chainLlm` | Inspect parameters |
| End Form | `form` | completion |
| Initiate DeepResearch | `executeWorkflow` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| JobType Router | `switch` | Inspect parameters |
| OpenAI Chat Model4 | `lmChatOpenAi` | Inspect parameters |
| Get Initial Query | `set` | Inspect parameters |
| Structured Output Parser4 | `outputParserStructured` | Inspect parameters |
| Create Row | `notion` | databasePage |
| Report Page Generator | `chainLlm` | Inspect parameters |
| Is Depth Reached? | `if` | Inspect parameters |
| Get Research Results | `set` | Inspect parameters |
| Get Existing Row | `notion` | databasePage / getAll |
| Set In-Progress | `notion` | databasePage / update |
| Set Done | `notion` | databasePage / update |
| Tags to Items | `splitOut` | Inspect parameters |
| Convert to HTML | `markdown` | Inspect parameters |
| HTML to Array | `set` | Inspect parameters |
| Notion Block Generator | `chainLlm` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Parse JSON blocks | `set` | Inspect parameters |
| Upload to Notion Page | `httpRequest` | PATCH |
| Get Existing Row1 | `notion` | databasePage / getAll |
| DeepResearch Report | `chainLlm` | Inspect parameters |
| DeepResearch Learnings | `chainLlm` | Inspect parameters |
| Generate Report | `executeWorkflow` | Inspect parameters |
| Generate Learnings | `executeWorkflow` | Inspect parameters |
| Confirmation | `form` | Inspect parameters |
| Research Request | `form` | Inspect parameters |
| Valid Blocks | `filter` | Inspect parameters |
| Append Blocks | `merge` | Inspect parameters |
| URL Sources to Lists | `code` | Inspect parameters |
| Empty Response | `set` | Inspect parameters |
| Has Content? | `if` | Inspect parameters |
| Combine & Send back to Loop | `aggregate` | Inspect parameters |
| For Each Block... | `splitInBatches` | Inspect parameters |
| Valid Results | `filter` | Inspect parameters |
| RAG Web Browser | `httpRequest` | POST |
| Get Markdown + URL | `set` | Inspect parameters |
| Is Apify Auth Error? | `if` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |

## Connection map

- Item Ref → RAG Web Browser (`main`, output 0, input 0)
- Create Row → Initiate DeepResearch (`main`, output 0, input 0)
- Confirmation → End Form (`main`, output 0, input 0)
- Has Content? → Get Markdown + URL (`main`, output 0, input 0)
- Has Content? → Empty Response (`main`, output 1, input 0)
- Valid Blocks → Append Blocks (`main`, output 0, input 0)
- Append Blocks → For Each Block... (`main`, output 0, input 0)
- HTML to Array → Tags to Items (`main`, output 0, input 0)
- SERP to Items → For Each Query... (`main`, output 0, input 0)
- Set Variables → Clarifying Questions (`main`, output 0, input 0)
- Tags to Items → Notion Block Generator (`main`, output 0, input 0)
- Valid Results → Has Content? (`main`, output 0, input 0)
- Empty Response → For Each Query... (`main`, output 0, input 0)
- Execution Data → JobType Router (`main`, output 0, input 0)
- JobType Router → Get Existing Row (`main`, output 0, input 0)
- JobType Router → Generate SERP Queries (`main`, output 1, input 0)
- JobType Router → Get Existing Row1 (`main`, output 2, input 0)
- Convert to HTML → HTML to Array (`main`, output 0, input 0)
- RAG Web Browser → Is Apify Auth Error? (`main`, output 0, input 0)
- Set In-Progress → Set Initial Query (`main`, output 0, input 0)
- Get Existing Row → Set In-Progress (`main`, output 0, input 0)
- Research Request → Set Variables (`main`, output 0, input 0)
- Results to Items → Set Next Queries (`main`, output 0, input 0)
- Set Next Queries → Generate Learnings (`main`, output 0, input 0)
- Feedback to Items → For Each Question... (`main`, output 0, input 0)
- For Each Block... → Set Done (`main`, output 0, input 0)
- For Each Block... → Upload to Notion Page (`main`, output 1, input 0)
- For Each Query... → Combine & Send back to Loop (`main`, output 0, input 0)
- For Each Query... → Item Ref (`main`, output 1, input 0)
- Get Existing Row1 → DeepResearch Report (`main`, output 0, input 0)
- Get Initial Query → Report Page Generator (`main`, output 0, input 0)
- Is Depth Reached? → Get Research Results (`main`, output 0, input 0)
- Is Depth Reached? → DeepResearch Results (`main`, output 1, input 0)
- OpenAI Chat Model → DeepResearch Learnings (`ai_languageModel`, output 0, input 0)
- Parse JSON blocks → Valid Blocks (`main`, output 0, input 0)
- Parse JSON blocks → URL Sources to Lists (`main`, output 0, input 0)
- Set Initial Query → Generate Learnings (`main`, output 0, input 0)
- Accumulate Results → Is Depth Reached? (`main`, output 0, input 0)
- Generate Learnings → Accumulate Results (`main`, output 0, input 0)
- Get Markdown + URL → DeepResearch Learnings (`main`, output 0, input 0)
- On form submission → Research Request (`main`, output 0, input 0)
- OpenAI Chat Model1 → DeepResearch Report (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Clarifying Questions (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Generate SERP Queries (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model4 → Report Page Generator (`ai_languageModel`, output 0, input 0)
- DeepResearch Report → Convert to HTML (`main`, output 0, input 0)
- Clarifying Questions → Feedback to Items (`main`, output 0, input 0)
- DeepResearch Results → Results to Items (`main`, output 0, input 0)
- For Each Question... → Get Initial Query (`main`, output 0, input 0)
- For Each Question... → Ask Clarity Questions (`main`, output 1, input 0)
- Get Research Results → Generate Report (`main`, output 0, input 0)
- Is Apify Auth Error? → Stop and Error (`main`, output 0, input 0)
- Is Apify Auth Error? → Valid Results (`main`, output 1, input 0)
- URL Sources to Lists → Append Blocks (`main`, output 0, input 1)
- Ask Clarity Questions → For Each Question... (`main`, output 0, input 0)
- Generate SERP Queries → SERP to Items (`main`, output 0, input 0)
- Initiate DeepResearch → Confirmation (`main`, output 0, input 0)
- Report Page Generator → Create Row (`main`, output 0, input 0)
- Upload to Notion Page → For Each Block... (`main`, output 0, input 0)
- DeepResearch Learnings → Research Goal + Learnings (`main`, output 0, input 0)
- Notion Block Generator → Parse JSON blocks (`main`, output 0, input 0)
- DeepResearch Subworkflow → Execution Data (`main`, output 0, input 0)
- Google Gemini Chat Model → Notion Block Generator (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → DeepResearch Learnings (`ai_outputParser`, output 0, input 0)
- Research Goal + Learnings → For Each Query... (`main`, output 0, input 0)
- Structured Output Parser1 → Clarifying Questions (`ai_outputParser`, output 0, input 0)
- Structured Output Parser2 → Generate SERP Queries (`ai_outputParser`, output 0, input 0)
- Structured Output Parser4 → Report Page Generator (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0719_Stopanderror_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0719_Stopanderror_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
