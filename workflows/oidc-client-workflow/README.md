# OIDC client workflow

This folder contains the **OIDC client workflow** workflow. Its executable nodes use `code`, `html`, `httpRequest`, `if`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`oidc-client-workflow.json`](oidc-client-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Code | `code` | Inspect parameters |
| user info | `httpRequest` | Inspect parameters |
| send back login page | `respondToWebhook` | Inspect parameters |
| IF token is present | `if` | Inspect parameters |
| Welcome page | `html` | Inspect parameters |
| send back welcome page | `respondToWebhook` | Inspect parameters |
| IF user info ok | `if` | Inspect parameters |
| login form | `html` | Inspect parameters |
| Set variables : auth, token, userinfo, client id, scope | `set` | Inspect parameters |
| IF we have code in URI and not in PKCE mode | `if` | Inspect parameters |
| get access_token from /token endpoint with code | `httpRequest` | POST |

## Connection map

- Code → IF we have code in URI and not in PKCE mode (`main`, output 0, input 0)
- Webhook → Set variables : auth, token, userinfo, client id, scope (`main`, output 0, input 0)
- user info → IF user info ok (`main`, output 0, input 0)
- login form → send back login page (`main`, output 0, input 0)
- Welcome page → send back welcome page (`main`, output 0, input 0)
- IF user info ok → Welcome page (`main`, output 0, input 0)
- IF user info ok → login form (`main`, output 1, input 0)
- IF token is present → user info (`main`, output 0, input 0)
- IF token is present → login form (`main`, output 1, input 0)
- IF we have code in URI and not in PKCE mode → get access_token from /token endpoint with code (`main`, output 0, input 0)
- IF we have code in URI and not in PKCE mode → IF token is present (`main`, output 1, input 0)
- get access_token from /token endpoint with code → user info (`main`, output 0, input 0)
- Set variables : auth, token, userinfo, client id, scope → Code (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2034_Code_Webhook_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/2034_Code_Webhook_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
