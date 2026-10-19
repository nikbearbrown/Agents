# ScenarioStressTestingAgent

This folder contains the **ScenarioStressTestingAgent** workflow. Its executable nodes use `chainLlm`, `chatTrigger`, `code`, `httpRequest`, `if`, `lmChatGroq`, `merge`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scenariostresstestingagent.json`](scenariostresstestingagent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `groqApi`

**Entry nodes:** Webhook Trigger, When chat message received

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook Trigger | `webhook` | Inspect parameters |
| Parse Input | `set` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Validate Portfolio | `code` | Inspect parameters |
| Custom Scenario? | `if` | Inspect parameters |
| Load_Template_Scenario | `code` | Inspect parameters |
| When chat message received | `chatTrigger` | Inspect parameters |
| Basic LLM Chain | `chainLlm` | Inspect parameters |
| Groq Chat Model | `lmChatGroq` | Inspect parameters |
| Parse_LLM_Response | `code` | Inspect parameters |
| Stress_Test_Engine | `code` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Fetch_Data | `httpRequest` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Save_Portfolio_Before_LLM | `code` | Inspect parameters |

## Connection map

- Webhook Trigger → Parse Input (`main`, output 0, input 0)
- Parse Input → Edit Fields (`main`, output 0, input 0)
- Edit Fields → Validate Portfolio (`main`, output 0, input 0)
- Edit Fields → Fetch_Data (`main`, output 0, input 0)
- Validate Portfolio → Merge (`main`, output 0, input 1)
- Custom Scenario? → Save_Portfolio_Before_LLM (`main`, output 0, input 0)
- Custom Scenario? → Load_Template_Scenario (`main`, output 1, input 0)
- Groq Chat Model → Basic LLM Chain (`ai_languageModel`, output 0, input 0)
- When chat message received → Basic LLM Chain (`main`, output 0, input 0)
- Basic LLM Chain → Parse_LLM_Response (`main`, output 0, input 0)
- Parse_LLM_Response → Merge1 (`main`, output 0, input 0)
- Load_Template_Scenario → Merge1 (`main`, output 0, input 1)
- Stress_Test_Engine → Respond to Webhook (`main`, output 0, input 0)
- Fetch_Data → Merge (`main`, output 0, input 0)
- Merge → Custom Scenario? (`main`, output 0, input 0)
- Merge1 → Stress_Test_Engine (`main`, output 0, input 0)
- Save_Portfolio_Before_LLM → Basic LLM Chain (`main`, output 0, input 0)
- Save_Portfolio_Before_LLM → Parse_LLM_Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: Nik Bear Brown; permission confirmed by repository owner. License: **MIT**; preserve [the notice](../../licenses/nikbearbrown-mit.txt) and embedded attribution. Repository owner confirmed redistribution rights and authorized MIT licensing on 2026-10-19.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
