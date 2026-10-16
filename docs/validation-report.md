# Local validation results

The checks used local files and disposable temporary directories on this Mac. Nothing was installed over existing user skills. No ClickUp calls, model runs, remote repository writes, uploads or sharing changes were made. Public GitHub sources and the existing authenticated account/destination were inspected read-only.

## Observed checks

The initial public payload contains 63 UTF-8 text files and 11 skills. All 163 local file links resolve. The exact publication payload is scanned separately from adjacent review evidence, and no source Git history or Karpathy implementation is included.

- All 11 included skills have matching folder/name metadata and nonempty descriptions. The installed Codex skill-authoring validator passed all 11 included skills using an existing Python 3.10.4 environment with PyYAML. No package installation was needed. The first attempt under Python 3.15 lacked PyYAML; the kit's own validator and scripts use only the standard library.
- All local Markdown file links resolve within the kit. The validator rejects linked files and checks common personal-path, email, production ClickUp URL, credential and provider-token patterns. Exact file/link counts are printed by `scripts/validate.py` and recorded in the local review evidence.
- Fourteen installer tests pass under Python 3.10.4 and 3.15.0. They cover a no-write preview, byte-identical Codex copies, repeat refusal, all-or-nothing collision preflight, dangling links, a linked destination/source, preservation of unrelated files, unsupported runtime refusal and cleanup after copy failure. Claude project/personal layout, explicit-only metadata adaptation, notice preservation, source immutability and collision refusal are exercised without launching a model or editing account configuration.
- Codex CLI 0.163.0 discovered all 11 included skills from a fresh temporary `CODEX_HOME/skills` location with zero parsing errors. The check used local app-server initialization and `skills/list`, without a conversation/model run or live account configuration. Temporary runtime data was removed.
- SHA-256 checks confirm that all 19 core source files and matching installed copies are unchanged from the initial snapshot. No source history was copied.
- Before/after snapshots, historical evaluation fixtures, transcripts and previous packaging artifacts were checked for publication risks. Personal paths, real task links and identifier-like strings occur in historical material. It is excluded from the draft. Credential-like pattern hits were not printed or treated as proof of a live credential.
- The offline task and output examples contain fictional role labels and identifiers. They illustrate evidence status, scoped unknowns and the local-write boundary. They are hand-prepared examples rather than a model evaluation.

## Remaining limitations

An earlier Claude Code version command timed out. A later isolated attempt failed during CLI startup. The installer now supports the documented Claude layout and translates the two explicit-invocation policies, but Claude runtime loading, invocation and live integration remain unverified. Live ClickUp collection/publication and provider-specific workflows were not exercised. Runtime discovery does not prove behavioral quality.

No dedicated secret-scanner executable was available. Pattern scans do not establish the absence of every secret or customer reference. Original contributions now have an authorized MIT grant attributed to the configured Git author. All four Matt Pocock supplements have exact normalized historical matches and verified same-commit MIT notices. The Karpathy-inspired source declares MIT but lacks a full copyright/permission notice in the inspected tree. The user resolved the core-rights question and authorized public MIT publication; inspect actual files before publishing. This report covers the 11-skill public package. The unresolved Karpathy adaptation is not included.

## Repeat the packaged checks

```sh
python3 scripts/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```
