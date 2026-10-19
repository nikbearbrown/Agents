# Colombian Invoices Processing

This folder contains the **Colombian Invoices Processing** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `compression`, `extractFromFile`, `filter`, `gmailTrigger`, `googleDrive`, `googleSheets`, `lmChatOpenAi`, `merge`, `noOp`, `outputParserStructured`, `splitInBatches`, `switch`, `toolCalculator`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`colombian-invoices-processing.json`](colombian-invoices-processing.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** On Email receipt

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Loop Over Items | `splitInBatches` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Calculator | `toolCalculator` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| On Email receipt | `gmailTrigger` | Inspect parameters |
| Get Filename and mimeType | `code` | Inspect parameters |
| Filter ZIP files only | `filter` | Inspect parameters |
| Unzip Invoice | `compression` | Inspect parameters |
| Just for style | `noOp` | Inspect parameters |
| Get filename and mimeType on extracted docs | `code` | Inspect parameters |
| Split XML and PDF | `switch` | Inspect parameters |
| Extract PDF Data | `extractFromFile` | pdf |
| Extract XML Data | `extractFromFile` | xml |
| Convert to JSON | `xml` | Inspect parameters |
| Append both Docs | `merge` | Inspect parameters |
| Aggregate all Data into 1 list | `aggregate` | Inspect parameters |
| Extract Data from PDF and XML | `agent` | Inspect parameters |
| Create initial PDF | `googleDrive` | Inspect parameters |
| Merge both flows | `merge` | Inspect parameters |
| Update PDF with actual name | `googleDrive` | update |
| Get Current Date | `code` | Inspect parameters |
| Create or update row | `googleSheets` | appendOrUpdate |

## Connection map

- Calculator → Extract Data from PDF and XML (`ai_tool`, output 0, input 0)
- Unzip Invoice → Loop Over Items (`main`, output 0, input 0)
- Convert to JSON → Append both Docs (`main`, output 0, input 1)
- Loop Over Items → Just for style (`main`, output 0, input 0)
- Loop Over Items → Get filename and mimeType on extracted docs (`main`, output 1, input 0)
- Append both Docs → Aggregate all Data into 1 list (`main`, output 0, input 0)
- Extract PDF Data → Append both Docs (`main`, output 0, input 0)
- Extract XML Data → Convert to JSON (`main`, output 0, input 0)
- Get Current Date → Create or update row (`main`, output 0, input 0)
- Merge both flows → Update PDF with actual name (`main`, output 0, input 0)
- On Email receipt → Get Filename and mimeType (`main`, output 0, input 0)
- OpenAI Chat Model → Extract Data from PDF and XML (`ai_languageModel`, output 0, input 0)
- Split XML and PDF → Create initial PDF (`main`, output 0, input 0)
- Split XML and PDF → Extract PDF Data (`main`, output 0, input 0)
- Split XML and PDF → Extract XML Data (`main`, output 1, input 0)
- Create initial PDF → Merge both flows (`main`, output 0, input 0)
- Create or update row → Loop Over Items (`main`, output 0, input 0)
- Filter ZIP files only → Unzip Invoice (`main`, output 0, input 0)
- Structured Output Parser → Extract Data from PDF and XML (`ai_outputParser`, output 0, input 0)
- Get Filename and mimeType → Filter ZIP files only (`main`, output 0, input 0)
- Update PDF with actual name → Get Current Date (`main`, output 0, input 0)
- Extract Data from PDF and XML → Merge both flows (`main`, output 0, input 1)
- Aggregate all Data into 1 list → Extract Data from PDF and XML (`main`, output 0, input 0)
- Get filename and mimeType on extracted docs → Split XML and PDF (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1765_Code_Filter_Process_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1765_Code_Filter_Process_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
