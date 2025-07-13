from tkinter import *


def main():
    window = Tk()
    window.title('My first gui program')
    window.minsize(width = 500, height = 300)

    text = Entry(width = 10)
    text.insert(END,'0')
    text.grid(column=1,row=0)

    label1 = Label(text = 'Miles', font=('Arial', 24, "bold"))
    label1.grid(column=2,row=0)
    label2 = Label(text = 'is equal to', font=('Arial', 24, "bold"))
    label2.grid(column=0,row=1)
    
    label3 = Label(text = '0', font=('Arial', 24, "bold"))
    label3.grid(column=1,row=1)
    label4 = Label(text = 'km', font=('Arial', 24, "bold"))
    label4.grid(column=2,row=1)


    

    button = Button(text = 'Calculate',command=lambda: result(text, label3))
    button.grid(column=1,row=2)
    
    window.mainloop()
   
def result(text,label):
    miles = text.get()
    label['text'] = int(float(miles)* 1.60934)

    return int(miles)* 1.60934

    
if __name__ == '__main__':
    main()