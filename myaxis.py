"""
Простая демонстрация "путешествий по оси X".
Создано с целью показать мысленные перемещаения воображаемого курсора во время вычислений, выполняемых "в уме".

Окно с осью Х и возможностью перемещаться
по этой оси от -50 до 50
"""

from tkinter import *
root = Tk()

scl = Scale(root, label="X axis", tickinterval=10, resolution=1, length=300, from_=-50, to=50)
var = IntVar()
scl.config(variable=var)
Label(root, text="Grafical calculator by Dmitry Pupkin (aka Inferno)").pack(side=TOP)

scl.config(orient='horizontal')
scl.pack(expand=YES,fill=X,anchor=CENTER)

ent = Entry()
ent.insert(0,'type exp here')
ent.config(width=100)

def mycalculator():
	myexp = ent.get()
	myexp = myexp.strip()
	myresult = eval(myexp)
	var.set(myresult)

Button(root, text="Calculate", command=mycalculator).pack(side=BOTTOM)


ent.pack(side=BOTTOM)
root.mainloop()
