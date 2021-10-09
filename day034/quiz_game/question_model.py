import html

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer.lower() == "true"
    def __str__(self):
         return f"{html.unescape(self.text)}"
        

if __name__ == "__main__":
    question = Question("2+3=5","True")
    print(f"{question}: {question.answer}")
    