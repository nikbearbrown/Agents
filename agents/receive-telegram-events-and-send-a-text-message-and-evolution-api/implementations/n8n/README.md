# Dary

This folder contains the **Dary** workflow. Its executable nodes use `code`, `evolutionApi`, `googleSheets`, `if`, `merge`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-telegram-events-and-send-a-text-message-and-evolution-api.json`](receive-telegram-events-and-send-a-text-message-and-evolution-api.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `evolutionApi`, `googleSheetsOAuth2Api`, `telegramApi`

**Entry nodes:** Telegram Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Telegram Trigger | `telegramTrigger` | Inspect parameters |
| Send a text message | `telegram` | Inspect parameters |
| Send text | `evolutionApi` | messages-api |
| If | `if` | Inspect parameters |
| Check if the number is exist or not | `googleSheets` | Inspect parameters |
| The number already exist | `set` | Inspect parameters |
| Add phone number to the sheet | `googleSheets` | append |
| Error Message | `set` | Inspect parameters |
| Message Done | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Code in JavaScript | `code` | Inspect parameters |
| Get row(s) in sheet | `googleSheets` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Update row in sheet | `googleSheets` | update |
| Merge1 | `merge` | Inspect parameters |

## Connection map

- Telegram Trigger → Check if the number is exist or not (`main`, output 0, input 0)
- Send text → Message Done (`main`, output 0, input 0)
- Send text → Error Message (`main`, output 1, input 0)
- If → The number already exist (`main`, output 0, input 0)
- If → Get row(s) in sheet (`main`, output 1, input 0)
- Check if the number is exist or not → If (`main`, output 0, input 0)
- The number already exist → Merge (`main`, output 0, input 0)
- Error Message → Merge (`main`, output 0, input 2)
- Error Message → Merge1 (`main`, output 0, input 1)
- Message Done → Merge (`main`, output 0, input 1)
- Message Done → Merge1 (`main`, output 0, input 0)
- Merge → Send a text message (`main`, output 0, input 0)
- Code in JavaScript → Send text (`main`, output 0, input 0)
- Get row(s) in sheet → Code in JavaScript (`main`, output 0, input 0)
- If1 → Update row in sheet (`main`, output 0, input 0)
- If1 → Add phone number to the sheet (`main`, output 1, input 0)
- Merge1 → If1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Mohamed-Shahen-AI/Dary/blob/c79d4506562689b3f84d2447fd04fec06aa33291/Dary.json](https://github.com/Mohamed-Shahen-AI/Dary/blob/c79d4506562689b3f84d2447fd04fec06aa33291/Dary.json). License: **MIT**; preserve [the notice](../../../../licenses/Mohamed-Shahen-AI--Dary.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
