# importing tkinter
from tkinter import *
# importing tkk
from tkinter import ttk
import random
# importing showinfo message box
from tkinter.messagebox import showinfo

# creating the main window
main_window = Tk()
main_window.title("Hangman Game")
main_window.geometry("400x400+100+200")

# adding three columns to main window
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

# creating a label for title and attaching it to the main window
my_label = Label(main_window, text="Hangman Game", bg="#b3b3b3", fg="#ff3300", font=("Courier", 15))
my_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# creating a label for a message and attaching it to the main window
my_label2 = Label(main_window, text="Word to Guess", bg="#cccccc", fg="#3399ff", font=("Courier", 15))
my_label2.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# creating a text field for empty string and attaching it to the main window
txt_word = StringVar()
tf_word = ttk.Entry(main_window, textvariable=txt_word, font=("Courier", 15), state='disabled')
tf_word.grid(row=2, column=0, columnspan=3, padx=2, pady=5)

# list of words (you can add more words if you want)
words = ["kite", "table", "mathematics", "english", "fabulous", "difficult", "example"]

# Initialize variables
word_to_guess = ""
rem_guess = 0  # Number of remaining guesses
cor_guess = 0  # Number of correctly guessed characters
empty_str = ""  # Holds the string displaying dashes
original_word = ""  # Holds the original word with characters separated by a vertical bar


def initialize_values():
    global word_to_guess
    global original_word
    global empty_str
    global rem_guess
    global cor_guess

    # randomly selecting the word to guess
    word_to_guess = random.choice(words)
    # setting default number of remaining wrong guesses
    rem_guess = 5
    # setting the default number of correct guesses
    cor_guess = 0
    # empty string to display on GUI
    empty_str = ""
    # string which keeps track of character indexes
    original_word = ""

    for char in word_to_guess:
        empty_str += "_|"
        original_word += char + "|"

    txt_word.set(empty_str)  # initializing values
    txt_rg.set(rem_guess)  # setting remaining guesses to the default value


# creating a label for input character
lbl_ip = Label(main_window, text="Enter Character", bg="#6699ff", fg="#595959", font=("Courier", 10))
lbl_ip.grid(row=3, column=0, padx=5, pady=5)

# creating a text field for input characters and attaching it to the main window
txt_ip = StringVar()
tf_ip = ttk.Entry(main_window, textvariable=txt_ip, font=("Courier", 10))
tf_ip.grid(row=3, column=1, padx=5, pady=5)

# creating a label for remaining guesses
lbl_rg = Label(main_window, text="Remaining wrong guesses:", bg="red", fg="black", font=("Courier", 10))
lbl_rg.grid(row=4, column=0, padx=5, pady=5)

# creating a text field for remaining wrong guesses and attaching it to the main window
txt_rg = StringVar()
txt_rg.set(rem_guess)  # setting remaining wrong guesses to the default value
tf_rg = ttk.Entry(main_window, textvariable=txt_rg, font=("Courier", 10), state='disabled')
tf_rg.grid(row=4, column=1, padx=5, pady=5)


def make_guess():
    global word_to_guess
    global original_word
    global empty_str
    global rem_guess
    global cor_guess
    global txt_ip

    # if the input string is empty or contains more than one character
    if txt_ip.get() == "" or len(txt_ip.get()) > 1:
        showinfo(title="Information", message="Input Cannot be Empty or more than one character")
        return

    input_char = txt_ip.get().lower()  # Convert to lowercase for consistency

    # if the input character exists in the word to be guessed
    if input_char not in word_to_guess:
        txt_ip.set("")
        rem_guess -= 1
        txt_rg.set(rem_guess)

        if rem_guess == 0:
            showinfo(title="Information",
                     message=f"You have used all your guesses. \nYou lost. \nThe correct word is: {word_to_guess}. \nTry Again")
            initialize_values()
            return
        else:
            showinfo(title="Information", message="Wrong Guess")
            return
    else:
        # if the guess is correct
        cor_guess += 1

        # if the number of correct guesses are equal to the word length
        if cor_guess == len(word_to_guess):
            showinfo(title="Information", message="Congratulations, You Won! \nPlay Again")
            initialize_values()
            return

        # Update the empty_str with the correctly guessed character
        positions = [i for i, char in enumerate(word_to_guess) if char == input_char]
        for pos in positions:
            empty_str = empty_str[:pos * 2] + input_char + empty_str[pos * 2 + 1:]

        txt_word.set(empty_str)
        txt_ip.set("")


# Initialize the game when the application starts
initialize_values()

# Creating a button for making a guess
btn_guess = Button(main_window, text="Make Guess", command=make_guess)
btn_guess.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Displaying the main window
main_window.mainloop()
