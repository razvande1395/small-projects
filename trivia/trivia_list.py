
foo = "questions-trivia.txt"

with open(foo, encoding="utf8") as foo_file:
    initial_list = foo_file.readlines()
    

question_list = [x.strip().split("\n") for x in initial_list]

foo = "answers-trivia.txt"
print()

with open(foo, "r") as foo_file:
    first_list = foo_file.readlines()
    

answers_list = [x.strip().split("\n") for x in first_list]