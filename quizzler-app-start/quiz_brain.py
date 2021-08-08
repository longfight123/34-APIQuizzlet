
class QuizBrain:
    """
    A class used to control the quiz.

    ...

    Attributes
    ----------
    question_number: int
        the current question number
    score: int
        the current score in the game
    question_list: list
        a list of Question objects
    current_question: Question
        the current Question object

    Methods
    -------
    still_has_questions()
        checks to see if there are questions left
    next_question(user_answer)
        calls check_answer and obtains the next Question
        object in the question_list
    check_answer(user_answer)
        checks the user_answer against the
        correct answer
    """

    def __init__(self, q_list):
        """
        Parameters
        ----------
        q_list: list
            a list of Question objects
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self):
        """checks to see if there are questions left
        """
        return self.question_number < len(self.question_list)

    def next_question(self, user_answer):
        """
        calls check_answer and obtains the next Question
        object in the question_list

        Parameters
        ----------
        user_answer: str
            the users answer
        """
        self.check_answer(user_answer)
        self.question_number += 1
        self.current_question = self.question_list[self.question_number]

    def check_answer(self, user_answer):
        """checks the user_answer against the
        correct answer

        Parameters
        ----------
        user_answer: str
            the users answer
        """
        correct_answer = self.current_question.answer
        if str(user_answer).lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")
