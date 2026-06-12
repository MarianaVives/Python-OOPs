from Question import Question
from questions_api import questions_and_ans as data
from quiz_app import QuizBrain
from ui import QuizInterface

question_bank=[]

for d in data:
    question_text = d["question"]
    question_answer = d["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions():
#    quiz.next_question()

print("***********************************************************************************************************")
print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")
print("***********************************************************************************************************")
