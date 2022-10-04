import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("おためしか")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning(txt,f"{txt}ボタンがクリックされました")

Button0=tk.Button(root,text="0",width=4,height=2,font=("Times New Roman",30))
Button1=tk.Button(root,text="1",width=4,height=2,font=("Times New Roman",30))
Button2=tk.Button(root,text="2",width=4,height=2,font=("Times New Roman",30))
Button3=tk.Button(root,text="3",width=4,height=2,font=("Times New Roman",30))
Button4=tk.Button(root,text="4",width=4,height=2,font=("Times New Roman",30))
Button5=tk.Button(root,text="5",width=4,height=2,font=("Times New Roman",30))
Button6=tk.Button(root,text="6",width=4,height=2,font=("Times New Roman",30))
Button7=tk.Button(root,text="7",width=4,height=2,font=("Times New Roman",30))
Button8=tk.Button(root,text="8",width=4,height=2,font=("Times New Roman",30))
Button9=tk.Button(root,text="9",width=4,height=2,font=("Times New Roman",30))

Button0.grid(row = 3,column=0)
Button1.grid(row = 2,column=2)
Button2.grid(row = 2,column=1)
Button3.grid(row = 2,column=0)
Button4.grid(row = 1,column=2)
Button5.grid(row = 1,column=1)
Button6.grid(row = 1,column=0)
Button7.grid(row = 0,column=2)
Button8.grid(row = 0,column=1)
Button9.grid(row = 0,column=0)


Button0.bind("<1>",button_click)
Button1.bind("<1>",button_click)
Button2.bind("<1>",button_click)
Button3.bind("<1>",button_click)
Button4.bind("<1>",button_click)
Button5.bind("<1>",button_click)
Button6.bind("<1>",button_click)
Button7.bind("<1>",button_click)
Button8.bind("<1>",button_click)
Button9.bind("<1>",button_click)

root.mainloop()