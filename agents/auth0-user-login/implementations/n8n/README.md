# Auth0 User Login

This folder contains the **Auth0 User Login** workflow. Its executable nodes use `httpRequest`, `if`, `respondToWebhook`, `set`, `stopAndError`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`auth0-user-login.json`](auth0-user-login.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** /login, /receive-token

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Request Access Token | `httpRequest` | POST |
| Get Userinfo | `httpRequest` | Inspect parameters |
| If | `if` | Inspect parameters |
| No Code Found | `stopAndError` | Inspect parameters |
| Open Auth Webpage | `respondToWebhook` | Inspect parameters |
| Set Application Details | `set` | Inspect parameters |
| Set Application Details1 | `set` | Inspect parameters |
| /login | `webhook` | Inspect parameters |
| /receive-token | `webhook` | Inspect parameters |

## Connection map

- If → Set Application Details1 (`main`, output 0, input 0)
- If → No Code Found (`main`, output 1, input 0)
- /login → Set Application Details (`main`, output 0, input 0)
- /receive-token → If (`main`, output 0, input 0)
- Request Access Token → Get Userinfo (`main`, output 0, input 0)
- Set Application Details → Open Auth Webpage (`main`, output 0, input 0)
- Set Application Details1 → Request Access Token (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1295_Stopanderror_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1295_Stopanderror_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
