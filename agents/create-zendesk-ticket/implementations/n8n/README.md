# Create Zendesk Ticket

This folder contains the **Create Zendesk Ticket** workflow. Its executable nodes use `airtable`, `googleCalendar`, `googleSheets`, `httpRequest`, `if`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-zendesk-ticket.json`](create-zendesk-ticket.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googleCalendarOAuth2Api`, `googleSheetsOAuth2Api`, `zendeskApi`

**Entry nodes:** Airtable Endpoint, Gcal Endpoint, Zendesk Endpoint, Voiceflow Endpoint

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check if user found | `if` | Inspect parameters |
| Check if available | `if` | Inspect parameters |
| Check for malformed date | `if` | Inspect parameters |
| Create Ticket | `httpRequest` | POST |
| Create Customer in DB | `httpRequest` | POST |
| Check if submitted succesfully | `if` | Inspect parameters |
| Ticket Created Successfully | `respondToWebhook` | Inspect parameters |
| Error Creating Ticket | `respondToWebhook` | Inspect parameters |
| Airtable Endpoint | `webhook` | Inspect parameters |
| Gcal Endpoint | `webhook` | Inspect parameters |
| Zendesk Endpoint | `webhook` | Inspect parameters |
| Voiceflow Endpoint | `webhook` | Inspect parameters |
| Extract Phone Number | `set` | Inspect parameters |
| Extract Zendesk Fields | `set` | Inspect parameters |
| Extract Gcal Data | `set` | Inspect parameters |
| Extract Airtable Data | `set` | Inspect parameters |
| Create Airtable Data | `airtable` | create |
| Query Google Sheets for Phone | `googleSheets` | Inspect parameters |
| Respond to Webhook with Customer Data | `respondToWebhook` | Inspect parameters |
| Respond to Webhook with Error | `respondToWebhook` | Inspect parameters |
| Set Error Data | `set` | Inspect parameters |
| Check Calendar Availability | `googleCalendar` | calendar |
| Create Calendar Event | `googleCalendar` | Inspect parameters |
| Set Calendar Success Message | `set` | Inspect parameters |
| Respond with Success | `respondToWebhook` | Inspect parameters |
| Set Calendar Error Data | `set` | Inspect parameters |
| Respond With Calendar Error data | `respondToWebhook` | Inspect parameters |
| Set Invalid Data Error | `set` | Inspect parameters |
| Respond with Generic Error | `respondToWebhook` | Inspect parameters |

## Connection map

- Create Ticket → Check if submitted succesfully (`main`, output 0, input 0)
- Gcal Endpoint → Extract Gcal Data (`main`, output 0, input 0)
- Set Error Data → Respond to Webhook with Error (`main`, output 0, input 0)
- Zendesk Endpoint → Extract Zendesk Fields (`main`, output 0, input 0)
- Airtable Endpoint → Extract Airtable Data (`main`, output 0, input 0)
- Extract Gcal Data → Check for malformed date (`main`, output 0, input 0)
- Check if available → Create Calendar Event (`main`, output 0, input 0)
- Check if available → Set Calendar Error Data (`main`, output 1, input 0)
- Voiceflow Endpoint → Extract Phone Number (`main`, output 0, input 0)
- Check if user found → Respond to Webhook with Customer Data (`main`, output 0, input 0)
- Check if user found → Set Error Data (`main`, output 1, input 0)
- Extract Phone Number → Query Google Sheets for Phone (`main`, output 0, input 0)
- Create Calendar Event → Set Calendar Success Message (`main`, output 0, input 0)
- Create Customer in DB → Create Ticket (`main`, output 0, input 0)
- Extract Airtable Data → Create Airtable Data (`main`, output 0, input 0)
- Extract Zendesk Fields → Create Customer in DB (`main`, output 0, input 0)
- Set Invalid Data Error → Respond with Generic Error (`main`, output 0, input 0)
- Set Calendar Error Data → Respond With Calendar Error data (`main`, output 0, input 0)
- Check for malformed date → Check Calendar Availability (`main`, output 0, input 0)
- Check for malformed date → Set Invalid Data Error (`main`, output 1, input 0)
- Check Calendar Availability → Check if available (`main`, output 0, input 0)
- Set Calendar Success Message → Respond with Success (`main`, output 0, input 0)
- Query Google Sheets for Phone → Check if user found (`main`, output 0, input 0)
- Check if submitted succesfully → Ticket Created Successfully (`main`, output 0, input 0)
- Check if submitted succesfully → Error Creating Ticket (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0702_Webhook_GoogleCalendar_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0702_Webhook_GoogleCalendar_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
