THEME_COLOR = "#375362"
MY_FONT = ('Arial', 20, 'italic')

import html
import tkinter
from quiz_brain import QuizBrain

class QuizInterface:

    """
    A class used to represent the user interface
    and send answers to Quiz_Brain.

    ...

    Attributes
    ----------
    quiz_brain: QuizBrain
        a QuizBrain objevt
    window: tkinter.Tk
        a window object
    canvas: tkinter.Canvas
        a canvas object
    question_text: tkinter.create_text
        a text object that displays the questions text
    score_text: tkinter.Label
        a label that displays the score
    checkmark_button: tkinter.Button
        a button to represent a True answer
    cross_button: tkinter.Button
        a button to represent a False answer

    Methods
    -------
    user_answer_true()
        checks to see if there are questions left,
        calls the quiz_brains.next_question() method
        with the answer 'True', then obtaining the next
        question or ending the game.
    user_answer_false()
        checks to see if there are questions left,
        calls the quiz_brains.next_question() method
        with the answer 'False', then obtaining the next
        question or ending the game.
    change_question(user_answer)
        changes the text on the canvas
    update_score()
        changes the score on the label
    no_more_questions()
        ends the game
    """
    def __init__(self, quiz_brain: QuizBrain):
        """
        Parameters
        ----------
        :param quiz_brain: QuizBrain
            A QuizBrain object that controls the game
        """
        self.quiz_brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #Canvas
        self.canvas = tkinter.Canvas(height=250, width=300, highlightthickness=0, bg='white')
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text=html.unescape(self.quiz_brain.current_question.text),
                                                     font=MY_FONT, fill=THEME_COLOR, width=280)
        #Score board label
        self.score_text = tkinter.Label(fg='white', text=f'Score: {quiz_brain.score}', bg=THEME_COLOR)
        self.score_text.grid(row=1, column=2)
        # Buttons
        checkmark_photo_img = tkinter.PhotoImage(file='./images/true.png')
        cross_photo_img = tkinter.PhotoImage(file='./images/false.png')
        self.checkmark_button = tkinter.Button(image=checkmark_photo_img, highlightthickness=0,
                                               command=self.user_answer_true)
        self.cross_button = tkinter.Button(image=cross_photo_img, highlightthickness=0,
                                           command=self.user_answer_false)
        self.checkmark_button.grid(row=3, column=1)
        self.cross_button.grid(row=3, column=2)

        self.window.mainloop()

    def user_answer_true(self):
        """checks to see if there are questions left,
        calls the quiz_brains.next_question() method
        with the answer 'True', then obtaining the next
        question or ending the game.
        """
        if self.quiz_brain.still_has_questions():
            self.quiz_brain.next_question(user_answer=True)
            self.update_score()
            self.change_question()
        else:
            self.no_more_questions()

    def user_answer_false(self):
        """checks to see if there are questions left,
        calls the quiz_brains.next_question() method
        with the answer 'False', then obtaining the next
        question or ending the game.
        """
        if self.quiz_brain.still_has_questions():
            self.quiz_brain.next_question(user_answer=False)
            self.update_score()
            self.change_question()
        else:
            self.no_more_questions()

    def change_question(self):
        """changes the text on the canvas
        """
        print(f'{self.quiz_brain.question_number} {self.quiz_brain.current_question.text} debug ui')
        self.canvas.itemconfig(self.question_text, text=html.unescape(self.quiz_brain.current_question.text))

    def update_score(self):
        """changes the score on the label
        """
        self.score_text.config(text=f'Score: {self.quiz_brain.score}')

    def no_more_questions(self):
        """ends the game
        """
        self.canvas.itemconfig(self.question_text, text='Sorry, no more questions!\nRestart the game.',fill=THEME_COLOR)
        pass