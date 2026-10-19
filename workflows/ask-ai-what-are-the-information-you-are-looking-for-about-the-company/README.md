# Ask AI what are the information you are looking for about the company

This folder contains the **Ask AI what are the information you are looking for about the company** workflow. Its executable nodes use `agent`, `googleSheets`, `lmChatOpenAi`, `manualTrigger`, `merge`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitInBatches`, `toolSerpApi`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ask-ai-what-are-the-information-you-are-looking-for-about-the-company.json`](ask-ai-what-are-the-information-you-are-looking-for-about-the-company.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `openAiApi`, `serpApi`

**Entry nodes:** When clicking "Test workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Input | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Get website content | `toolWorkflow` | Inspect parameters |
| SerpAPI - Search Google | `toolSerpApi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| AI Researcher Output Data | `set` | Inspect parameters |
| Google Sheets - Update Row with data | `googleSheets` | update |
| Merge data | `merge` | Inspect parameters |
| Get rows to enrich | `googleSheets` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| AI company researcher | `agent` | Inspect parameters |
| Search Google with ScrapingBee | `toolWorkflow` | Inspect parameters |

## Connection map

- Input → Loop Over Items (`main`, output 0, input 0)
- Merge data → Google Sheets - Update Row with data (`main`, output 0, input 0)
- Loop Over Items → AI company researcher (`main`, output 1, input 0)
- Loop Over Items → Merge data (`main`, output 1, input 0)
- Schedule Trigger → Get rows to enrich (`main`, output 0, input 0)
- OpenAI Chat Model → AI company researcher (`ai_languageModel`, output 0, input 0)
- Get rows to enrich → Input (`main`, output 0, input 0)
- Get website content → AI company researcher (`ai_tool`, output 0, input 0)
- AI company researcher → AI Researcher Output Data (`main`, output 0, input 0)
- SerpAPI - Search Google → AI company researcher (`ai_tool`, output 0, input 0)
- Structured Output Parser → AI company researcher (`ai_outputParser`, output 0, input 0)
- AI Researcher Output Data → Merge data (`main`, output 0, input 1)
- When clicking "Test workflow" → Get rows to enrich (`main`, output 0, input 0)
- Google Sheets - Update Row with data → Loop Over Items (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0527_Schedule_Manual_Update_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0527_Schedule_Manual_Update_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
