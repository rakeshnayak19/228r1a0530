import tkinter as tk
from tkinter import ttk

def is_leap_year(year):
    try:
        year = int(year)

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result_label.config(text=f"{year} is a Leap Year!")
        else:
            result_label.config(text=f"{year} is not a Leap Year.")

    except ValueError:
        result_label.config(text="Please enter a valid numeric value for the year.")

def on_check_button_click():
    year = year_entry.get()
    is_leap_year(year)

# Create the main window
window = tk.Tk()
window.title("Leap Year Checker")

# Create and configure the frame
frame = ttk.Frame(window, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create and place widgets in the frame
year_label = ttk.Label(frame, text="Enter Year:")
year_label.grid(column=0, row=0, sticky=tk.W)

year_entry = ttk.Entry(frame)
year_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

check_button = ttk.Button(frame, text="Check Leap Year", command=on_check_button_click)
check_button.grid(column=0, row=1, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=1, columnspan=2)
result_entry = ttk.Entry(frame)
result_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Start the Tkinter event loop
window.mainloop()