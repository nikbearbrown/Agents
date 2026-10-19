# Get Apprropraite Data

This folder contains the **Get Apprropraite Data** workflow. Its executable nodes use `agent`, `code`, `erpNext`, `extractFromFile`, `httpRequest`, `if`, `lmChatGoogleGemini`, `merge`, `microsoftOutlook`, `set`, `switch`, `webhook`, `whatsApp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-apprropraite-data.json`](get-apprropraite-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `erpNextApi`, `googlePalmApi`, `microsoftOutlookOAuth2Api`, `whatsAppApi`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Code | `code` | Inspect parameters |
| ApplicantData | `set` | Inspect parameters |
| ERPNext - Reject if Resume not Attached | `erpNext` | update |
| Applied Against Job | `if` | Inspect parameters |
| ERPNext - Hold Applicant | `erpNext` | update |
| Get Job Opening | `erpNext` | get |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Convert to Fields | `code` | Inspect parameters |
| If score less than 80 | `if` | Inspect parameters |
| Reject Applicant | `httpRequest` | PUT |
| Update Applicant Data | `httpRequest` | PUT |
| Reume Attachment Link | `set` | Inspect parameters |
| Resume Link Provided | `if` | Inspect parameters |
| Accept Applicant | `httpRequest` | PUT |
| Webhook | `webhook` | Inspect parameters |
| File Type | `switch` | Inspect parameters |
| Download PDF Resume | `httpRequest` | Inspect parameters |
| PDF to Text | `extractFromFile` | pdf |
| Txt File to Text (Example) | `extractFromFile` | text |
| Merge1 | `merge` | Inspect parameters |
| Recruitment AI Agent | `agent` | Inspect parameters |
| Microsoft Outlook | `microsoftOutlook` | Inspect parameters |
| WhatsApp Business Cloud | `whatsApp` | send |

## Connection map

- Code → ApplicantData (`main`, output 0, input 0)
- Merge1 → Get Job Opening (`main`, output 0, input 0)
- Webhook → Code (`main`, output 0, input 0)
- File Type → Download PDF Resume (`main`, output 0, input 0)
- PDF to Text → Merge1 (`main`, output 0, input 0)
- ApplicantData → Resume Link Provided (`main`, output 0, input 0)
- Get Job Opening → Recruitment AI Agent (`main`, output 0, input 0)
- Accept Applicant → WhatsApp Business Cloud (`main`, output 0, input 0)
- Reject Applicant → Microsoft Outlook (`main`, output 0, input 0)
- Convert to Fields → Update Applicant Data (`main`, output 0, input 0)
- Applied Against Job → Reume Attachment Link (`main`, output 0, input 0)
- Applied Against Job → ERPNext - Hold Applicant (`main`, output 1, input 0)
- Download PDF Resume → PDF to Text (`main`, output 0, input 0)
- Recruitment AI Agent → Convert to Fields (`main`, output 0, input 0)
- Resume Link Provided → Applied Against Job (`main`, output 0, input 0)
- Resume Link Provided → ERPNext - Reject if Resume not Attached (`main`, output 1, input 0)
- If score less than 80 → Reject Applicant (`main`, output 0, input 0)
- If score less than 80 → Accept Applicant (`main`, output 1, input 0)
- Reume Attachment Link → File Type (`main`, output 0, input 0)
- Update Applicant Data → If score less than 80 (`main`, output 0, input 0)
- Google Gemini Chat Model → Recruitment AI Agent (`ai_languageModel`, output 0, input 0)
- Txt File to Text (Example) → Merge1 (`main`, output 0, input 1)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0692_Webhook_Code_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0692_Webhook_Code_Update_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
