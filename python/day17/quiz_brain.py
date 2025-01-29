from main import question_bank

class Quiz:
    def __init__(self,q_list):
        self.ques_list = q_list
        self. question_number = 0

    def print_question(self):
        current_question = self.ques_list[self.question_number]
        input(f"Q{self.question_number+1}. {question_bank[0]} True/false: ")
