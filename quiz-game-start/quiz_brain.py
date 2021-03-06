##TODO 1: Asking question
##TODO 2: Check if answer correct
##TODO 3: Check if were at end of quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def still_have_question(self):
        return self.question_number < len(self.question_list)
#        if self.question_number <= len(self.question_list)
#            return True
#        else:
#            False
# 5 > 3 returns True
# 3 > 5 returns False
    def next_question(self):
        current_question = self.question_list[self.question_number]
#        current_question.text
        self.question_number+= 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True or False): \n")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"THe correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")