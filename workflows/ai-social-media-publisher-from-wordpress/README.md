# AI Social Media Publisher from WordPress

This folder contains the **AI Social Media Publisher from WordPress** workflow. Its executable nodes use `chainLlm`, `facebookGraphApi`, `googleSheets`, `httpRequest`, `linkedIn`, `lmChatOpenRouter`, `manualTrigger`, `openAi`, `outputParserStructured`, `twitter`, `wordpress`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`ai-social-media-publisher-from-wordpress.json`](ai-social-media-publisher-from-wordpress.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `googleSheetsOAuth2Api`, `linkedInOAuth2Api`, `openAiApi`, `openRouterApi`, `twitterOAuth2Api`, `wordpressApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Google Sheets | `googleSheets` | Inspect parameters |
| OpenRouter Chat Model | `lmChatOpenRouter` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Image Instagram | `openAi` | image |
| Image Facebook e Linkedin | `openAi` | image |
| Social Media Manager | `chainLlm` | Inspect parameters |
| Linkedin OK | `googleSheets` | update |
| Facebook Ok | `googleSheets` | update |
| Instagram OK | `googleSheets` | update |
| Get Post | `wordpress` | get |
| Publish on X | `twitter` | Inspect parameters |
| X OK | `googleSheets` | update |
| Publish on LinkedIn | `linkedIn` | Inspect parameters |
| Publish on Facebook | `facebookGraphApi` | Inspect parameters |
| Publish on Instagram | `httpRequest` | POST |

## Connection map

- Get Post → Social Media Manager (`main`, output 0, input 0)
- Publish on X → X OK (`main`, output 0, input 0)
- Google Sheets → Get Post (`main`, output 0, input 0)
- Image Instagram → Publish on Instagram (`main`, output 0, input 0)
- Publish on Facebook → Facebook Ok (`main`, output 0, input 0)
- Publish on LinkedIn → Linkedin OK (`main`, output 0, input 0)
- Publish on Instagram → Instagram OK (`main`, output 0, input 0)
- Social Media Manager → Image Instagram (`main`, output 0, input 0)
- Social Media Manager → Image Facebook e Linkedin (`main`, output 0, input 0)
- Social Media Manager → Publish on X (`main`, output 0, input 0)
- OpenRouter Chat Model → Social Media Manager (`ai_languageModel`, output 0, input 0)
- Structured Output Parser → Social Media Manager (`ai_outputParser`, output 0, input 0)
- Image Facebook e Linkedin → Publish on LinkedIn (`main`, output 0, input 0)
- Image Facebook e Linkedin → Publish on Facebook (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Google Sheets (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1709_Linkedin_Wordpress_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1709_Linkedin_Wordpress_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
