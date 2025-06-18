from question_model import Question
from data import question_data as qd

# print(question_data[0]['text'])

question_bank = []

# for i in range(len(qd)):
#     question_bank.append(Question(qd[i]['text'], qd[i]['answer']))

for i in qd:
    qd_text = i['text']
    qd_answer = i['answer']
    new_question = Question(qd_text, qd_answer)
    question_bank.append(new_question)


for i in question_bank:
    print(f"question: {i.text}\n"
          f"answer: {i.answer}")
