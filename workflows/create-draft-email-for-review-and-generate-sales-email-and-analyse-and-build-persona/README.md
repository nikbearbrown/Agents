# create draft email for review and generate sales email and analyse and build persona

This folder contains the **create draft email for review and generate sales email and analyse and build persona** workflow. Its executable nodes use `gmail`, `hubspot`, `informationExtractor`, `lmChatGoogleGemini`, `manualTrigger`, `noOp`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-draft-email-for-review-and-generate-sales-email-and-analyse-and-build-persona.json`](create-draft-email-for-review-and-generate-sales-email-and-analyse-and-build-persona.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `hubspotAppToken`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Variables | `set` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Create Draft Email For Review | `gmail` | draft |
| Generate Sales Email | `informationExtractor` | Inspect parameters |
| Analyse and Build Persona | `informationExtractor` | Inspect parameters |
| Get All Customer's Correspondence | `gmail` | getAll |
| Get Contacts | `hubspot` | search |
| For Each Contact | `splitInBatches` | Inspect parameters |
| Contact Ref | `noOp` | Inspect parameters |

## Connection map

- Variables → Get All Customer's Correspondence (`main`, output 0, input 0)
- Contact Ref → Variables (`main`, output 0, input 0)
- Get Contacts → For Each Contact (`main`, output 0, input 0)
- For Each Contact → Contact Ref (`main`, output 1, input 0)
- Generate Sales Email → Create Draft Email For Review (`main`, output 0, input 0)
- Google Gemini Chat Model → Analyse and Build Persona (`ai_languageModel`, output 0, input 0)
- Analyse and Build Persona → Generate Sales Email (`main`, output 0, input 0)
- Google Gemini Chat Model1 → Generate Sales Email (`ai_languageModel`, output 0, input 0)
- Create Draft Email For Review → For Each Contact (`main`, output 0, input 0)
- Get All Customer's Correspondence → Analyse and Build Persona (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Contacts (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0821_Manual_Noop_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/0821_Manual_Noop_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
