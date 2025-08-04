"""
day 27: Graphical User Interfaces with TKInter
"""
from tkinter import *

# Text
# text = Text(height=5, width=30)
# text.focus() # Put cursor in textbox
# text.insert(END, "Sample of multiline text entry.")
# # Get current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# # Spinbox
# def spinbox_used():
#     """get current value in spinbox."""
#     print(spinbox.get())
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
# def checkbutton_used():
#     # Prints if on button checked, otherwise 0.
#     print(checked_state.get())
# # variable to hold on to a checked state, 0 is off, 1 is on
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On? ",
#                           variable=checked_state,
#                           command= checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1,
#                            variable=radio_state,
#                            command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2,
#                            variable=radio_state,
#                            command=radio_used)
#
# radiobutton1.pack()
# radiobutton2.pack()
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox.
#     print(listbox.get(listbox.curselection()))
#
# listbox= Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#
# # Binding event handler to listbox
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


# # Create a new window
# window = Tk()
#
# # Adding a title
# window.title("First GUI program")
#
# # Changing the size
# window.minsize(width=500, height=300)
#
# # Adding padding
# window.config(padx=10, pady=10)
#
# # Label
# my_label = Label(text="I am a label", font=('Arial', 24, "italic"))
# # my_label.pack() # Place and center on Screen
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
#
# # Applying an event listener to the button
# def button_clicked():
#     my_label["text"] = entry.get()
#
#
# # Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# button2 = Button(text="New Button")
# # button2.place(x=0, y=100)
# button2.grid(column=2, row=0)
#
# # Entry / Input (Single line Input)
# entry = Entry(width=10)
# # entry.pack()
# entry.grid(column=3, row=3)
#
# # Keep the window open and active
# # Must remain at the bottom of the program.
# window.mainloop()
#
# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #     return sum
# #
# # print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))


"""
Mile to Km Converter Project
"""
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_output.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_output = Label(text="0")
km_output.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calc_btn = Button(text="Calculate", command=miles_to_km)
calc_btn.grid(row=2, column=1)



# Keep window open
window.mainloop()