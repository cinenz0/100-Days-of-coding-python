import turtle
import pandas as pd
from writer import Writer
screen = turtle.Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)



df = pd.read_csv('50_states.csv')
writer = Writer()

states = df['state']
correct = []
#check if the guess is in the states list
while True:
    user_answer = screen.textinput(title=f"{len(correct)}/50 States Correct",prompt = 'Whats the name of a US').title()
    if user_answer == 'Exit':
        missed_states = []
        [missed_states.append(state) for state in states.tolist() if state not in correct]
        learning = {'States': missed_states}
        learning = pd.DataFrame(learning)
        learning.to_csv('Learning.csv')
        break
    if user_answer in states.tolist():
        full_state = df.loc[states == user_answer]
        state,x,y = full_state['state'].item(), full_state['x'].item(), full_state['y'].item()
    
        writer.x = x
        writer.y = y
        writer.write_state(word=state)
        correct.append(user_answer)
        screen.update()

