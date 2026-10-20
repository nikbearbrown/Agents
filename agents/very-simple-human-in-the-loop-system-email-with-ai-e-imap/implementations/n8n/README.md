# Very simple Human in the loop system email with AI e IMAP

This folder contains the **Very simple Human in the loop system email with AI e IMAP** workflow. Its executable nodes use `agent`, `chainSummarization`, `emailReadImap`, `emailSend`, `if`, `lmChatOpenAi`, `markdown`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`very-simple-human-in-the-loop-system-email-with-ai-e-imap.json`](very-simple-human-in-the-loop-system-email-with-ai-e-imap.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `imap`, `openAiApi`, `smtp`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Email Summarization Chain | `chainSummarization` | Inspect parameters |
| Write email | `agent` | Inspect parameters |
| OpenAI | `lmChatOpenAi` | Inspect parameters |
| Approve Email | `emailSend` | sendAndWait |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Set Email text | `set` | Inspect parameters |
| Approved? | `if` | Inspect parameters |

## Connection map

- OpenAI → Write email (`ai_languageModel`, output 0, input 0)
- Markdown → Email Summarization Chain (`main`, output 0, input 0)
- Approved? → Send Email (`main`, output 0, input 0)
- Write email → Set Email text (`main`, output 0, input 0)
- Approve Email → Approved? (`main`, output 0, input 0)
- Set Email text → Approve Email (`main`, output 0, input 0)
- OpenAI Chat Model → Email Summarization Chain (`ai_languageModel`, output 0, input 0)
- Email Trigger (IMAP) → Markdown (`main`, output 0, input 0)
- Email Summarization Chain → Write email (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Markdown/1571_Markdown_Stickynote_Send.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Markdown/1571_Markdown_Stickynote_Send.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
