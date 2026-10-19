# Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide

This folder contains the **Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide** workflow. Its executable nodes use `filter`, `gmail`, `googleSheets`, `googleSheetsTrigger`, `httpRequest`, `if`, `openAi`, `respondToWebhook`, `twilio`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`build-a-phone-agent-to-qualify-outbound-leads-and-inbound-calls-with-retellai-vide.json`](build-a-phone-agent-to-qualify-outbound-leads-and-inbound-calls-with-retellai-vide.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `openAiApi`, `twilioApi`

**Entry nodes:** Detect new lead in Google Sheets, Receive inbound call from RetellAI (webhook), Receive post-call data from RetellAI (webhook)

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Detect new lead in Google Sheets | `googleSheetsTrigger` | Inspect parameters |
| Send SMS reminder to call lead in 5 minutes | `twilio` | call |
| Wait 5 minutes before making call | `wait` | Inspect parameters |
| Call new lead using RetellAI | `httpRequest` | POST |
| Receive inbound call from RetellAI (webhook) | `webhook` | Inspect parameters |
| Check if phone number exists in Google Sheets | `googleSheets` | Inspect parameters |
| Send response to inbound webhook call | `respondToWebhook` | Inspect parameters |
| Receive post-call data from RetellAI (webhook) | `webhook` | Inspect parameters |
| Filter for analyzed calls only | `filter` | Inspect parameters |
| Check if call was outbound | `if` | Inspect parameters |
| Update lead record in Google Sheets | `googleSheets` | update |
| Send call summary email | `gmail` | Inspect parameters |
| Generate call summary with OpenAI | `openAi` | Inspect parameters |
| Send confirmation email to lead | `gmail` | Inspect parameters |

## Connection map

- Check if call was outbound → Update lead record in Google Sheets (`main`, output 0, input 0)
- Check if call was outbound → Generate call summary with OpenAI (`main`, output 1, input 0)
- Filter for analyzed calls only → Check if call was outbound (`main`, output 0, input 0)
- Detect new lead in Google Sheets → Send SMS reminder to call lead in 5 minutes (`main`, output 0, input 0)
- Generate call summary with OpenAI → Send confirmation email to lead (`main`, output 0, input 0)
- Wait 5 minutes before making call → Call new lead using RetellAI (`main`, output 0, input 0)
- Update lead record in Google Sheets → Send call summary email (`main`, output 0, input 0)
- Send SMS reminder to call lead in 5 minutes → Wait 5 minutes before making call (`main`, output 0, input 0)
- Receive inbound call from RetellAI (webhook) → Check if phone number exists in Google Sheets (`main`, output 0, input 0)
- Check if phone number exists in Google Sheets → Send response to inbound webhook call (`main`, output 0, input 0)
- Receive post-call data from RetellAI (webhook) → Filter for analyzed calls only (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1362_Wait_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1362_Wait_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
