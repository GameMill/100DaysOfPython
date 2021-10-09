import random
from question_model import Question
class Quiz:
    def __init__(self,questions: list[Question]):
        self.current = 0
        self.score = 0
        self.questions = questions
        self.lenght = len(questions)
        self.current_question = None
        

    def next_question(self):
        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)
        self.current += 1
        return self.current_question.__str__()

    def is_complate(self):
        return self.current == self.lenght
        
    def check_answer(self,answer:bool) -> bool:
        print(f"{self.current_question.answer} == {answer} {self.current_question.answer == answer}")
        if(self.current_question.answer == answer):
            self.score += 1
            return True
        else:
            return False


    def __str__(self):
        return f"Score: {self.score}"