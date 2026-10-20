# Tech Radar: shared specification

**Status: source-derived draft.** The source contains 37 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

## Purpose

Adapt the published “Tech Radar” workflow to other implementations while preserving its documented behavior.

The title is inherited from the source, not proof of intent. Confirm the actual user outcome before porting. Deterministic automations are included in this library; “agent” does not imply autonomous model judgment.

## Observed entry points

- Cron
- Google Drive - Doc File Updated
- When Executed by Another Workflow
- API Request - Webhook

## Terminal nodes

- Doc File Data Loader
- MySQL - insert all from sheets
- Google Docs - Update GDoc
- Content - Recursive Character Text Splitter
- 1_Get DB Schema and Tables List
- 2_Get Table Definition
- 3_Execute actual query
- AI Agent -DB Sql Agent
- Pinecone Vector Store (Retrieval)
- 4_RagTool
- AI Agent - RAG
- Embeddings - Tech Radar Data Embedding
- Pinecone - Vector Store for Embedding Content
- Retrieve Embeddings - Tech Radar Vector DB
- AI Agent - Retrieval
- AI Chat Model - Claude 3.5 Sonnet
- AI Chat Model - QwQ 32b
- AI Chatmodel - Deepseek 32B
- AI Chat Model - llama3-8b
- API Response - Respond to Webhook
- User Conversation history

## Inputs, outputs, decisions and state

Input and output schemas are not yet established. Read the exact parameters, expressions, prompts, code, branch ports, retries, disabled nodes, and execution settings in the n8n implementation. A terminal node is a graph endpoint, not necessarily a user-facing output. Model/tool links are dependencies, not necessarily sequential control flow.

## Required access

Declared credential types: `anthropicApi`, `googleApi`, `googleDriveOAuth2Api`, `googlePalmApi`, `googleSheetsOAuth2Api`, `groqApi`, `mySql`, `pineconeApi`. Use local credentials or environment variables, never public exports.

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
