# xSend and check TTS (Text-to-speech) voice calls end email verification

This folder contains the **xSend and check TTS (Text-to-speech) voice calls end email verification** workflow. Its executable nodes use `code`, `emailSend`, `form`, `formTrigger`, `httpRequest`, `if`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`xsend-and-check-tts-text-to-speech-voice-calls-end-email-verification.json`](xsend-and-check-tts-text-to-speech-voice-calls-end-email-verification.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `smtp`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Send Voice | `httpRequest` | POST |
| On form submission | `formTrigger` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Code for voice | `code` | Inspect parameters |
| Set voice code | `set` | Inspect parameters |
| Verify voice code | `form` | Inspect parameters |
| Fail voice code | `form` | completion |
| Set email code | `set` | Inspect parameters |
| Verify email code | `form` | Inspect parameters |
| Is email code correct? | `if` | Inspect parameters |
| Is voice code correct? | `if` | Inspect parameters |
| Success | `form` | completion |
| Fail email code | `form` | completion |

## Connection map

- Send Email → Verify email code (`main`, output 0, input 0)
- Send Voice → Verify voice code (`main`, output 0, input 0)
- Code for voice → Send Voice (`main`, output 0, input 0)
- Set email code → Send Email (`main`, output 0, input 0)
- Set voice code → Code for voice (`main`, output 0, input 0)
- Verify email code → Is email code correct? (`main`, output 0, input 0)
- Verify voice code → Is voice code correct? (`main`, output 0, input 0)
- On form submission → Set voice code (`main`, output 0, input 0)
- Is email code correct? → Success (`main`, output 0, input 0)
- Is email code correct? → Fail email code (`main`, output 1, input 0)
- Is voice code correct? → Set email code (`main`, output 0, input 0)
- Is voice code correct? → Fail voice code (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0362_Code_HTTP_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0362_Code_HTTP_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
