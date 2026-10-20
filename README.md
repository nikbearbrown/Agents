# Agents

**One purpose, multiple implementations, explicit evidence.** Curated by Nik Bear Brown.

Explore the [searchable website](https://www.bearbrown.co/agents), [agent catalog](CATALOG.md), or [machine-readable index](agents-catalog.json).

## What is here

There are **1,877 agent packages**: **1,876 collected n8n workflow families**, plus **Lectern job search**, an original multi-workflow package. “Agent” is an organizational term: many entries are deterministic automations and do not involve model judgment.

Each `agents/<slug>/` folder holds a shared specification, a Mermaid diagram, implementation records, and separate build/operate instructions for Claude, Codex, Grok Bot, Muse and Dots. Every collected package retains its sanitized n8n source under `implementations/n8n/`. Python, Pydantic AI, CrewAI Flow, CrewAI Crew and LangGraph targets have porting plans. **A planned folder or an untested prompt is not a working implementation.**

The first specifications and Mermaid maps are derived from source structure. They preserve observed nodes and connections rather than inventing a verified business process. Review intent, schemas, side effects and expected outputs before treating them as a shared behavioral contract. Ten collected sources have structural graph findings recorded in their agent metadata and the migration report.

## Start here

- [Telegram echo-bot](agents/telegram-echo-bot/README.md): a small source graph to inspect.
- [Lectern job search](agents/lectern-job-search/README.md): five workflows with preserved fixtures and reported parity tests.
- [All collected agents](CATALOG.md): existing source templates and their implementation plans.
- [Architecture and contribution contract](ARCHITECTURE.md): how to add an implementation without duplicating an agent.
- [Migration review](MIGRATION.md): validation results, source findings and next implementation work.
- [Migration details](migration.json): original paths, new paths and unchanged source hashes.

## Use an implementation

Read the agent specification and the selected implementation README. Import n8n JSON inactive, or follow an implemented backend's setup. Supply your own credentials outside source control. Inspect external destinations and test synthetic inputs before enabling writes or schedules. A prompt's operating section does not authorize unattended work.

## Evidence means what it says

- `source-available`: code or workflow exists; execution has not been established.
- `planned`: instructions exist, but no executable port is supplied.
- `reported-fixture-tested`: previous test reports are retained; read their scope and dates.
- `fixture-tested`: local deterministic tests have been run and recorded; live services may remain unverified.
- `live-tested`: requires a dated, scoped receipt; never inferred from a successful import.

The bulk collection is not runtime-tested. Agreement between implementations is evidence of parity, not proof of correctness. Model decisions need independent labels and failure tests. Public logs must be sanitized; private payloads and credentials do not belong here.

## Provenance, licensing and compatibility

The original collection selected 1,900 families from 8,070 snapshots; 24 formatting-only pairs were subsequently consolidated to 1,876. See [consolidation.json](consolidation.json). The Agents migration does not rewrite any collected n8n JSON bytes. Per-source provenance, configuration records and [license notices](licenses/) remain intact. No blanket license overrides the original licenses, and curation is not a claim of authorship.

The repository was named `N8N`. GitHub's repository rename preserves repository redirects. Old `workflows/<slug>/README.md` paths are compatibility landing pages, not duplicate agents. Moved raw GitHub JSON paths are listed in migration.json with their original commit for recovery; website JSON download URLs remain stable. Do not create another `nikbearbrown/N8N` repository, which would displace the old-name redirect.

Run `python3 scripts/validate.py` for publication checks and `python3 scripts/validate_agents.py` for package, diagram, prompt, hash and local-link checks. Validation does not execute workflows. See [ANNOTATION.md](ANNOTATION.md) for annotation policy.
