# Creates a folder in Google Drive to store the generated content and outline

This folder contains the **Creates a folder in Google Drive to store the generated content and outline** workflow. Its executable nodes use `aggregate`, `code`, `convertToFile`, `formTrigger`, `googleDrive`, `googleSheets`, `if`, `merge`, `openAi`, `set`, `sort`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`creates-a-folder-in-google-drive-to-store-the-generated-content-and-outline.json`](creates-a-folder-in-google-drive-to-store-the-generated-content-and-outline.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleDriveOAuth2Api`, `googleSheetsOAuth2Api`, `openAiApi`

**Entry nodes:** receive_topic

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| create_folder | `googleDrive` | folder |
| input_brief | `set` | Inspect parameters |
| new_lines | `set` | Inspect parameters |
| input_sections | `set` | Inspect parameters |
| section_text | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Sort | `sort` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| final_article | `set` | Inspect parameters |
| set_introduction | `set` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| receive_topic | `formTrigger` | Inspect parameters |
| add_row | `googleSheets` | append |
| topic_variables | `set` | Inspect parameters |
| markdown_to_file | `convertToFile` | toText |
| split_out | `splitOut` | Inspect parameters |
| section_starts_with_# | `if` | Inspect parameters |
| 25_percent_chance | `if` | Inspect parameters |
| set_section_content | `set` | Inspect parameters |
| add_2_new_lines | `code` | Inspect parameters |
| final_article_file | `convertToFile` | toText |
| upload_fiinalArticle | `googleDrive` | Inspect parameters |
| update_article_link | `googleSheets` | update |
| upload_outline_file | `googleDrive` | Inspect parameters |
| section_paragraphs | `openAi` | Inspect parameters |
| change_section_format | `openAi` | Inspect parameters |
| create_outline | `openAi` | Inspect parameters |

## Connection map

- Sort → add_2_new_lines (`main`, output 0, input 0)
- Merge → Sort (`main`, output 0, input 0)
- Merge1 → Aggregate (`main`, output 0, input 0)
- add_row → topic_variables (`main`, output 0, input 0)
- Aggregate → final_article (`main`, output 0, input 0)
- new_lines → split_out (`main`, output 0, input 0)
- split_out → section_starts_with_# (`main`, output 0, input 0)
- input_brief → new_lines (`main`, output 0, input 0)
- section_text → 25_percent_chance (`main`, output 0, input 0)
- create_folder → create_outline (`main`, output 0, input 0)
- final_article → final_article_file (`main`, output 0, input 0)
- receive_topic → add_row (`main`, output 0, input 0)
- create_outline → markdown_to_file (`main`, output 0, input 0)
- input_sections → section_paragraphs (`main`, output 0, input 0)
- add_2_new_lines → Merge1 (`main`, output 0, input 1)
- topic_variables → create_folder (`main`, output 0, input 0)
- markdown_to_file → upload_outline_file (`main`, output 0, input 0)
- set_introduction → Merge1 (`main`, output 0, input 0)
- 25_percent_chance → change_section_format (`main`, output 0, input 0)
- 25_percent_chance → Merge (`main`, output 1, input 1)
- final_article_file → upload_fiinalArticle (`main`, output 0, input 0)
- section_paragraphs → section_text (`main`, output 0, input 0)
- set_section_content → Merge (`main`, output 0, input 0)
- upload_outline_file → input_brief (`main`, output 0, input 0)
- upload_fiinalArticle → update_article_link (`main`, output 0, input 0)
- change_section_format → set_section_content (`main`, output 0, input 0)
- section_starts_with_# → set_introduction (`main`, output 0, input 0)
- section_starts_with_# → input_sections (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0625_Splitout_Code_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0625_Splitout_Code_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
