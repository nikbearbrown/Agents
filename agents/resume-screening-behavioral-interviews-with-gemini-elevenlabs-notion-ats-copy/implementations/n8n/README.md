# Resume Screening & Behavioral Interviews with Gemini, Elevenlabs, & Notion ATS copy

This folder contains the **Resume Screening & Behavioral Interviews with Gemini, Elevenlabs, & Notion ATS copy** workflow. Its executable nodes use `agent`, `chainLlm`, `chainSummarization`, `extractFromFile`, `filter`, `formTrigger`, `googleDrive`, `googleSheets`, `httpRequest`, `informationExtractor`, `lmChatGoogleGemini`, `merge`, `notion`, `notionTool`, `outputParserStructured`, `set`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`resume-screening-behavioral-interviews-with-gemini-elevenlabs-notion-ats-copy.json`](resume-screening-behavioral-interviews-with-gemini-elevenlabs-notion-ats-copy.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `notionApi`

**Entry nodes:** ElevenLabs Web Hook, Application Form 1 of 3, Application Form 2 of 3, Application form 3 of 3

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Merge | `merge` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| HR Expert | `chainLlm` | Inspect parameters |
| Upload CV | `googleDrive` | Inspect parameters |
| Extract Resume | `extractFromFile` | pdf |
| Applicant Summary | `chainSummarization` | Inspect parameters |
| Job Description Summary | `chainLlm` | Inspect parameters |
| Applicant Qualifications | `informationExtractor` | Inspect parameters |
| Applicant Personal Data | `informationExtractor` | Inspect parameters |
| Application Data | `set` | Inspect parameters |
| ElevenLabs Web Hook | `webhook` | Inspect parameters |
| ai_convo_items | `set` | Inspect parameters |
| Extract_Audio | `httpRequest` | Inspect parameters |
| Filter_Notion_db | `filter` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Link Audio in Notion | `notion` | databasePage / update |
| Resume URL | `set` | Inspect parameters |
| Get Applicant Record | `notion` | databasePage / getAll |
| Embed Resume in Notion | `notion` | databasePage / update |
| Wait | `wait` | Inspect parameters |
| Application Form 1 of 3 | `formTrigger` | Inspect parameters |
| Application Form 2 of 3 | `formTrigger` | Inspect parameters |
| Application form 3 of 3 | `formTrigger` | Inspect parameters |
| Get Job Description | `notion` | databasePage / getAll |
| Job Description Mapping | `set` | Inspect parameters |
| Applicant Data Backup | `googleSheets` | append |
| Create Applicant Record | `notion` | databasePage |
| Upload Audio to Drive | `googleDrive` | Inspect parameters |
| Google Gemini | `lmChatGoogleGemini` | Inspect parameters |
| Evaluation Criteria | `notionTool` | databasePage / getAll |
| Applicant Record | `notion` | databasePage / getAll |
| Update_Applicant_Record | `notion` | databasePage / update |
| Google Gemini Model | `lmChatGoogleGemini` | Inspect parameters |

## Connection map

- Wait → Get Applicant Record (`main`, output 0, input 0)
- Merge → Applicant Summary (`main`, output 0, input 0)
- AI Agent → Applicant Record (`main`, output 0, input 0)
- HR Expert → Applicant Data Backup (`main`, output 0, input 0)
- Upload CV → Resume URL (`main`, output 0, input 0)
- Resume URL → Wait (`main`, output 0, input 0)
- Extract_Audio → Upload Audio to Drive (`main`, output 0, input 0)
- Google Gemini → Applicant Summary (`ai_languageModel`, output 0, input 0)
- Google Gemini → Applicant Qualifications (`ai_languageModel`, output 0, input 0)
- Google Gemini → HR Expert (`ai_languageModel`, output 0, input 0)
- Google Gemini → Applicant Personal Data (`ai_languageModel`, output 0, input 0)
- Google Gemini → Job Description Summary (`ai_languageModel`, output 0, input 0)
- Extract Resume → Applicant Qualifications (`main`, output 0, input 0)
- Extract Resume → Applicant Personal Data (`main`, output 0, input 0)
- ai_convo_items → AI Agent (`main`, output 0, input 0)
- Applicant Record → Filter_Notion_db (`main`, output 0, input 0)
- Application Data → Extract Resume (`main`, output 0, input 0)
- Filter_Notion_db → Update_Applicant_Record (`main`, output 0, input 0)
- Applicant Summary → Get Job Description (`main`, output 0, input 0)
- ElevenLabs Web Hook → ai_convo_items (`main`, output 0, input 0)
- Evaluation Criteria → AI Agent (`ai_tool`, output 0, input 0)
- Get Job Description → Job Description Summary (`main`, output 0, input 0)
- Google Gemini Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Get Applicant Record → Embed Resume in Notion (`main`, output 0, input 0)
- Applicant Data Backup → Create Applicant Record (`main`, output 0, input 0)
- Upload Audio to Drive → Link Audio in Notion (`main`, output 0, input 0)
- Applicant Personal Data → Merge (`main`, output 0, input 0)
- Application Form 1 of 3 → Upload CV (`main`, output 0, input 0)
- Application Form 1 of 3 → Application Data (`main`, output 0, input 0)
- Application Form 2 of 3 → Upload CV (`main`, output 0, input 0)
- Application Form 2 of 3 → Application Data (`main`, output 0, input 0)
- Application form 3 of 3 → Upload CV (`main`, output 0, input 0)
- Application form 3 of 3 → Application Data (`main`, output 0, input 0)
- Job Description Mapping → HR Expert (`main`, output 0, input 0)
- Job Description Summary → Job Description Mapping (`main`, output 0, input 0)
- Update_Applicant_Record → Extract_Audio (`main`, output 0, input 0)
- Applicant Qualifications → Merge (`main`, output 0, input 1)
- Structured Output Parser → HR Expert (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1639_Wait_Webhook_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1639_Wait_Webhook_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
