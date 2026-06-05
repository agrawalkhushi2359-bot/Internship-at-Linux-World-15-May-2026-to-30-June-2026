# a game with computer 😃
from tkinter import *
import random
computer_choice = random.randint(1, 10)
chance = 3
r = Tk()
r.geometry("380x350")
r.title("Game with Computer 😃")
r.config(bg="lightpink")
Label(r, text="🎮 Number Guessing Game",bg="lightpink", fg="black", font=("Arial", 18, "bold")).pack(pady=10)
Label(r, text="1. Enter number from 1 to 10 🤔", bg="lightpink", fg="blue", font=("Arial", 12)).pack()
Label(r, text="2. You have only 3 chances 😗",bg="lightpink", fg="red",font=("Arial", 12, "bold")).pack()
e = Entry(r, font=("Arial", 16), justify="center")
e.pack(pady=20)
l = Label(r, text="❤️ Chances Left : 3",bg="lightpink", fg="purple",font=("Arial", 13, "bold"))
l.pack()
res = Label(r, bg="lightpink",font=("Arial", 14, "bold"))
res.pack(pady=15)
def check():
    global chance
    user_choice = int(e.get())
    if user_choice >= 1 and user_choice <= 10:
        chance -= 1
        l.config(text=f"❤️ Chances Left : {chance}")
        if user_choice == computer_choice:
            res.config(text="🎉 You Win!! 😎", fg="green")
            e.config(state="disabled")
        else:
            if chance == 0:
                res.config(text="😢 You Lose!! 🥲", fg="red")
                e.config(state="disabled")
            else:
                res.config(text="❌ Wrong Guess Try Again", fg="orange")
    else:
        res.config(text="⚠ Enter Number 1 to 10 Only 🤷‍♀️", fg="blue")
Button(r, text="CHECK", command=check,bg="white", fg="black",font=("Arial", 12, "bold")).pack(pady=10)
Button(r, text="EXIT", command=r.destroy, bg="red", fg="white",font=("Arial", 12, "bold")).pack()
r.mainloop()