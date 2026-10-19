# receive chat events and http request and respond to chat

This folder contains the **receive chat events and http request and respond to chat** workflow. Its executable nodes use `chat`, `chatTrigger`, `code`, `httpRequest`, `if`, `merge`, `set`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-chat-events-and-http-request-and-respond-to-chat.json`](receive-chat-events-and-http-request-and-respond-to-chat.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`

**Entry nodes:** When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| Create Thread | `httpRequest` | POST |
| Start Run | `httpRequest` | POST |
| Poll State | `set` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Get run | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| Get Message | `httpRequest` | Inspect parameters |
| Set response | `set` | Inspect parameters |
| If1 | `if` | Inspect parameters |
| Merge Thread ID | `set` | Inspect parameters |
| Merge Thread ID1 | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Respond to Chat | `chat` | Inspect parameters |
| Create payload | `set` | Inspect parameters |
| Simple Thread Storage | `code` | Inspect parameters |
| Simple Thread Storage 2 | `code` | Inspect parameters |
| Set thread id | `set` | Inspect parameters |

## Connection map

- When chat message received → Create payload (`main`, output 0, input 0)
- Create Thread → Simple Thread Storage 2 (`main`, output 0, input 0)
- Start Run → Poll State (`main`, output 0, input 0)
- Poll State → Wait (`main`, output 0, input 0)
- Wait → Get run (`main`, output 0, input 0)
- Get run → If (`main`, output 0, input 0)
- If → Get Message (`main`, output 0, input 0)
- If → Wait (`main`, output 1, input 0)
- Get Message → Set response (`main`, output 0, input 0)
- Set response → Respond to Chat (`main`, output 0, input 0)
- If1 → Merge Thread ID (`main`, output 0, input 0)
- If1 → Create Thread (`main`, output 1, input 0)
- Merge Thread ID → Merge (`main`, output 0, input 0)
- Merge Thread ID1 → Merge (`main`, output 0, input 0)
- Merge → Set thread id (`main`, output 0, input 0)
- Create payload → Simple Thread Storage (`main`, output 0, input 0)
- Simple Thread Storage → If1 (`main`, output 0, input 0)
- Simple Thread Storage 2 → Merge Thread ID1 (`main`, output 0, input 0)
- Set thread id → Start Run (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/blackbaddl13/r-KSODI-POC/blob/cbbe896ee41d933b114ddb8886c5a23d9b1bca89/n8n.json](https://github.com/blackbaddl13/r-KSODI-POC/blob/cbbe896ee41d933b114ddb8886c5a23d9b1bca89/n8n.json). License: **MIT**; preserve [the notice](../../licenses/blackbaddl13--r-KSODI-POC.txt) and embedded attribution. Source intake metadata plus license retrieved at its recorded source commit.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
