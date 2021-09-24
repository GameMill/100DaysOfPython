import random
class Quiz:
    def __init__(self,questions):
        self.current = 0
        self.score = 0
        self.questions = questions
        self.lenght = len(questions)
        self.current_question = None
        self.next_question()

    def safe_true_false_input(self,text):
        """check the user has inputed yes or y for yes and no or n for no and returns 'yes' or 'no' Prevents invalid input"""

        try:
            true = ["true","t"]
            false = ["false","f"]
            data =  input(text).strip().lower()
            if true.__contains__(data):
                return True
            elif false.__contains__(data):
                return False
            else:
                return self.safe_true_false_input(text)
        except:
            return self.safe_true_false_input(text)

    def next_question(self):
        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)
        self.current += 1
        if self.safe_true_false_input(f"Q.{self.current}: {self.current_question}? True or False: ") == self.current_question.answer:
            print("You got it right!")
            self.score += 1
        print(f"The correct answer was: {self.current_question.answer}")
        print(self.__str__())

    def is_complate(self):
        return self.current == self.lenght
        

    def __str__(self):
        return f"Your current score is: {self.score}/{self.current}"