# Set receiving email account

This folder contains the **Set receiving email account** workflow. Its executable nodes use `chainLlm`, `emailReadImap`, `hubspot`, `if`, `lmChatOpenAi`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`set-receiving-email-account.json`](set-receiving-email-account.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`, `imap`, `openAiApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Creates an email engagement | `hubspot` | engagement |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Search for the contact via email | `hubspot` | search |
| Parse the mail with AI | `chainLlm` | Inspect parameters |
| When an email is received | `emailReadImap` | Inspect parameters |
| Set the output Json | `outputParserStructured` | Inspect parameters |
| contact exists? | `if` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Creates contact | `hubspot` | Inspect parameters |

## Connection map

- Edit Fields → Creates an email engagement (`main`, output 0, input 0)
- Creates contact → Creates an email engagement (`main`, output 0, input 0)
- contact exists? → Edit Fields (`main`, output 0, input 0)
- contact exists? → Creates contact (`main`, output 1, input 0)
- OpenAI Chat Model → Parse the mail with AI (`ai_languageModel`, output 0, input 0)
- Set the output Json → Parse the mail with AI (`ai_outputParser`, output 0, input 0)
- Parse the mail with AI → Search for the contact via email (`main`, output 0, input 0)
- When an email is received → Parse the mail with AI (`main`, output 0, input 0)
- Search for the contact via email → contact exists? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0893_Stickynote_Emailreadimap_Create.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stickynote/0893_Stickynote_Emailreadimap_Create.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
