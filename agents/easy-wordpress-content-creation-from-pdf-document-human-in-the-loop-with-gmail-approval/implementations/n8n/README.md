# 📄✨ Easy Wordpress Content Creation from PDF Document + Human In The Loop with Gmail Approval

This folder contains the **📄✨ Easy Wordpress Content Creation from PDF Document + Human In The Loop with Gmail Approval** workflow. Its executable nodes use `chainLlm`, `code`, `extractFromFile`, `formTrigger`, `gmail`, `httpRequest`, `if`, `lmChatOpenAi`, `markdown`, `merge`, `telegram`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`easy-wordpress-content-creation-from-pdf-document-human-in-the-loop-with-gmail-approval.json`](easy-wordpress-content-creation-from-pdf-document-human-in-the-loop-with-gmail-approval.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`, `telegramApi`, `wordpressApi`

**Entry nodes:** Upload PDF

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Upload PDF | `formTrigger` | Inspect parameters |
| Extract Text | `extractFromFile` | pdf |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| pollinations.ai | `httpRequest` | Inspect parameters |
| Create Wordpress Post | `wordpress` | Inspect parameters |
| Upload Image to Wordpress | `httpRequest` | POST |
| Set Image on Wordpress Post | `httpRequest` | POST |
| Send Error Message | `telegram` | Inspect parameters |
| Is there Title & Content? | `if` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Markdown | `markdown` | Inspect parameters |
| Human In The Loop Approve Blog Post | `gmail` | sendAndWait |
| Is Approved? | `if` | Inspect parameters |
| Gmail Final Blog | `gmail` | Inspect parameters |
| Telegram Partial Blog | `telegram` | sendPhoto |
| Get Blog Post | `code` | Inspect parameters |
| Write Blog Post | `chainLlm` | Inspect parameters |
| Get Base64 | `extractFromFile` | binaryToPropery |
| Save Image to imgbb.com | `httpRequest` | POST |

## Connection map

- Merge → Telegram Partial Blog (`main`, output 0, input 0)
- Merge → Gmail Final Blog (`main`, output 0, input 0)
- Markdown → Merge (`main`, output 0, input 0)
- Get Base64 → Save Image to imgbb.com (`main`, output 0, input 0)
- Upload PDF → Extract Text (`main`, output 0, input 0)
- gpt-4o-mini → Write Blog Post (`ai_languageModel`, output 0, input 0)
- Extract Text → Write Blog Post (`main`, output 0, input 0)
- Is Approved? → Create Wordpress Post (`main`, output 0, input 0)
- Get Blog Post → Is there Title & Content? (`main`, output 0, input 0)
- Write Blog Post → Get Blog Post (`main`, output 0, input 0)
- pollinations.ai → Upload Image to Wordpress (`main`, output 0, input 0)
- pollinations.ai → Merge (`main`, output 0, input 1)
- pollinations.ai → Get Base64 (`main`, output 0, input 0)
- Create Wordpress Post → pollinations.ai (`main`, output 0, input 0)
- Is there Title & Content? → Human In The Loop Approve Blog Post (`main`, output 0, input 0)
- Is there Title & Content? → Send Error Message (`main`, output 1, input 0)
- Upload Image to Wordpress → Set Image on Wordpress Post (`main`, output 0, input 0)
- Set Image on Wordpress Post → Markdown (`main`, output 0, input 0)
- Human In The Loop Approve Blog Post → Is Approved? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1424_Telegram_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1424_Telegram_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
