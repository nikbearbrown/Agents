# Key Sections of n8n Workflow

This folder contains the **Key Sections of n8n Workflow** workflow. Its executable nodes use `agent`, `code`, `dateTime`, `filter`, `html`, `lmChatGoogleGemini`, `merge`, `microsoftOutlook`, `mySql`, `scheduleTrigger`, `set`, `splitInBatches`, `toolCalculator`, `toolThink`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`key-sections-of-n8n-workflow.json`](key-sections-of-n8n-workflow.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| YTD vs Prevoius Month1 | `mySql` | executeQuery |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| CostCentrs | `set` | Inspect parameters |
| Date & Time | `dateTime` | Inspect parameters |
| PreviousMonth | `code` | Inspect parameters |
| Selected Cost Center | `set` | Inspect parameters |
| Get Cost Centers with Budgets | `mySql` | executeQuery |
| Filter | `filter` | Inspect parameters |
| HTML | `html` | Inspect parameters |
| verticalPL | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Microsoft Outlook2 | `microsoftOutlook` | Inspect parameters |
| CostCenter | `code` | Inspect parameters |
| WIP1 | `code` | Inspect parameters |
| Employees | `mySql` | executeQuery |
| Employees1 | `code` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Financial Performance | `code` | Inspect parameters |
| Email Data | `set` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Business Performance AI Agent (Analyst) | `agent` | Inspect parameters |
| Think | `toolThink` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Departments  | `mySql` | executeQuery |
| Projects | `mySql` | executeQuery |

## Connection map

- Code → HTML (`main`, output 0, input 0)
- HTML → Business Performance AI Agent (Analyst) (`main`, output 0, input 0)
- WIP1 → Merge (`main`, output 0, input 2)
- Wait → Loop Over Items (`main`, output 0, input 0)
- Merge → Code (`main`, output 0, input 0)
- Think → Business Performance AI Agent (Analyst) (`ai_tool`, output 0, input 0)
- Filter → Loop Over Items (`main`, output 0, input 0)
- Projects → WIP1 (`main`, output 0, input 0)
- Employees → Employees1 (`main`, output 0, input 0)
- Calculator → Business Performance AI Agent (Analyst) (`ai_tool`, output 0, input 0)
- CostCenter → Merge (`main`, output 0, input 0)
- CostCentrs → Filter (`main`, output 0, input 0)
- Email Data → Microsoft Outlook2 (`main`, output 0, input 0)
- Employees1 → Merge (`main`, output 0, input 3)
- verticalPL → Merge (`main`, output 0, input 1)
- Date & Time → PreviousMonth (`main`, output 0, input 0)
- Departments  → verticalPL (`main`, output 0, input 0)
- PreviousMonth → Get Cost Centers with Budgets (`main`, output 0, input 0)
- Loop Over Items → Selected Cost Center (`main`, output 1, input 0)
- Schedule Trigger → Date & Time (`main`, output 0, input 0)
- Microsoft Outlook2 → Wait (`main`, output 0, input 0)
- Selected Cost Center → YTD vs Prevoius Month1 (`main`, output 0, input 0)
- Selected Cost Center → Departments  (`main`, output 0, input 0)
- Selected Cost Center → Projects (`main`, output 0, input 0)
- Selected Cost Center → Employees (`main`, output 0, input 0)
- Financial Performance → Email Data (`main`, output 0, input 0)
- YTD vs Prevoius Month1 → CostCenter (`main`, output 0, input 0)
- Google Gemini Chat Model → Business Performance AI Agent (Analyst) (`ai_languageModel`, output 0, input 0)
- Get Cost Centers with Budgets → CostCentrs (`main`, output 0, input 0)
- Business Performance AI Agent (Analyst) → Financial Performance (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0869_Wait_Datetime_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0869_Wait_Datetime_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
