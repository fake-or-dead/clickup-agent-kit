# Make an offline rebrief and developer card

Use a fictional board-game lending desk to practice turning requirements into a rebrief and a self-contained card. The exercise needs no ClickUp connector. `DEMO-001` is a fixture identifier, and all people are role labels.

## Get the fixture files

The skills CLI installs skill folders without the repository-level examples. Clone or download this repository and work from its root. For a clone:

```sh
git clone https://github.com/fake-or-dead/clickup-agent-kit.git
cd clickup-agent-kit
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent codex claude-code
```

Select the runtime and project scope you use. Open that runtime in the clone. See [installation options](../docs/installation.md) if skills with the same names already exist.

## Create the local drafts

1. Read [the fictional task](fictional-task.json) and [source receipt](source-receipt.md).
2. Choose a writable local output directory. Replace `<output directory>` below, then use the prompt. For Claude Code replace `$techlead-analyse-clickup` with `/techlead-analyse-clickup`.

```text
Use $techlead-analyse-clickup. Work offline using examples/fictional-task.json
and examples/source-receipt.md only. Treat DEMO-001 as fictional.
Prepare a concise English rebrief and one self-contained developer card in
<output directory>. Do not connect to ClickUp, browse, publish, send messages,
implement code or change account configuration.
Hours per person-day, currency and rates have not been supplied.
```

3. Compare the drafts with the [illustrative rebrief](expected-rebrief.md) and [developer card](expected-card.md).

## Check the result

The sample availability is 2 for `GAME-A` and 0 for `GAME-B`. The lost-item rule stays unknown, the proposed UI stays a proposal, and reservations and payments stay outside scope. The drafts must state that only fixture evidence was read and avoid numeric cost conversion without rates and units.

The expected files are illustrative examples rather than recorded model outputs. Wording can differ. You can inspect all fixtures without installing anything, or try the [inline README prompt](../README.md) without fixture files.
