from tkinter import *
import tkinter as tk

root = Tk()

window = tk.Tk()
window.title("Nigga Calc MK1™")


def calculate_hypotenuse():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        hypotenuse = (a ** 2 + b ** 2) ** 0.5

        result_label.config(text=f"The length of the hypotenuse is: {hypotenuse}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values for both legs.")


label_a = tk.Label(window, text="Enter the length of the first leg:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Enter the length of the second leg:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_hypotenuse)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
