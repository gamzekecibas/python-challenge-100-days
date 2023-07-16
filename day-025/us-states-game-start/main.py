import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## Alternative way to learn coordinates on the screen
#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

states_df = pd.read_csv('50_states.csv')
states_df["state"] = states_df["state"].str.lower()
all_states = states_df['state'].to_list()

correct_states = 0
guessed_states = []

while correct_states != len(states_df):
    answer_state = screen.textinput(title = f"{correct_states}/{len(states_df)} States Correct ", prompt = "What's another state name?").lower()

    if answer_state == 'exit':
        non_guessed_states = states_df[~states_df["state"].isin(guessed_states)]
        non_guessed_states['state'] = non_guessed_states['state'].str.title()
        non_guessed_states['state'].to_csv('missing_states.csv')
        print(f'Missing {len(non_guessed_states)}/{len(states_df)} states are writing to missing_states.csv!')
        break

    if answer_state in all_states:
        current_state_x, current_state_y = (float(states_df[states_df.state == answer_state].x),
                                            float(states_df[states_df.state == answer_state].y))
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(current_state_x, current_state_y)
        t.write(answer_state.title())
        guessed_states.append(answer_state)
        correct_states += 1



