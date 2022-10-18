import tkinter as tk
import maze_maker as mm # 練習8

# 練習5
def key_down(event):
    global key
    key = event.keysym


# 練習6
def key_up(event):
    global key
    key = ""

def count_up():
    global tmr
    tmr = tmr+1
    label["text"]=tmr
    jid = root.after(1000,count_up)


# 練習7
def main_proc():
    global mx,my
    global cx, cy
    global tori
    if key == "Up":
        tori = tk.PhotoImage(file="fig/4.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        my -= 1
    if key == "Down":
        tori = tk.PhotoImage(file="fig/3.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        my += 1
    if key == "Left":
        tori = tk.PhotoImage(file="fig/1.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        mx -= 1
    if key == "Right":
        tori = tk.PhotoImage(file="fig/6.png")
        canv.create_image(cx, cy, image=tori, tag="tori")
        mx += 1
    if maze_lst[my][mx]==0:
        cx,cy = mx*100+50,my*100+50
        if key == "Up":
            tori = tk.PhotoImage(file="fig/4.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
        if key == "Down":
            tori = tk.PhotoImage(file="fig/3.png")
            canv.create_image(cx, cy, image=tori, tag="tori") 
        if key == "Left":
            tori = tk.PhotoImage(file="fig/1.png")
            canv.create_image(cx, cy, image=tori, tag="tori")
        if key == "Right":
            tori = tk.PhotoImage(file="fig/6.png")
            canv.create_image(cx, cy, image=tori, tag="tori")

    else:
        if key == "Up": 
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    


    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    root1 =tk.Tk()
    label = tk.Label(root1,font=("",80))
    label.pack()

    tmr = 0
   

    

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習9,10
    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst) # 1:壁／0:床
    mm.show_maze(canv, maze_lst) 

    # 練習3
    tori = tk.PhotoImage(file="fig/5.png")
    mx,my = 1,1 
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 練習7
    main_proc()

       
    #root.mainloop()
    root1.after(1000,count_up)
    root1.mainloop()
    