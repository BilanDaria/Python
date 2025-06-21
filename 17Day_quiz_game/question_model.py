class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_text(self):
        return self.text