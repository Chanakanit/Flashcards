import random
from bl.question_manager import QuestionManager

def run_exam(question_manager: QuestionManager):
    questions = question_manager.list_questions()
    if not questions:
        print("ยังไม่มีคำถามในระบบ")
        return

    score = 0
    count_questions = 0
    random.shuffle(questions)

    for i, (question, answer) in enumerate(questions, start=1):
        print(f"คำถาม {i}: {question}")
        user_answer = input("ตอบคำถาม: ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("✅ คำตอบถูกต้อง!")
            score += 1
        else:
            print(f"❌ คำตอบผิด! คำตอบที่ถูกต้องคือ: {answer}")

        count_questions += 1

        if i < len(questions):
            stop = input("ต้องการหยุดตอบคำถามหรือไม่? (พิมพ์ 'y' เพื่อหยุด, หรือกด Enter เพื่อทำต่อ): ").strip()
            if stop.lower() == 'y':
                break

    print(f"คะแนนของคุณ: {score}/{count_questions}")