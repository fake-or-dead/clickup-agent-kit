# ติดตั้งด้วย skills CLI

ต้องมี Node.js 22.20+ และ `npx` สำหรับ skills CLI 1.7.2 ที่ใช้ทดสอบ รันในโฟลเดอร์โปรเจกต์ที่ต้องการใช้ kit:

```sh
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent codex claude-code
```

เลือก **Project** และ **Symlink** หาก CLI ถาม จากนั้นตรวจ summary แล้ว confirm จะได้ทั้ง 11 skills สำหรับ Codex และ Claude Code พร้อม references, templates และ license notices `--skill '*'` สำคัญเพราะ skills เชื่อมไฟล์ข้าม folder จึงควรติดตั้งทั้งชุด

## เลือก agent หรือ scope

| ต้องการ | เปลี่ยนคำสั่งอย่างไร |
| --- | --- |
| Codex อย่างเดียว | เปลี่ยน agent list เป็น `--agent codex` |
| Claude Code อย่างเดียว | เปลี่ยนเป็น `--agent claude-code` |
| ใช้ทุกโปรเจกต์ของผู้ใช้ | เติม `--global` หรือ `-g` |
| ใช้ copies แทน symlinks | เติม `--copy` |
| ดูรายการก่อนติดตั้ง | ใช้ `npx skills add fake-or-dead/clickup-agent-kit --list` |
| ติดตั้งแบบไม่ถาม confirmation | เติม `--yes` หรือ `-y` หลังคำสั่ง `add` เมื่อเลือก agent/scope แล้ว |

Project ติดตั้ง Codex ใน `.agents/skills` และ Claude Code ใน `.claude/skills` Symlink mode ใช้สำเนากลางใน `.agents/skills` ส่วน global ใช้ user skill locations ตาม CLI/runtime อย่าลบสำเนากลางเมื่อยังใช้ symlinks

CLI มาตรฐานสามารถแทนที่ skills ชื่อเดิมได้ ตรวจ summary ก่อน confirm โดยเฉพาะ generic names อย่าง `to-prd` ถ้าต้องการ preview และ refusal เมื่อชื่อชน ให้ใช้ fallback ด้านล่าง

`to-prd` และ `to-issues` มี Claude `disable-model-invocation: true` ใน `SKILL.md` และ Codex `allow_implicit_invocation: false` ใน `agents/openai.yaml` อยู่แล้ว CLI มาตรฐาน copy metadata เหล่านี้ได้โดยไม่ต้องรัน adapter เพิ่ม

## ตรวจว่าติดตั้งแล้ว

เปิด Codex/Claude Code ในโปรเจกต์ที่ติดตั้ง ใช้ `/skills` แล้วตรวจชื่อทั้ง 11 ตัวตาม catalog ใน README จากนั้นลอง offline prompt ใน Quick start การทดสอบ CLI ยืนยันไฟล์, relative links, notices และ Codex discovery ไม่ใช่การรับรอง model behavior หรือ live ClickUp integration

skills CLI ติดตั้งเฉพาะ skill folders ไม่ได้ copy repository-level `examples/`, docs หรือ tests มายังโปรเจกต์ หากต้องการใช้ fixture files ให้ clone repo ตาม [offline example](../examples/getting-started.md) หรือใช้ inline prompt ใน README

## เชื่อม ClickUp แยกต่างหาก

ติดตั้ง skills อย่างเดียวไม่ตั้งค่า MCP, credentials หรือ workspace access ถ้าจะอ่านข้อมูลจริง ต้องมี ClickUp connector ที่เข้าถึง scope นั้นและผ่าน authentication ของผู้ใช้ อ่าน [ClickUp setup สำหรับ Claude Code](claude-code.md) หรือ [capabilities ที่ต้องมี](dependencies.md) สำหรับ runtime อื่น การตรวจ task ไม่อนุญาตให้แก้ status หรือ publish โดยอัตโนมัติ

## Fallback และ maintainer checks

สำหรับผู้ที่ไม่ใช้ Node/skills CLI ให้ clone repo แล้วใช้ Python 3.10+ จาก root ของ clone คำสั่งนี้ preview ก่อน:

```sh
python3 scripts/install.py --runtime codex --destination ../my-project/.agents/skills
```

เติม `--apply` เพื่อ copy เปลี่ยนเป็น `--runtime claude-code` และ destination `../my-project/.claude/skills` สำหรับ Claude Code ชื่อ project เป็นตัวอย่าง เลือก path จริงเอง Fallback ปฏิเสธทุกชื่อที่ชนก่อน copy และไม่แก้ authentication configuration

Maintainers ตรวจ package จาก root ของ clone ได้ด้วย:

```sh
python3 scripts/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

## แหล่งอ้างอิงและขอบเขตทดสอบ

วิธีและ flags อ้าง [official Vercel skills CLI](https://github.com/vercel-labs/skills#install-a-skill) และ [CLI documentation](https://skills.sh/docs/cli) ตำแหน่ง/runtime policies อ้าง [official Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) และ [official Claude skills documentation](https://code.claude.com/docs/en/skills)

ทดสอบ skills CLI 1.7.2 ทั้ง remote discovery, project symlink และ project copy ให้ Codex/Claude Code ใน temporary directories พร้อมตรวจ supporting files และ relative links ทุกไฟล์ โดยปิด telemetry และแยก npm cache ไม่ติดตั้ง global หรือแก้ auth ของผู้ใช้ Global option อ้างเอกสารและไม่ได้รันทับ user home

Repo นี้เป็น standalone skill collection ไม่มี Claude marketplace manifest กลไก [Claude plugins/marketplaces](https://code.claude.com/docs/en/plugins) รองรับ plugin packages อีกแบบหนึ่ง จึงไม่เพิ่ม marketplace/namespace เพื่อแทนการติดตั้ง skill folders ที่ทดสอบได้อยู่แล้ว
