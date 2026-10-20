# Extract spend details (template)

This folder contains the **Extract spend details (template)** workflow. Its executable nodes use `chainLlm`, `extractFromFile`, `gmailTrigger`, `googleSheets`, `html`, `lmChatGoogleGemini`, `lmChatGroq`, `merge`, `outputParserStructured`, `set`, `splitOut`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`extract-spend-details-template.json`](extract-spend-details-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `googleSheetsOAuth2Api`, `groqApi`

**Entry nodes:** Get invoice, Get payment

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get invoice | `gmailTrigger` | Inspect parameters |
| Get payment | `gmailTrigger` | Inspect parameters |
| Extract invoice | `extractFromFile` | pdf |
| Extract payment | `extractFromFile` | pdf |
| HTML | `html` | extractHtmlContent |
| Split Out | `splitOut` | Inspect parameters |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Send | `googleSheets` | append |
| Set data 0 | `set` | Inspect parameters |
| Set data 1 | `set` | Inspect parameters |
| Set data 2 | `set` | Inspect parameters |
| Invoice data | `set` | Inspect parameters |
| Payment data | `set` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Send1 | `googleSheets` | append |
| Extract details1 | `chainLlm` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Extract details | `chainLlm` | Inspect parameters |

## Connection map

- HTML → Split Out (`main`, output 0, input 0)
- Merge → Extract details (`main`, output 0, input 0)
- Switch → HTML (`main`, output 0, input 0)
- Switch → Set data 1 (`main`, output 1, input 0)
- Switch → Set data 2 (`main`, output 2, input 0)
- Split Out → Set data 0 (`main`, output 0, input 0)
- Set data 0 → Merge (`main`, output 0, input 0)
- Set data 1 → Merge (`main`, output 0, input 1)
- Set data 2 → Extract details1 (`main`, output 0, input 0)
- Get invoice → Extract invoice (`main`, output 0, input 0)
- Get payment → Extract payment (`main`, output 0, input 0)
- Invoice data → Switch (`main`, output 0, input 0)
- Payment data → Switch (`main`, output 0, input 0)
- Extract details → Send (`main`, output 0, input 0)
- Extract invoice → Invoice data (`main`, output 0, input 0)
- Extract payment → Payment data (`main`, output 0, input 0)
- Groq Chat Model → Extract details1 (`ai_languageModel`, output 0, input 0)
- Extract details1 → Send1 (`main`, output 0, input 0)
- Structured Output Parser → Extract details1 (`ai_outputParser`, output 0, input 0)
- Google Gemini Chat Model1 → Extract details (`ai_languageModel`, output 0, input 0)
- Structured Output Parser1 → Extract details (`ai_outputParser`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1935_Splitout_Extractfromfile_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1935_Splitout_Extractfromfile_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
