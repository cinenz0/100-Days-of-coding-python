from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK = [1,3,5,7]
SHORT_BREAK = [2,4,6]
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_marks
    window.after_cancel(timer)
    title.config(text='Timer',fg ='RED')
    check_marks = ''
    check_mark.config(text = check_marks)
    canvas.itemconfig(timer_text,text= '00:00')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps in WORK:
        title.config(text = 'Work Time', fg = GREEN)
        count_down(work_sec)
    elif reps == 8:
        title.config(text = 'Long Break', fg = RED)
        count_down(long_break_sec)
    elif reps in SHORT_BREAK:
        title.config(text = 'Short break', fg = PINK)
        count_down(short_break_sec)
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_marks
    global timer

    count_minute = math.floor(count / 60)
    count_sec = count%60
    if len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_sec}')
    if count > 0:
        timer =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks += '✔'
            check_mark.config(text = check_marks)
            

    
# ---------------------------- UI SETUP ------------------------------- #
window  =Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width = 200, height = 224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill = 'white',font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1,row =1)



title = Label(text='Timer', font=(FONT_NAME, 35, "bold"),fg=GREEN,bg = YELLOW)
title.grid(column =1,row =0)

start_button = Button(text = 'Start',highlightthickness=0, command= start_timer)
start_button.grid(column =0,row =2)
reset_button = Button(text = 'Reset',highlightthickness=0, command = reset_timer)
reset_button.grid(column =2,row =2)

check_marks = ''
check_mark = Label(text=check_marks,fg=GREEN,bg = YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()