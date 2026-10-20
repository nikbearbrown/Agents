# Microsoft Outlook AI Email Assistant

This folder contains the **Microsoft Outlook AI Email Assistant** workflow. Its executable nodes use `agent`, `airtable`, `if`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `merge`, `microsoftOutlook`, `mondayCom`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`microsoft-outlook-ai-email-assistant.json`](microsoft-outlook-ai-email-assistant.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `microsoftOutlookOAuth2Api`, `mondayComApi`, `openAiApi`

**Entry nodes:** When clicking ‘Test workflow’, Check Mail Schedule Trigger, Update Contacts Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Microsoft Outlook23 | `microsoftOutlook` | getAll |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Set Category | `microsoftOutlook` | update |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| If | `if` | Inspect parameters |
| Set Importance | `microsoftOutlook` | update |
| AI: Analyse Email | `agent` | Inspect parameters |
| Check Mail Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Update Contacts Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Monday.com - Get Contacts | `mondayCom` | boardItem / getAll |
| Airtable - Contacts | `airtable` | upsert |
| Convert to Markdown | `markdown` | Inspect parameters |
| Email Messages | `set` | Inspect parameters |
| Rules | `airtable` | search |
| Categories | `airtable` | search |
| Delete Rules | `airtable` | search |
| Contact | `airtable` | search |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Merge | `merge` | Inspect parameters |

## Connection map

- If → Set Importance (`main`, output 0, input 0)
- If → Loop Over Items (`main`, output 1, input 0)
- Merge → AI: Analyse Email (`main`, output 0, input 0)
- Rules → Merge (`main`, output 0, input 1)
- Contact → Merge (`main`, output 0, input 0)
- Categories → Merge (`main`, output 0, input 2)
- Delete Rules → Merge (`main`, output 0, input 3)
- Set Category → If (`main`, output 0, input 0)
- Email Messages → Loop Over Items (`main`, output 0, input 0)
- Set Importance → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Contact (`main`, output 1, input 0)
- AI: Analyse Email → Set Category (`main`, output 0, input 0)
- OpenAI Chat Model → AI: Analyse Email (`ai_languageModel`, output 0, input 0)
- Convert to Markdown → Email Messages (`main`, output 0, input 0)
- Microsoft Outlook23 → Convert to Markdown (`main`, output 0, input 0)
- Structured Output Parser → AI: Analyse Email (`ai_outputParser`, output 0, input 0)
- Monday.com - Get Contacts → Airtable - Contacts (`main`, output 0, input 0)
- Check Mail Schedule Trigger → Microsoft Outlook23 (`main`, output 0, input 0)
- Update Contacts Schedule Trigger → Monday.com - Get Contacts (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Microsoft Outlook23 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Rules (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Categories (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Delete Rules (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1974_Mondaycom_Schedule_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mondaycom/1974_Mondaycom_Schedule_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
