import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# create widgets
text_input = tk.Text(master=window)
text_input.pack()

# ttk widgets
label = ttk.Label(master=window, text='This is a test')
label.pack()

# ttk entry
entry = tk.Entry(master=window)
entry.pack()

# button
button = ttk.Button(master=window, text='Save',
                    command=lambda: print('some command'))
button.pack()

# new label
new_label = ttk.Label(master=window, text="Some test we want to show")
new_label.pack()

# run
window.mainloop()
