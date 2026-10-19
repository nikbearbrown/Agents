# list gmail and delete gmail and ai check email

This folder contains the **list gmail and delete gmail and ai check email** workflow. Its executable nodes use `agent`, `aggregate`, `gmail`, `if`, `lmChatGoogleGemini`, `manualTrigger`, `noOp`, `outputParserStructured`, `set`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-gmail-and-delete-gmail-and-ai-check-email.json`](list-gmail-and-delete-gmail-and-ai-check-email.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `telegramApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Get Email | `gmail` | getAll |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| GmailDeleteEmail | `gmail` | delete |
| AI Check Email | `agent` | Inspect parameters |
| Unwanted Email Output Parser | `outputParserStructured` | Inspect parameters |
| If Unwanted Marketing or Spam | `if` | Inspect parameters |
| Telegram Sent Email Deleted Notification | `telegram` | Inspect parameters |
| Telegram Sent Email Not Deleted Notification | `telegram` | Inspect parameters |
| Telegram Sent AI Error Notification | `telegram` | Inspect parameters |
| Telegram Sent Delete Email Failed Notification | `telegram` | Inspect parameters |
| Success | `noOp` | Inspect parameters |
| Increment Loop Var | `set` | Inspect parameters |
| Forward Prev Page Num | `set` | Inspect parameters |
| Initialize Loop Vars | `set` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Gmail | `gmail` | addLabels |

## Connection map

- Gmail → Telegram Sent Email Not Deleted Notification (`main`, output 0, input 0)
- Success → Aggregate (`main`, output 0, input 0)
- Aggregate → Forward Prev Page Num (`main`, output 0, input 0)
- AI Check Email → If Unwanted Marketing or Spam (`main`, output 0, input 0)
- AI Check Email → Telegram Sent AI Error Notification (`main`, output 1, input 0)
- Gmail Get Email → AI Check Email (`main`, output 0, input 0)
- GmailDeleteEmail → Telegram Sent Email Deleted Notification (`main`, output 0, input 0)
- GmailDeleteEmail → Telegram Sent Delete Email Failed Notification (`main`, output 1, input 0)
- Increment Loop Var → Gmail Get Email (`main`, output 0, input 0)
- Initialize Loop Vars → Increment Loop Var (`main`, output 0, input 0)
- Forward Prev Page Num → Initialize Loop Vars (`main`, output 0, input 0)
- Google Gemini Chat Model → AI Check Email (`ai_languageModel`, output 0, input 0)
- Unwanted Email Output Parser → AI Check Email (`ai_outputParser`, output 0, input 0)
- If Unwanted Marketing or Spam → GmailDeleteEmail (`main`, output 0, input 0)
- If Unwanted Marketing or Spam → Gmail (`main`, output 1, input 0)
- When clicking ‘Test workflow’ → Initialize Loop Vars (`main`, output 0, input 0)
- Telegram Sent AI Error Notification → Success (`main`, output 0, input 0)
- Telegram Sent AI Error Notification → Success (`main`, output 1, input 0)
- Telegram Sent Email Deleted Notification → Success (`main`, output 0, input 0)
- Telegram Sent Email Deleted Notification → Success (`main`, output 1, input 0)
- Telegram Sent Email Not Deleted Notification → Success (`main`, output 0, input 0)
- Telegram Sent Email Not Deleted Notification → Success (`main`, output 1, input 0)
- Telegram Sent Delete Email Failed Notification → Success (`main`, output 0, input 0)
- Telegram Sent Delete Email Failed Notification → Success (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1841_Telegram_Manual_Automate_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1841_Telegram_Manual_Automate_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
