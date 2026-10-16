# Provenance and adaptations

## Local ClickUp core

The seven core skills derive from the local refactor snapshot and matching installed copies. All 19 original files matched before staging and remain unchanged. No enclosing Git repository was available. The user subsequently authorized public MIT publication of the core and clarified that it contains ClickUp working methods rather than customer material. Earlier before/after snapshots and historical artifacts were checked for publication risk, then excluded. No source history, transcript or private source URL is bundled.

## Verified public supplementary sources

The comparison downloaded public primary-source files at specific GitHub commits and compared them with the installed source after normalizing whitespace. This identifies the inherited source text, not just similar filenames. Only hashes, revisions and comparison results are retained in adjacent local review evidence.

| Installed source | Public source | Evidence |
| --- | --- | --- |
| `codebase-design` | [matching revision](https://github.com/mattpocock/skills/blob/ee8bae40062cd6b435073368ed0c540f48c35862/skills/engineering/codebase-design/SKILL.md) | Whitespace-normalized exact match; MIT license verified at the same commit |
| `domain-modeling` | [matching revision](https://github.com/mattpocock/skills/blob/ee8bae40062cd6b435073368ed0c540f48c35862/skills/engineering/domain-modeling/SKILL.md) | Whitespace-normalized exact match; MIT license verified at the same commit |
| `to-prd` | [matching revision](https://github.com/mattpocock/skills/blob/3832253f149ea165f45a32ea727886e6d0094d60/skills/engineering/to-prd/SKILL.md) | Whitespace-normalized exact match; MIT license verified at the same commit |
| `to-issues` | [matching revision](https://github.com/mattpocock/skills/blob/788b5c382b769155afcbac0d8402c3b56eae02fd/skills/engineering/to-issues/SKILL.md) | Whitespace-normalized exact match; MIT license verified at the same commit |
| `karpathy-guidelines` | [multica-ai revision](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md) | Whitespace-normalized exact match; source declares MIT but full license/copyright notice is absent from the inspected tree |

Only the Karpathy-named supplement carries the four adapted engineering themes from the Karpathy-inspired source. The four other supplements are Matt Pocock's work. No evidence attributes the seven ClickUp stages, their templates, PRD synthesis, issue decomposition, domain modeling or deep-module vocabulary to Karpathy. General overlap in engineering advice is not proof of derivation or authorship.

## Kit adaptations

The draft keeps stage routing and explicit external-write scope, replaces machine-specific symlinks with real files, rewrites templates, and removes fixed language/timezone/search/estimate/company defaults. `to-prd` and `to-issues` become local drafting supplements without tracker setup, labels, automatic publication or mandatory interviews. `domain-modeling` no longer creates repository glossary/ADR files automatically during collection. `codebase-design` stays within scoped interface planning. `karpathy-guidelines` is a short engineering aid.

Original skills are not represented as tested cross-runtime implementations. For standard installation, the two explicit-only supplements contain Claude frontmatter alongside their existing Codex policy. The fallback installer preserves this metadata without duplicating it. Provider-specific Azure/LINE/pstack helpers are optional and not bundled. New scripts, examples and documentation are covered by the scoped original-contribution MIT grant. Full upstream MIT notices accompany the four Matt Pocock adaptations.

See [license scope](license-scope.md), [third-party notices](../THIRD_PARTY_NOTICES.md) and [runtime evidence](runtime-support.md).
