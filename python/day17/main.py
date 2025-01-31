from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for question_info in question_data:
    questions = question_info['text']
    answers = question_info['answer']
    new_question = Question(questions, answers)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
quiz.print_question()