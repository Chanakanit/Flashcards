class QuestionManager:
    def __init__(self):
        self.questions = []  

    def add_question(self, question, answer):
        for q, _ in self.questions:
            if q.strip().lower() == question.strip().lower():
                return False  
        self.questions.append((question.strip(), answer.strip()))
        return True  

    def list_questions(self):
        return self.questions

    def delete_question(self, index: int):
        if 0 <= index - 1 < len(self.questions):
            del self.questions[index - 1]
            return True
        return False

    def edit_answer(self, index: int, new_answer) :
        if 0 <= index - 1 < len(self.questions):
            question = self.questions[index - 1][0]
            self.questions[index - 1] = (question, new_answer.strip())
            return True
        return False

    def reset_questions(self):
        self.questions = []