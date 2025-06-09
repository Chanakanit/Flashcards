from bl.user import UserManager

def handle_login_menu(user_manager: UserManager):
    while True:
        print("\n--- ระบบทบทวนความจำ ---")
        print("1. ลงทะเบียน")
        print("2. ล็อกอิน")
        print("3. ลืมรหัสผ่าน")
        print("4. ออกจากระบบ")
        choice = input("เลือกเมนู: ")

        if choice == "1":
            while True:
                student_id = input("กรอกรหัสนักศึกษา: ").strip()
                if len(student_id) == 11 :
                    break

            while True:
                password = input("ตั้งรหัสผ่าน: ").strip()
                if len(password) >= 3:
                    break
                print("รหัสผ่านต้องมีอย่างน้อย 3 ตัวอักษร")
                
            if user_manager.register(student_id, password):
                print("ลงทะเบียนสำเร็จ!")
            else:
                print("รหัสนักศึกษานี้ถูกใช้ไปแล้ว")
        elif choice == "2":
            student_id = input("กรอกรหัสนักศึกษา: ")
            password = input("กรอกรหัสผ่าน: ")
            current_user = user_manager.login(student_id, password)
            if current_user:
                print("ล็อกอินสำเร็จ!")
                return current_user # ส่งคืน user ที่ล็อกอินสำเร็จ
            else:
                print("รหัสนักศึกษาหรือรหัสผ่านไม่ถูกต้อง")
        elif choice == "3":
            student_id = input("กรอกรหัสนักศึกษา: ").strip()
            if len(student_id) != 11 or not student_id.startswith("67130500"):
                print("รหัสนักศึกษาไม่ถูกต้อง")
                continue

            new_password = input("ตั้งรหัสผ่านใหม่: ").strip()
            if len(new_password) < 3:
                print("รหัสผ่านต้องมีอย่างน้อย 3 ตัวอักษร")
            elif user_manager.reset_password(student_id, new_password):
                print("เปลี่ยนรหัสผ่านสำเร็จ!")
            else:
                print("ไม่พบรหัสนักศึกษาในระบบ")

        elif choice == "4":
            print("ออกจากระบบ...")
            return None # ออกจากระบบ
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")