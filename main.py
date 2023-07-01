import tkinter

window = tkinter.Tk()
window.title("My first tkinter GUI program")
window.minsize(width=500, height=500)

# Create a label
my_label = tkinter.Label(text="I am a new label", font=("Arial", 24, "bold"))
my_label.pack()

# Create a function for the btm


def button_clicked():
    print("I got clicked")


# Create a btn
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
