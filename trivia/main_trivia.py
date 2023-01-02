from trivia import Question_Class
from trivia_list import answers_list, question_list


quest = Question_Class()

number = 0

while number < len(question_list):
    
    quest.display_question(question_list[number])
    answer = input("Please type your answer: ")
    quest.check_answer(answer, str(answers_list[number]))
    
    number += 1


if quest.score == 10:
    print("You're very good at this game, you got every answer!")
elif quest.score == 0:
    print("You're pretty bad at this trivia thing, you scored 0 points.")
elif quest.score > 5:
    print(f"Well done! Your score is {quest.score}.")
else:
    print(f"Your score is {quest.score}.")

