# Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)

This folder contains the **Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)** workflow. Its executable nodes use `emailSend`, `function`, `github`, `if`, `merge`, `openAi`, `postgres`, `respondToWebhook`, `slack`, `start`, `switch`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`pyragogy-ai-village-orchestrazione-master-architettura-profonda-v2.json`](pyragogy-ai-village-orchestrazione-master-architettura-profonda-v2.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `emailSend`, `githubApi`, `openAiApi`, `postgres`

**Entry nodes:** Start, Webhook Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start | `start` | Inspect parameters |
| Webhook Trigger | `webhook` | Inspect parameters |
| Check DB Connection | `postgres` | executeQuery |
| Meta-Orchestrator | `openAi` | chat |
| Parse Orchestration Plan | `function` | Inspect parameters |
| More Agents to Run? | `if` | Inspect parameters |
| Prepare Agent Input | `function` | Inspect parameters |
| Route Agents with Switch | `switch` | Inspect parameters |
| Summarizer Agent | `openAi` | chat |
| Synthesizer Agent | `openAi` | chat |
| Peer Reviewer Agent | `openAi` | chat |
| Sensemaking Agent | `openAi` | chat |
| Prompt Engineer Agent | `openAi` | chat |
| Onboarding/Explainer Agent | `openAi` | chat |
| Add Handbook Metadata | `function` | Inspect parameters |
| Generate Content for Review | `function` | Inspect parameters |
| Generate Review ID | `function` | Inspect parameters |
| Send Review Request Email | `emailSend` | Inspect parameters |
| Wait for Human Approval | `wait` | Inspect parameters |
| Human Decision Split | `if` | Inspect parameters |
| Save to handbook_entries | `postgres` | insert |
| Prepare Approved Contribution Data | `function` | Inspect parameters |
| Save Agent Contribution (Approved) | `postgres` | insert |
| Generate GitHub File Path | `function` | Inspect parameters |
| GitHub Enabled? | `if` | Inspect parameters |
| Commit to GitHub (Approved) | `github` | file / createUpdate |
| Log Human Rejection | `function` | Inspect parameters |
| Merge Archivist Paths | `merge` | Inspect parameters |
| Evaluate Board Consensus | `function` | Inspect parameters |
| Check Redraft Needed | `if` | Inspect parameters |
| Handle Redraft | `function` | Inspect parameters |
| Process Agent Output | `function` | Inspect parameters |
| Slack Enabled? | `if` | Inspect parameters |
| Notify Slack | `slack` | Inspect parameters |
| Final Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Webhook Trigger → Check DB Connection (`main`, output 0, input 0)
- Check DB Connection → Meta-Orchestrator (`main`, output 0, input 0)
- Meta-Orchestrator → Parse Orchestration Plan (`main`, output 0, input 0)
- Parse Orchestration Plan → More Agents to Run? (`main`, output 0, input 0)
- More Agents to Run? → Prepare Agent Input (`main`, output 0, input 0)
- More Agents to Run? → Slack Enabled? (`main`, output 1, input 0)
- Prepare Agent Input → Route Agents with Switch (`main`, output 0, input 0)
- Route Agents with Switch → Summarizer Agent (`main`, output 0, input 0)
- Route Agents with Switch → Synthesizer Agent (`main`, output 1, input 1)
- Route Agents with Switch → Peer Reviewer Agent (`main`, output 2, input 2)
- Route Agents with Switch → Sensemaking Agent (`main`, output 3, input 3)
- Route Agents with Switch → Prompt Engineer Agent (`main`, output 4, input 4)
- Route Agents with Switch → Onboarding/Explainer Agent (`main`, output 5, input 5)
- Route Agents with Switch → Add Handbook Metadata (`main`, output 6, input 6)
- Summarizer Agent → Process Agent Output (`main`, output 0, input 0)
- Synthesizer Agent → Process Agent Output (`main`, output 0, input 0)
- Peer Reviewer Agent → Sensemaking Agent (`main`, output 0, input 0)
- Sensemaking Agent → Prompt Engineer Agent (`main`, output 0, input 0)
- Prompt Engineer Agent → Evaluate Board Consensus (`main`, output 0, input 0)
- Onboarding/Explainer Agent → Process Agent Output (`main`, output 0, input 0)
- Add Handbook Metadata → Generate Content for Review (`main`, output 0, input 0)
- Generate Content for Review → Generate Review ID (`main`, output 0, input 0)
- Generate Review ID → Send Review Request Email (`main`, output 0, input 0)
- Send Review Request Email → Wait for Human Approval (`main`, output 0, input 0)
- Wait for Human Approval → Human Decision Split (`main`, output 0, input 0)
- Human Decision Split → Save to handbook_entries (`main`, output 0, input 0)
- Human Decision Split → Log Human Rejection (`main`, output 1, input 0)
- Save to handbook_entries → Prepare Approved Contribution Data (`main`, output 0, input 0)
- Prepare Approved Contribution Data → Save Agent Contribution (Approved) (`main`, output 0, input 0)
- Save Agent Contribution (Approved) → Generate GitHub File Path (`main`, output 0, input 0)
- Generate GitHub File Path → GitHub Enabled? (`main`, output 0, input 0)
- GitHub Enabled? → Commit to GitHub (Approved) (`main`, output 0, input 0)
- GitHub Enabled? → Merge Archivist Paths (`main`, output 1, input 0)
- Commit to GitHub (Approved) → Merge Archivist Paths (`main`, output 0, input 0)
- Log Human Rejection → Merge Archivist Paths (`main`, output 0, input 0)
- Merge Archivist Paths → Process Agent Output (`main`, output 0, input 0)
- Evaluate Board Consensus → Check Redraft Needed (`main`, output 0, input 0)
- Check Redraft Needed → Handle Redraft (`main`, output 0, input 0)
- Check Redraft Needed → Process Agent Output (`main`, output 1, input 0)
- Handle Redraft → More Agents to Run? (`main`, output 0, input 0)
- Process Agent Output → More Agents to Run? (`main`, output 0, input 0)
- Slack Enabled? → Notify Slack (`main`, output 0, input 0)
- Slack Enabled? → Final Response (`main`, output 1, input 0)
- Notify Slack → Final Response (`main`, output 0, input 0)
- Notify Slack → Final Response (`error`, output 0, input 0)

## Verification and provenance

Selected from 2 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"javascript_syntax": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/generate-collaborative-handbooks-with-gpt4o-multi-agent-orchestration-human-review.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Deep/generate-collaborative-handbooks-with-gpt4o-multi-agent-orchestration-human-review.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
