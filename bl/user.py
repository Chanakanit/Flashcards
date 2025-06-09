from bl.question_manager import QuestionManager

class User:
    def __init__(self, student_id, password):
        self.student_id = student_id
        self.password = password
        self.question_manager = QuestionManager()

    def get_question_manager(self):
        return self.question_manager

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, student_id, password):
        if student_id in self.users:
            return False
        self.users[student_id] = User(student_id, password)
        return True

    def login(self, student_id, password):
        user = self.users.get(student_id)
        if user and user.password == password:
            return user
        return None

    def reset_password(self, student_id, new_password):
        user = self.users.get(student_id)
        if user:
            user.password = new_password
            return True
        return False