import pandas
import turtle


def print_state_name(state_name, x, y):
    label = turtle.Turtle()
    label.penup()
    label.hideturtle()
    label.setx(x)
    label.sety(y)
    label.write(state_name)


SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
TOTAL_STATES = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
screen.bgpic("blank_states_img.gif")

states_csv = pandas.read_csv("50_states.csv")
states_names = states_csv["state"].tolist()

correct_guesses = 0

while correct_guesses < TOTAL_STATES:
    player_guess = screen.textinput(f"{correct_guesses}/50 States Correct", "Name a state:").title()
    print(player_guess)

    if player_guess == "Exit":
        pandas.DataFrame(states_names).to_csv("states_to_learn.csv")
        break
    elif player_guess in states_names:
        state = states_csv[states_csv["state"] == player_guess]
        print_state_name(player_guess, int(state["x"]), int(state["y"]))
        states_names.remove(player_guess)
        correct_guesses += 1

screen.exitonclick()
