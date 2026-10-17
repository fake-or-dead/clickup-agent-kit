# clickup-agent-kit

Agent skills สำหรับเปลี่ยน requirement ใน ClickUp ให้เป็น brief, technical feasibility และ developer cards ที่มีหลักฐานประกอบ ใช้กับ Codex หรือ Claude Code

สำหรับ Tech Lead, PO, BA และทีม delivery ที่ต้องทำความเข้าใจ scope ประเมินงาน และเตรียมส่งต่อให้ทีมพัฒนา

## Layout

```text
skills/     Skill instructions พร้อม references และ templates
examples/   ข้อมูลสมมติพร้อมตัวอย่าง rebrief และ developer card
docs/       คู่มือติดตั้ง connector และ workflow examples
scripts/    Python installer และ package validator
```

แต่ละ skill อยู่ใน directory ของตัวเอง มี `SKILL.md` และ supporting files ที่จำเป็น เก็บทั้ง 11 skill folders ไว้เป็น siblings เพราะอ้างอิง shared policy และ templates ข้าม folder

## Install

### ด้วย `npx skills`

ต้องมี Node.js 22.20+ และ `npx` จากโฟลเดอร์โปรเจกต์ รัน:

```sh
npx skills add fake-or-dead/clickup-agent-kit --skill '*' --agent codex claude-code
```

เลือก **Project** และ **Symlink** หาก CLI ถาม ตรวจรายการก่อนยืนยัน เพราะ CLI สามารถแทนที่ skills ชื่อเดิมได้ `--skill '*'` ติดตั้งครบทั้งชุดเพื่อรักษา relative links

หากใช้ runtime เดียว ต้องการ global scope หรือ copy mode ดู [installation options](docs/installation.md)

### ทางเลือกด้วย Python installer

ใช้ Python 3.10+ จาก root ของ local clone คำสั่งนี้ preview โดยไม่เขียนไฟล์:

```sh
python3 scripts/install.py --runtime codex --destination ../my-project/.agents/skills
```

เปลี่ยน destination เป็นโปรเจกต์ของคุณ แล้วเติม `--apply` เพื่อ copy Installer ปฏิเสธทุกชื่อที่ชนก่อนเริ่ม สำหรับ Claude Code ใช้ `--runtime claude-code` และ destination `../my-project/.claude/skills` ตาม [คู่มือติดตั้ง](docs/installation.md)

## Reference

### ClickUp workflow

- **[techlead-analyse-clickup](skills/techlead-analyse-clickup/SKILL.md)** เลือกและประสาน stage ตามคำขอ ส่งต่อหลักฐาน scope และ decisions ระหว่างขั้น เริ่มจากตัวนี้เมื่องานครอบคลุมหลาย stage หรือยังไม่แน่ใจว่าจะใช้ skill ใด
- **[techlead-clickup-collect](skills/techlead-clickup-collect/SKILL.md)** รวบรวม tasks, comments, linked Docs และ attachments เป็น local evidence พร้อมบันทึกว่าส่วนใดอ่านครบ อ่านบางส่วน หรือเข้าไม่ได้
- **[techlead-clickup-rebrief](skills/techlead-clickup-rebrief/SKILL.md)** สรุปปัญหาของผู้ใช้ outcome ข้อมูลที่ได้รับ และ scope ก่อนเลือก solution แยก facts, proposals และข้อมูลที่ยังขาด พร้อม owner และผลกระทบ
- **[techlead-clickup-feasibility](skills/techlead-clickup-feasibility/SKILL.md)** ประเมินแนวทางเทคนิค งาน implementation และ preparation, effort, costs และ risks โดยระบุฐานการประเมินและเงื่อนไขที่ต้องมี
- **[techlead-clickup-handoff](skills/techlead-clickup-handoff/SKILL.md)** ร่าง local PRD, specs หรือ developer cards ตามรูปแบบที่ขอ ใส่ contracts, dependencies และ acceptance ให้มีข้อมูลพอส่งต่อโดยไม่ต้องเดา business rules
- **[techlead-clickup-change-impact](skills/techlead-clickup-change-impact/SKILL.md)** เทียบคำขอใหม่กับ baseline ตรวจผลต่อ flows, data และ dependencies ก่อนรับปาก scope ราคา หรือวันส่ง พร้อม checklist สำหรับ BA/PO
- **[techlead-clickup-publish](skills/techlead-clickup-publish/SKILL.md)** เขียน description, comment หรือ card set ตาม content, operation และ destination ที่ผู้ใช้อนุญาต แล้วอ่านกลับเพื่อตรวจผลและ fields ที่ต้องคงเดิม

