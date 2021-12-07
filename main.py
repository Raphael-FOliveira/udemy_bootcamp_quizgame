from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"]) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print(50 * "\n" + "You have finished the Quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")