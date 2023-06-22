from question_model import Question
from questions import question_data

question_store = []
for item in question_data:
    question_store.append(Question(item['text'], item['answer']))

print(len(question_store))