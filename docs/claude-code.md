# ติดตั้งใน Claude Code

Instructions นี้อ้าง [official Skills documentation](https://code.claude.com/docs/en/skills) ตำแหน่ง project คือ `.claude/skills/<name>/SKILL.md` ส่วน personal คือ `~/.claude/skills/<name>/SKILL.md` ให้เลือก scope และตรวจชื่อที่ชนก่อนใช้

## ติดตั้ง skills

ใช้ [standard skills CLI](installation.md) จากโฟลเดอร์โปรเจกต์:

```sh
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent claude-code
```

เลือก Project หาก CLI ถาม หรือเติม `--global` สำหรับ personal use ทั้ง 11 skills ต้องอยู่ด้วยกันเพื่อให้ relative links ครบ ส่วน explicit-only metadata ของ `to-prd`/`to-issues` อยู่ใน source แล้ว ไม่ต้องรัน adapter เพิ่ม ดู agent/scope/copy options และ fallback ใน installation guide

เปิด Claude Code ในโปรเจกต์ ใช้ `/skills` ตรวจ catalog แล้วลอง offline prompt ใน README ก่อน การทดสอบ installer ยืนยันไฟล์และ policies ที่ติดตั้ง ไม่ใช่ runtime-loading หรือ model-behavior certification

## ClickUp connector prerequisites

ต้องมี Claude Code ที่ใช้งานได้, ClickUp account/workspace access ที่เหมาะกับ tasks ที่เลือก และสิทธิ์จากองค์กรเมื่อจำเป็น Official ClickUp MCP ใช้ [endpoint และ OAuth ตามเอกสาร ClickUp](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) ไม่ใส่ token ใน kit

คำสั่งต่อไปนี้เป็น setup ที่ผู้ใช้เลือกทำภายหลัง ไม่ได้ถูกรันระหว่างเตรียม kit ตรวจ `claude mcp list` ก่อนเพื่อหลีกเลี่ยง server name ที่ชน แล้วเลือกเพียง scope เดียว:

```sh
claude mcp add --transport http --scope local clickup https://mcp.clickup.com/mcp
```

`local` ของ MCP ผูกกับ project ปัจจุบันแต่เก็บ config ใน user account ต่างจาก project-local skill files ถ้าต้องการ connector ทุก project ให้เปลี่ยนเป็น `--scope user` ส่วน `--scope project` สร้าง/แก้ `.mcp.json` ที่อาจแชร์กับทีมได้ อ่าน [official MCP scopes/authentication](https://code.claude.com/docs/en/mcp) ก่อนเลือก

ใช้ `/mcp` เพื่อ authenticate ผ่าน OAuth ตรวจ server/tools และลองอ่าน task ทดสอบที่ผู้ใช้อนุญาตอย่างเดียว บันทึก task identity, read boundary และ capability ที่ขาด ไม่สร้างหรือแก้ task เพื่อพิสูจน์การเชื่อมต่อ การส่ง comment/แก้ description/สร้าง cards ต้องเป็นคำขอและ authorization แยกที่ชัดเจน

## ขอบเขตที่ทดสอบแล้ว

ทดสอบ standard skills CLI ใน temporary project directories ทั้ง symlink/copy modes พร้อม byte preservation, notices, explicit invocation metadata และ cross-skill links แล้ว รวมถึง tests ของ fallback สำหรับ project/personal layouts, collisions และ no-write preview ไม่ได้ติดตั้งทับ skills จริงหรือเปลี่ยน auth config

Claude CLI ที่มีบนเครื่องยังเริ่มทำงานไม่สำเร็จในการตรวจแบบ isolated จึงยังไม่ยืนยัน runtime loading, slash-command behavior, model behavior หรือ live ClickUp integration Instructions ตรงกับเอกสารปัจจุบัน แต่ผลทดสอบไฟล์ไม่ใช่ compatibility certification ดู [runtime support](runtime-support.md)
