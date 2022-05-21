class QuizBrain:

    def __init__(self, q_list):
        self.que_no = 0
        self.question_list = q_list
        self.score = 0

    def is_still_has_question(self):
        return self.que_no < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.que_no]
        self.que_no += 1
        user_answer = input(f"Q.{self.que_no} {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it wright!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer was:{current_answer}")
        print(f"Your current score is {self.score}/{self.que_no}")



