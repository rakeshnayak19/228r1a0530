import tkinter as tk
from tkinter import ttk

def si(principal, rate, time):
    try:
        principal = float(principal)
        rate = float(rate)
        time = float(time)

        interest = (principal * rate * time) / 100
        result_label.config(text=f"Simple Interest: {interest:.2f} USD")

    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

def on_calculate_button_click():
    principal = principal_entry.get()
    rate = rate_entry.get()
    time = time_entry.get()

    si(principal, rate, time)

# Create the main window
window = tk.Tk()
window.title("Simple Interest Calculator")

# Create and configure the frame
frame = ttk.Frame(window, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create and place widgets in the frame
principal_label = ttk.Label(frame, text="Principal amount:")
principal_label.grid(column=0, row=0, sticky=tk.W)

principal_entry = ttk.Entry(frame)
principal_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

rate_label = ttk.Label(frame, text="Rate of interest:")
rate_label.grid(column=0, row=1, sticky=tk.W)

rate_entry = ttk.Entry(frame)
rate_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

time_label = ttk.Label(frame, text="Time (in years):")
time_label.grid(column=0, row=2, sticky=tk.W)

time_entry = ttk.Entry(frame)
time_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate_button_click)
calculate_button.grid(column=0, row=3, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=4, columnspan=2)

# Start the Tkinter event loop
window.mainloop()