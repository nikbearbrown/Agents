# 🔒 This workflow demonstrates Redis-based locking to prevent concurrent execution of workflows.

This folder contains the **🔒 This workflow demonstrates Redis-based locking to prevent concurrent execution of workflows.** workflow. Its executable nodes use `code`, `if`, `noOp`, `redis`, `set`, `switch`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`this-workflow-demonstrates-redis-based-locking-to-prevent-concurrent-execution-of-workflows.json`](this-workflow-demonstrates-redis-based-locking-to-prevent-concurrent-execution-of-workflows.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `redis`

**Entry nodes:** Incoming Webhook Data

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| END | `noOp` | Inspect parameters |
| Workflow 1 | `set` | Inspect parameters |
| Workflow 2 | `set` | Inspect parameters |
| Workflow 3 | `set` | Inspect parameters |
| Incoming Webhook Data | `webhook` | Inspect parameters |
| Fetch Webhook Data & Declare lockValue | `code` | Inspect parameters |
| Check Redis Lock | `redis` | get |
| Acquire Redis Lock | `redis` | set |
| redisLock existence boolean | `if` | Inspect parameters |
| redisLock acquired booleans | `if` | Inspect parameters |
| Poll for lock | `wait` | Inspect parameters |
| duplicateWebhook boolean | `if` | Inspect parameters |
| Discard Redis Lock | `redis` | delete |
| Workflow Switch | `switch` | Inspect parameters |

## Connection map

- Workflow 1 → Discard Redis Lock (`main`, output 0, input 0)
- Workflow 2 → Discard Redis Lock (`main`, output 0, input 0)
- Workflow 3 → Discard Redis Lock (`main`, output 0, input 0)
- Poll for lock → duplicateWebhook boolean (`main`, output 0, input 0)
- Workflow Switch → Workflow 1 (`main`, output 0, input 0)
- Workflow Switch → Workflow 2 (`main`, output 1, input 0)
- Workflow Switch → Workflow 3 (`main`, output 2, input 0)
- Check Redis Lock → redisLock existence boolean (`main`, output 0, input 0)
- Acquire Redis Lock → Workflow Switch (`main`, output 0, input 0)
- Incoming Webhook Data → Fetch Webhook Data & Declare lockValue (`main`, output 0, input 0)
- duplicateWebhook boolean → END (`main`, output 0, input 0)
- duplicateWebhook boolean → Check Redis Lock (`main`, output 1, input 0)
- redisLock acquired booleans → Acquire Redis Lock (`main`, output 0, input 0)
- redisLock acquired booleans → Poll for lock (`main`, output 1, input 0)
- redisLock existence boolean → Acquire Redis Lock (`main`, output 0, input 0)
- redisLock existence boolean → redisLock acquired booleans (`main`, output 1, input 0)
- Fetch Webhook Data & Declare lockValue → Check Redis Lock (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0831_Wait_Code_Monitor_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0831_Wait_Code_Monitor_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
