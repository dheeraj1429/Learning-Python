import tkinter

window = tkinter.Tk()
window.title("My first tk enter program")
window.minsize(width=500, height=500)

# project
input = tkinter.Entry()
input.pack()

label = tkinter.Label(text='In KM: ')
label.pack()


def convert_handler():
    try:
        value = int(input.get())
        in_km = value * 0.001
        label.config(text=f"In KM: {in_km}")
    except ValueError:
        label.config(text='Please enter a number')


button = tkinter.Button(text="Convert into KM.", command=convert_handler)
button.pack()

# project


# def add(**keywards):
#     sum = 0
#     for (key, value) in keywards.items():
#         sum += value
#     return sum


# print(add(a=10, b=10, c=10, d=20))

# class Car():
# def __init__(self, **kw):
#     self.name = kw["name"]
#     self.model = kw["model"]

# def __init__(self, **kw):
#     self.name = kw.get('name')
#     self.model = kw.get('model')


# new_car = Car(name='Neshan', model="new model")
# new_car = Car(name='Neshan')

# label
# my_label = tkinter.Label(text='This is the label', font=('Arial', 24, 'bold'))
# my_label.pack(side='bottom')
# my_label.pack(side="left")
# my_label.pack(expand=True)

# update the label
# my_label["text"] = "This is the"
# my_label.config(text='Some updated information')


# input
# input = tkinter.Entry(width=10)
# input.pack()
# input.grid(column=0, row=0)
# input.place(x=1, y=1)

# button


# def click_handle():
#     print(input.get())


# button = tkinter.Button(text="Click me", command=click_handle)
# button.pack()


window.mainloop()
