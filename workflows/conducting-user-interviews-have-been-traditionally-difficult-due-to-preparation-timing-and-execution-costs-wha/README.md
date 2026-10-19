# Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?

This folder contains the **Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?** workflow. Its executable nodes use `agent`, `crypto`, `form`, `formTrigger`, `googleSheets`, `html`, `if`, `lmChatGroq`, `memoryBufferWindow`, `memoryManager`, `redis`, `respondToWebhook`, `set`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`conducting-user-interviews-have-been-traditionally-difficult-due-to-preparation-timing-and-execution-costs-wha.json`](conducting-user-interviews-have-been-traditionally-difficult-due-to-preparation-timing-and-execution-costs-wha.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `groqApi`, `redis`

**Entry nodes:** Start Interview, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Stop Interview? | `if` | Inspect parameters |
| Generate Row | `set` | Inspect parameters |
| Generate Row1 | `set` | Inspect parameters |
| Clear For Next Interview | `memoryManager` | Inspect parameters |
| Send Reply To Agent | `set` | Inspect parameters |
| Start Interview | `formTrigger` | Inspect parameters |
| Get Answer | `form` | Inspect parameters |
| Set Interview Topic | `set` | Inspect parameters |
| UUID | `crypto` | Inspect parameters |
| Generate Row2 | `set` | Inspect parameters |
| Create Session | `redis` | set |
| Update Session | `redis` | push |
| Update Session1 | `redis` | push |
| Update Session2 | `redis` | push |
| Valid Session? | `if` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Window Buffer Memory2 | `memoryBufferWindow` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Redirect to Completion Screen | `form` | completion |
| Webhook | `webhook` | Inspect parameters |
| 404 Not Found | `html` | Inspect parameters |
| AI Researcher | `agent` | Inspect parameters |
| Parse Response | `set` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Show Transcript | `html` | Inspect parameters |
| Save to Google Sheet | `googleSheets` | append |
| Session to List | `splitOut` | Inspect parameters |
| Messages To JSON | `set` | Inspect parameters |
| Query By Session | `redis` | get |
| Get Session | `redis` | get |

## Connection map

- UUID → Create Session (`main`, output 0, input 0)
- Webhook → Query By Session (`main`, output 0, input 0)
- Get Answer → Generate Row (`main`, output 0, input 0)
- Get Session → Session to List (`main`, output 0, input 0)
- Generate Row → Update Session1 (`main`, output 0, input 0)
- 404 Not Found → Respond to Webhook (`main`, output 0, input 0)
- AI Researcher → Parse Response (`main`, output 0, input 0)
- Generate Row1 → Update Session2 (`main`, output 0, input 0)
- Generate Row2 → Update Session (`main`, output 0, input 0)
- Create Session → Generate Row2 (`main`, output 0, input 0)
- Parse Response → Stop Interview? (`main`, output 0, input 0)
- Update Session → Set Interview Topic (`main`, output 0, input 0)
- Valid Session? → Show Transcript (`main`, output 0, input 0)
- Valid Session? → 404 Not Found (`main`, output 1, input 0)
- Groq Chat Model → AI Researcher (`ai_languageModel`, output 0, input 0)
- Session to List → Messages To JSON (`main`, output 0, input 0)
- Show Transcript → Respond to Webhook (`main`, output 0, input 0)
- Start Interview → UUID (`main`, output 0, input 0)
- Stop Interview? → Generate Row1 (`main`, output 0, input 0)
- Stop Interview? → Get Answer (`main`, output 1, input 0)
- Update Session1 → Send Reply To Agent (`main`, output 0, input 0)
- Update Session2 → Clear For Next Interview (`main`, output 0, input 0)
- Messages To JSON → Save to Google Sheet (`main`, output 0, input 0)
- Query By Session → Valid Session? (`main`, output 0, input 0)
- Send Reply To Agent → AI Researcher (`main`, output 0, input 0)
- Set Interview Topic → AI Researcher (`main`, output 0, input 0)
- Window Buffer Memory → Clear For Next Interview (`ai_memory`, output 0, input 0)
- Window Buffer Memory2 → AI Researcher (`ai_memory`, output 0, input 0)
- Clear For Next Interview → Redirect to Completion Screen (`main`, output 0, input 0)
- Redirect to Completion Screen → Get Session (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0638_Splitout_Redis_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0638_Splitout_Redis_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
