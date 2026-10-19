# Docsify example

This folder contains the **Docsify example** workflow. Its executable nodes use `chainLlm`, `code`, `convertToFile`, `executeCommand`, `extractFromFile`, `html`, `if`, `lmChatOpenAi`, `merge`, `n8n`, `noOp`, `outputParserAutofixing`, `outputParserStructured`, `readWriteFile`, `respondToWebhook`, `set`, `sort`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`docsify-example.json`](docsify-example.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`, `openAiApi`

**Entry nodes:** single workflow, docsify

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| CONFIG | `set` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| HasFile? | `if` | Inspect parameters |
| Extract from File | `extractFromFile` | text |
| Main Page | `html` | Inspect parameters |
| Instance overview | `html` | Inspect parameters |
| Sort-workflows | `sort` | Inspect parameters |
| doc action | `switch` | Inspect parameters |
| Empty Set | `set` | Inspect parameters |
| Load Doc File | `readWriteFile` | Inspect parameters |
| Respond with markdown | `respondToWebhook` | Inspect parameters |
| Respond with HTML | `respondToWebhook` | Inspect parameters |
| Save New Doc File | `readWriteFile` | write |
| Blank Doc File | `set` | Inspect parameters |
| Fetch Single Workflow1 | `n8n` | get |
| Fill Workflow Table | `set` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Respond with main page HTML | `respondToWebhook` | Inspect parameters |
| Workflow Tags | `html` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Fallback file name | `html` | Inspect parameters |
| mkdir | `executeCommand` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Edit Page | `html` | Inspect parameters |
| Workflow md content | `html` | Inspect parameters |
| Is Action Edit?1 | `if` | Inspect parameters |
| Is Action Edit?2 | `if` | Inspect parameters |
| Generate Mermaid Chart | `code` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Generated Doc | `set` | Inspect parameters |
| Passthrough | `noOp` | Inspect parameters |
| Merge3 | `merge` | Inspect parameters |
| Merge4 | `merge` | Inspect parameters |
| Merge5 | `merge` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Is Action Save? | `if` | Inspect parameters |
| Merge6 | `merge` | Inspect parameters |
| Respond OK on Save | `respondToWebhook` | Inspect parameters |
| single workflow | `webhook` | Inspect parameters |
| file types | `switch` | Inspect parameters |
| Get All Workflows | `n8n` | Inspect parameters |
| md files | `switch` | Inspect parameters |
| Get Workflow tags | `n8n` | Inspect parameters |
| docsify | `webhook` | Inspect parameters |

## Connection map

- Merge → Is Action Edit?1 (`main`, output 0, input 0)
- mkdir → Merge1 (`main`, output 0, input 1)
- CONFIG → Merge4 (`main`, output 0, input 1)
- CONFIG → Merge5 (`main`, output 0, input 0)
- Merge1 → HasFile? (`main`, output 0, input 0)
- Merge2 → Generated Doc (`main`, output 0, input 0)
- Merge3 → Is Action Edit?2 (`main`, output 0, input 0)
- Merge4 → Main Page (`main`, output 0, input 0)
- Merge5 → file types (`main`, output 0, input 0)
- Merge6 → Is Action Save? (`main`, output 0, input 0)
- docsify → CONFIG (`main`, output 0, input 0)
- docsify → Merge4 (`main`, output 0, input 0)
- HasFile? → Extract from File (`main`, output 0, input 0)
- HasFile? → Fetch Single Workflow1 (`main`, output 1, input 0)
- md files → Get All Workflows (`main`, output 0, input 0)
- md files → doc action (`main`, output 1, input 0)
- md files → Get Workflow tags (`main`, output 2, input 0)
- md files → Get All Workflows (`main`, output 3, input 0)
- md files → No Operation, do nothing (`main`, output 4, input 0)
- Edit Page → Respond with HTML (`main`, output 0, input 0)
- Empty Set → Merge1 (`main`, output 0, input 0)
- Main Page → Respond with main page HTML (`main`, output 0, input 0)
- doc action → mkdir (`main`, output 0, input 0)
- doc action → Load Doc File (`main`, output 0, input 0)
- doc action → Passthrough (`main`, output 0, input 0)
- doc action → mkdir (`main`, output 1, input 0)
- doc action → Load Doc File (`main`, output 1, input 0)
- doc action → Passthrough (`main`, output 1, input 0)
- doc action → mkdir (`main`, output 2, input 0)
- doc action → Empty Set (`main`, output 2, input 0)
- doc action → Passthrough (`main`, output 2, input 0)
- doc action → Edit Fields (`main`, output 3, input 0)
- file types → md files (`main`, output 0, input 0)
- Edit Fields → Convert to File (`main`, output 0, input 0)
- Edit Fields → Merge6 (`main`, output 0, input 1)
- Passthrough → Merge3 (`main`, output 0, input 1)
- Passthrough → Merge (`main`, output 0, input 0)
- Generated Doc → Convert to File (`main`, output 0, input 0)
- Generated Doc → Is Action Edit?2 (`main`, output 0, input 0)
- Load Doc File → Merge1 (`main`, output 0, input 0)
- Workflow Tags → Respond with markdown (`main`, output 0, input 0)
- Blank Doc File → Is Action Edit?2 (`main`, output 0, input 0)
- Sort-workflows → Fill Workflow Table (`main`, output 0, input 0)
- Basic LLM Chain → Merge2 (`main`, output 0, input 1)
- Convert to File → Save New Doc File (`main`, output 0, input 0)
- Is Action Save? → Respond OK on Save (`main`, output 0, input 0)
- single workflow → CONFIG (`main`, output 0, input 0)
- single workflow → Merge5 (`main`, output 0, input 1)
- single workflow → CONFIG (`main`, output 1, input 0)
- single workflow → Merge5 (`main`, output 1, input 1)
- Is Action Edit?1 → Blank Doc File (`main`, output 0, input 0)
- Is Action Edit?1 → Basic LLM Chain (`main`, output 1, input 0)
- Is Action Edit?1 → Merge2 (`main`, output 1, input 0)
- Is Action Edit?2 → Edit Page (`main`, output 0, input 0)
- Is Action Edit?2 → Workflow md content (`main`, output 1, input 0)
- Extract from File → Merge3 (`main`, output 0, input 0)
- Get All Workflows → Sort-workflows (`main`, output 0, input 0)
- Get Workflow tags → Workflow Tags (`main`, output 0, input 0)
- Instance overview → Respond with markdown (`main`, output 0, input 0)
- OpenAI Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Save New Doc File → Merge6 (`main`, output 0, input 0)
- Fallback file name → Respond with markdown (`main`, output 0, input 0)
- Fill Workflow Table → Instance overview (`main`, output 0, input 0)
- Workflow md content → Respond with markdown (`main`, output 0, input 0)
- Fetch Single Workflow1 → Generate Mermaid Chart (`main`, output 0, input 0)
- Fetch Single Workflow1 → Merge (`main`, output 0, input 1)
- Generate Mermaid Chart → Merge (`main`, output 0, input 2)
- No Operation, do nothing → Fallback file name (`main`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Basic LLM Chain (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1726_Code_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1726_Code_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
