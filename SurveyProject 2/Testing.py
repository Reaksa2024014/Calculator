# pip install pygame
# pip install textblob

from tkinter import *
from pygame import mixer
from textblob import TextBlob

def check_spelling():
    word = enter_text.get()
    corrected_word = TextBlob(word).correct()
    if corrected_word.lower() != word.lower():  # Compare ignoring case
        #add sounds to display when users enter the words
        spell.config(text=f"Your word is not correct! Did you mean: {corrected_word}")
        play_sound("FINAL CSA/mixkit-classic-alarm-995.wav")
    else:
        spell.config(text="Your word is correct!")
        play_sound("FINAL CSA/mixkit-trumpet-fanfare-2293.wav")

def play_sound(sound_file):
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()

def clear_entry():
    enter_text.delete(0, END)
    spell.config(text="")

root = Tk()
root.title("Spelling Checker")
root.geometry("700x500")
root.config(background="white")

heading = Label(root, text="Spelling Checker", font="Arial 20 bold", bg="white")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("Arial", 25), bg="white", bd=2)
enter_text.pack(pady=10)
enter_text.focus()

button_check = Button(root, text="Check", font="Arial 20 bold", fg="red", bg="red", command=check_spelling)
button_check.pack()
#add button to display clear function
button_clear = Button(root, text="Clear", font="Arial 20 bold", fg="white", bg="grey", command=clear_entry)
button_clear.pack()

spell = Label(root, font=("Arial", 20), bg="lightblue", fg="#364971")
spell.pack(pady=(30, 0))


# Initialize Pygame mixer
mixer.init()


root.mainloop()