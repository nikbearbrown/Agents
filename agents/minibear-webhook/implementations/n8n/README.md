# MiniBear Webhook

This folder contains the **MiniBear Webhook** workflow. Its executable nodes use `agent`, `httpRequest`, `if`, `lmChatOpenRouter`, `microsoftOneDrive`, `microsoftTeams`, `microsoftToDo`, `outputParserStructured`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`minibear-webhook.json`](minibear-webhook.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `microsoftOneDriveOAuth2Api`, `microsoftTeamsOAuth2Api`, `microsoftToDoOAuth2Api`, `openRouterApi`

**Entry nodes:** Line Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Line Webhook | `webhook` | Inspect parameters |
| Line Loading Animation | `httpRequest` | POST |
| Switch | `switch` | Inspect parameters |
| Get Image | `httpRequest` | Inspect parameters |
| Line Reply (image) | `httpRequest` | POST |
| Line Reply (Text) | `httpRequest` | POST |
| Line Reply (Not Supported 2) | `httpRequest` | POST |
| Line Reply (Not Supported 1) | `httpRequest` | POST |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Image Router | `agent` | Inspect parameters |
| Microsoft Teams | `microsoftTeams` | channelMessage |
| Microsoft To Do | `microsoftToDo` | create |
| Line Reply (Text)1 | `httpRequest` | POST |
| If namecard | `if` | Inspect parameters |
| Other Images | `agent` | Inspect parameters |
| Microsoft Teams1 | `microsoftTeams` | channelMessage |
| OpenRouter Chat Model2 | `lmChatOpenRouter` | Inspect parameters |
| Microsoft OneDrive | `microsoftOneDrive` | Inspect parameters |
| Microsoft OneDrive1 | `microsoftOneDrive` | rename |
| Get Image2 | `httpRequest` | Inspect parameters |
| Microsoft To Do1 | `microsoftToDo` | create |
| HTTP Request | `httpRequest` | POST |
| OpenRouter Chat Model3 | `lmChatOpenRouter` | Inspect parameters |
| NamecardExtract | `agent` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Line Reply Namecard | `httpRequest` | POST |
| Get Image3 | `httpRequest` | Inspect parameters |

## Connection map

- Switch → Microsoft To Do (`main`, output 0, input 0)
- Switch → Microsoft Teams (`main`, output 1, input 0)
- Switch → Get Image (`main`, output 2, input 0)
- Switch → Line Reply (Not Supported 1) (`main`, output 3, input 0)
- Switch → Line Reply (Not Supported 2) (`main`, output 4, input 0)
- Get Image → Image Router (`main`, output 0, input 0)
- Get Image2 → Other Images (`main`, output 0, input 0)
- Get Image3 → NamecardExtract (`main`, output 0, input 0)
- If namecard → Get Image3 (`main`, output 0, input 0)
- If namecard → Microsoft OneDrive (`main`, output 1, input 0)
- Image Router → If namecard (`main`, output 0, input 0)
- Line Webhook → Line Loading Animation (`main`, output 0, input 0)
- Other Images → Microsoft Teams1 (`main`, output 0, input 0)
- Microsoft Teams → Line Reply (Text) (`main`, output 0, input 0)
- Microsoft To Do → Line Reply (Text)1 (`main`, output 0, input 0)
- NamecardExtract → Microsoft To Do1 (`main`, output 0, input 0)
- Microsoft Teams1 → Line Reply (image) (`main`, output 0, input 0)
- Microsoft To Do1 → Line Reply Namecard (`main`, output 0, input 0)
- Microsoft OneDrive → Microsoft OneDrive1 (`main`, output 0, input 0)
- Line Reply Namecard → HTTP Request (`main`, output 0, input 0)
- Microsoft OneDrive1 → Get Image2 (`main`, output 0, input 0)
- OpenRouter Chat Model → Image Router (`ai_languageModel`, output 0, input 0)
- Line Loading Animation → Switch (`main`, output 0, input 0)
- OpenRouter Chat Model2 → Other Images (`ai_languageModel`, output 0, input 0)
- OpenRouter Chat Model3 → NamecardExtract (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → NamecardExtract (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsofttodo/1494_Microsofttodo_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsofttodo/1494_Microsofttodo_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
