# Runtime support and evidence

| Environment | Verified evidence | Unverified boundary |
| --- | --- | --- |
| Codex CLI 0.163.0 | Isolated local `skills/list` discovered all 11 included skills with zero parse errors from `CODEX_HOME/skills`; installer behavior is retested for this revision | Model behavior and live ClickUp |
| Claude Code | Official skill locations and invocation metadata checked; temporary project/personal installation tests exercise the adapter | Installed CLI fails startup in an isolated configuration; runtime loading and live integration are unverified |
| Python 3.10.4 and 3.15.0 | Local validation and installer tests | Other versions |

The installer accepts `codex` and `claude-code`, requires an explicit destination and previews by default. It does not infer a user/project target, edit account configuration or overwrite existing skill names. Claude installs adapt only the two explicit-only supplements, with the source files left unchanged. See [Claude instructions](claude-code.md).

For an isolated Codex smoke test, use a new temporary parent with its own `skills` directory and set `CODEX_HOME` for that process. No credentials or connector settings need copying. An arbitrary copy destination is not automatically a discoverable runtime location.

The kit bundles neither the runtimes nor a ClickUp connector. Installation, discovery, invocation and read/write integration are separate checks. A later live test needs its own authorized target and scope.
