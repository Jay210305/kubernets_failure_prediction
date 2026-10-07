# System-map method for this repository

Use this reference when `map/CONTEXT.md` no longer answers what an object is or what a change affects within two reads. Keep the project tree as source of truth; the map cites it and does not become a second specification.

## Status vocabulary

- **live**: in force; implement and cite against it.
- **leftover**: still present but not the main path; touch only when that path is in scope.
- **ghost**: named or documented but not wired. Do not implement against it.
- **missing**: required for the research path but absent or unverified.

State both the project name and filename when they differ. For runtime claims, distinguish configured, documented, and observed state.

## Map slices

1. **Inventory:** list the in-scope files and classify them as catalog, contract, factory/reference, product/output, or possibly dead. Do not move or delete files in this pass.
2. **Catalog:** keep a concise object index with one line per noun, source of truth, status, and first-order impact. Add a folder contract when a working area lacks inputs, process, outputs, and human check.
3. **Objects:** add a card only when a concept needs more than the catalog row. Cite the owning code or document, explain the design reason, connections, first-order hits, consumers, and source path.
4. **Processes:** document only movements that really run or are followed. Use `Input → Movement → Output`, numbered steps with source citations, and links to the affected objects.
5. **Impact routes:** for each common change, list which cards/files to open. Keep dependency chains in the cards rather than copying them into a second waterfall.
6. **Recheck:** verify load-bearing claims and links against source after edits. If proposing a move, first find in-tree and known external referrers; copy and compare before removal. Never silently archive an apparently unused file.

Do not create empty `objects/`, `processes/`, or `effects/` folders. This repository currently fits one catalog (`map/CONTEXT.md`); add structure only when there is a real need.

## Walk test

A cold agent should be able to answer where to learn about a concept and what a change hits from `AGENTS.md`, this map, and at most one cited source. Every folder-level contract names exact inputs, its job, outputs, and a human review step. Status should be derivable from the files and explicit frontmatter, not from conversational memory.
