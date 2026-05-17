from bl.user import UserManager
from ui.login_ui import handle_login_menu
from ui.exam_ui import run_exam
from ui.question_settings_ui import handle_question_settings

def main():
    user_manager = UserManager()
    current_user = None

    while True:
        if not current_user:
            current_user = handle_login_menu(user_manager)
            if current_user is None: 
                break
        else:
            print(f"\nรหัสนักศึกษา: {current_user.student_id}")
            print("\n--- เมนู ---")
            print("1. ทำแบบทดสอบ")
            print("2. ตั้งค่าคำถาม")    
            print("3. ล็อกเอ้า")
            choice = input("เลือกเมนู: ")

            if choice == "1":  # ทำแบบทดสอบ
                question_manager = current_user.get_question_manager()
                run_exam(question_manager)
            elif choice == "2":  # ตั้งค่าคำถาม
                question_manager = current_user.get_question_manager()
                handle_question_settings(question_manager)
            elif choice == "3":  # ล็อกเอ้า
                print("ล็อกเอ้า...")
                current_user = None
            else:
                print("กรุณาเลือกเมนูที่ถูกต้อง")
                
if __name__ == "__main__":
    main()