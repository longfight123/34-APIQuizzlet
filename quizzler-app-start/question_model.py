class Question:
    """
    A class used to represent a Question.

    ...

    Attributes
    ----------
    text: str
        the question
    answer: str
        the answer

    """
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
