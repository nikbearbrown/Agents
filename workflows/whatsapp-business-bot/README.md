# WhatsApp business bot

This folder contains the **WhatsApp business bot** workflow. Its executable nodes use `filter`, `googleSheets`, `googleSheetsTrigger`, `if`, `scheduleTrigger`, `splitInBatches`, `wait`, `whatsApp`, `whatsAppTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`whatsapp-business-bot.json`](whatsapp-business-bot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `whatsAppApi`, `whatsAppTriggerApi`

**Entry nodes:** WhatsApp Trigger, Schedule Trigger, Get new entries

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Sent notification  template | `whatsApp` | Inspect parameters |
| WhatsApp Trigger | `whatsAppTrigger` | Inspect parameters |
| Is message? | `if` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Get new answers | `googleSheets` | Inspect parameters |
| Reply to the user | `whatsApp` | send |
| Update message status | `googleSheets` | update |
| Wait 1 sec | `wait` | Inspect parameters |
| New message from the user | `googleSheets` | append |
| Get new entries | `googleSheetsTrigger` | Inspect parameters |
| User consented for WA messages? | `filter` | Inspect parameters |

## Connection map

- Wait 1 sec → Loop Over Items (`main`, output 0, input 0)
- Is message? → New message from the user (`main`, output 0, input 0)
- Get new answers → Loop Over Items (`main`, output 0, input 0)
- Get new entries → User consented for WA messages? (`main`, output 0, input 0)
- Loop Over Items → Reply to the user (`main`, output 1, input 0)
- Schedule Trigger → Get new answers (`main`, output 0, input 0)
- WhatsApp Trigger → Is message? (`main`, output 0, input 0)
- Reply to the user → Update message status (`main`, output 0, input 0)
- Update message status → Wait 1 sec (`main`, output 0, input 0)
- User consented for WA messages? → Sent notification  template (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1572_Wait_Schedule_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1572_Wait_Schedule_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
