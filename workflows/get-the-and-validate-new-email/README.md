# Get the and Validate  New Email

This folder contains the **Get the and Validate  New Email** workflow. Its executable nodes use `emailSend`, `gmail`, `gmailTrigger`, `if`, `lmChatGoogleGemini`, `sendInBlue`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-the-and-validate-new-email.json`](get-the-and-validate-new-email.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `sendInBlueApi`, `smtp`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Text Classifier | `textClassifier` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| GuestPost Inquiry | `emailSend` | Inspect parameters |
| Youtube Video Inquiry | `emailSend` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Mark as Read | `gmail` | markAsRead |
| Apply Label | `gmail` | addLabels |
| Create Contact in Brevo | `sendInBlue` | contact / upsert |
| Emails from Existing Contracts | `if` | Inspect parameters |
| Reply | `if` | Inspect parameters |

## Connection map

- Reply → Text Classifier (`main`, output 0, input 0)
- Send Email → Mark as Read (`main`, output 0, input 0)
- Mark as Read → Apply Label (`main`, output 0, input 0)
- Mark as Read → Create Contact in Brevo (`main`, output 0, input 0)
- Gmail Trigger → Emails from Existing Contracts (`main`, output 0, input 0)
- Text Classifier → GuestPost Inquiry (`main`, output 0, input 0)
- Text Classifier → Youtube Video Inquiry (`main`, output 1, input 0)
- Text Classifier → Send Email (`main`, output 2, input 0)
- GuestPost Inquiry → Mark as Read (`main`, output 0, input 0)
- Youtube Video Inquiry → Mark as Read (`main`, output 0, input 0)
- Google Gemini Chat Model → Text Classifier (`ai_languageModel`, output 0, input 0)
- Emails from Existing Contracts → Reply (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0796_Stickynote_Gmail_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0796_Stickynote_Gmail_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
