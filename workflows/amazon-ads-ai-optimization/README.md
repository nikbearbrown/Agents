# Amazon Ads AI Optimization

This folder contains the **Amazon Ads AI Optimization** workflow. Its executable nodes use `chainLlm`, `code`, `extractFromFile`, `gmail`, `googleDrive`, `if`, `lmChatOpenAi`, `manualTrigger`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`amazon-ads-ai-optimization.json`](amazon-ads-ai-optimization.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| List Files | `googleDrive` | fileFolder |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| is XLSX | `if` | Inspect parameters |
| Get File | `googleDrive` | download |
| Merge XLSX and CSV | `merge` | Inspect parameters |
| Format Data | `code` | Inspect parameters |
| Set fileName | `set` | Inspect parameters |
| Preserve File Name | `set` | Inspect parameters |
| Email Optimizations | `gmail` | Inspect parameters |
| Extract XLSX Data | `extractFromFile` | xlsx |
| Extract CSV Data | `extractFromFile` | Inspect parameters |
| Preserve CSV File Name | `set` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Email Options | `set` | Inspect parameters |
| AI Analyze | `chainLlm` | Inspect parameters |

## Connection map

- is XLSX → Extract XLSX Data (`main`, output 0, input 0)
- is XLSX → Extract CSV Data (`main`, output 1, input 0)
- Get File → Set fileName (`main`, output 0, input 0)
- AI Analyze → Email Optimizations (`main`, output 0, input 0)
- List Files → Get File (`main`, output 0, input 0)
- Format Data → AI Analyze (`main`, output 0, input 0)
- Set fileName → is XLSX (`main`, output 0, input 0)
- Email Options → List Files (`main`, output 0, input 0)
- Extract CSV Data → Preserve CSV File Name (`main`, output 0, input 0)
- Extract XLSX Data → Preserve File Name (`main`, output 0, input 0)
- OpenAI Chat Model → AI Analyze (`ai_languageModel`, output 0, input 0)
- Merge XLSX and CSV → Format Data (`main`, output 0, input 0)
- Preserve File Name → Merge XLSX and CSV (`main`, output 0, input 0)
- Preserve CSV File Name → Merge XLSX and CSV (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Email Options (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1301_Code_Extractfromfile_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1301_Code_Extractfromfile_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
