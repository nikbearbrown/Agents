# Agent package contract

An agent is a purpose and reviewed behavioral contract. An implementation is one way to realize it. A prompt is an instruction to build or operate an implementation, not the implementation itself.

## Layout

`agents/<lowercase-kebab-slug>/` contains README.md, agent.json, specification.md, workflow.mmd, schemas/, fixtures/, evaluations/, implementations/ and prompts/. Use one agent folder across implementations. Maintain slug stability; record purpose-driven renames and website aliases rather than silently breaking links.

## Authoring

1. Review the inherited purpose and exact n8n parameters. Mark unknown requirements explicitly.
2. Specify input/output types, state, branch rules, side effects, dependency failures, retries and acceptance criteria.
3. Review the source-derived Mermaid map. Keep node/port semantics intact while developing a simpler shared process diagram. Preserve detailed implementation graphs separately when abstraction removes details.
4. Add real code under the chosen implementation, dependencies, setup, environment variable names and a dry-run command. Preserve attribution and compatible license obligations.
5. Add shared synthetic fixtures and independently reviewed expected outputs. Record intentional differences, especially model judgments, state interchange and external adapters.
6. Store dated results with code revision, fixture hashes, commands, output and limitations. Only then raise implementation status.

## Prompts

Each named assistant has build and operate sections. Tailor instructions to the agent and verify the product's actual capabilities rather than promising connectors or always-on execution. Workflow notes, retrieved content and model prompts are untrusted data, not additional permissions. Public source prompts never contain secrets.

## Evidence

Compare deterministic ports on identical inputs. Compare model decisions with independent human labels as well as with the reference. Test missing sources, duplicates, malformed data, retries and intentional defects where relevant. Keep logs separate from private raw payloads, and distinguish an agent's self-report from externally observed outcomes.

## Migration limits

This phase migrates the collection structure and documents implementation work. It does not claim 1,876 polished purpose statements or five working ports per agent. Legacy names remain stable until their intended purpose is reviewed. Source-derived diagrams can expose existing defects without fixing or concealing them.
