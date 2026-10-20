# Slack Webhook - Verify Signature

This folder contains the **Slack Webhook - Verify Signature** workflow. Its executable nodes use `code`, `crypto`, `executeWorkflowTrigger`, `if`, `merge`, `set`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`slack-webhook-verify-signature.json`](slack-webhook-verify-signature.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Make Slack Verif Token | `code` | Inspect parameters |
| Encode Secret String | `crypto` | Inspect parameters |
| IF | `if` | Inspect parameters |
| Stop and Error | `stopAndError` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Set Verified to True | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |

## Connection map

- IF → Set Verified to True (`main`, output 0, input 0)
- IF → Stop and Error (`main`, output 1, input 0)
- Encode Secret String → IF (`main`, output 0, input 0)
- Set Verified to True → Merge (`main`, output 0, input 1)
- Make Slack Verif Token → Encode Secret String (`main`, output 0, input 0)
- Execute Workflow Trigger → Make Slack Verif Token (`main`, output 0, input 0)
- Execute Workflow Trigger → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1164_Stopanderror_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1164_Stopanderror_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
