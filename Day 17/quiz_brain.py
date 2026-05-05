class QuizBrain():

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = (self.question_list[self.question_number]).text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question} (True / False)?:")
        self.is_answer_correct(current_answer, user_ans)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def is_answer_correct(self, correct_ans, answer):
        if correct_ans == answer:
            print("correct")
            self.score += 1
        else:
            print("That is wrong")
            print(f"The correct answer is: {correct_ans}")
        print(f"Your current score is {self.score}/{len(self.question_list)}")
        print("\n")