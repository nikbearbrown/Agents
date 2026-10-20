# Prepare data in Google Sheets

This folder contains the **Prepare data in Google Sheets** workflow. Its executable nodes use `aggregate`, `chainLlm`, `executeWorkflow`, `executeWorkflowTrigger`, `googleDrive`, `googleSheets`, `httpRequest`, `if`, `lmChatOpenAi`, `manualTrigger`, `set`, `splitInBatches`, `splitOut`, `strapi`, `switch`, `webflow`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`prepare-data-in-google-sheets.json`](prepare-data-in-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Format QA Pair1 | `set` | Inspect parameters |
| For Each Question...1 | `splitInBatches` | Inspect parameters |
| Question to List1 | `splitOut` | Inspect parameters |
| Questions to Object...1 | `aggregate` | Inspect parameters |
| Format DisplayName + Questions1 | `set` | Inspect parameters |
| Create From Text | `googleDrive` | createFromText |
| Define Sheets | `set` | Inspect parameters |
| Sheets To List... | `splitOut` | Inspect parameters |
| Get Services | `googleSheets` | Inspect parameters |
| Single Integration Cred-only | `set` | Inspect parameters |
| Single Integration Native | `set` | Inspect parameters |
| Categories | `set` | Inspect parameters |
| For Each Sheet... | `splitInBatches` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Prepare Job | `set` | Inspect parameters |
| For Each Service... | `splitInBatches` | Inspect parameters |
| Update Row Status | `googleSheets` | update |
| Single Integration Non-native | `set` | Inspect parameters |
| If has Data | `if` | Inspect parameters |
| Needs AI Completion?1 | `switch` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Strapi | `strapi` | create |
| Wordpress | `wordpress` | Inspect parameters |
| Webflow | `webflow` | create |
| HTTP Request | `httpRequest` | Inspect parameters |
| AI Completion1 | `chainLlm` | Inspect parameters |

## Connection map

- Switch → Single Integration Native (`main`, output 0, input 0)
- Switch → Single Integration Cred-only (`main`, output 1, input 0)
- Switch → Single Integration Non-native (`main`, output 2, input 0)
- Switch → Categories (`main`, output 3, input 0)
- Categories → Question to List1 (`main`, output 0, input 0)
- If has Data → Execute Workflow (`main`, output 0, input 0)
- If has Data → For Each Service... (`main`, output 1, input 0)
- Prepare Job → For Each Sheet... (`main`, output 0, input 0)
- Get Services → Prepare Job (`main`, output 0, input 0)
- Define Sheets → Sheets To List... (`main`, output 0, input 0)
- AI Completion1 → Format QA Pair1 (`main`, output 0, input 0)
- Format QA Pair1 → For Each Question...1 (`main`, output 0, input 0)
- Create From Text → Update Row Status (`main`, output 0, input 0)
- Execute Workflow → For Each Service... (`main`, output 0, input 0)
- For Each Sheet... → For Each Service... (`main`, output 0, input 0)
- For Each Sheet... → Get Services (`main`, output 1, input 0)
- OpenAI Chat Model → AI Completion1 (`ai_languageModel`, output 0, input 0)
- Question to List1 → For Each Question...1 (`main`, output 0, input 0)
- Sheets To List... → For Each Sheet... (`main`, output 0, input 0)
- Update Row Status → Strapi (`main`, output 0, input 0)
- For Each Service... → If has Data (`main`, output 1, input 0)
- For Each Question...1 → Questions to Object...1 (`main`, output 0, input 0)
- For Each Question...1 → Needs AI Completion?1 (`main`, output 1, input 0)
- Needs AI Completion?1 → Format QA Pair1 (`main`, output 0, input 0)
- Needs AI Completion?1 → AI Completion1 (`main`, output 1, input 0)
- Questions to Object...1 → Format DisplayName + Questions1 (`main`, output 0, input 0)
- Execute Workflow Trigger → Switch (`main`, output 0, input 0)
- Single Integration Native → Question to List1 (`main`, output 0, input 0)
- Single Integration Cred-only → Question to List1 (`main`, output 0, input 0)
- Single Integration Non-native → Question to List1 (`main`, output 0, input 0)
- Format DisplayName + Questions1 → Create From Text (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Define Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Strapi/0584_Strapi_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Strapi/0584_Strapi_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
