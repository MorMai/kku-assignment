from cProfile import label
import tkinter
import random as rd
import secrets
import math as m
from tkinter import *
from PIL import ImageTk, Image


def easyStart():

    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)


    def try_again():
        try_again.num1update = rd.randint(0,999)
        try_again.num2update = rd.randint(0,999)
        op_choices = ["+", "-", "*", "/"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999)
            try_again.num2update = rd.randint(0,99)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    easytext = Label(
        root,
        text = "EASY MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    easytext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)


def normalStart():

    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)


    def try_again():
        try_again.num1update = rd.randint(0,99999)
        try_again.num2update = rd.randint(0,99999)
        op_choices = ["+", "-", "*", "/", "^"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(1,9)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,99)
            try_again.num2update = rd.randint(0,3)
            try_again.ans = try_again.num1update ** try_again.num2update
            newQ = Label(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    normaltext = Label(
        root,
        text = "NORMAL MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    normaltext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)


def hardStart():

    def submt(var1):
        if var1.get() == str(resultPLUS()):
            correct = Label(
                root,
                text="Correct!",
                fg="green",
                font=("Courier", 16))
            correct.place(relx=0.435, rely=0.17)
        else:
            wrong = Label(
                root,
                text="Wrong!!!",
                fg="red",
                font=("Courier", 16))
            wrong.place(relx=0.435, rely=0.17)


    def try_again():
        try_again.num1update = rd.randint(0,9999999)
        try_again.num2update = rd.randint(0,9999999)
        op_choices = ["+", "-", "*", "/", "^", "sqrt"]
        try_again.op_rand = secrets.choice(op_choices)
        
        if try_again.op_rand == "+":
            try_again.ans = try_again.num1update + try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} + {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "-":
            try_again.num1update = rd.randint(0,999999)
            try_again.num2update = rd.randint(0,99999)
            try_again.ans = try_again.num1update - try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} - {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "*":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(0,999)
            try_again.ans = try_again.num1update * try_again.num2update

            newQ = Label(
                root,
                text=f"{try_again.num1update} * {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "/":
            try_again.num1update = rd.randint(0,9999)
            try_again.num2update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (try_again.num1update / try_again.num2update))
            newQ = Label(
                root,
                text=f"{try_again.num1update} / {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "^":
            try_again.num1update = rd.randint(0,30)
            try_again.num2update = rd.randint(0,9)
            try_again.ans = try_again.num1update ** try_again.num2update
            newQ = Label(
                root,
                text=f"{try_again.num1update} ^ {try_again.num2update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

        if try_again.op_rand == "sqrt":
            try_again.num1update = rd.randint(1,999)
            try_again.ans = ("%.2f" % (m.sqrt(try_again.num1update)))
            newQ = Label(
                root,
                text=f"√{try_again.num1update}",
                font=("Courier", 16)
            )
            newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


    def resultPLUS():
        try_again
        return try_again.ans

    def delete():
        solving.delete(1)

    hardtext = Label(
        root,
        text = "HARD MODE",
        font = ("Comic sans MS",16,"bold"),
        background = "#ffffff")
    hardtext.pack(pady=(30,0))

    start = Button(
        root,
        text = "Start",
        font = ("Courier", 16),
        command = try_again)
    start.place(relx=0.45, rely=0.2)

    solving = Entry(
        root,
        justify = "center",
        font = ("Courier", 16))
    solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

    submit = Button(
        root,
        text = "Submit",
        font = ("Courier", 16),
        command=lambda: submt(solving))
    submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

    try_again = Button(
        root,
        text = "Try Again",
        font = ("Courier", 16),
        command = try_again)
    try_again.place(relx=0.42, rely=0.9)


root = tkinter.Tk()
root.title("Super Quiz")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

def easyIspressed():
    labeltext.destroy()
    btnStartEasy.destroy()
    btnStartNormal.destroy()
    btnStartHard.destroy()
    lblInstruction.destroy()
    easyStart()

def normalIspressed():
    labeltext.destroy()
    btnStartEasy.destroy()
    btnStartNormal.destroy()
    btnStartHard.destroy()
    lblInstruction.destroy()
    normalStart()

def hardIspressed():
    labeltext.destroy()
    btnStartEasy.destroy()
    btnStartNormal.destroy()
    btnStartHard.destroy()
    lblInstruction.destroy()
    hardStart()

labeltext = Label(
    root,
    text = "Super Math Quiz",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff"
)
labeltext.pack(pady=(30,10))

easy = PhotoImage(file="easy.png")

btnStartEasy = Button(
    root,
    image = easy,
    relief = FLAT,
    border = 0,
    command = easyIspressed,
    background = "#ffffff"
)
btnStartEasy.pack(pady=(10,0))

normal = PhotoImage(file="normal.png")

btnStartNormal = Button(
    root,
    image = normal,
    relief = FLAT,
    border = 0,
    command = normalIspressed,
    background = "#ffffff"
)
btnStartNormal.pack(pady=(10,0))

hard = PhotoImage(file="hard.png")

btnStartHard = Button(
    root,
    image = hard,
    relief = FLAT,
    border = 0,
    command = hardIspressed,
    background = "#ffffff"
)
btnStartHard.pack(pady=(10,20))

lblInstruction = Label(
    root,
    text = "Math Quiz is a great way to check your math skills! \n Children pick from four math quizzes: Addition, Subtraction, Multiplication & Division.",
    font = ("Consolas",8),
    justify = "center",
    background = "#ffffff"
)
lblInstruction.pack()

root.mainloop()