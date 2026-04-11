import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    computer_choice = random.choice(choices)
    
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    

    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)
    result_label.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")


title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack(pady=10)

user_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)


root.mainloop()