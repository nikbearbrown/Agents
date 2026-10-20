# 📄🛠️PDF2Blog

This folder contains the **📄🛠️PDF2Blog** workflow. Its executable nodes use `agent`, `code`, `extractFromFile`, `formTrigger`, `ghost`, `if`, `lmChatOpenAi`, `noOp`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pdf2blog.json`](pdf2blog.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `ghostAdminApi`, `openAiApi`

**Entry nodes:** Upload PDF

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Upload PDF | `formTrigger` | Inspect parameters |
| Extract Text | `extractFromFile` | pdf |
| Post to Ghost | `ghost` | create |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Structured Output - JSON | `outputParserStructured` | Inspect parameters |
| Separate Title & Content | `code` | Inspect parameters |
| If | `if` | Inspect parameters |
| Do Nothing | `noOp` | Inspect parameters |
| Create Structured Blog Post | `agent` | Inspect parameters |

## Connection map

- If → Post to Ghost (`main`, output 0, input 0)
- If → Do Nothing (`main`, output 1, input 0)
- Upload PDF → Extract Text (`main`, output 0, input 0)
- gpt-4o-mini → Create Structured Blog Post (`ai_languageModel`, output 0, input 0)
- Extract Text → Create Structured Blog Post (`main`, output 0, input 0)
- Separate Title & Content → If (`main`, output 0, input 0)
- Structured Output - JSON → Create Structured Blog Post (`ai_outputParser`, output 0, input 0)
- Create Structured Blog Post → Separate Title & Content (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1837_Code_Ghost_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1837_Code_Ghost_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
