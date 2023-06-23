class QuizMaster():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()
        self.check_answer(answer, current_question.answer)

    def more_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, r_answer):
        if answer == r_answer:
            print("That's right")
            self.score += 1
        else:
            print("WRONG!!")

        print(f"Your current score is: {self.score} / {len(self.question_list)}\n")
