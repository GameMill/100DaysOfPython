import tkinter
import os
import tkinter.messagebox

from quiz_brain import Quiz

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial",20,"italic")
ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"


class QuizInterface:

    def __init__(self,quiz_brain: Quiz):
        self.quiz = quiz_brain
        self.tk = tkinter.Tk()
        self.tk.title("Quiz Game")
        self.tk.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score = 0

        # Score Label
        self.score_label = tkinter.Label(text=self.quiz.__str__())
        self.score_label.grid(column=1,row=0,padx=20)
        self.score_label.config(bg=THEME_COLOR,fg="white")
        
        # Question Text (Canvas Box)
        self.canvas = tkinter.Canvas(width=300,height=250)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="Loading Question...",
            width=250,
            font=QUESTION_FONT,
            fill=THEME_COLOR
            )
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)

        true_image = tkinter.PhotoImage(file=f"{ROOT}images/true.png",width=100,height=98)
        self.true_button = tkinter.Button(image=true_image,command=self.true,highlightthickness=0)
        self.true_button.grid(column=0,row=2)

        false_image = tkinter.PhotoImage(file=f"{ROOT}images/false.png",width=100,height=98)
        self.false_button = tkinter.Button(image=false_image,command=self.false,highlightthickness=0)
        self.false_button.grid(column=1,row=2)

        self.get_next_question()

        self.tk.mainloop()


    def  get_next_question(self):
        self.canvas.config(bg="white")
        if(self.quiz.is_complate() == False):
            self.set_button_state(True)
            self.score_label.config(text=self.quiz.__str__())
            self.canvas.itemconfigure(self.canvas_text,text=self.quiz.next_question())
        else:
            self.set_button_state(False)
           

    def set_button_state(self,enabled:bool):
        if(enabled):
            self.true_button["state"] = "normal"
            self.false_button["state"] = "normal"
        else:
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"
        
    def show_incorrect_box(self,is_correct:bool):
        self.set_button_state(False)
        if(is_correct == False):
           self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        self.tk.after(2000,self.get_next_question)


    def true(self):
        self.show_incorrect_box(self.quiz.check_answer(True))

    def false(self):
        self.show_incorrect_box(self.quiz.check_answer(False))


            
            

if __name__ == "__main__":
    test = QuizInterface()
    