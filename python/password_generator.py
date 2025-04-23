from string import digits as digi
from string import ascii_lowercase as asl
from string import ascii_uppercase as asu
from string import punctuation as p 
import random as r
import tkinter as tk
def check_selection():
    selected = listBox.curselection()
    list_of = [listBox.get(i) for i in selected]
    n = characters.get()
    s = ""
    if "uppercase" in list_of:
        s += asu
    if "lowercase" in list_of:
        s += asl
    if "digits" in list_of:
        s += digi 
    if "punctuations" in list_of:
        s += p 
     
    ss = ""
    for _ in range(n):
        ss += r.choice(s)
    text_area.delete("1.0",tk.END)
    text_area.insert(tk.END,ss)

        


Tin = tk.Tk()
Tin.geometry("300x300")
Tin.title("password generator")
label = tk.Label(Tin,text="choose the options for strong password")
label.pack()

characters = tk.IntVar()
listBox = tk.Listbox(bg="black",selectmode="multiple",height=4,fg="white")
listBox.insert(1,"uppercase")
listBox.insert(2,"lowercase")
listBox.insert(3,"digits")
listBox.insert(4,"punctuations")
text_area = tk.Text(Tin,height=2,width=20)
label1 = tk.Label(Tin,text="choose the number of characters")
char_entry = tk.Entry(Tin,textvariable=characters)
button1 = tk.Button(Tin,text="generate",width=25,bg="blue",command=check_selection,fg="white")

listBox.pack()

label1.pack()
char_entry.pack()
button1.pack(padx=5,pady=5)
text_area.pack(padx=5,pady=5)

Tin.mainloop()