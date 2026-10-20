# Send follow-up emails if appropriate

This folder contains the **Send follow-up emails if appropriate** workflow. Its executable nodes use `code`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `gmail`, `googleSheets`, `if`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-follow-up-emails-if-appropriate.json`](send-follow-up-emails-if-appropriate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`

**Entry nodes:** Execute Workflow Trigger, Every hour

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Update last contacted time | `googleSheets` | update |
| Set message template | `set` | Inspect parameters |
| Email sequence | `set` | Inspect parameters |
| Fill message placeholders | `code` | Inspect parameters |
| Compose message | `set` | Inspect parameters |
| Get previous message threads | `gmail` | thread |
| Get thread details | `gmail` | thread / get |
| Classify threads | `code` | Inspect parameters |
| Next message due? | `filter` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Replying? | `if` | Inspect parameters |
| Send new message | `gmail` | Inspect parameters |
| Call message send sub-workflow | `executeWorkflow` | Inspect parameters |
| Prepare reply params | `set` | Inspect parameters |
| Prepare first message params | `set` | Inspect parameters |
| Call message send sub-workflow1 | `executeWorkflow` | Inspect parameters |
| To email? | `filter` | Inspect parameters |
| Decode messages | `code` | Inspect parameters |
| Decode placeholder values | `code` | Inspect parameters |
| Package placeholder values | `code` | Inspect parameters |
| Settings | `set` | Inspect parameters |
| Reply to message | `gmail` | reply |
| Get emails | `googleSheets` | Inspect parameters |
| Every hour | `scheduleTrigger` | Inspect parameters |
| Don't email on weekends | `filter` | Inspect parameters |

## Connection map

- Settings → Email sequence (`main`, output 0, input 0)
- Replying? → Reply to message (`main`, output 0, input 0)
- Replying? → Send new message (`main`, output 1, input 0)
- To email? → Prepare first message params (`main`, output 0, input 0)
- Every hour → Don't email on weekends (`main`, output 0, input 0)
- Get emails → To email? (`main`, output 0, input 0)
- Email sequence → Get previous message threads (`main`, output 0, input 0)
- Email sequence → Get emails (`main`, output 0, input 0)
- Compose message → Replying? (`main`, output 0, input 0)
- Decode messages → Classify threads (`main`, output 0, input 0)
- Classify threads → Next message due? (`main`, output 0, input 0)
- Next message due? → Prepare reply params (`main`, output 0, input 0)
- Get thread details → Decode messages (`main`, output 0, input 0)
- Prepare reply params → Decode placeholder values (`main`, output 0, input 0)
- Set message template → Fill message placeholders (`main`, output 0, input 0)
- Don't email on weekends → Settings (`main`, output 0, input 0)
- Execute Workflow Trigger → Set message template (`main`, output 0, input 0)
- Decode placeholder values → Call message send sub-workflow (`main`, output 0, input 0)
- Fill message placeholders → Compose message (`main`, output 0, input 0)
- Package placeholder values → Call message send sub-workflow1 (`main`, output 0, input 0)
- Get previous message threads → Get thread details (`main`, output 0, input 0)
- Prepare first message params → Package placeholder values (`main`, output 0, input 0)
- Call message send sub-workflow1 → Update last contacted time (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0437_Code_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0437_Code_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
