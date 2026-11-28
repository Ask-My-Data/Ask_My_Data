# Ask My Data

[![CI](https://github.com/Ask-My-Data/Ask_My_Data/actions/workflows/ci.yml/badge.svg)](https://github.com/Ask-My-Data/Ask_My_Data/actions/workflows/ci.yml)

Multi-agent engine to query structured data (PostgreSQL, CSV) in natural language, with traceable answers: executed SQL, sources and agent steps.

## Requirements

- [uv](https://docs.astral.sh/uv/) (also installs Python 3.12 if needed)
- Git

## Installation

```bash
git clone git@github.com:Ask-My-Data/Ask_My_Data.git
cd Ask_My_Data
uv sync
uv run pre-commit install
uv run askmydata --help
```

## Development commands

| Action | Command |
|--------|---------|
| Lint | `uv run ruff check` |
| Format | `uv run ruff format` |
| Type check | `uv run mypy` |
| Tests | `uv run pytest` |
| All hooks | `uv run pre-commit run --all-files` |

Pre-commit hooks automatically run lint, formatting and type checking on every commit.

The CI pipeline (`.github/workflows/ci.yml`) runs on every pull request to `main`: lint, format check, type check, tests and dependency vulnerability audit. A pull request cannot be merged until it passes.

Add a dependency: `uv add <package>` (or `uv add --dev <package>` for a development tool). The `uv.lock` file is committed.

## Repository layout

```
src/askmydata/
├── harness/      Agentic loop, sessions, tool registry, traces
├── agents/       Supervisor, Discovery, SQL Analyst, Validator
├── connectors/   Common interface, PostgreSQL, CSV/DuckDB
├── sql/          SQL validation and read-only policy
├── rag/          Indexing and retrieval (schemas and business documentation)
├── api/          FastAPI backend shared by the CLI and the Web app
├── cli/          Command-line interface (Typer)
└── web/          Web interface (templates and static files)
tests/            Unit, integration and end-to-end tests
```
