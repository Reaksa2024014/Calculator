from tkinter import *
from pygame import mixer

def load_khmer_dictionary():
    """Load a list of Khmer words into memory."""
    khmer_words_content = """
    សួស្តី
    អរុណសួស្តី
    ជំរាបសួរ
    សុខសប្បាយ
    កម្ពុជា
    ភាសាខ្មែរ
    និស្សិត
    មនុស្ស
    គ្រួសារ
    មិត្តភាព
    អាហារ
    ទឹក
    ផ្ទះ
    សាលា
    សៀវភៅ
    កុមារ
    ចិត្ត
    ការងារ
    មុខម្ហូប
    កំសាន្ត
    ពេលវេលា
    ថ្ងៃចន្ទ
    ថ្ងៃអង្គារ
    ថ្ងៃព្រហស្បតិ៍
    ថ្ងៃសុក្រ
    ថ្ងៃសៅរ៍
    ថ្ងៃអាទិត្យ
    ចំណេះដឹង
    ការអប់រំ
    ការសិក្សា
    សុខភាព
    គំនិត
    ធ្វើការ
    ចេះរាំ
    ចេះនិយាយខ្មែរ
    ចេះសរសេរ
    ជួយគ្នា
    បងប្អូន
    មិត្តភក្តិ
    ការសម្រេចចិត្ត
    អារម្មណ៍ល្អ
    អារម្មណ៍អាក្រក់
    ជោគជ័យ
    បរាជ័យ
    គូរ
    គុំគួន
    """

    # Split the content into lines and create a set of words.
    khmer_words = {line.strip() for line in khmer_words_content.strip().splitlines() if line.strip()}
    
    return khmer_words

def check_khmer_spelling():
    """Check if the entered word exists in the Khmer dictionary."""
    word = enter_text.get().strip()
    
    # Debugging output to see what word is being checked.
    print(f"Checking word: '{word}'")
    
    if word in khmer_words:
        spell.config(text="ពាក្យរបស់អ្នកត្រឹមត្រូវ!", fg="green")  # "Your word is correct!" in Khmer.
        play_sound("mixkit-trumpet-fanfare-2293.wav")
        print("Result: Correct")
        print(f"The word '{word}' is in the dictionary.")
        
        history.insert(END, f"Correct: {word}")
        
        # Optionally, you could add more feedback here.
        
    else:
        suggestions = get_suggestions(word)
        suggestion_text = f"ពាក្យរបស់អ្នកមិនត្រឹមត្រូវទេ! សូមពិនិត្យមើល: {word}\n"  
        if suggestions:
            suggestion_text += "សូមពិនិត្យមើលពាក្យដូចខាងក្រោម:\n" + "\n".join(suggestions)  
        spell.config(text=suggestion_text, fg="red")
        play_sound("mixkit-classic-alarm-995.wav")
        
        print("Result: Incorrect")
        print(f"Suggestions: {suggestions}")
        
        history.insert(END, f"Incorrect: {word}")

def get_suggestions(word):
    """Generate spelling suggestions based on the entered word."""
    return [w for w in khmer_words if w.startswith(word[0])][:5]  

def play_sound(sound_file):
    """Play a sound file using Pygame mixer."""
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    
    try:
        mixer.music.load(sound_file)
        mixer.music.play()
        
        # Wait until sound is finished playing (optional)
        while mixer.music.get_busy():
            pass
            
    except Exception as e:
        print(f"Error playing sound: {e}")

def clear_entry():
   """Clear the input field and reset the label."""
   enter_text.delete(0, END)
   spell.config(text="")
   
def clear_history():
   """Clear the history listbox."""
   history.delete(0, END)

# Main application window setup.
root = Tk()
root.title("Spelling Checker (Khmer)")
root.geometry("700x600")
root.config(background="lightgray")

# Heading with a specific font that supports Khmer characters.
heading = Label(root, text="Spelling Checker (Khmer)", font=("Khmer OS", 20, 'bold'), bg="lightgray")
heading.pack(pady=(20, 10))

# Input Entry with a specific font that supports Khmer characters.
enter_text = Entry(root, justify="center", width=30, font=("Khmer OS", 25), bg="white", bd=2)
enter_text.pack(pady=10)
enter_text.focus()

# Check Button with new red color.
button_check = Button(root, text="ពិនិត្យ", font="Arial 20 bold", fg="black", bg="#f44336", command=check_khmer_spelling)  # Red color for "Check".
button_check.pack(pady=(10, 5))

# Clear Button with a different color.
button_clear = Button(root, text="សម្អាត", font="Arial 20 bold", fg="black", bg="#4CAF50", command=clear_entry)  # Green color for "Clear".
button_clear.pack(pady=(5, 5))

# Clear History Button with blue color.
button_clear_history = Button(root, text="លុបប្រវត្តិ", font="Arial 20 bold", fg="black", bg="#2196F3", command=clear_history)  # Blue color for "Clear History".
button_clear_history.pack(pady=(5, 20))

# Result Label.
spell = Label(root, font=("Arial", 18), bg="lightblue", fg="#364971", wraplength=600)
spell.pack(pady=(10, 20))

# History Listbox to show checked words.
history_label = Label(root, text="ប្រវត្តិការពិនិត្យ:", font=("Arial", 16), bg="lightgray")
history_label.pack(pady=(10, 0))
history = Listbox(root, width=50, height=10, font=("Arial", 14))
history.pack(pady=(0, 20))

# Load the Khmer dictionary once when the app starts.
khmer_words = load_khmer_dictionary()

# Initialize Pygame mixer.
mixer.init()

# Start the main loop.
root.mainloop()