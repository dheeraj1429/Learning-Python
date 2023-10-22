import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_str_var.set(f"Km: {km_output}")


# window
window = ttk.Window()
window.title('demo')
window.geometry('350x150')

# title
title_label = tk.Label(
    master=window, text='Miles to kilometers', font='Roboto 24 bold')
title_label.pack()

# input filed
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side='left', padx=5)
button.pack(side='left')
input_frame.pack()

# output
output_str_var = tk.StringVar()
output_str_var.set("Output in kilometers")
output_label = ttk.Label(master=window, text='Output',
                         font='Roboto 15', textvariable=output_str_var)
output_label.pack()

# run loop
window.mainloop()
