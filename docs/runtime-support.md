# Runtime support and evidence

| Environment | Verified evidence | Unverified boundary |
| --- | --- | --- |
| Codex CLI 0.163.0 | Standard CLI project installation into `.agents/skills`, followed by isolated local `skills/list`, discovered all 11 included skills with zero parse errors and the dual-runtime metadata present | Model behavior and live ClickUp |
| Claude Code | Standard skills CLI project symlink/copy installation, supporting files, cross-skill links and native explicit-only metadata checked; fallback project/personal tests pass | Installed CLI fails startup in an isolated configuration; runtime loading and live integration are unverified |
| Python 3.10.4 and 3.15.0 | Local validation and installer tests | Other versions |

The primary route is the [standard skills CLI](installation.md), tested at version 1.7.2 with Node.js 26.12.0. It installs all 11 sibling skill folders into standard project locations for Codex and Claude Code. Source metadata contains both runtimes' explicit-only policies. Global scope is documented, not exercised against the real user home. The Python installer remains a preview-first fallback with collision refusal and idempotent Claude metadata handling. Neither installer configures ClickUp authentication.

For an isolated Codex smoke test, use a new temporary parent with its own `skills` directory and set `CODEX_HOME` for that process. No credentials or connector settings need copying. An arbitrary copy destination is not automatically a discoverable runtime location.

The kit bundles neither the runtimes nor a ClickUp connector. Installation, discovery, invocation and read/write integration are separate checks. A later live test needs its own authorized target and scope.
