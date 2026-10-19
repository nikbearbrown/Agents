# Calling a Sub-workflow

This folder contains the **Calling a Sub-workflow** workflow. Its executable nodes use `code`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `gmail`, `googleSheets`, `httpRequest`, `if`, `manualTrigger`, `merge`, `noOp`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`calling-a-sub-workflow.json`](calling-a-sub-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `httpHeaderAuth`, `hubspotOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get list of owners | `httpRequest` | Inspect parameters |
| Get list of clients for owner | `httpRequest` | POST |
| If | `if` | Inspect parameters |
| Edit | `set` | Inspect parameters |
| Increment Page | `set` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Merge al the entries | `code` | Inspect parameters |
| If linkedin url is empty | `if` | Inspect parameters |
| if new post | `if` | Inspect parameters |
| Get list of clients | `executeWorkflow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Get last post | `executeWorkflow` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Search for user by link | `httpRequest` | Inspect parameters |
| Do nothing | `noOp` | Inspect parameters |
| Merge profileURL | `code` | Inspect parameters |
| Set last_post | `set` | Inspect parameters |
| Set last_position | `set` | Inspect parameters |
| if new position | `if` | Inspect parameters |
| Set data here | `set` | Inspect parameters |
| Change this for testing | `filter` | Inspect parameters |
| Create entry with email | `googleSheets` | appendOrUpdate |
| Get rows from document | `googleSheets` | Inspect parameters |
| Search for user profile by names | `httpRequest` | Inspect parameters |
| Profile URL not found? | `if` | Inspect parameters |
| Set the profile URL | `set` | Inspect parameters |
| Set the profile URL1 | `set` | Inspect parameters |
| Update last post | `googleSheets` | appendOrUpdate |
| Updates last position | `googleSheets` | appendOrUpdate |
| Set post_updated | `set` | Inspect parameters |
| Set position_updated | `set` | Inspect parameters |
| Generate the email text | `code` | Inspect parameters |
| Merge on email | `merge` | Inspect parameters |
| Split Out owners | `splitOut` | Inspect parameters |
| Get current owner | `filter` | Inspect parameters |

## Connection map

- If → Merge al the entries (`main`, output 0, input 0)
- If → Get list of clients for owner (`main`, output 1, input 0)
- Edit → Get list of clients for owner (`main`, output 0, input 0)
- if new post → Update last post (`main`, output 0, input 0)
- Get last post → Set last_post (`main`, output 0, input 0)
- Set data here → Get list of owners (`main`, output 0, input 0)
- Set last_post → if new post (`main`, output 0, input 0)
- Increment Page → If (`main`, output 0, input 0)
- Merge on email → Generate the email text (`main`, output 0, input 0)
- if new position → Updates last position (`main`, output 0, input 0)
- Merge profileURL → Search for user by link (`main`, output 0, input 0)
- Set post_updated → Merge on email (`main`, output 0, input 0)
- Split Out owners → Get current owner (`main`, output 0, input 0)
- Update last post → Set post_updated (`main`, output 0, input 0)
- Get current owner → Get list of clients (`main`, output 0, input 0)
- Set last_position → if new position (`main`, output 0, input 0)
- Get list of owners → Split Out owners (`main`, output 0, input 0)
- Get list of clients → Change this for testing (`main`, output 0, input 0)
- Set the profile URL → Merge profileURL (`main`, output 0, input 0)
- Merge al the entries → Split Out1 (`main`, output 0, input 0)
- Set position_updated → Merge on email (`main`, output 0, input 1)
- Set the profile URL1 → Merge profileURL (`main`, output 0, input 0)
- Updates last position → Set position_updated (`main`, output 0, input 0)
- Get rows from document → If linkedin url is empty (`main`, output 0, input 0)
- Profile URL not found? → Do nothing (`main`, output 0, input 0)
- Profile URL not found? → Set the profile URL (`main`, output 1, input 0)
- Change this for testing → Create entry with email (`main`, output 0, input 0)
- Create entry with email → Get rows from document (`main`, output 0, input 0)
- Generate the email text → Gmail (`main`, output 0, input 0)
- Search for user by link → Get last post (`main`, output 0, input 0)
- Search for user by link → Set last_position (`main`, output 0, input 0)
- If linkedin url is empty → Search for user profile by names (`main`, output 0, input 0)
- If linkedin url is empty → Set the profile URL1 (`main`, output 1, input 0)
- Get list of clients for owner → Increment Page (`main`, output 0, input 0)
- Search for user profile by names → Profile URL not found? (`main`, output 0, input 0)
- When Executed by Another Workflow → Edit (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set data here (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0915_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0915_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
