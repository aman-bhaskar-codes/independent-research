# Independent Research

This repository is my central research workspace and public research hub. It supports multiple independent research programmes over time, containing research planning, reading notes, experiments, code, reproducibility information, and negative results.

> **Note**: This initial repository is a scaffold and currently contains no completed experimental findings.

## Start Here

| Area | Description | Location |
|---|---|---|
| **Programmes** | Broad research themes and long-term questions | [`programmes/`](./programmes/) |
| **Projects** | Specific, bounded experimental investigations | [`projects/`](./projects/) |
| **Writing** | Blogs, articles, and research papers | [`writing/`](./writing/) |
| **Reading** | Literature notes and bibliography | [`reading/`](./reading/) |
| **Templates** | Copyable starting points for all content types | [`templates/`](./templates/) |
| **Docs** | Conventions, workflows, and decision records | [`docs/`](./docs/) |
| **Roadmap** | High-level plan for the repository | [`ROADMAP.md`](./ROADMAP.md) |

## Research Structure

This repository separates research into three distinct categories:

- **Programme**: Groups related research questions under a broad theme. Example: *Reliable Autonomous Learning*.
- **Project**: Investigates a bounded question with specific experiments, data, and code. Example: *Improvement Verification Harness*.
- **Publication**: Communicates work and links to its supporting projects. Includes blogs, articles, and formal research papers.

Each artifact lives in one authoritative location. Publications reference projects by identifier; projects reference programmes. Nothing is duplicated.

## Current Research Direction

### Initial Programme: Reliable Autonomous Learning (RAL)

The initial research programme focuses on Reliable Autonomous Learning (RAL). Its central concern is establishing trustworthy evidence that an autonomous system genuinely improves from experience, generalizes to unseen tasks, preserves previous capabilities, and avoids evaluator gaming.

RAL is the first programme, not the permanent boundary of this repository. See the [RAL Programme](./programmes/ral/README.md) for the constitution, open questions, and scientific roadmap.

### Initial Project: Improvement Verification Harness

The first planned project under the RAL programme is the Improvement Verification Harness. This project aims to design a rigorous protocol for verifying adaptation in autonomous agents, narrowed to small coding tasks with execution-based scoring.

See the [project brief and draft protocol](./projects/improvement-verification/README.md).

## Publications

Publications are strictly separated by type. No completed publications exist yet.

- **[Blogs](./writing/blogs/)**: Accessible explanations, learning reflections, and progress updates.
- **[Articles](./writing/articles/)**: Substantial technical explainers, literature syntheses, and perspectives.
- **[Research Papers](./writing/papers/)**: Formal studies with explicit questions, methods, evidence, limitations, and defensible contributions.

## Repository Map

```
independent-research/
├── README.md                          ← You are here
├── ROADMAP.md                         ← High-level plan
├── CONTRIBUTING.md                    ← How to engage
├── CHANGELOG.md                       ← Notable changes
├── CODE_OF_CONDUCT.md
├── .gitignore
├── .editorconfig
├── programmes/                        ← Research programmes
│   └── ral/                           ← Reliable Autonomous Learning
│       ├── constitution.md
│       ├── questions.md
│       ├── roadmap.md
│       └── sources/                   ← Origin documents
├── projects/                          ← Experimental projects
│   └── improvement-verification/      ← First project
│       ├── protocol.md                ← Draft experimental protocol
│       ├── src/                       ← Harness implementation
│       ├── configs/                   ← Experiment configs
│       ├── experiments/               ← Run records
│       ├── analysis/                  ← Analysis scripts
│       ├── results/                   ← Raw outputs
│       ├── tests/                     ← Infrastructure tests
│       └── environment/               ← Sandbox definitions
├── writing/                           ← Publications
│   ├── blogs/
│   ├── articles/
│   └── papers/
├── reading/                           ← Literature
│   ├── bibliography.bib
│   └── notes/
├── templates/                         ← Copyable templates
│   ├── programme.md
│   ├── project.md
│   ├── experiment.md
│   ├── reading-note.md
│   ├── blog.md
│   ├── article.md
│   ├── paper/
│   └── decision-record.md
├── docs/                              ← Conventions and decisions
│   ├── conventions.md
│   ├── reproducibility.md
│   ├── publication-workflow.md
│   ├── licensing.md
│   └── decisions/
├── scripts/
│   └── check_repository.py           ← Local repository checker
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── pull_request_template.md
    └── workflows/
        └── checks.yml                ← CI checks
```

## How to Add Content

### Add a Programme

1. Copy [`templates/programme.md`](./templates/programme.md) to `programmes/<name>/README.md`.
2. Fill in the `id`, `title`, `status`, and `created` frontmatter fields.
3. Create `constitution.md`, `questions.md`, and `roadmap.md` alongside it as the programme develops.
4. Add an entry to [`programmes/README.md`](./programmes/README.md).

### Add a Project

1. Copy [`templates/project.md`](./templates/project.md) to `projects/<name>/README.md`.
2. Fill in the `id`, `title`, `status`, `programme`, and `created` frontmatter fields.
3. Create subdirectories as needed: `src/`, `configs/`, `experiments/`, `analysis/`, `results/`, `tests/`, `environment/`.
4. Write a `protocol.md` describing the experimental design before running experiments.

### Add an Experiment Record

1. Copy [`templates/experiment.md`](./templates/experiment.md) to `projects/<project>/experiments/<experiment-name>.md`.
2. Fill in all frontmatter fields, especially `code_commit`, `dataset_version`, and `run_timestamp`.
3. Record any deviations from the planned protocol explicitly.

### Add a Reading Note

1. Copy [`templates/reading-note.md`](./templates/reading-note.md) to `reading/notes/<descriptive-name>.md`.
2. Fill in the frontmatter and add the corresponding BibTeX entry to [`reading/bibliography.bib`](./reading/bibliography.bib).

### Add a Blog, Article, or Paper

1. Copy the relevant template from [`templates/`](./templates/) to `writing/blogs/`, `writing/articles/`, or `writing/papers/`.
2. For papers, copy the entire `templates/paper/` directory.
3. Fill in the frontmatter metadata. Update `status` as the piece progresses—see [`docs/publication-workflow.md`](./docs/publication-workflow.md) for valid statuses.
4. Topic tags can be added or changed freely without moving files.

## Research Standards

This research adheres to strict standards for scientific integrity:

- **Provenance**: All claims must be traceable to specific experiments and code commits.
- **Controls**: Baselines and ablations are required to validate improvements.
- **Reproducibility**: Environment, configuration, and seed details must be recorded for all runs. See [`docs/reproducibility.md`](./docs/reproducibility.md).
- **Uncertainty & Limitations**: Results must discuss variance, failure modes, and limitations.
- **Negative Results**: Failed approaches and hypotheses are explicitly documented, not silently discarded.

## Local Checks

Run the repository checker to validate links, required files, and metadata:

```bash
python3 scripts/check_repository.py
```

This runs automatically in CI on push and pull request to `main`.

## Contributing

This repository is primarily for independent research, but I welcome feedback and discussions. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licensing

No license has been selected yet. Code, writing, and data may receive different licenses in the future. See [`docs/licensing.md`](./docs/licensing.md) for details.
