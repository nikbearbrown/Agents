# Load Prompts from Github Repo and auto populate n8n expressions

This folder contains the **Load Prompts from Github Repo and auto populate n8n expressions** workflow. Its executable nodes use `agent`, `code`, `extractFromFile`, `github`, `if`, `lmChatOllama`, `manualTrigger`, `set`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`load-prompts-from-github-repo-and-auto-populate-n8n-expressions.json`](load-prompts-from-github-repo-and-auto-populate-n8n-expressions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `githubApi`, `ollamaApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| GitHub | `github` | file / get |
| Extract from File | `extractFromFile` | text |
| setVars | `set` | Inspect parameters |
| replace variables | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| Check All Prompt Vars Present | `code` | Inspect parameters |
| SetPrompt | `set` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Set Completed Prompt | `set` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Prompt Output | `set` | Inspect parameters |
| Ollama Chat Model | `lmChatOllama` | Inspect parameters |

## Connection map

- If → replace variables (`main`, output 0, input 0)
- If → Stop and Error (`main`, output 1, input 0)
- GitHub → Extract from File (`main`, output 0, input 0)
- setVars → GitHub (`main`, output 0, input 0)
- AI Agent → Prompt Output (`main`, output 0, input 0)
- SetPrompt → Check All Prompt Vars Present (`main`, output 0, input 0)
- Extract from File → SetPrompt (`main`, output 0, input 0)
- Ollama Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- replace variables → Set Completed Prompt (`main`, output 0, input 0)
- Set Completed Prompt → AI Agent (`main`, output 0, input 0)
- Check All Prompt Vars Present → If (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → setVars (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1623_Stopanderror_Code_Import_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1623_Stopanderror_Code_Import_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
