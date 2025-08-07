"""
ui.py: handles the UI config code
"""
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 12, 'bold')
QUESTION_FONT = ('Arial', 16, 'italic')

# Class-based Tkinter UI setup
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR,
                                 fg='white', font=SCORE_FONT)
        self.score_label.grid(row=0, column=1, pady=20)

        # Creating canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="Amazon acquired Twitch in August"
                                                                    " 2014 for $970 million dollars.",
                                                     fill=THEME_COLOR, font=QUESTION_FONT,
                                                     width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # Buttons
        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_img, bg=THEME_COLOR,
                          borderwidth=0, command=self.selected_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_img, bg=THEME_COLOR,
                           borderwidth=0, command=self.selected_false)
        self.false_btn.grid(row=2, column=1)

        # Get the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')  # Reset canvas.
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()

            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfigure(
                self.question_text,
                text="You've reached the end of the quiz\n"
                    f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def selected_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def selected_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
