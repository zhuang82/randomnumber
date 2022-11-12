import tkinter,random
w = tkinter.Tk()
n = tkinter.StringVar()
def a():
    global n
    n.set(str(random.choice([random.choice([x,]) for x in range(1,58) if not x in [19,]])))
t = tkinter.Label(text=n,textvariable=n,font=("MesloLGS-NF-Bold.ttf",96),borderwidth=96)
b = tkinter.Button(text="生成",command=a)
t.pack()
b.pack()
w.mainloop()