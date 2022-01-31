from tkinter import *
tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.create_oval(50,50,450,450,fill='yellow')
canvas.create_oval(150,100,200,150,fill='black')
canvas.create_oval(300,100,350,150,fill='black')
canvas.create_arc(100,100,400,400,start=180,extent=180,style='arc')
canvas.pack()
