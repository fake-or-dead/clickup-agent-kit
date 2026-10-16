# Runtime support

| Runtime | ขอบเขตที่รองรับและตรวจแล้ว | สิ่งที่ยังไม่ยืนยัน |
| --- | --- | --- |
| Codex | Standard skills CLI ติดตั้งใน project `.agents/skills` ได้ Native discovery บน Codex CLI 0.163.0 อ่านครบ 11 skills และ metadata ได้ | Model behavior และ live ClickUp integration |
| Claude Code | Standard skills CLI ติดตั้ง project layout ได้ทั้ง symlink และ copy พร้อม supporting files และ explicit-only metadata | Native loading, invocation, model behavior และ live ClickUp integration |

วิธีหลักใช้ [skills CLI](installation.md) ที่ตรวจด้วย version 1.7.2 บน Node.js 26.12.0 โดย CLI version นี้ต้องการ Node.js 22.20+ Global scope มีใน CLI แต่ยังไม่มีการทดสอบติดตั้งใน user home จริง

Python fallback ใช้ Python 3.10+ มี preview ก่อน copy และปฏิเสธชื่อชน การติดตั้งแบบ project และ personal ผ่านการตรวจ file-copy behavior แล้ว

`to-prd` และ `to-issues` มี explicit-only policy สำหรับทั้งสอง runtimes ส่วน skills อื่นใช้การเลือก skill ตามความสามารถของ runtime หรือเรียกชื่อโดยตรง

การติดตั้งไฟล์ การค้นพบ skills และการทำงานของ model เป็นคนละขอบเขตกัน ต้องมี runtime ที่ใช้งานได้และ [ClickUp connector](dependencies.md) แยกต่างหากสำหรับ live work
