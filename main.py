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
all_color = data.color.to_list()
guessed_colors = []

# Add a new column to your dataframe with the timestamp
data['timestamp'] = timestamp


while len(guessed_colors) < 50:
    answer_color = screen.textinput(title=f"{len(guessed_colors)}/50 colors Correct",
                                    prompt="What's another color?").title()

    if answer_color == "Exit":
        missing_color = []
        for color in all_color:
            if color not in guessed_colors:
                missing_color.append(color)
        print(missing_color)
        new_data = pandas.DataFrame(missing_color)
        new_file = screen.textinput(title=f"Save file as",
                                    prompt="What is your name?")
        new_data.to_csv(f"{new_file}_{timestamp}.csv")
        break

    if answer_color in all_color:
        guessed_colors.append(answer_color)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        color_data = data[data.color == answer_color]
        t.goto(int(color_data.x), int(color_data.y))
        t.write(answer_color)
        print(f"NICE! {answer_color} is on the MAP!!!")

screen.exitonclick()
