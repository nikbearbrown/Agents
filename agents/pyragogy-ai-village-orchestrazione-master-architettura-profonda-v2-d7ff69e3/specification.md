# Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2): shared specification

**Status: source-derived draft.** The source contains 36 executable nodes and 0 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

## Purpose

Adapt the published “Pyragogy AI Village - Orchestrazione Master (Architettura Profonda V2)” workflow to other implementations while preserving its documented behavior.

The title is inherited from the source, not proof of intent. Confirm the actual user outcome before porting. Deterministic automations are included in this library; “agent” does not imply autonomous model judgment.

## Observed entry points

- Start
- Webhook Trigger

## Terminal nodes

- Start
- Webhook Trigger
- Check DB Connection
- Meta-Orchestrator
- Parse Orchestration Plan
- More Agents to Run?
- Prepare Agent Input
- Route Agents with Switch
- Summarizer Agent
- Synthesizer Agent
- Peer Reviewer Agent
- Sensemaking Agent
- Prompt Engineer Agent
- Onboarding/Explainer Agent
- Add Handbook Metadata
- Generate Content for Review
- Generate Review ID
- Send Review Request Email
- Wait for Human Approval
- Human Decision Split
- Save to handbook_entries
- Prepare Approved Contribution Data
- Save Agent Contribution (Approved)
- Generate GitHub File Path
- GitHub Enabled?
- Commit to GitHub (Approved)
- Log Human Rejection
- Merge Archivist Paths
- Evaluate Board Consensus
- Check Redraft Needed
- Handle Redraft
- Process Agent Output
- Slack Enabled?
- Notify Slack
- Final Response
- Error Handler

## Inputs, outputs, decisions and state

Input and output schemas are not yet established. Read the exact parameters, expressions, prompts, code, branch ports, retries, disabled nodes, and execution settings in the n8n implementation. A terminal node is a graph endpoint, not necessarily a user-facing output. Model/tool links are dependencies, not necessarily sequential control flow.

## Required access

Declared credential types: `emailSend`, `githubApi`, `openAiApi`, `postgres`. Use local credentials or environment variables, never public exports.

## Port acceptance criteria

- Write a reviewed purpose and concrete input/output schema.
- Preserve identifiers, ordering, routing ports, expressions, state semantics, retries, and disabled behavior unless a documented change is intended.
- Add representative success, empty-input, malformed-input, authentication failure, unavailable dependency, and duplicate/retry fixtures where relevant.
- Start with fixtures and dry-run adapters. No messages, writes, purchases, or scheduled work from a build prompt.
- Compare deterministic translations on identical fixtures. Measure model judgments against human-labeled examples separately from agreement with the old implementation.
- Record code revision, fixture hash, command, observed output and limitations. Never infer a passing test from a diagram or a generated explanation.

## Unresolved questions

- Define input/output schemas and expected outputs.
- Review source expressions, external actions, and failure behavior.
- Determine whether model judgment is required or deterministic rules suffice.
