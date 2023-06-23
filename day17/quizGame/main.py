'''
    This program asks user questions which user aswers with either true or false.
    Program runs until all questions are asked.
'''

from question_model import Question
from questions import question_data
from quiz_master import QuizMaster

question_store = []
for item in question_data:
    question_store.append(Question(item['text'], item['answer']))

quiz = QuizMaster(question_store)
while quiz.more_questions():
    quiz.next_question()

print(f"Your final score was: {quiz.score} / {len(question_store)}")