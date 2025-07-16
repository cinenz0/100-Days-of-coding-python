from tkinter import *
import pandas as pd
import json
import random
import time
DATA = pd.read_csv('data/french_words.csv')
BACKGROUND_COLOR = "#B1DDC6"
word_index = None
#---------------- Right button ---------------#
def right_b():
    global word_index
    print(word_index)
    try:
        df_to_learn = pd.read_csv('data/minus_right.csv')
        
    except FileNotFoundError:
        df_to_learn = DATA
       
    df_to_learn = df_to_learn.drop(index=word_index)
    df_to_learn.to_csv('data/minus_right.csv',index=False)
    button_pressed(df_to_learn)
#---------------- Wrong button ---------------#

#---------------- Button pressed -------------#
def button_pressed(biscoito = pd.DataFrame({})):
    canvas.itemconfig(image, image = CARD_FRONT)
    canvas.itemconfig(lang, text = 'French')
    if not biscoito.empty:
        random_word_french(biscoito)
    else:
        random_word_french()
    
#------------------ Random word --------------#
def random_word_french(data = DATA):
    french_dict = data['French'].to_dict()
    values = french_dict.values()
    random_word = random.choice(list(values))
    global word_index
    word_index = data[data['French'] == random_word].index[0]
    #index = DATA[random_word].index
    canvas.itemconfig(word, text = random_word)
    window.after(1000, flip, word_index)
    return word_index


#--------------- Flip the Card ---------------#
def flip(index):
    eng_dict = DATA['English'].to_dict()
    new_word = eng_dict[index]
    canvas.itemconfig(image, image = CARD_BACK)
    canvas.itemconfig(lang, text = 'English')
    canvas.itemconfig(word, text = new_word)
    
    
#---------------------- UI -------------------#

window = Tk()
CARD_BACK = PhotoImage(file = 'images/card_back.png')
CARD_FRONT = PhotoImage(file = 'images/card_front.png')
RIGHT = PhotoImage(file = 'images/right.png')
WRONG = PhotoImage(file = 'images/wrong.png')

window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
window.title('Flashy')

#Canvas image setup
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column = 0, row = 0, columnspan = 3)
image = canvas.create_image(400,263,image = CARD_FRONT)

#Canvas text setup
lang = canvas.create_text(400,150,text="",fill = 'black',font=('Arial', 40, "italic"))
word = canvas.create_text(400,253,text="",fill = 'black',font=('Arial', 60, "bold"))
#Buttons setup
wrong_button = Button(image = WRONG, highlightthickness = 0, command = button_pressed)
wrong_button.grid(column = 0, row = 1)
right_button = Button(image = RIGHT, highlightthickness = 0, command = right_b)
right_button.grid(column = 2, row = 1)
button_pressed()
window.mainloop()