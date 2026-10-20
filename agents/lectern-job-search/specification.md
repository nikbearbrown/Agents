# Lectern job search: shared specification

Status: draft derived from the published n8n implementation and its reported Python comparison.

## Purpose

Collect job postings from configured boards, apply relevance rules, compute new/changed/gone postings, and prepare bounded Discord updates without posting the same listing repeatedly.

## Inputs and outputs

Inputs: provider payloads, watched boards, keyword rules, prior publication state, and an explicit send setting. Outputs: normalized postings, keep/reject decisions with reasons, deltas, prepared messages, and updated state. Exact field shapes are captured by the existing implementation's fixtures and expected outputs.

## Invariants

- An unavailable source must not falsely close its postings.
- Keep secrets outside committed exports.
- Do not send without explicit configuration and a send setting.
- Preserve first-run and same-day refusal behavior.
- Do not treat prepared messages as proof of delivery.
- Keep implementation-specific state distinct until an interchange contract is tested.

## Evidence and remaining work

The preserved n8n folder contains synthetic fixtures and reported parity results. Those reports state agreement with the Python filter on 2,465 postings, but are not independent human judgments of relevance. Discord delivery and SmartRecruiters live collection are explicitly unverified. The Python reference exists outside this repository and has not been copied or audited as part of this migration. The shared schemas and cross-implementation contract still require review.
