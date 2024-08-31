import tkinter as tk
from random import choice

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(choices)
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create and place the buttons
rock_button = tk.Button(root, text="Rock", width=15, height=2, command=lambda: determine_winner('Rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=15, height=2, command=lambda: determine_winner('Paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=15, height=2, command=lambda: determine_winner('Scissors'))
scissors_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=('Helvetica', 12), pady=20)
result_label.pack()

# Run the application
root.mainloop()
