# AI Logo Sheet Extractor to Airtable

This folder contains the **AI Logo Sheet Extractor to Airtable** workflow. Its executable nodes use `agent`, `airtable`, `code`, `crypto`, `formTrigger`, `html`, `lmChatOpenAi`, `merge`, `noOp`, `outputParserStructured`, `set`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-logo-sheet-extractor-to-airtable.json`](ai-logo-sheet-extractor-to-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `openAiApi`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Retrieve and Parser Agent | `agent` | Inspect parameters |
| JSON it | `set` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Check if Attribute exists | `airtable` | upsert |
| Merge | `merge` | Inspect parameters |
| Map Attribute ID | `set` | Inspect parameters |
| Loop Over Attributes | `splitInBatches` | Inspect parameters |
| All Attributes | `set` | Inspect parameters |
| Wait for Attribute Creation | `merge` | Inspect parameters |
| Change each Attribute to the corresponding RecID | `code` | Inspect parameters |
| Split Out Tools | `splitOut` | Inspect parameters |
| Split Out each Attribute String | `splitOut` | Inspect parameters |
| Generate Unique Hash for Name | `crypto` | Inspect parameters |
| Create if not Exist | `airtable` | upsert |
| Merge Old Data + RecID | `merge` | Inspect parameters |
| Only what we need | `set` | Inspect parameters |
| Determine Attributes we should save | `code` | Inspect parameters |
| Split Out similar | `splitOut` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Generate Unique Hash for Similar | `crypto` | Inspect parameters |
| It Should exists | `airtable` | upsert |
| All Similar | `set` | Inspect parameters |
| Merge2 | `merge` | Inspect parameters |
| Change each Smiliar to the corresponding RecID | `code` | Inspect parameters |
| Determine Similar we should save | `code` | Inspect parameters |
| Save all this juicy data | `airtable` | upsert |
| Map Agent Input | `set` | Inspect parameters |
| gpt-4o | `lmChatOpenAi` | Inspect parameters |
| Table: Tools | `noOp` | Inspect parameters |
| Table: Attributes | `noOp` | Inspect parameters |
| make it a readable list | `html` | Inspect parameters |
| Get Schema | `airtable` | base / getSchema |

## Connection map

- Merge → Map Attribute ID (`main`, output 0, input 0)
- Merge1 → All Similar (`main`, output 0, input 0)
- Merge2 → Change each Smiliar to the corresponding RecID (`main`, output 0, input 0)
- gpt-4o → Retrieve and Parser Agent (`ai_languageModel`, output 0, input 0)
- JSON it → Split Out Tools (`main`, output 0, input 0)
- Get Schema → make it a readable list (`main`, output 0, input 0)
- All Similar → Merge2 (`main`, output 0, input 1)
- Table: Tools → Table: Tools (`main`, output 0, input 0)
- Table: Tools → Table: Attributes (`main`, output 0, input 0)
- All Attributes → Wait for Attribute Creation (`main`, output 0, input 1)
- Map Agent Input → Retrieve and Parser Agent (`main`, output 0, input 0)
- Split Out Tools → Loop Over Attributes (`main`, output 0, input 0)
- Split Out Tools → Wait for Attribute Creation (`main`, output 0, input 0)
- It Should exists → Merge1 (`main`, output 0, input 0)
- Map Attribute ID → Loop Over Attributes (`main`, output 0, input 0)
- Only what we need → Merge Old Data + RecID (`main`, output 0, input 1)
- Split Out similar → Generate Unique Hash for Similar (`main`, output 0, input 0)
- Split Out similar → Merge1 (`main`, output 0, input 1)
- On form submission → Map Agent Input (`main`, output 0, input 0)
- Create if not Exist → Only what we need (`main`, output 0, input 0)
- Loop Over Attributes → All Attributes (`main`, output 0, input 0)
- Loop Over Attributes → Split Out each Attribute String (`main`, output 1, input 0)
- Merge Old Data + RecID → Determine Attributes we should save (`main`, output 0, input 0)
- Structured Output Parser → Retrieve and Parser Agent (`ai_outputParser`, output 0, input 0)
- Check if Attribute exists → Merge (`main`, output 0, input 0)
- Retrieve and Parser Agent → JSON it (`main`, output 0, input 0)
- Wait for Attribute Creation → Change each Attribute to the corresponding RecID (`main`, output 0, input 0)
- Generate Unique Hash for Name → Create if not Exist (`main`, output 0, input 0)
- Generate Unique Hash for Name → Merge Old Data + RecID (`main`, output 0, input 0)
- Split Out each Attribute String → Check if Attribute exists (`main`, output 0, input 0)
- Split Out each Attribute String → Merge (`main`, output 0, input 1)
- Determine Similar we should save → Save all this juicy data (`main`, output 0, input 0)
- Generate Unique Hash for Similar → It Should exists (`main`, output 0, input 0)
- Determine Attributes we should save → Split Out similar (`main`, output 0, input 0)
- Determine Attributes we should save → Merge2 (`main`, output 0, input 0)
- Change each Smiliar to the corresponding RecID → Determine Similar we should save (`main`, output 0, input 0)
- Change each Attribute to the corresponding RecID → Generate Unique Hash for Name (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1834_Splitout_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1834_Splitout_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
