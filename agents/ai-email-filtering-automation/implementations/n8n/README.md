# AI Email Filtering Automation

This folder contains the **AI Email Filtering Automation** workflow. Its executable nodes use `code`, `errorTrigger`, `gmail`, `gmailTrigger`, `httpRequest`, `if`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-email-filtering-automation.json`](ai-email-filtering-automation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`

**Entry nodes:** Gmail Trigger, Error Trigger Handler

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Preprocess Email Data | `code` | Inspect parameters |
| Analyze Email with Gemini | `httpRequest` | POST |
| Parse Gemini Response | `code` | Inspect parameters |
| Conditional Routing (IF) | `if` | Inspect parameters |
| Discord Webhook Notification | `httpRequest` | POST |
| Telegram Bot Notification | `httpRequest` | POST |
| Mark Email as Read | `gmail` | message / addLabels |
| Move Email to Trash | `gmail` | message / trash |
| Log Trashed Email | `code` | Inspect parameters |
| Error Trigger Handler | `errorTrigger` | Inspect parameters |
| Log Execution Failure | `code` | Inspect parameters |

## Connection map

- Gmail Trigger → Preprocess Email Data (`main`, output 0, input 0)
- Preprocess Email Data → Analyze Email with Gemini (`main`, output 0, input 0)
- Analyze Email with Gemini → Parse Gemini Response (`main`, output 0, input 0)
- Parse Gemini Response → Conditional Routing (IF) (`main`, output 0, input 0)
- Conditional Routing (IF) → Discord Webhook Notification (`main`, output 0, input 0)
- Conditional Routing (IF) → Move Email to Trash (`main`, output 1, input 0)
- Discord Webhook Notification → Telegram Bot Notification (`main`, output 0, input 0)
- Telegram Bot Notification → Mark Email as Read (`main`, output 0, input 0)
- Move Email to Trash → Log Trashed Email (`main`, output 0, input 0)
- Error Trigger Handler → Log Execution Failure (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Shazil-Qureshi/AI-Email-Filtering-Automation/blob/cc55b99a3ca9109ae52ce96dd4738512b67ae6dd/workflow.json](https://github.com/Shazil-Qureshi/AI-Email-Filtering-Automation/blob/cc55b99a3ca9109ae52ce96dd4738512b67ae6dd/workflow.json). License: **MIT**; preserve [the notice](../../../../licenses/Shazil-Qureshi--AI-Email-Filtering-Automation.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
