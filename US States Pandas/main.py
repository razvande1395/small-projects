import pandas
import turtle


def answer_check(state_answer: str, states: list):
    global states_guessed
    for i in states:
        if state_answer == str(i):
            states_guessed += 1
            guessed_list.append(i)
            return str(i)


def get_coords(state):
    x, y = [0, 0]
    coordinates = states_data.loc[states_data.state == state]
    x = coordinates.iloc[0]["x"]
    y = coordinates.iloc[0]["y"]
    return x, y


def write_state(x, y):
    cursor.hideturtle()
    cursor.penup()
    cursor.goto(x, y)
    cursor.write(current_state)
    cursor.pendown()


x_state = 0
y_state = 0
states_guessed = 0
total_states = 50
guessed_list = []

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()


cursor = turtle.Turtle()
screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_list) < 50:

    answer = screen.textinput(title= f"{states_guessed}/{total_states} States Correct", prompt= "Type in a state's name").title()
    
    if answer in states_list and answer not in guessed_list:
        current_state = answer_check(answer, states_list)
        x_state, y_state = get_coords(current_state)
        write_state(x_state, y_state)
    elif answer == "Exit":
        missed_states = [x for x in states_list if x not in guessed_list]
        missed_states = pandas.DataFrame(missed_states, columns= ["State"])
        missed_states.to_csv("Missed-States.csv")
        break

screen.exitonclick()
