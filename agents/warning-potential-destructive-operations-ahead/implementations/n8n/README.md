# 🚨 Warning! Potential destructive operations ahead!

This folder contains the **🚨 Warning! Potential destructive operations ahead!** workflow. Its executable nodes use `chainLlm`, `executeCommand`, `if`, `lmChatMistralCloud`, `localFileTrigger`, `outputParserStructured`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`warning-potential-destructive-operations-ahead.json`](warning-potential-destructive-operations-ahead.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mistralCloudApi`

**Entry nodes:** Local File Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Local File Trigger | `localFileTrigger` | Inspect parameters |
| Get Files and Folders | `executeCommand` | Inspect parameters |
| Files and Folders to Array | `set` | Inspect parameters |
| Mistral Cloud Chat Model | `lmChatMistralCloud` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Set Variables | `set` | Inspect parameters |
| Move Files into Folders | `executeCommand` | Inspect parameters |
| If Has Target Files... | `if` | Inspect parameters |
| Get Suggestions to List | `splitOut` | Inspect parameters |
| AI File Manager | `chainLlm` | Inspect parameters |

## Connection map

- Set Variables → Get Files and Folders (`main`, output 0, input 0)
- AI File Manager → Get Suggestions to List (`main`, output 0, input 0)
- Local File Trigger → Set Variables (`main`, output 0, input 0)
- Get Files and Folders → Files and Folders to Array (`main`, output 0, input 0)
- If Has Target Files... → AI File Manager (`main`, output 0, input 0)
- Get Suggestions to List → Move Files into Folders (`main`, output 0, input 0)
- Mistral Cloud Chat Model → AI File Manager (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → AI File Manager (`ai_outputParser`, output 0, input 0)
- Files and Folders to Array → If Has Target Files... (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executecommand/0534_Executecommand_Localfile_Process_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executecommand/0534_Executecommand_Localfile_Process_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