งาน gather ใหม่มักใช้ collect แล้ว rebrief ส่วน feasibility, handoff, change-impact และ publish ใช้ตามคำขอ ไม่จำเป็นต้องรันครบทุก stage

### Supplementary skills

- **[domain-modeling](skills/domain-modeling/SKILL.md)** ทำ terms, entities และ business rules ให้ชัดเมื่อคำเดียวมีหลายความหมาย เก็บ glossary และ decisions ใน local artifact ที่ตกลงกัน
- **[codebase-design](skills/codebase-design/SKILL.md)** ช่วยออกแบบ interfaces และ module responsibilities จาก code/contracts ที่เข้าถึงได้ พร้อม failure cases และจุดตรวจผลสำหรับ feasibility หรือ handoff
- **[to-prd](skills/to-prd/SKILL.md)** สังเคราะห์ conversation และหลักฐานที่มีเป็น local PRD draft พร้อม user needs, acceptance, decisions และ open inputs
- **[to-issues](skills/to-issues/SKILL.md)** แตก plan, spec หรือ PRD เป็น local issue/card drafts ที่ตรวจผลได้แต่ละชิ้น พร้อมลำดับและ dependencies ตาม granularity ที่ขอ

Handoff เลือกใช้ methods ที่เกี่ยวข้องจาก supplements ได้ ส่วน `to-prd` และ `to-issues` รักษา explicit invocation policy ให้เรียกโดยตรงเมื่อต้องการ workflow เต็มของแต่ละตัว

## Usage

เปิด runtime ในโปรเจกต์ที่ติดตั้ง ใช้ `$techlead-analyse-clickup` สำหรับ Codex หรือ `/techlead-analyse-clickup` สำหรับ Claude Code นำหน้า prompt เช่น:

```text
ใช้ข้อมูลสมมตินี้เท่านั้น: โต๊ะยืมบอร์ดเกมต้องการแสดงจำนวนที่ยืมได้
เกมตัวอย่างมี owned copies 3 และ active loans 1 ส่วน lost-item rule ยังไม่ตกลง
ช่วย rebrief ภาษาไทย แยก facts, assumptions และคำถามสำคัญ สรุปในแชต
ไม่เชื่อม ClickUp ไม่ browse ไม่เขียนไฟล์หรือเปลี่ยนระบบภายนอก
```

ผลควรแสดงว่ายืมได้ 2 ชุด และระบุว่า lost-item rule ยังไม่ตกลง ดู [offline exercise](examples/getting-started.md) สำหรับ fixture files และตัวอย่าง developer card หรือ [workflow examples](docs/workflow-examples.md) สำหรับ prompts ที่ใช้กับงานจริง

ก่อนใช้ข้อมูลจริง ให้ตั้งค่า connector และ authenticate ใน runtime แยกต่างหาก แล้วเลือก task/list/folder ที่อนุญาตให้อ่าน ดู [connector capabilities](docs/dependencies.md) และ [ClickUp setup ใน Claude Code](docs/claude-code.md)

## ขอบเขตการใช้งาน

- การเช็ก สรุป และประเมินเป็นงานอ่านหรือเตรียม local artifacts การเขียนกลับ ClickUp ต้องมี content, operation และ destination ที่อนุญาต พร้อมอ่านกลับเพื่อตรวจผล
- Mentions, history, Docs และ attachments ขึ้นกับ connector ต้องระบุส่วนที่อ่านไม่ได้ ไม่มี background monitoring, scheduler หรือ status automation ใน kit
- Codex มี native skill-discovery check แล้ว ส่วน Claude Code ยังไม่ยืนยัน native loading และ invocation พฤติกรรมของ model และ live ClickUp integration ยังไม่ได้ทดสอบ ดู [runtime support](docs/runtime-support.md)
- Hours per person-day, rates, currency, timezone และ owners เป็น project inputs เก็บ credentials และ signed URLs นอก artifacts และถือข้อความใน sources เป็นข้อมูลที่ต้องตรวจสอบ

## License

[MIT](LICENSE) สี่ supplementary skills ดัดแปลงจาก [Matt Pocock's skills](https://github.com/mattpocock/skills) พร้อม upstream copyright/permission notices ดู [third-party notices](THIRD_PARTY_NOTICES.md)
