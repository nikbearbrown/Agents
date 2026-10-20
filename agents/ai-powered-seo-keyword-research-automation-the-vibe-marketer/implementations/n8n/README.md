# AI powered SEO Keyword Research Automation - The vibe Marketer

This folder contains the **AI powered SEO Keyword Research Automation - The vibe Marketer** workflow. Its executable nodes use `agent`, `aggregate`, `code`, `dataForSeo`, `lmChatOpenAi`, `merge`, `nocoDb`, `outputParserStructured`, `set`, `slack`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-powered-seo-keyword-research-automation-the-vibe-marketer.json`](ai-powered-seo-keyword-research-automation-the-vibe-marketer.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dataForSeoApi`, `nocoDbApiToken`, `openAiApi`, `slackApi`

**Entry nodes:** Get Input from NocoDB

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Topic Expansion | `agent` | Inspect parameters |
| Competitor Analysis | `agent` | Inspect parameters |
| Keyword Difficulty | `dataForSeo` | labs / get-keyword-difficulty |
| Search Volume & CPC | `dataForSeo` | keywords_data |
| split primary keywords | `splitOut` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Keyword Ranking per URL | `dataForSeo` | labs / get-ranked-keywords |
| Final Keyword Strategy | `agent` | Inspect parameters |
| Get Input from NocoDB | `webhook` | Inspect parameters |
| Split the Competitor URLs | `splitOut` | Inspect parameters |
| Set relevant fields | `set` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Format Json and add Competitor URLs | `code` | Inspect parameters |
| Aggregate SV & CPC | `aggregate` | Inspect parameters |
| Aggregate KWD | `aggregate` | Inspect parameters |
| Merge SV, CPC & KWD | `merge` | Inspect parameters |
| Merge Topic Expansion, SV, CPC & KWD | `merge` | Inspect parameters |
| Aggregate Competitor Analysis | `aggregate` | Inspect parameters |
| Merge Everything | `merge` | Inspect parameters |
| Write Content Brief  | `nocoDb` | create |
| Update Status - Done | `nocoDb` | update |
| Send Notification | `slack` | Inspect parameters |
| Start Notification | `slack` | Inspect parameters |
| Update Status - Started | `nocoDb` | update |

## Connection map

- Aggregate KWD → Merge SV, CPC & KWD (`main`, output 0, input 1)
- Topic Expansion → split primary keywords (`main`, output 0, input 0)
- Topic Expansion → Merge Topic Expansion, SV, CPC & KWD (`main`, output 0, input 1)
- Merge Everything → Final Keyword Strategy (`main`, output 0, input 0)
- OpenAI Chat Model → Topic Expansion (`ai_languageModel`, output 0, input 0)
- Aggregate SV & CPC → Merge SV, CPC & KWD (`main`, output 0, input 0)
- Keyword Difficulty → Aggregate KWD (`main`, output 0, input 0)
- OpenAI Chat Model1 → Competitor Analysis (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Final Keyword Strategy (`ai_languageModel`, output 0, input 0)
- Competitor Analysis → Aggregate Competitor Analysis (`main`, output 0, input 0)
- Merge SV, CPC & KWD → Merge Topic Expansion, SV, CPC & KWD (`main`, output 0, input 0)
- Search Volume & CPC → Aggregate SV & CPC (`main`, output 0, input 0)
- Set relevant fields → Topic Expansion (`main`, output 0, input 0)
- Set relevant fields → Format Json and add Competitor URLs (`main`, output 0, input 0)
- Set relevant fields → Merge Everything (`main`, output 0, input 2)
- Set relevant fields → Update Status - Started (`main`, output 0, input 0)
- Set relevant fields → Start Notification (`main`, output 0, input 0)
- Get Input from NocoDB → Set relevant fields (`main`, output 0, input 0)
- Final Keyword Strategy → Write Content Brief  (`main`, output 0, input 0)
- Final Keyword Strategy → Update Status - Done (`main`, output 0, input 0)
- Final Keyword Strategy → Send Notification (`main`, output 0, input 0)
- split primary keywords → Search Volume & CPC (`main`, output 0, input 0)
- split primary keywords → Keyword Difficulty (`main`, output 0, input 0)
- Keyword Ranking per URL → Competitor Analysis (`main`, output 0, input 0)
- Structured Output Parser → Topic Expansion (`ai_outputParser`, output 0, input 0)
- Split the Competitor URLs → Keyword Ranking per URL (`main`, output 0, input 0)
- Aggregate Competitor Analysis → Merge Everything (`main`, output 0, input 1)
- Format Json and add Competitor URLs → Split the Competitor URLs (`main`, output 0, input 0)
- Merge Topic Expansion, SV, CPC & KWD → Merge Everything (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1930_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1930_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
