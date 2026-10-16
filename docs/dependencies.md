# Dependencies and capability boundaries

## Required local files and tools

Keep all eleven folders under `skills/` as siblings. Each ClickUp stage uses the orchestrator's shared policy. Handoff uses the supplementary planning skills and bundled templates. No symlinks, package manager, provider SDK, external planning plugin or secret configuration ships in the kit.

The standard skills CLI needs Node.js 22.20+ and npx for the tested CLI 1.7.2. Python 3.10+ is required only for fallback installation and maintainer checks. Skill text can be read without Python. A runtime must support loading skills and resolving their relative files. Only the installed Codex version has a local discovery check for this draft.

## Live source collection

A separately configured ClickUp connector needs permission to read the selected task or hierarchy, descriptions, comments/replies, relevant relations and available attachments/Docs. Capabilities vary. The skill discovers actual tools and records pagination, partial reads and unavailable content. It does not guess tool names or make a tool exist.

An attachment can require a permitted file reader or browser. If access is missing, mark it unread/inaccessible and continue only the analysis that the available evidence supports. Do not store signed download links or credentials in deliverables.

## Optional live publication

Publishing needs a separately authorized description update, comment creation or task-creation capability plus a read-back capability. Runtime safety controls remain in force. No live ClickUp operation is part of the example, installer or validator. The kit supplies no API implementation or secret-handling script.

## Optional research and specialist methods

Current provider details/prices need permitted access to official sources. Without it, leave claims unverified. Azure, LINE and pstack guidance are not bundled and not mandatory dependencies. Domain-specific setup must be discovered for the actual project. Mermaid diagrams are text; rendering is optional and depends on the reader.

The four bundled supplements are shortened adaptations. Existing separately installed versions with the same names can have different publishing behavior. The installer refuses name collisions so a user can review that difference before deciding how to manage their installed skills.
