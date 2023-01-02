class Question_Class:

    score = 0


    def display_question(self, question):
        print(question)


    def check_answer(self, user_answer, answer_list):
        if user_answer in answer_list:
            Question_Class.score += 1
            print("Correct!")
        else:
            print("Wrong answer.")
    
