import turtle
import pandas

screen = turtle.Screen()
screen.title("Country Test")
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
state_list = []
guessed_states = []

state_data = pandas.read_csv('./50_states.csv')
all_states = state_data["state"].tolist()

while len(guessed_states) < 50:
    answer_state = turtle.textinput(
        title=f'Guess your state {len(guessed_states)}/50', prompt="What's a state name")

    if answer_state in all_states:
        state_value = state_data[state_data["state"] == answer_state]
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_value['x']), int(state_value["y"]))
        t.write(answer_state)
    else:
        print("State not found")

screen.exitonclick()
