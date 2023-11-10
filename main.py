import turtle
import pandas
from datetime import datetime

screen = turtle.Screen()
screen.title("Color guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Generate a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

data = pandas.read_csv("50_color.csv")
# data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Add a new column to your dataframe with the timestamp
data['timestamp'] = timestamp


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 colors Correct",
                                    prompt="What's another color?").title()

    if answer_state == "Exit":
        missing_color = []
        for color in all_states:
            if color not in guessed_states:
                missing_color.append(color)
        print(missing_color)
        new_data = pandas.DataFrame(missing_color)
        new_file = screen.textinput(title=f"Save file as",
                                    prompt="What is your name?")
        new_data.to_csv(f"{new_file}_{timestamp}.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        print(f"NICE! {answer_state} is on the MAP!!!")

screen.exitonclick()
