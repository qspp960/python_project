import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="What's the another states name?").title()
    if answer_state == 'Exit':
        #unguessed_states = []
        #for state in all_states:
        #    if state in guessed_states:
        #       pass
        #   else:
        #      unguessed_states.append(state)
        unguessed_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(unguessed_states)
        df.to_csv("unguessed_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)




screen.exitonclick()