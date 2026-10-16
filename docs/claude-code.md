# ติดตั้งใน Claude Code

Instructions นี้อ้าง [official Skills documentation](https://code.claude.com/docs/en/skills) ตำแหน่ง project คือ `.claude/skills/<name>/SKILL.md` ส่วน personal คือ `~/.claude/skills/<name>/SKILL.md` ให้เลือก scope และตรวจชื่อที่ชนก่อนใช้

## Project-local skills

จาก root ของ kit ชี้ไปยัง project ที่เลือก ตัวอย่าง `../my-project` เป็นชื่อสมมติและอยู่นอก kit:

```sh
python3 scripts/install.py --runtime claude-code --destination ../my-project/.claude/skills
python3 scripts/install.py --runtime claude-code --destination ../my-project/.claude/skills --apply
```

คำสั่งแรก preview เท่านั้น คำสั่งที่สองจึง copy Installer ไม่เขียน `settings.json`, `.mcp.json`, `CLAUDE.md` หรือ authentication configuration

## Personal skills

```sh
python3 scripts/install.py --runtime claude-code --destination "$HOME/.claude/skills"
python3 scripts/install.py --runtime claude-code --destination "$HOME/.claude/skills" --apply
```

ใช้ personal scope เมื่อต้องการให้ทุก local project ของผู้ใช้เห็น skills ไม่ได้หมายความว่าจะติดตั้งให้ teammates หรือ cloud sessions หากมีชื่อชน installer หยุดทั้งชุด ไม่ merge/overwrite ต้นฉบับ

## Metadata และการตรวจหลังติดตั้ง

Installer เพิ่ม `disable-model-invocation: true` ให้สำเนา `to-prd` และ `to-issues` ตาม Codex policy ของต้นฉบับ ไม่เปลี่ยน source package `agents/openai.yaml` ยังคงอยู่เพื่อเก็บ metadata แต่ไม่ใช้เป็น Claude invocation policy อ้าง [invocation controls](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill)

เปิด Claude Code ใน project ที่เลือก ตรวจ `/skills` ว่ามีชื่อจาก `kit.json` และเลือก `/techlead-analyse-clickup` ถ้ามีหลาย scope ให้ตรวจ path/origin ว่ากำลังใช้สำเนาที่ตั้งใจ จากนั้นลอง offline prompt ใน README ก่อนเชื่อมข้อมูลจริง การเห็นชื่อใน menu ยังไม่พิสูจน์ connector behavior

## ClickUp connector prerequisites

ต้องมี Claude Code ที่ใช้งานได้, ClickUp account/workspace access ที่เหมาะกับ tasks ที่เลือก และสิทธิ์จากองค์กรเมื่อจำเป็น Official ClickUp MCP ใช้ [endpoint และ OAuth ตามเอกสาร ClickUp](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) ไม่ใส่ token ใน kit

คำสั่งต่อไปนี้เป็น setup ที่ผู้ใช้เลือกทำภายหลัง ไม่ได้ถูกรันระหว่างเตรียม kit ตรวจ `claude mcp list` ก่อนเพื่อหลีกเลี่ยง server name ที่ชน แล้วเลือกเพียง scope เดียว:

```sh
claude mcp add --transport http --scope local clickup https://mcp.clickup.com/mcp
```

`local` ของ MCP ผูกกับ project ปัจจุบันแต่เก็บ config ใน user account ต่างจาก project-local skill files ถ้าต้องการ connector ทุก project ให้เปลี่ยนเป็น `--scope user` ส่วน `--scope project` สร้าง/แก้ `.mcp.json` ที่อาจแชร์กับทีมได้ อ่าน [official MCP scopes/authentication](https://code.claude.com/docs/en/mcp) ก่อนเลือก

ใช้ `/mcp` เพื่อ authenticate ผ่าน OAuth ตรวจ server/tools และลองอ่าน task ทดสอบที่ผู้ใช้อนุญาตอย่างเดียว บันทึก task identity, read boundary และ capability ที่ขาด ไม่สร้างหรือแก้ task เพื่อพิสูจน์การเชื่อมต่อ การส่ง comment/แก้ description/สร้าง cards ต้องเป็นคำขอและ authorization แยกที่ชัดเจน

## ขอบเขตที่ทดสอบแล้ว

ทดสอบ installer ใน temporary directories สำหรับทั้ง project/personal layout, byte preservation, notices, explicit invocation metadata, collisions และ no-write preview แล้ว ไม่ได้ติดตั้งทับ skills จริงหรือเปลี่ยน auth config

Claude CLI ที่มีบนเครื่องยังเริ่มทำงานไม่สำเร็จในการตรวจแบบ isolated จึงยังไม่ยืนยัน runtime loading, slash-command behavior, model behavior หรือ live ClickUp integration Instructions ตรงกับเอกสารปัจจุบัน แต่ผลทดสอบไฟล์ไม่ใช่ compatibility certification ดู [runtime support](runtime-support.md)
