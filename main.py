from tkinter import *

window = Tk()
window.title("My first tkinter GUI program")
window.minsize(width=500, height=500)

# Create a label
my_label = Label(text="I am a new label", font=("Arial", 24, "bold"))
my_label.pack()

# Create a function for the btm


def button_clicked():
    # print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Create a btn
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Create an entry compontent (input)
input = Entry(width=10)
input.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

window.mainloop()
