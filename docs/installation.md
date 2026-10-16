# ติดตั้ง clickup-agent-kit

ต้องมี Node.js 22.20+ และ `npx` สำหรับ skills CLI วิธีนี้ใช้กับ Codex และ Claude Code โดยเลือกติดตั้งให้ runtime เดียวหรือทั้งคู่ได้

## ติดตั้งในโปรเจกต์

จากโฟลเดอร์โปรเจกต์ รัน:

```sh
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent codex claude-code
```

เลือก **Project** และ **Symlink** หาก CLI ถาม ตรวจ destination และรายการ skills ก่อนยืนยัน `--skill '*'` ติดตั้งทั้ง 11 folders พร้อม references, templates และ notices ที่เชื่อมกันด้วย relative links

CLI สามารถแทนที่ skills ชื่อเดิมได้ ตรวจชื่อทั่วไปอย่าง `to-prd` ก่อนยืนยัน ถ้าต้องการ preview ที่ไม่เขียนไฟล์และปฏิเสธชื่อชน ใช้ Python installer ด้านล่าง

## เลือก runtime, scope และวิธี copy

| ต้องการ | ตัวเลือก |
| --- | --- |
| Codex อย่างเดียว | ใช้ `--agent codex` |
| Claude Code อย่างเดียว | ใช้ `--agent claude-code` |
| ใช้ทุกโปรเจกต์ของผู้ใช้ | เติม `--global` หรือ `-g` |
| ใช้ copies แทน symlinks | เติม `--copy` |
| ดูรายการก่อนติดตั้ง | ใช้ `npx skills add fake-or-dead/clickup-agent-kit --list` |
| ไม่แสดง confirmation prompts | เติม `--yes` หรือ `-y` เมื่อเลือก runtime และ scope แล้ว |

Project scope ใช้ `.agents/skills` สำหรับ Codex และ `.claude/skills` สำหรับ Claude Code ใน Symlink mode มีสำเนากลางใน `.agents/skills` ให้เก็บสำเนากลางไว้ขณะยังใช้ symlinks ส่วน global scope ใช้ user skill locations ตาม CLI และ runtime

`to-prd` และ `to-issues` เป็น explicit-only skills Metadata สำหรับทั้งสอง runtimes อยู่ใน source แล้ว จึงไม่ต้องแปลงไฟล์หลังติดตั้ง

## เริ่มใช้งาน

เปิด runtime ในโปรเจกต์ที่ติดตั้ง ตรวจ catalog ด้วย `/skills` แล้วลอง [prompt แรกใน README](../README.md) สำหรับ Codex ใช้ `$techlead-analyse-clickup` สำหรับ Claude Code ใช้ `/techlead-analyse-clickup`

CLI ติดตั้งเฉพาะ skill folders หากต้องการใช้ fixture files ใน `examples/` ให้ clone หรือ download repo ตาม [offline exercise](../examples/getting-started.md) ส่วน inline prompt ใน README ใช้ได้โดยไม่ต้องมี fixture files

อ่าน [runtime support](runtime-support.md) สำหรับขอบเขต compatibility และ [connector prerequisites](dependencies.md) ก่อนใช้ข้อมูลจริง การติดตั้ง skills ไม่ตั้งค่า ClickUp, credentials หรือ workspace access

## ใช้ Python installer แทน CLI

ต้องมี Python 3.10+ และ local copy ของ repo จาก root ของ repo ให้ preview ไปยังโปรเจกต์ที่เลือก:

```sh
python3 scripts/install.py --runtime codex --destination ../my-project/.agents/skills
```

เปลี่ยน `../my-project` เป็น path ของคุณ ตรวจ preview แล้วเติม `--apply` เพื่อ copy สำหรับ Claude Code ใช้ `--runtime claude-code` กับ destination `../my-project/.claude/skills`

Installer นี้ปฏิเสธทุกชื่อที่ชนก่อน copy และเก็บ unrelated skills ไว้ ไม่มีขั้นตอน authenticate หรือแก้ account configuration

## เอกสารอ้างอิง

ดู flags และ locations เพิ่มใน [skills CLI documentation](https://skills.sh/docs/cli), [Vercel skills CLI](https://github.com/vercel-labs/skills#install-a-skill), [Codex skills](https://learn.chatgpt.com/docs/build-skills) และ [Claude Code skills](https://code.claude.com/docs/en/skills)
