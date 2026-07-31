# 📐 Main Code Execution Flow

---

# Purpose

This document captures the **current runtime execution flow** of **Project Foundation (PF)**.

Its purpose is to identify the orchestration path from the CLI entry point through the major subsystems responsible for repository discovery, model construction, parsing, and presentation.

Unlike the Code Architecture document, this document focuses on **execution order** and **runtime behavior**.

Implementation details remain documented within the corresponding Discovery Units and engineering assessments.

---

# Entry Point

```text
main()
```

Located in:

```text
src/pf/__main__.py
```

This function serves as the application entry point.

It parses CLI arguments and delegates execution to the appropriate command.

---

# Static Call Graph

The following illustrates the current function call hierarchy.

```text
main()
│
├── argparse.ArgumentParser()
│
├── scan()
│      └── cli/commands.py
│            │
│            ├── RepositoryScanner.scan()
│            │      └── scanner/filesystem.py
│            │
│            └── TreePrinter.print()
│                   └── printers/tree_printer.py
│
└── print_tree()
       └── cli/commands.py
             │
             ├── TreeParser.parse()
             │      └── parsers/tree_parser.py
             │
             └── TreePrinter.print()
                    └── printers/tree_printer.py
```

This view is intended primarily for navigation.

---

# Runtime Execution Flow

Example execution:

```bash
pf scan .
```

Execution sequence:

```text
[CLI Entry Point]
        │
        ▼
__main__.py

        │
        ├── Parse CLI arguments
        │
        ├── Resolve command
        │
        └── Execute scan()
                │
                ▼
commands.py

        │
        ├── Validate repository path
        │
        ├── RepositoryScanner.scan()
        │
        │       filesystem.py
        │
        │       ├── Create Repository
        │       ├── Traverse directories
        │       ├── Apply ignore rules
        │       ├── Build Directory nodes
        │       ├── Build File nodes
        │       └── Return Repository model
        │
        └── TreePrinter.print()
                │
                ▼
tree_printer.py

        │
        ├── Traverse Repository
        ├── Format hierarchy
        ├── Optionally compute file sizes
        └── Render tree
```

---

# Tree Replay Execution Flow

Example execution:

```bash
pf tree repository.tree
```

Execution sequence:

```text
[CLI Entry Point]
        │
        ▼
__main__.py

        │
        ├── Parse CLI arguments
        │
        └── Execute print_tree()
                │
                ▼
commands.py

        │
        ├── TreeParser.parse()
        │
        │       tree_parser.py
        │
        │       ├── Read tree file
        │       ├── Parse indentation
        │       ├── Reconstruct hierarchy
        │       ├── Create Repository model
        │       └── Return Repository
        │
        └── TreePrinter.print()
                │
                ▼
tree_printer.py

        └── Display repository tree
```

---

# Execution Phases

| Phase                   | Primary Function           | Primary Module             |
| ----------------------- | -------------------------- | -------------------------- |
| CLI Initialization      | `main()`                   | `__main__.py`              |
| Command Resolution      | `scan()` / `print_tree()`  | `commands.py`              |
| Repository Discovery    | `RepositoryScanner.scan()` | `scanner/filesystem.py`    |
| Ignore Filtering        | `should_ignore()`          | `scanner/filesystem.py`    |
| Repository Construction | `Directory.add()`          | `models/node.py`           |
| Tree Parsing            | `TreeParser.parse()`       | `parsers/tree_parser.py`   |
| Tree Rendering          | `TreePrinter.print()`      | `printers/tree_printer.py` |

---

# Major Module Participation

| Module        | Responsibility                                           |
| ------------- | -------------------------------------------------------- |
| CLI           | Application entry point and argument parsing             |
| Commands      | Runtime orchestration                                    |
| Scanner       | Repository discovery                                     |
| Models        | Repository object graph                                  |
| Parser        | Tree deserialization                                     |
| Printer       | Tree visualization                                       |
| Configuration | Project metadata and CLI registration (`pyproject.toml`) |

---

# Runtime Architecture

The current execution architecture is intentionally layered.

```text
CLI
        │
        ▼
Commands
        │
        ▼
Scanner / Parser
        │
        ▼
Repository Model
        │
        ▼
Printer
```

Each subsystem owns a single engineering responsibility.

---

# Related Discovery Documents

## Discovery

* `01-current-pf-codebase.md`
* `02-pf-code-validation.md`
* `03-code-architecture.md`

---

# Related Discovery Units

| Discovery Unit        | Scope                               |
| --------------------- | ----------------------------------- |
| CLI                   | `__main__.py`, `commands.py`        |
| Models                | `node.py`, `repository.py`          |
| Scanner               | `filesystem.py`, `ignore.py`        |
| Tree Serialization    | `tree_parser.py`, `tree_printer.py` |
| Project Configuration | `pyproject.toml`                    |

---

# Discovery Notes

This document intentionally describes **runtime orchestration only**.

Implementation details, engineering observations, validation notes, and future improvements are documented within the corresponding Discovery Units.

As Project Foundation evolves, additional execution flows (Repository Packaging, Discovery Package Generation, AFK Integration, etc.) should be documented as separate execution-flow documents under:

```text
_docs/
└── 01-discovery/
    └── code-execution-flow/
```

to preserve readability and maintainability.

---

## Metadata

| Field    | Value               |
| -------- | ------------------- |
| Document | `main-flow.md`      |
| Scope    | Project Foundation  |
| Category | Discovery           |
| Type     | Code Execution Flow |
| Status   | Reviewed            |
| Version  | 1.0                 |
| As Of    | 07.30.2026          |
