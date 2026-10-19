# http request and get mailbox ids and split out

This folder contains the **http request and get mailbox ids and split out** workflow. Its executable nodes use `emailReadImap`, `filter`, `httpRequest`, `openAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`http-request-and-get-mailbox-ids-and-split-out.json`](http-request-and-get-mailbox-ids-and-split-out.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `imap`, `openAiApi`

**Entry nodes:** No recognized trigger; inspect the graph for an external entry point.

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Session | `httpRequest` | Inspect parameters |
| Get Mailbox IDs | `httpRequest` | POST |
| Split Out | `splitOut` | Inspect parameters |
| Email Trigger (IMAP) | `emailReadImap` | Inspect parameters |
| Get fields from source email | `set` | Inspect parameters |
| OpenAI | `openAi` | Inspect parameters |
| Filter for drafts folder | `filter` | Inspect parameters |
| upload draft email | `httpRequest` | POST |
| gather data for draft email | `set` | Inspect parameters |

## Connection map

- OpenAI → Session (`main`, output 0, input 0)
- Session → Get Mailbox IDs (`main`, output 0, input 0)
- Split Out → Filter for drafts folder (`main`, output 0, input 0)
- Get Mailbox IDs → Split Out (`main`, output 0, input 0)
- Email Trigger (IMAP) → Get fields from source email (`main`, output 0, input 0)
- Filter for drafts folder → gather data for draft email (`main`, output 0, input 0)
- gather data for draft email → upload draft email (`main`, output 0, input 0)
- Get fields from source email → OpenAI (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0587_Splitout_Filter_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0587_Splitout_Filter_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.

## Consolidated snapshot

The former `http-request-and-get-mailbox-ids-and-split-out-1f85ae58` folder was consolidated here after comparison of nodes, connections, settings, and parameter strings. Differences were limited to horizontal whitespace inside strings; the retained JSON preserves its original formatting and has not been rewritten. This does not establish runtime equivalence. Both source hashes and license records remain in [the consolidation manifest](../../consolidation.json). The original snapshot remains recoverable from Git commit `7367bc452f26c4dd029175d0828a95ec08ce83b7`.
