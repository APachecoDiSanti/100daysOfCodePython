from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data["results"]:
    question_bank.append(
        Question(question["question"], question["correct_answer"])
    )

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print(f"Quiz is over! Your final score: {quiz_brain.score}/{quiz_brain.question_number}")
