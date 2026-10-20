# OpenAI Security Analysis

This folder contains the **OpenAI Security Analysis** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `formTrigger`, `gmail`, `httpRequest`, `lmChatOpenAi`, `merge`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`openai-security-analysis.json`](openai-security-analysis.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Landing Page Url

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Landing Page Url | `formTrigger` | Inspect parameters |
| Scrape Website | `httpRequest` | Inspect parameters |
| OpenAI Headers Analysis | `lmChatOpenAi` | Inspect parameters |
| OpenAI Content Analysis | `lmChatOpenAi` | Inspect parameters |
| Security Vulnerabilities Audit | `agent` | Inspect parameters |
| Security Configuration Audit | `agent` | Inspect parameters |
| Merge Security Results | `merge` | Inspect parameters |
| Aggregate Audit Results | `aggregate` | Inspect parameters |
| Process Audit Results | `code` | Inspect parameters |
| Send Security Report | `gmail` | Inspect parameters |
| Extract Headers for Debug | `code` | Inspect parameters |
| convert to HTML | `code` | Inspect parameters |

## Connection map

- Scrape Website → Security Vulnerabilities Audit (`main`, output 0, input 0)
- Scrape Website → Extract Headers for Debug (`main`, output 0, input 0)
- convert to HTML → Send Security Report (`main`, output 0, input 0)
- Landing Page Url → Scrape Website (`main`, output 0, input 0)
- Process Audit Results → convert to HTML (`main`, output 0, input 0)
- Merge Security Results → Aggregate Audit Results (`main`, output 0, input 0)
- Aggregate Audit Results → Process Audit Results (`main`, output 0, input 0)
- OpenAI Content Analysis → Security Vulnerabilities Audit (`ai_languageModel`, output 0, input 0)
- OpenAI Headers Analysis → Security Configuration Audit (`ai_languageModel`, output 0, input 0)
- Extract Headers for Debug → Security Configuration Audit (`main`, output 0, input 0)
- Security Configuration Audit → Merge Security Results (`main`, output 0, input 0)
- Security Vulnerabilities Audit → Merge Security Results (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0808_Code_Form_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0808_Code_Form_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
