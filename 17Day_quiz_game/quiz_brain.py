class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


    def next_question(self):
        text = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {text.text} (True/False)?: ")
        if answer.lower() == 'true' or answer.lower() == 'false':
            self.check_answer(answer, text.answer)
            return True
        else:
            print("The unknown answer was inputted. It's the end of the program.")
            return False

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def get_final_result(self):
        print("You've completed the quiz!\n"
              f"Your final score was: {self.score}/{self.question_number}")