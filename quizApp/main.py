from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for d in question_data['results']:
    question_bank.append(Question(d['question'], d['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've reach the end of the quiz.")
print(f"Your total score is: {quiz.score}/{quiz.question_number}")