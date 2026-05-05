from Question import Question
from data import question_data as data
from quiz_brain import QuizBrain

question_bank=[]

for d in data:
    question_text = d["text"]
    question_answer = d["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("***********************************************************************************************************")
print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")
print("***********************************************************************************************************")
