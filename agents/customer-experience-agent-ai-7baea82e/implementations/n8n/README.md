# Customer Experience Agent (AI)

This folder contains the **Customer Experience Agent (AI)** workflow. Its executable nodes use `agent`, `code`, `emailSend`, `gmail`, `lmChatGoogleGemini`, `stravaTrigger`, `whatsApp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`customer-experience-agent-ai-7baea82e.json`](customer-experience-agent-ai-7baea82e.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `smtp`, `stravaOAuth2Api`, `whatsAppApi`

**Entry nodes:** Strava Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Strava Trigger | `stravaTrigger` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Combine Everything | `code` | Inspect parameters |
| Fitness Coach | `agent` | Inspect parameters |
| Structure Output | `code` | Inspect parameters |
| Conver to HTML | `code` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Code | `code` | Inspect parameters |
| WhatsApp Business Cloud | `whatsApp` | send |

## Connection map

- Code → Combine Everything (`main`, output 0, input 0)
- Fitness Coach → Structure Output (`main`, output 0, input 0)
- Conver to HTML → Send Email (`main`, output 0, input 0)
- Strava Trigger → Code (`main`, output 0, input 0)
- Structure Output → Conver to HTML (`main`, output 0, input 0)
- Combine Everything → Fitness Coach (`main`, output 0, input 0)
- Google Gemini Chat Model → Fitness Coach (`ai_languageModel`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0701_Code_Strava_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0701_Code_Strava_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
