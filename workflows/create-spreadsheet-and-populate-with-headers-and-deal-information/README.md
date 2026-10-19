# Create spreadsheet and populate with headers and deal information

This folder contains the **Create spreadsheet and populate with headers and deal information** workflow. Its executable nodes use `code`, `crypto`, `gmail`, `gmailTrigger`, `googleSheets`, `html`, `if`, `noOp`, `openAi`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-spreadsheet-and-populate-with-headers-and-deal-information.json`](create-spreadsheet-and-populate-with-headers-and-deal-information.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** On email received, On feedback given

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Generate reply | `openAi` | Inspect parameters |
| On email received | `gmailTrigger` | Inspect parameters |
| Only continue for specific emails | `if` | Inspect parameters |
| Configure | `set` | Inspect parameters |
| Send reply to recipient | `gmail` | reply |
| Generate UUID | `crypto` | Inspect parameters |
| Thanks for your response! | `html` | Inspect parameters |
| Extract message content (advanced) | `code` | Inspect parameters |
| If spreadsheet doesn't exist | `if` | Inspect parameters |
| Successfully created or updated row | `noOp` | Inspect parameters |
| Create spreadsheet | `googleSheets` | spreadsheet |
| Store spreadsheet ID | `code` | Inspect parameters |
| Paste data | `googleSheets` | append |
| If no sheet IDs | `if` | Inspect parameters |
| Create or update rows | `googleSheets` | appendOrUpdate |
| Get data from `Format data` | `code` | Inspect parameters |
| Get data from `Format data` node | `code` | Inspect parameters |
| Format data | `set` | Inspect parameters |
| Send email reply | `noOp` | Inspect parameters |
| On feedback given | `webhook` | Inspect parameters |
| Send feedback for fine-tuned data | `googleSheets` | update |
| Show HTML page | `respondToWebhook` | Inspect parameters |
| Get sheet IDs #1 | `code` | Inspect parameters |
| If no spreadsheet in configuration #2 | `if` | Inspect parameters |
| Store specific sheet IDs #2 | `code` | Inspect parameters |
| Get sheet IDs #2 | `code` | Inspect parameters |
| If no spreadsheet in configuration #1 | `if` | Inspect parameters |
| Store specific sheet IDs #1 | `code` | Inspect parameters |
| Email template | `html` | Inspect parameters |
| Record feedback | `noOp` | Inspect parameters |
| Fallback route | `noOp` | Inspect parameters |
| Identify trigger #2 | `set` | Inspect parameters |
| Identify trigger #1 | `set` | Inspect parameters |
| Do not send unfinished email reply | `noOp` | Inspect parameters |
| If reply is complete | `if` | Inspect parameters |
| Do not send email to this recipient | `noOp` | Inspect parameters |
| Send reply to database | `noOp` | Inspect parameters |
| Determine which trigger ran | `switch` | Inspect parameters |
| Is text within token limit? | `if` | Inspect parameters |
| Do nothing | `noOp` | Inspect parameters |

## Connection map

- Configure → Determine which trigger ran (`main`, output 0, input 0)
- Format data → If no spreadsheet in configuration #1 (`main`, output 0, input 0)
- Generate UUID → Extract message content (advanced) (`main`, output 0, input 0)
- Email template → Send reply to recipient (`main`, output 0, input 0)
- Generate reply → Send reply to database (`main`, output 0, input 0)
- Generate reply → If reply is complete (`main`, output 0, input 0)
- Show HTML page → If no spreadsheet in configuration #2 (`main`, output 0, input 0)
- If no sheet IDs → Create spreadsheet (`main`, output 0, input 0)
- If no sheet IDs → Get data from `Format data` (`main`, output 1, input 0)
- Record feedback → Thanks for your response! (`main`, output 0, input 0)
- Get sheet IDs #1 → If no sheet IDs (`main`, output 0, input 0)
- Get sheet IDs #2 → Send feedback for fine-tuned data (`main`, output 0, input 0)
- Send email reply → Email template (`main`, output 0, input 0)
- On email received → Identify trigger #1 (`main`, output 0, input 0)
- On feedback given → Identify trigger #2 (`main`, output 0, input 0)
- Create spreadsheet → Store spreadsheet ID (`main`, output 0, input 0)
- Identify trigger #1 → Configure (`main`, output 0, input 0)
- Identify trigger #2 → Configure (`main`, output 0, input 0)
- If reply is complete → Send email reply (`main`, output 0, input 0)
- If reply is complete → Do not send unfinished email reply (`main`, output 1, input 0)
- Store spreadsheet ID → Get data from `Format data` node (`main`, output 0, input 0)
- Create or update rows → If spreadsheet doesn't exist (`main`, output 0, input 0)
- Send reply to database → Format data (`main`, output 0, input 0)
- Thanks for your response! → Show HTML page (`main`, output 0, input 0)
- Determine which trigger ran → Only continue for specific emails (`main`, output 0, input 0)
- Determine which trigger ran → Record feedback (`main`, output 1, input 0)
- Determine which trigger ran → Fallback route (`main`, output 3, input 0)
- Get data from `Format data` → Create or update rows (`main`, output 0, input 0)
- Is text within token limit? → Generate reply (`main`, output 0, input 0)
- Is text within token limit? → Do nothing (`main`, output 1, input 0)
- Store specific sheet IDs #1 → If no sheet IDs (`main`, output 0, input 0)
- Store specific sheet IDs #2 → Send feedback for fine-tuned data (`main`, output 0, input 0)
- If spreadsheet doesn't exist → Create spreadsheet (`main`, output 0, input 0)
- If spreadsheet doesn't exist → Successfully created or updated row (`main`, output 1, input 0)
- Get data from `Format data` node → Paste data (`main`, output 0, input 0)
- Only continue for specific emails → Generate UUID (`main`, output 0, input 0)
- Only continue for specific emails → Do not send email to this recipient (`main`, output 1, input 0)
- Extract message content (advanced) → Is text within token limit? (`main`, output 0, input 0)
- If no spreadsheet in configuration #1 → Get sheet IDs #1 (`main`, output 0, input 0)
- If no spreadsheet in configuration #1 → Store specific sheet IDs #1 (`main`, output 1, input 0)
- If no spreadsheet in configuration #2 → Get sheet IDs #2 (`main`, output 0, input 0)
- If no spreadsheet in configuration #2 → Store specific sheet IDs #2 (`main`, output 1, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1653_Code_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1653_Code_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
