# Example Customer Data

This folder contains the **Example Customer Data** workflow. Its executable nodes use `chainLlm`, `filter`, `gmail`, `googleSheets`, `if`, `lmChatGoogleGemini`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`example-customer-data.json`](example-customer-data.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `googleSheetsOAuth2Api`

**Entry nodes:** Scheduled Start: Daily Churn Check

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Scheduled Start: Daily Churn Check | `scheduleTrigger` | Inspect parameters |
| Fetch Customer Data from Sheet | `googleSheets` | Inspect parameters |
| Filter High Churn Risk & No Campaign Customers | `filter` | Inspect parameters |
| Check if Eligible Customers Found | `if` | Inspect parameters |
| Process Each Eligible Customer | `splitInBatches` | Inspect parameters |
| Generate Win-Back Offer | `chainLlm` | Inspect parameters |
| (LLM Model for Offer Generation) | `lmChatGoogleGemini` | Inspect parameters |
| (Parse Offer JSON) | `outputParserStructured` | Inspect parameters |
| Log Sent Offer in System Log | `googleSheets` | appendOrUpdate |
| Send Win-Back Offer via Email | `gmail` | Inspect parameters |
| Set 'Not Found' Status | `set` | Inspect parameters |
| Log 'Not Found' in System Log | `googleSheets` | appendOrUpdate |

## Connection map

- (Parse Offer JSON) → Generate Win-Back Offer (`ai_outputParser`, output 0, input 0)
- Set 'Not Found' Status → Log 'Not Found' in System Log (`main`, output 0, input 0)
- Generate Win-Back Offer → Log Sent Offer in System Log (`main`, output 0, input 0)
- Log Sent Offer in System Log → Send Win-Back Offer via Email (`main`, output 0, input 0)
- Send Win-Back Offer via Email → Process Each Eligible Customer (`main`, output 0, input 0)
- Fetch Customer Data from Sheet → Filter High Churn Risk & No Campaign Customers (`main`, output 0, input 0)
- Process Each Eligible Customer → Generate Win-Back Offer (`main`, output 1, input 0)
- (LLM Model for Offer Generation) → Generate Win-Back Offer (`ai_languageModel`, output 0, input 0)
- Check if Eligible Customers Found → Process Each Eligible Customer (`main`, output 0, input 0)
- Check if Eligible Customers Found → Set 'Not Found' Status (`main`, output 1, input 0)
- Scheduled Start: Daily Churn Check → Fetch Customer Data from Sheet (`main`, output 0, input 0)
- Filter High Churn Risk & No Campaign Customers → Check if Eligible Customers Found (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0948_Filter_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/0948_Filter_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
