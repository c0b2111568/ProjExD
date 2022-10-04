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
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") 
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 
numbers = list(range(9, -1, -1)) 
pulus = ["+"] 
for i, num in enumerate(numbers+pulus, 1):
    botton = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    botton.bind("<1>", click_number)
    botton.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
botton = tk.Button(root, text = f"=",font=("",30),width=4,height=2)
botton.bind("<1>", click_equal)
botton.grid(row=r, column=c)
root.mainloop()