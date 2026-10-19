# Find WooCommerce User-ID

This folder contains the **Find WooCommerce User-ID** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `code`, `dhl`, `executeWorkflowTrigger`, `httpRequest`, `if`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `respondToWebhook`, `set`, `splitOut`, `toolWorkflow`, `webhook`, `wooCommerce`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`find-woocommerce-user-id.json`](find-woocommerce-user-id.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dhlApi`, `openAiApi`, `wooCommerceApi`

**Entry nodes:** Execute Workflow Trigger, Chat Trigger, Webhook Example Page

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| No email provided | `set` | Inspect parameters |
| If email provided | `if` | Inspect parameters |
| If user found | `if` | Inspect parameters |
| No customer found | `set` | Inspect parameters |
| If contains DHL data | `if` | Inspect parameters |
| Extract Tracking Data | `set` | Inspect parameters |
| Merge Orders | `merge` | Inspect parameters |
| Merge Order and Tracking Data | `merge` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Merge Tracking Data | `merge` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| WooCommerce - Get User | `wooCommerce` | customer / getAll |
| If order found | `if` | Inspect parameters |
| WooCommerce Get Orders | `httpRequest` | Inspect parameters |
| No order found | `set` | Inspect parameters |
| Add Error Information | `set` | Inspect parameters |
| DHL | `dhl` | Inspect parameters |
| Send Response | `set` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| WooCommerce_Tool | `toolWorkflow` | Inspect parameters |
| Chat Trigger | `chatTrigger` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Webhook Example Page | `webhook` | Inspect parameters |
| Decrypt email | `code` | Inspect parameters |
| Encrypt email | `code` | Inspect parameters |
| Example encrypted email | `set` | Inspect parameters |
| Decrypt email address | `code` | Inspect parameters |
| AI Agent | `agent` | Inspect parameters |
| Mock Data | `set` | Inspect parameters |

## Connection map

- DHL → Merge Tracking Data (`main`, output 0, input 0)
- DHL → Add Error Information (`main`, output 1, input 0)
- Aggregate → Merge Orders (`main`, output 0, input 0)
- Mock Data → AI Agent (`main`, output 0, input 0)
- Split Out → DHL (`main`, output 0, input 0)
- Chat Trigger → Decrypt email address (`main`, output 0, input 0)
- Merge Orders → Merge Order and Tracking Data (`main`, output 0, input 0)
- If user found → WooCommerce Get Orders (`main`, output 0, input 0)
- If user found → No customer found (`main`, output 1, input 0)
- If order found → Extract Tracking Data (`main`, output 0, input 0)
- If order found → Merge Order and Tracking Data (`main`, output 0, input 1)
- If order found → No order found (`main`, output 1, input 0)
- WooCommerce_Tool → AI Agent (`ai_tool`, output 0, input 0)
- If email provided → WooCommerce - Get User (`main`, output 0, input 0)
- If email provided → No email provided (`main`, output 1, input 0)
- OpenAI Chat Model → AI Agent (`ai_languageModel`, output 0, input 0)
- Merge Tracking Data → Aggregate (`main`, output 0, input 0)
- If contains DHL data → Split Out (`main`, output 0, input 0)
- If contains DHL data → Merge Orders (`main`, output 1, input 1)
- Webhook Example Page → Respond to Webhook (`main`, output 0, input 0)
- Window Buffer Memory → AI Agent (`ai_memory`, output 0, input 0)
- Add Error Information → Merge Tracking Data (`main`, output 0, input 1)
- Decrypt email address → Mock Data (`main`, output 0, input 0)
- Extract Tracking Data → If contains DHL data (`main`, output 0, input 0)
- WooCommerce - Get User → If user found (`main`, output 0, input 0)
- WooCommerce Get Orders → If order found (`main`, output 0, input 0)
- Example encrypted email → Decrypt email (`main`, output 0, input 0)
- Execute Workflow Trigger → If email provided (`main`, output 0, input 0)
- Merge Order and Tracking Data → Send Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0457_Splitout_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0457_Splitout_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
