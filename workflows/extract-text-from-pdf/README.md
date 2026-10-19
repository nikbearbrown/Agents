# Extract text from PDF

This folder contains the **Extract text from PDF** workflow. Its executable nodes use `chainLlm`, `code`, `convertToFile`, `extractFromFile`, `httpRequest`, `if`, `lmChatOpenAi`, `merge`, `noOp`, `outputParserAutofixing`, `outputParserStructured`, `set`, `telegram`, `telegramTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-text-from-pdf.json`](extract-text-from-pdf.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `telegramApi`

**Entry nodes:** Telegram trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Convert education to HTML | `code` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Convert employment history to HTML | `code` | Inspect parameters |
| Convert projects to HTML | `code` | Inspect parameters |
| Convert volunteering to HTML | `code` | Inspect parameters |
| Telegram trigger | `telegramTrigger` | Inspect parameters |
| Auth | `if` | Inspect parameters |
| No operation (unauthorized) | `noOp` | Inspect parameters |
| Check if start message | `if` | Inspect parameters |
| No operation (start message) | `noOp` | Inspect parameters |
| Get file | `telegram` | file |
| Extract text from PDF | `extractFromFile` | pdf |
| Set parsed fileds | `set` | Inspect parameters |
| Personal info | `set` | Inspect parameters |
| Technologies | `set` | Inspect parameters |
| Employment history | `set` | Inspect parameters |
| Education | `set` | Inspect parameters |
| Projects | `set` | Inspect parameters |
| Volunteering | `set` | Inspect parameters |
| Merge education and employment history | `merge` | Inspect parameters |
| Merge projects and volunteering | `merge` | Inspect parameters |
| Merge personal info and technologies | `merge` | Inspect parameters |
| Merge all | `merge` | Inspect parameters |
| Set final data | `set` | Inspect parameters |
| Convert raw to base64 | `code` | Inspect parameters |
| Convert to HTML | `convertToFile` | toBinary |
| Generate plain PDF doc | `httpRequest` | POST |
| Send PDF to the user | `telegram` | sendDocument |
| Parse resume data | `chainLlm` | Inspect parameters |
| Merge other data | `merge` | Inspect parameters |

## Connection map

- Auth → Check if start message (`main`, output 0, input 0)
- Auth → No operation (unauthorized) (`main`, output 1, input 0)
- Get file → Extract text from PDF (`main`, output 0, input 0)
- Projects → Merge projects and volunteering (`main`, output 0, input 0)
- Education → Merge education and employment history (`main`, output 0, input 1)
- Merge all → Set final data (`main`, output 0, input 0)
- Technologies → Merge personal info and technologies (`main`, output 0, input 1)
- Volunteering → Merge projects and volunteering (`main`, output 0, input 1)
- Personal info → Merge personal info and technologies (`main`, output 0, input 0)
- Set final data → Convert raw to base64 (`main`, output 0, input 0)
- Convert to HTML → Generate plain PDF doc (`main`, output 0, input 0)
- Merge other data → Merge all (`main`, output 0, input 1)
- Telegram trigger → Auth (`main`, output 0, input 0)
- OpenAI Chat Model → Parse resume data (`ai_languageModel`, output 0, input 0)
- Parse resume data → Set parsed fileds (`main`, output 0, input 0)
- Set parsed fileds → Convert employment history to HTML (`main`, output 0, input 0)
- Set parsed fileds → Convert education to HTML (`main`, output 0, input 0)
- Set parsed fileds → Convert projects to HTML (`main`, output 0, input 0)
- Set parsed fileds → Personal info (`main`, output 0, input 0)
- Set parsed fileds → Convert volunteering to HTML (`main`, output 0, input 0)
- Set parsed fileds → Technologies (`main`, output 0, input 0)
- Employment history → Merge education and employment history (`main`, output 0, input 0)
- OpenAI Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Convert raw to base64 → Convert to HTML (`main`, output 0, input 0)
- Extract text from PDF → Parse resume data (`main`, output 0, input 0)
- Check if start message → Get file (`main`, output 0, input 0)
- Check if start message → No operation (start message) (`main`, output 1, input 0)
- Generate plain PDF doc → Send PDF to the user (`main`, output 0, input 0)
- Convert projects to HTML → Projects (`main`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Parse resume data (`ai_outputParser`, output 0, input 0)
- Convert education to HTML → Education (`main`, output 0, input 0)
- Convert volunteering to HTML → Volunteering (`main`, output 0, input 0)
- Merge projects and volunteering → Merge other data (`main`, output 0, input 1)
- Convert employment history to HTML → Employment history (`main`, output 0, input 0)
- Merge personal info and technologies → Merge all (`main`, output 0, input 0)
- Merge education and employment history → Merge other data (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0462_Telegram_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0462_Telegram_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
