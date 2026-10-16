# ใช้ clickup-agent-kit ใน Claude Code

ติดตั้ง skills ก่อน แล้วเชื่อม ClickUp เมื่อจะใช้ข้อมูลจริง การติดตั้ง skills และการตั้งค่า MCP เป็นคนละขั้นตอน

## ติดตั้ง skills

จากโฟลเดอร์โปรเจกต์ รัน:

```sh
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent claude-code
```

เลือก **Project** หาก CLI ถาม หรือเติม `--global` เพื่อใช้ทุกโปรเจกต์ของผู้ใช้ ตรวจชื่อที่ชนก่อนยืนยัน เก็บทั้ง 11 skills ไว้ด้วยกันเพื่อให้ relative links ครบ ดู [installation options](installation.md) สำหรับ copy mode และ Python fallback

เปิด Claude Code ในโปรเจกต์ ตรวจ catalog ด้วย `/skills` แล้วลอง `/techlead-analyse-clickup` กับ [fictional prompt ใน README](../README.md) Native loading และ invocation ใน Claude Code ยังไม่ยืนยัน ดู [runtime support](runtime-support.md)

## เชื่อม ClickUp

ต้องมี Claude Code ที่ใช้งานได้ บัญชี ClickUp ที่เข้าถึง tasks ที่เลือก และสิทธิ์ใช้งาน connector ตามนโยบายขององค์กร [Official ClickUp MCP](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) ใช้ OAuth โดยไม่ต้องใส่ token ใน kit

ตรวจ `claude mcp list` เพื่อหลีกเลี่ยง server name ที่ชน จากโฟลเดอร์โปรเจกต์ เพิ่ม connector ที่ผูกกับโปรเจกต์ปัจจุบัน:

```sh
claude mcp add --transport http --scope local clickup https://mcp.clickup.com/mcp
```

`local` ของ MCP เก็บ configuration ใน user account และผูกกับโปรเจกต์ปัจจุบัน ต่างจาก skill files ใน `.claude/skills` หากต้องการใช้ connector ทุกโปรเจกต์ เลือก `--scope user` ส่วน `--scope project` เขียน `.mcp.json` ที่อาจแชร์กับทีมได้ เลือก scope เดียวตามที่ต้องการ อ่าน [MCP scopes และ authentication](https://code.claude.com/docs/en/mcp) เพิ่มเติมก่อนใช้ shared configuration

ใช้ `/mcp` เพื่อ authenticate ผ่าน OAuth แล้วตรวจ server และ tools ที่มี ลองอ่าน task ที่คุณอนุญาตให้เข้าถึงก่อน พร้อมตรวจว่า description, comments และ sources ที่เกี่ยวข้องอ่านได้ครบเพียงใด

การส่ง comment แก้ description หรือสร้าง cards ต้องมีคำขอที่ระบุ content, operation และ destination พร้อม read-back capability การอ่าน task ไม่ได้อนุญาตให้แก้ status หรือ fields อื่นเอง ดู [capability boundaries](dependencies.md)

ตำแหน่ง skills และ invocation อ้าง [official Claude Code skills documentation](https://code.claude.com/docs/en/skills)
