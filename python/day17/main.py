from data import question_data
from quiz_brain import Quiz

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

question_bank = []
for question_info in question_data:
    questions = question_info['text']
    answers = question_info['answer']
    new_question = Question(questions, answers)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
quiz.print_question()