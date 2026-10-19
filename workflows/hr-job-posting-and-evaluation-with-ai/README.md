# HR Job Posting and Evaluation with AI

This folder contains the **HR Job Posting and Evaluation with AI** workflow. Its executable nodes use `agent`, `airtable`, `airtableTool`, `emailSend`, `extractFromFile`, `form`, `formTrigger`, `googleCalendarTool`, `googleDrive`, `if`, `lmChatOpenAi`, `openAi`, `outputParserStructured`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hr-job-posting-and-evaluation-with-ai.json`](hr-job-posting-and-evaluation-with-ai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `googleCalendarOAuth2Api`, `googleDriveOAuth2Api`, `openAiApi`, `smtp`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Airtable | `airtable` | create |
| Upload CV to google drive | `googleDrive` | Inspect parameters |
| applicant details | `set` | Inspect parameters |
| download CV | `googleDrive` | download |
| Extract from File | `extractFromFile` | pdf |
| AI Agent | `agent` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Airtable1 | `airtableTool` | search |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| shortlisted? | `if` | Inspect parameters |
| Rejected | `airtable` | update |
| Potential Hire | `airtable` | update |
| Airtable2 | `airtableTool` | search |
| generate questionnaires | `openAi` | Inspect parameters |
| questionnaires | `form` | Inspect parameters |
| update questionnaires | `airtable` | update |
| job_posting | `airtableTool` | search |
| candidate_insights | `airtableTool` | Inspect parameters |
| Personalize email | `openAi` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Book Meeting | `openAi` | Inspect parameters |
| Google Calendar | `googleCalendarTool` | Inspect parameters |
| update phone meeting time | `airtable` | update |
| Screening Questions | `openAi` | Inspect parameters |
| job_posting1 | `airtableTool` | search |
| candidate_insights1 | `airtableTool` | Inspect parameters |
| screening questions | `airtable` | update |
| Edit Fields1 | `set` | Inspect parameters |

## Connection map

- AI Agent → shortlisted? (`main`, output 0, input 0)
- Airtable → download CV (`main`, output 0, input 0)
- Airtable1 → AI Agent (`ai_tool`, output 0, input 0)
- Airtable2 → generate questionnaires (`ai_tool`, output 0, input 0)
- Send Email → Book Meeting (`main`, output 0, input 0)
- Edit Fields → Send Email (`main`, output 0, input 0)
- download CV → Extract from File (`main`, output 0, input 0)
- job_posting → Personalize email (`ai_tool`, output 0, input 0)
- Book Meeting → update phone meeting time (`main`, output 0, input 0)
- Edit Fields1 → screening questions (`main`, output 0, input 0)
- job_posting1 → Screening Questions (`ai_tool`, output 0, input 0)
- shortlisted? → Potential Hire (`main`, output 0, input 0)
- shortlisted? → Rejected (`main`, output 1, input 0)
- Potential Hire → generate questionnaires (`main`, output 0, input 0)
- questionnaires → update questionnaires (`main`, output 0, input 0)
- Google Calendar → Book Meeting (`ai_tool`, output 0, input 0)
- Extract from File → AI Agent (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Personalize email → Edit Fields (`main`, output 0, input 0)
- applicant details → Airtable (`main`, output 0, input 0)
- On form submission → Upload CV to google drive (`main`, output 0, input 0)
- candidate_insights → Personalize email (`ai_tool`, output 0, input 0)
- Screening Questions → Edit Fields1 (`main`, output 0, input 0)
- candidate_insights1 → Screening Questions (`ai_tool`, output 0, input 0)
- update questionnaires → Personalize email (`main`, output 0, input 0)
- generate questionnaires → questionnaires (`main`, output 0, input 0)
- Structured Output Parser → AI Agent (`ai_outputParser`, output 0, input 0)
- Upload CV to google drive → applicant details (`main`, output 0, input 0)
- update phone meeting time → Screening Questions (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1847_Extractfromfile_Form_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Extractfromfile/1847_Extractfromfile_Form_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
