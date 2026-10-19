# Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example)

This folder contains the **Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example)** workflow. Its executable nodes use `aggregate`, `bambooHr`, `chainLlm`, `debugHelper`, `filter`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `merge`, `noOp`, `outputParserAutofixing`, `outputParserStructured`, `postBin`, `renameKeys`, `set`, `slack`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`test-webhooks-in-n8n-without-changing-webhook-url-postbin-bamboohr-example.json`](test-webhooks-in-n8n-without-changing-webhook-url-postbin-bamboohr-example.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `bambooHrApi`, `httpBasicAuth`, `openAiApi`, `slackApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Create Bin | `httpRequest` | POST |
| GET Bin | `postBin` | get |
| Format url for webhook | `set` | Inspect parameters |
| GET most recent request | `postBin` | request / removeFirst |
| MOCK request | `postBin` | request / send |
| Create Bin1 | `httpRequest` | POST |
| GET Bin1 | `postBin` | get |
| Format url for webhook1 | `set` | Inspect parameters |
| SET BambooHR subdomain | `set` | Inspect parameters |
| Split out fields | `splitOut` | Inspect parameters |
| Combine fields to monitor | `aggregate` | Inspect parameters |
| Format payload for BambooHR webhook | `set` | Inspect parameters |
| Create webhook in BambooHR | `httpRequest` | POST |
| Create dummy data for employees | `debugHelper` | Inspect parameters |
| Keep only new employee fields | `filter` | Inspect parameters |
| GET all possible fields to monitor in BambooHR | `httpRequest` | Inspect parameters |
| Register and test webhook | `noOp` | Inspect parameters |
| Check BambooHR for calls to webhook | `httpRequest` | Inspect parameters |
| Create employee records with dummy data | `bambooHr` | Inspect parameters |
| Split out employees | `splitOut` | Inspect parameters |
| Format displayName | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Combine employees into list | `aggregate` | Inspect parameters |
| Pluralize key | `renameKeys` | Inspect parameters |
| Welcome employees on Slack | `slack` | Inspect parameters |
| DELETE BambooHR webhook | `httpRequest` | DELETE |
| GET most recent request1 | `postBin` | request / removeFirst |
| Wait 60 + 1 seconds for webhook to fire | `wait` | Inspect parameters |

## Connection map

- Merge → Format payload for BambooHR webhook (`main`, output 0, input 0)
- GET Bin → Format url for webhook (`main`, output 0, input 0)
- GET Bin1 → Format url for webhook1 (`main`, output 0, input 0)
- Create Bin → GET Bin (`main`, output 0, input 0)
- Create Bin1 → GET Bin1 (`main`, output 0, input 0)
- Pluralize key → Basic LLM Chain (`main`, output 0, input 0)
- Basic LLM Chain → Welcome employees on Slack (`main`, output 0, input 0)
- Split out fields → Keep only new employee fields (`main`, output 0, input 0)
- OpenAI Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- Format displayName → Combine employees into list (`main`, output 0, input 0)
- OpenAI Chat Model1 → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Split out employees → Format displayName (`main`, output 0, input 0)
- Format url for webhook → Register and test webhook (`main`, output 0, input 0)
- SET BambooHR subdomain → GET all possible fields to monitor in BambooHR (`main`, output 0, input 0)
- Format url for webhook1 → Merge (`main`, output 0, input 0)
- GET most recent request1 → Split out employees (`main`, output 0, input 0)
- Structured Output Parser → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Basic LLM Chain (`ai_outputParser`, output 0, input 0)
- Combine fields to monitor → Merge (`main`, output 0, input 1)
- Register and test webhook → GET most recent request (`main`, output 0, input 0)
- Create webhook in BambooHR → Create dummy data for employees (`main`, output 0, input 0)
- Combine employees into list → Pluralize key (`main`, output 0, input 0)
- Keep only new employee fields → Combine fields to monitor (`main`, output 0, input 0)
- Create dummy data for employees → Create employee records with dummy data (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Create Bin1 (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → SET BambooHR subdomain (`main`, output 0, input 0)
- Format payload for BambooHR webhook → Create webhook in BambooHR (`main`, output 0, input 0)
- Create employee records with dummy data → Wait 60 + 1 seconds for webhook to fire (`main`, output 0, input 0)
- Wait 60 + 1 seconds for webhook to fire → Check BambooHR for calls to webhook (`main`, output 0, input 0)
- Wait 60 + 1 seconds for webhook to fire → GET most recent request1 (`main`, output 0, input 0)
- GET all possible fields to monitor in BambooHR → Split out fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1977_Wait_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1977_Wait_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
