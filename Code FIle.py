import random
from tkinter import *
import tkinter.font as tkFont
import time

root =Tk()
root.title("Project")
root.geometry("850x600")

root.configure(bg='#39B55F')

#Title
l=Label(root,text="Typing  Speed Test ",font=("Times new roman",20),bg="orange",fg="black").pack()
##Icon
root.iconbitmap('D:\Python Project\icon.ico')
##Creating Input
large_font = ('Verdana',20)
e = Entry(root, width='50', bg="white", fg="black",font=large_font)
e.place(x=27, y=100)
e.focus()
# DISPLAY SENTENCES
fontStyle = tkFont.Font(family="Lucida Grande", size=25)
text = Label(root,font=("Times new roman",20),bg="blue",fg="white")
text.place(x=27, y=50)
def randomTXT():
    f = open('D:\Python Project\Sentence.txt').read()
    sentences = f.split('\n')
    display = random.choice(sentences)
    text.config(text=display)
randomTXT()
##Button
switch = Button(root, text="Switch", bg='white', fg='black', font=("Aerial",10), padx=15, pady=5,command=randomTXT)
switch.place(x=150,y=200)

t0 = time.time()
def calculate(args,*kwargs):
    t1 = time.time()
    st = e.get()
    w_count = len(st.split())
    mylabel = Label(root, text="TOTAL WORDS: " + str(w_count))
    mylabel.place(x=85, y=435)
    mylabel = Label(root, text="TIME TAKEN: " + str(round(t1 - t0)))
    mylabel.place(x=315, y=435)
    if (t1 - t0) >= 60:
        mylabel = Label(root, text="SPEED: POOR")
        mylabel.place(x=533, y=435)
    elif(t1 - t0) >= 30 and (t1 - t0) <= 60    :
        mylabel = Label(root, text="SPEED: AVERAGE")
        mylabel.place(x=533, y=435)
    else:
        mylabel = Label(root, text="SPEED: EXCELLENT")
        mylabel.place(x=533, y=435)

calculate()

b=Button(root,text="Result",font=("Aerial",10),padx=15,pady=5,bg="white",fg="black",command=calculate)
b.place(x=300,y=200)

# Clear ENTRY
def clearfunc():
    e.delete(0, 'end')

switch = Button(root,text="RESET", bg='white', fg='black', font=("Aerial",10), padx=15, pady=5,command=clearfunc)
switch.place(x=450, y=200)
root.mainloop()
