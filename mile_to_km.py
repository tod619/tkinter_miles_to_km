# miles to kilometer
# this program converts miles to kilometer through a GUI
# 03/07/2023
from tkinter import *

# create window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Create widgets
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_btn = Button(text="Caluclate")
calculate_btn.grid(column=1, row=2)


# Display window until closed
window.mainloop()
