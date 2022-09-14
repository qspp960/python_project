class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        question = self.question_list[self.question_number]

        user_input = input(f"Q{self.question_number+1}: {question.text} (True/False)")
        self.question_number += 1
        self.check_answer(user_input,question.answer)


    def check_answer(self, user_input, answer):
        if user_input.lower() == answer.lower():
            print("You got it")
            self.score += 1
        else:
            print("NO answer")