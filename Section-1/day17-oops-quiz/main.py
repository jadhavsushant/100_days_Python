from data import question_data
from question_model import Question

from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    que_text = question['question']
    que_ans = question['correct_answer']
    new_question = Question(que_text, que_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.is_still_has_question():
    quiz.next_question()

print("\nYou have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.que_no}")