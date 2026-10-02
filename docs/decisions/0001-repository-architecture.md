# Repository Architecture Decision

**Date:** 2026-10-02
**Status:** Accepted

## Context
This repository serves as a central hub for long-term independent research. It needs to support multiple concurrent or sequential research programmes without becoming disorganized. It must also handle a mix of prose (blogs, papers) and code (experiments), while maintaining clear traceability between claims and evidence.

## Decision
We adopt a structured architecture with explicit separation of concerns:
- **Programmes**: High-level groupings of related research questions.
- **Projects**: Bounded experimental investigations.
- **Writing**: Public communication (blogs, articles, papers).
- **Reading**: Literature notes and bibliographies.

## Consequences
- **Easier navigation**: Clear separation makes it obvious where to find or place specific artifacts.
- **Traceability**: Writing and projects are explicitly linked through metadata.
- **Flexibility**: New programmes can be added without disrupting existing ones.
- **Maintenance**: Requires adherence to templates and structure, enforced by a lightweight check script.
