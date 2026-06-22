# Program Name: Assignment.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 3
# Due Date: 06/22/2026
# Purpose: This program will be a GUI application that will convert miles per gallon into kilometers per liter.
# I used geeks for geeks to learn how to use labels. I used chatGPT to learn how to use key release to make the conversion instant. I also used a local model to finish the exception handling.

import tkinter as tk

#Create window 
root = tk.Tk()
root.title("MPG to KPL Converter")
root.geometry("300x150")

#Input label and entry
input_label = tk.Label(root, text="Enter miles per gallon:")   
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()
input_entry.bind("<KeyRelease>", lambda event: convert_mpg_to_kpl())

#Output label and entry
output_label = tk.Label(root, text="Kilometers per liter:")   
output_label.pack()

output_entry = tk.Entry(root)
output_entry.pack()

#conversion function
def convert_mpg_to_kpl():
    try:
        mpg = float(input_entry.get())
        kpl = mpg * 0.425144
        output_entry.delete(0, tk.END)
        output_entry.insert(0, f"{kpl:.2f}")
    except ValueError:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Invalid input")


root.mainloop()