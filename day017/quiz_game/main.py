from question_model import Question
from data import question_data
from quiz_brain import Quiz
import random


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


def get_random_question(lenght):
    questions = []
    for item in range(lenght):
        questions.append(random.choice(question_bank))
    return questions
            
    



quiz = Quiz(get_random_question(safe_int_input("What is the lenght you what for the quiz: ")))

while(quiz.is_complate() == False):
    print("")
    quiz.next_question()
