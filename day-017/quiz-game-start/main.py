from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in range(len(question_data)):
    question_bank.append(Question(
        question_data[q]['text'],    ## when data is used from open database, the key should be 'question' &
        question_data[q]['answer']   ## the key should be 'correct_answer'
    ))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): ## if quiz still remaining:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score: {quiz.score}/{len(question_bank)}")