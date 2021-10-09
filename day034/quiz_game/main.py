from question_model import Question
from quiz_brain import Quiz
from data import question_data
import random
from ui import QuizInterface


def safe_int_input(text):
    """turn the user input into an int. Prevents invalid input"""
    try:
        data =  int(input(text).strip())
        return data
    except:
        return safe_int_input(text)
        
question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"],item["correct_answer"]))



quiz = Quiz(question_bank)
quiz_ui = QuizInterface(quiz)

# while(quiz.is_complate() == False):
#     print("")
#     quiz.next_question()

