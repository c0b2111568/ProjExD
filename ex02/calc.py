
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

def click_AC(event):
    entry.delete(0,tk.END)

def click_C(event):
    C = entry.get()
    entry.delete(len(C)-1,tk.END)
    

root = tk.Tk() 
root.geometry("400x700")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") 
entry.grid(row=0, column=0, columnspan=3)

r_num, c_num = 2, 0 
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

r_Ca, c_Ca = 2, 0 
for j in Calcula:
    botton_Ca = tk.Button(root, text=f"{j}", font=("", 30), width=4, height=2,bg="#FFD700")
    botton_Ca.bind("<1>", click_number)
    botton_Ca.grid(row=r_Ca, column=3-c_Ca)
    r_Ca += 1
    if r_Ca==6:
        r_Ca=5
        c_Ca=2

btn_eq = tk.Button(root, text = f"=",font=("",30),width=4,height=2,bg="#FFD700")
btn_eq.bind("<1>", click_equal)
btn_eq.grid(row=5, column=2)

btn_AC = tk.Button(root, text = f"AC",font=("",30),width=4,height=2,bg="#FFD700")
btn_AC.bind("<1>", click_AC)
btn_AC.grid(row=1, column=0)

btn_C = tk.Button(root, text = f"C",font=("",30),width=4,height=2,bg="#FFD700")
btn_C.bind("<1>", click_C)
btn_C.grid(row=1, column=1)

root.mainloop()