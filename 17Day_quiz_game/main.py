from question_model import Question
from data import question_data as qd
from data import question_data2 as qd2
from quiz_brain import QuizBrain

question_bank = []

# for i in range(len(qd)):
#     question_bank.append(Question(qd[i]['text'], qd[i]['answer']))

# for i in qd:
#     qd_text = i['text']
#     qd_answer = i['answer']
#     new_question = Question(qd_text, qd_answer)
#     question_bank.append(new_question)

for i in qd2:
    qd_text = i['question']
    qd_answer = i['correct_answer']
    new_question = Question(qd_text, qd_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    if quiz_brain.next_question():
        continue
    else:
        break

print("You've completed the quiz!\n"
      f"Your final score was: {quiz_brain.score}/{len(question_bank)}")

# quiz_brain.get_final_result()

# Test Prints
# print(question_data[0]['text'])
# for i in question_bank:
#     print(f"question: {i.text}\n"
#           f"answer: {i.answer}")
