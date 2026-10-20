# High-Level Service Page SEO Blueprint Report

This folder contains the **High-Level Service Page SEO Blueprint Report** workflow. Its executable nodes use `chainLlm`, `code`, `convertToFile`, `formTrigger`, `httpRequest`, `lmChatGoogleGemini`, `set`, `splitInBatches`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`high-level-service-page-seo-blueprint-report.json`](high-level-service-page-seo-blueprint-report.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`

**Entry nodes:** Start

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Convert URLs to Items | `code` | Inspect parameters |
| Start | `formTrigger` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Get URL HTML | `httpRequest` | Inspect parameters |
| Extract HTML Elements | `code` | Inspect parameters |
| Set URL Data | `set` | Inspect parameters |
| Code | `code` | Inspect parameters |
| Edit Fields1 | `set` | Inspect parameters |
| Google Gemini Chat Model | `lmChatGoogleGemini` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Google Gemini Chat Model1 | `lmChatGoogleGemini` | Inspect parameters |
| Set Competitor Analysis | `set` | Inspect parameters |
| Set User Intent Analysis | `set` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Google Gemini Chat Model2 | `lmChatGoogleGemini` | Inspect parameters |
| Competitors Analysis | `chainLlm` | Inspect parameters |
| User Intent Analysis | `chainLlm` | Inspect parameters |
| Synthesis & Gap Analysis | `chainLlm` | Inspect parameters |
| Set Synthesis & Gap Analysis | `set` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| Google Gemini Chat Model3 | `lmChatGoogleGemini` | Inspect parameters |
| Ideal Page Outline Generation | `chainLlm` | Inspect parameters |
| Set Page Outline | `set` | Inspect parameters |
| Wait3 | `wait` | Inspect parameters |
| Google Gemini Chat Model4 | `lmChatGoogleGemini` | Inspect parameters |
| UX, Conversion & Copywriting Enhancement | `chainLlm` | Inspect parameters |
| Set UX & Conversions Enhancements | `set` | Inspect parameters |
| Google Gemini Chat Model5 | `lmChatGoogleGemini` | Inspect parameters |
| Final Service Page Blueprint | `chainLlm` | Inspect parameters |
| Edit Fields2 | `set` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- Code → Edit Fields1 (`main`, output 0, input 0)
- Wait → User Intent Analysis (`main`, output 0, input 0)
- Start → Edit Fields (`main`, output 0, input 0)
- Wait1 → Synthesis & Gap Analysis (`main`, output 0, input 0)
- Wait2 → Ideal Page Outline Generation (`main`, output 0, input 0)
- Wait3 → UX, Conversion & Copywriting Enhancement (`main`, output 0, input 0)
- Edit Fields → Convert URLs to Items (`main`, output 0, input 0)
- Edit Fields1 → Competitors Analysis (`main`, output 0, input 0)
- Edit Fields2 → Convert to File (`main`, output 0, input 0)
- Get URL HTML → Extract HTML Elements (`main`, output 0, input 0)
- Set URL Data → Loop Over Items (`main`, output 0, input 0)
- Loop Over Items → Code (`main`, output 0, input 0)
- Loop Over Items → Get URL HTML (`main`, output 1, input 0)
- Set Page Outline → Wait3 (`main`, output 0, input 0)
- Competitors Analysis → Set Competitor Analysis (`main`, output 0, input 0)
- User Intent Analysis → Set User Intent Analysis (`main`, output 0, input 0)
- Convert URLs to Items → Loop Over Items (`main`, output 0, input 0)
- Extract HTML Elements → Set URL Data (`main`, output 0, input 0)
- Set Competitor Analysis → Wait (`main`, output 0, input 0)
- Google Gemini Chat Model → Competitors Analysis (`ai_languageModel`, output 0, input 0)
- Set User Intent Analysis → Wait1 (`main`, output 0, input 0)
- Synthesis & Gap Analysis → Set Synthesis & Gap Analysis (`main`, output 0, input 0)
- Google Gemini Chat Model1 → User Intent Analysis (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model2 → Synthesis & Gap Analysis (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model3 → Ideal Page Outline Generation (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model4 → UX, Conversion & Copywriting Enhancement (`ai_languageModel`, output 0, input 0)
- Google Gemini Chat Model5 → Final Service Page Blueprint (`ai_languageModel`, output 0, input 0)
- Final Service Page Blueprint → Edit Fields2 (`main`, output 0, input 0)
- Set Synthesis & Gap Analysis → Wait2 (`main`, output 0, input 0)
- Ideal Page Outline Generation → Set Page Outline (`main`, output 0, input 0)
- Set UX & Conversions Enhancements → Final Service Page Blueprint (`main`, output 0, input 0)
- UX, Conversion & Copywriting Enhancement → Set UX & Conversions Enhancements (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1745_Wait_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1745_Wait_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
