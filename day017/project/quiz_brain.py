class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list

    def next_question(self):
        """
        Asks the user the next question and updates the question index for an upcoming call.
        Checks that the user answered correctly or not.
        """
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}\ntrue/false: ")
        self.check_answer(question.answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

