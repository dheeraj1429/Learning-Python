import tkinter as tk
from tkinter import ttk


def button_handler():
    entry_text = entry.get()
    label.configure(text=entry_text)
    # label['text'] = entry_text
    # entry['state'] = 'disabled'


# window
window = tk.Tk()
window.title('Getting and setting')
window.geometry('400x300')

label = tk.Label(master=window, text='Some label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Save',
                    command=button_handler)
button.pack()

# main loop
window.mainloop()
