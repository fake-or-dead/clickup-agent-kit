# Installation validation results

The installation update was tested in disposable project directories with npm cache/config isolated and skills CLI telemetry disabled. No existing user skills or authentication configuration was changed. The tests made no live ClickUp calls or model requests.

## Standard CLI checks

- Official skills CLI 1.7.2 was tested with Node.js 26.12.0. Its npm package requires Node.js 22.20 or later.
- Remote discovery of `fake-or-dead/clickup-agent-kit` found all 11 skills and left the discovery project's contents unchanged.
- The published baseline installed into both Codex and Claude Code project layouts using symlink and copy modes. All 39 supporting skill files matched the source bytes, and all 43 relative links within the installed skills resolved for each agent.
- The candidate preserves the two explicit-only supplements through source Claude frontmatter and the existing Codex policy. Standard CLI installation of the local candidate passed both modes, with the same complete files, references/templates, license notices and links. No custom post-install transformation is needed.
- Codex CLI 0.163.0 discovered all 11 candidate skills from the standard project `.agents/skills` installation with zero parsing errors. This used local app-server `skills/list` with an isolated configuration directory and no model run.
- Global scope is documented from official CLI/runtime sources but was not installed into the real user home. The interactive documentation command uses the same source/skill/agent flags as the noninteractive tests, which added `--yes`.

## Package and fallback checks

The package validator checks all local file links, naming/frontmatter, both explicit-only policies, symlinks and common publication-risk patterns. Exact current counts are printed by `scripts/validate.py`. Full YAML parsing separately confirms names/descriptions and boolean policy values for all 11 skills.

Fourteen fallback-installer tests cover no-write preview, byte preservation, collision/symlink refusal, preservation of unrelated files, copy-failure cleanup, both Claude layouts and non-duplicated explicit-only metadata. They pass on Python 3.10.4 and 3.15.0. Python is needed only for these checks or fallback installation, not the primary CLI route.

The older Codex-only scaffold validator rejects the Claude-specific `disable-model-invocation` key on two skills. Its fixed key allowlist is not a cross-runtime parser. Those files are instead checked with full YAML parsing, the kit's policy validator and actual Codex discovery, which accepts them without parse errors. No installed validator or skill was modified.

## Limits and preservation

Claude runtime loading, model behavior and live ClickUp integration remain unverified because the installed Claude CLI failed startup during the earlier isolated check. File installation and metadata preservation are separate evidence from runtime execution. No scheduler or background monitoring is bundled.

MIT terms and upstream notices remain intact. The unresolved Karpathy implementation remains excluded. Original source/installed skill preservation checks and the earlier publication scan are kept in separate local review evidence. No source Git history or private/customer examples are introduced by this update. Pattern scans cannot guarantee discovery of every secret or customer reference.

## Repeat packaged checks

```sh
python3 scripts/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```
