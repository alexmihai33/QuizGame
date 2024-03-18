from quiz_brain import QuizBrain
from questions import question_data
from question_model import Question

question_bank = []

for i in range(len(question_data)):
    new_question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print("Welcome to the quiz game!")
print("Type 'True' or 'False' as answers.")

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz! Thanks for playing!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
