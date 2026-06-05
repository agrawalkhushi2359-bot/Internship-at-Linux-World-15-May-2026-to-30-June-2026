import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "√":
        try:
            screen.set(math.sqrt(float(screen.get())))
        except:
            screen.set("Error")
    elif text == "sin":
        screen.set(math.sin(math.radians(float(screen.get()))))
    elif text == "cos":
        screen.set(math.cos(math.radians(float(screen.get()))))
    elif text == "tan":
        screen.set(math.tan(math.radians(float(screen.get()))))
    elif text == "log":
        try:
            screen.set(math.log10(float(screen.get())))
        except:
            screen.set("Error")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Scientific Calculator")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    '7','8','9','/','C',
    '4','5','6','*','sin',
    '1','2','3','-','cos',
    '0','.','=','+','tan',
    '√','log'
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(frame, text=button, font="Arial 15", width=5, height=2)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()