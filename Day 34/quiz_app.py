import html
class QuizBrain():

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        #self.current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True / False)?:"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def is_answer_correct(self, user_ans:str):
        correct_ans = self.current_question.answer
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            return True
        else:
            return False
