# ✍️🌄 Your First Wordpress Content Creator - Quick Start

This folder contains the **✍️🌄 Your First Wordpress Content Creator - Quick Start** workflow. Its executable nodes use `agent`, `code`, `googleDrive`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `outputParserStructured`, `set`, `telegram`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`your-first-wordpress-content-creator-quick-start.json`](your-first-wordpress-content-creator-quick-start.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `openAiApi`, `telegramApi`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Structured Output - JSON | `outputParserStructured` | Inspect parameters |
| Separate Title & Content | `code` | Inspect parameters |
| gpt-4o-mini1 | `lmChatOpenAi` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| gpt-4o-mini2 | `lmChatOpenAi` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| gpt-4o-mini3 | `lmChatOpenAi` | Inspect parameters |
| If3 | `if` | Inspect parameters |
| Rewrite for Grade 5 Reading Level | `agent` | Inspect parameters |
| Rewrite for Grade 2 Reading Level | `agent` | Inspect parameters |
| Rewrite for Grade 9 Reading Level | `agent` | Inspect parameters |
| Create Structured Blog Post | `agent` | Inspect parameters |
| DeepSeek | `lmChatOpenAi` | Inspect parameters |
| Google Drive | `googleDrive` | createFromText |
| Set Blog Topic | `set` | Inspect parameters |
| pollinations.ai | `httpRequest` | Inspect parameters |
| Create Wordpress Post | `wordpress` | Inspect parameters |
| Upload Image to Wordpress | `httpRequest` | POST |
| Set Image on Wordpress Post | `httpRequest` | POST |
| HTML to Markdown | `markdown` | Inspect parameters |
| Tiltle & Content Exist? | `if` | Inspect parameters |
| Send Error Message | `telegram` | Inspect parameters |
| Send Error Message1 | `telegram` | Inspect parameters |
| Send Error Message2 | `telegram` | Inspect parameters |
| Send Error Message3 | `telegram` | Inspect parameters |
| Send Success Message | `telegram` | Inspect parameters |

## Connection map

- If1 → Create Wordpress Post (`main`, output 0, input 0)
- If1 → Send Error Message1 (`main`, output 1, input 0)
- If2 → Send Error Message2 (`main`, output 1, input 0)
- If3 → Send Error Message3 (`main`, output 1, input 0)
- gpt-4o-mini → Create Structured Blog Post (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini1 → Rewrite for Grade 9 Reading Level (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini2 → Rewrite for Grade 5 Reading Level (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini3 → Rewrite for Grade 2 Reading Level (`ai_languageModel`, output 0, input 0)
- Set Blog Topic → Create Structured Blog Post (`main`, output 0, input 0)
- pollinations.ai → Upload Image to Wordpress (`main`, output 0, input 0)
- HTML to Markdown → Rewrite for Grade 9 Reading Level (`main`, output 0, input 0)
- HTML to Markdown → Google Drive (`main`, output 0, input 0)
- Create Wordpress Post → pollinations.ai (`main`, output 0, input 0)
- Tiltle & Content Exist? → HTML to Markdown (`main`, output 0, input 0)
- Tiltle & Content Exist? → Send Error Message (`main`, output 1, input 0)
- Separate Title & Content → Tiltle & Content Exist? (`main`, output 0, input 0)
- Structured Output - JSON → Create Structured Blog Post (`ai_outputParser`, output 0, input 0)
- Upload Image to Wordpress → Set Image on Wordpress Post (`main`, output 0, input 0)
- Create Structured Blog Post → Separate Title & Content (`main`, output 0, input 0)
- Set Image on Wordpress Post → Send Success Message (`main`, output 0, input 0)
- Rewrite for Grade 2 Reading Level → If3 (`main`, output 0, input 0)
- Rewrite for Grade 5 Reading Level → If2 (`main`, output 0, input 0)
- Rewrite for Grade 9 Reading Level → If1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Blog Topic (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1291_Telegram_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1291_Telegram_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
