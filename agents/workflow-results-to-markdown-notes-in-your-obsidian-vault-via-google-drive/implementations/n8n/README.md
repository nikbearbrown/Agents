# Workflow Results to Markdown Notes in Your Obsidian Vault, via Google Drive

This folder contains the **Workflow Results to Markdown Notes in Your Obsidian Vault, via Google Drive** workflow. Its executable nodes use `agent`, `executeWorkflowTrigger`, `googleDrive`, `if`, `lmChatOpenAi`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-results-to-markdown-notes-in-your-obsidian-vault-via-google-drive.json`](workflow-results-to-markdown-notes-in-your-obsidian-vault-via-google-drive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** Receive results from any workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Save Markdown file | `googleDrive` | createFromText |
| Receive results from any workflow | `executeWorkflowTrigger` | Inspect parameters |
| If the input has binary attachment | `if` | Inspect parameters |
| Write Zettlekasten note from input1 | `agent` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Restructure JSON | `set` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Write YAML Frontmatter | `agent` | Inspect parameters |
| Save attachment | `googleDrive` | Inspect parameters |

## Connection map

- OpenAI Chat Model → Write Zettlekasten note from input1 (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Write YAML Frontmatter (`ai_languageModel`, output 0, input 0)
- Write YAML Frontmatter → Restructure JSON (`main`, output 0, input 0)
- Structured Output Parser → Write Zettlekasten note from input1 (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → Write YAML Frontmatter (`ai_outputParser`, output 0, input 0)
- Receive results from any workflow → If the input has binary attachment (`main`, output 0, input 0)
- Receive results from any workflow → Save Markdown file (`main`, output 0, input 0)
- If the input has binary attachment → Save attachment (`main`, output 0, input 0)
- Write Zettlekasten note from input1 → Write YAML Frontmatter (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0947_Executeworkflow_Stickynote_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executeworkflow/0947_Executeworkflow_Stickynote_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
