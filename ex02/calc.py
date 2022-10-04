import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num) 

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0,tk.END)
    entry.insert(tk.END, res) 



root = tk.Tk() 
root.geometry("400x700")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") 
entry.grid(row=0, column=0, columnspan=3)

r_num, c_num = 1, 0 
numbers = list(range(9, -1, -1)) 
Calcula = ["+","-","*","/","."] 

for i, num in enumerate(numbers, 1):
    botton_num = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2,bg = "#FFFFFF")
    botton_num.bind("<1>", click_number)
    botton_num.grid(row=r_num, column=c_num)
    c_num += 1
    if i%3 == 0:
        r_num += 1
        c_num = 0

r_Ca, c_Ca = 1, 0 
for j in Calcula:
    botton_Ca = tk.Button(root, text=f"{j}", font=("", 30), width=4, height=2,bg="#FFD700")
    botton_Ca.bind("<1>", click_number)
    botton_Ca.grid(row=r_Ca, column=3-c_Ca)
    r_Ca += 1
    if r_Ca==5:
        r_Ca=4
        c_Ca=2

botton = tk.Button(root, text = f"=",font=("",30),width=4,height=2,bg="#FFD700")
botton.bind("<1>", click_equal)
botton.grid(row=r_num, column=c_num+1)
root.mainloop()