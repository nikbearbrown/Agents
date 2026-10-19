# agent and reply gmail and text extract from file

This folder contains the **agent and reply gmail and text extract from file** workflow. Its executable nodes use `agent`, `code`, `extractFromFile`, `gmail`, `gmailTrigger`, `if`, `lmChatOpenAi`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`agent-and-reply-gmail-and-text-extract-from-file.json`](agent-and-reply-gmail-and-text-extract-from-file.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Email Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If | `if` | Inspect parameters |
| Check the format | `code` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Reply | `gmail` | reply |
| Extract the HTML | `code` | Inspect parameters |
| HTML from binary | `extractFromFile` | text |
| Email Trigger | `gmailTrigger` | Inspect parameters |
| Download Attachment | `gmail` | get |

## Connection map

- AI Agent → Reply (`main`, output 0, input 0)
- Email Trigger → If (`main`, output 0, input 0)
- Check the format → AI Agent (`main`, output 0, input 0)
- Extract the HTML → Check the format (`main`, output 0, input 0)
- HTML from binary → Extract the HTML (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0828_Extractfromfile_Gmail_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/0828_Extractfromfile_Gmail_Send_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
