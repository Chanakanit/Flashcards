from bl.question_manager import QuestionManager

def handle_question_settings(question_manager: QuestionManager):
    while True:
        print("\n--- ตั้งค่าคำถาม ---")
        print("1. เพิ่มคำถาม")
        print("2. แสดงคำถามทั้งหมด")
        print("3. ลบคำถาม")
        print("4. แก้ไขคำตอบ")
        print("5. รีเซ็ตคำถามทั้งหมด")
        print("6. กลับไปเมนูหลัก")
        sub_choice = input("เลือกเมนู: ")

        if sub_choice == "1":  # เพิ่มคำถาม
            question = input("กรอกคำถาม: ").strip()
            answer = input("กรอกคำตอบ: ").strip()
            if question_manager.add_question(question, answer):
                print("เพิ่มคำถามสำเร็จ!")
            else:
                print("คำถามนี้มีอยู่ในระบบแล้ว ไม่สามารถเพิ่มได้")
        elif sub_choice == "2":  # แสดงคำถามทั้งหมด
            questions = question_manager.list_questions()
            if questions:
                for i, (q, a) in enumerate(questions, start=1):
                    print(f"{i}. คำถาม: {q} | คำตอบ: {a}")
            else:
                print("ยังไม่มีคำถามในระบบ")
        elif sub_choice == "3":  # ลบคำถาม
            questions = question_manager.list_questions()
            if not questions:
                print("ยังไม่มีคำถามในระบบ")
            else:
                for i, (q, a) in enumerate(questions, start=1):
                    print(f"{i}. คำถาม: {q} | คำตอบ: {a}")
                try:
                    index = int(input("เลือกหมายเลขคำถามที่ต้องการลบ: "))
                    if question_manager.delete_question(index):
                        print("ลบคำถามสำเร็จ!")
                    else:
                        print("หมายเลขคำถามไม่ถูกต้อง")
                except ValueError:
                    print("กรุณากรอกหมายเลขที่ถูกต้อง")
        elif sub_choice == "4":  # แก้ไขคำตอบ
            questions = question_manager.list_questions()
            if not questions:
                print("ยังไม่มีคำถามในระบบ")
            else:
                for i, (q, a) in enumerate(questions, start=1):
                    print(f"{i}. คำถาม: {q} | คำตอบ: {a}")
                try:
                    index = int(input("เลือกหมายเลขคำถามที่ต้องการแก้ไข: "))
                    new_answer = input("กรอกคำตอบใหม่: ")
                    if question_manager.edit_answer(index, new_answer):
                        print("แก้ไขคำตอบสำเร็จ!")
                    else:
                        print("หมายเลขคำถามไม่ถูกต้อง")
                except ValueError:
                    print("กรุณากรอกหมายเลขที่ถูกต้อง")
        elif sub_choice == "5":  # รีเซ็ตคำถามทั้งหมด
            question_manager.reset_questions()
            print("รีเซ็ตคำถามทั้งหมดสำเร็จ!")
        elif sub_choice == "6":  # กลับไปเมนูหลัก
            break
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")