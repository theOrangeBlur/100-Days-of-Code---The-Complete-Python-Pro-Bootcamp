import turtle
import pandas

screen = turtle.Screen()
screen.title("Fifty States Game")
image = "Day25-Pandas/states/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

data = pandas.read_csv("Day25-Pandas/states/50_states.csv")

name_turt = turtle.Turtle()
name_turt.penup()
name_turt.hideturtle()


#turtle.onscreenclick(get_mouse_click_coor)
score = 0
correct_guess_list = []
while len(correct_guess_list) < 50:
    answer_state = screen.textinput(title="Guess the States!", prompt=f"{score}/50:")
    answer_state = answer_state.title()

    if len(data[data.state == answer_state]) and correct_guess_list.count(answer_state) == 0:
        state_row = data[data.state == answer_state]
        name_turt.goto(state_row.x.item(), state_row.y.item())
        name_turt.write(answer_state)
        score += 1
        correct_guess_list.append(answer_state)
    elif answer_state == 'Exit':
        break
    else:
        pass

#forgotten_states = data
#for guessed_state in correct_guess_list:
#    forgotten_states = forgotten_states.drop(forgotten_states[forgotten_states.state == guessed_state].index[0])
forgotten_states = [state for state in data.state.to_list() if state not in correct_guess_list]
df = pandas.DataFrame(forgotten_states)
df.to_csv("Day25-Pandas/states/forgotten.csv")



turtle.mainloop()