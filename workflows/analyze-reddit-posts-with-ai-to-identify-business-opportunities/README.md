# Analyze Reddit Posts with AI to Identify Business Opportunities

This folder contains the **Analyze Reddit Posts with AI to Identify Business Opportunities** workflow. Its executable nodes use `agent`, `chainSummarization`, `gmail`, `googleSheets`, `if`, `lmChatOpenAi`, `manualTrigger`, `merge`, `openAi`, `reddit`, `sentimentAnalysis`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`analyze-reddit-posts-with-ai-to-identify-business-opportunities.json`](analyze-reddit-posts-with-ai-to-identify-business-opportunities.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `openAiApi`, `redditOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Post Sentiment Analysis | `sentimentAnalysis` | Inspect parameters |
| Positive Posts Draft | `gmail` | draft |
| Neutral  Posts Draft | `gmail` | draft |
| Negative  Posts Draft | `gmail` | draft |
| Find Proper Solutions | `openAi` | Inspect parameters |
| Post Summarization | `chainSummarization` | Inspect parameters |
| Merge Input | `merge` | Inspect parameters |
| Output The Results | `googleSheets` | append |
| Merge 3 Inputs | `merge` | Inspect parameters |
| Filter Posts By Features | `if` | Inspect parameters |
| Filter Posts By Content | `if` | Inspect parameters |
| Select Key Fields | `set` | Inspect parameters |
| Analysis Content  By AI | `agent` | Inspect parameters |
| Get Posts | `reddit` | search |

## Connection map

- Get Posts → Filter Posts By Features (`main`, output 0, input 0)
- Merge Input → Filter Posts By Content (`main`, output 0, input 0)
- Merge 3 Inputs → Output The Results (`main`, output 0, input 0)
- OpenAI Chat Model → Analysis Content  By AI (`ai_languageModel`, output 0, input 0)
- Select Key Fields → Merge Input (`main`, output 0, input 1)
- Select Key Fields → Analysis Content  By AI (`main`, output 0, input 0)
- OpenAI Chat Model1 → Post Summarization (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Post Sentiment Analysis (`ai_languageModel`, output 0, input 0)
- Post Summarization → Merge 3 Inputs (`main`, output 0, input 0)
- Find Proper Solutions → Merge 3 Inputs (`main`, output 0, input 1)
- Analysis Content  By AI → Merge Input (`main`, output 0, input 0)
- Filter Posts By Content → Post Summarization (`main`, output 0, input 0)
- Filter Posts By Content → Find Proper Solutions (`main`, output 0, input 0)
- Filter Posts By Content → Merge 3 Inputs (`main`, output 0, input 2)
- Filter Posts By Content → Post Sentiment Analysis (`main`, output 0, input 0)
- Post Sentiment Analysis → Positive Posts Draft (`main`, output 0, input 0)
- Post Sentiment Analysis → Neutral  Posts Draft (`main`, output 1, input 0)
- Post Sentiment Analysis → Negative  Posts Draft (`main`, output 2, input 0)
- Filter Posts By Features → Select Key Fields (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Posts (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1766_Manual_GoogleSheets_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Manual/1766_Manual_GoogleSheets_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
