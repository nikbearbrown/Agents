# Gmail AI auto-responder: create draft replies to incoming emails

This folder contains the **Gmail AI auto-responder: create draft replies to incoming emails** workflow. Its executable nodes use `chainLlm`, `gmail`, `gmailTrigger`, `if`, `lmChatOpenAi`, `outputParserStructured`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`gmail-ai-auto-responder-create-draft-replies-to-incoming-emails.json`](gmail-ai-auto-responder-create-draft-replies-to-incoming-emails.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `openAiApi`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| If Needs Reply | `if` | Inspect parameters |
| JSON Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Gmail - Create Draft | `gmail` | draft |
| Assess if message needs a reply | `chainLlm` | Inspect parameters |
| Generate email reply | `chainLlm` | Inspect parameters |

## Connection map

- JSON Parser → Assess if message needs a reply (`ai_outputParser`, output 0, input 0)
- OpenAI Chat → Assess if message needs a reply (`ai_languageModel`, output 0, input 0)
- Gmail Trigger → Assess if message needs a reply (`main`, output 0, input 0)
- If Needs Reply → Generate email reply (`main`, output 0, input 0)
- OpenAI Chat Model → Generate email reply (`ai_languageModel`, output 0, input 0)
- Generate email reply → Gmail - Create Draft (`main`, output 0, input 0)
- Assess if message needs a reply → If Needs Reply (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmail/1479_Gmail_Stickynote_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Gmail/1479_Gmail_Stickynote_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
