
import tkinter as tk
from tkinter import ttk

def calculate_electricity_bill(units_consumed):
    try:
        units_consumed = float(units_consumed)

        # Define your electricity tariff structure here
        # You can customize the rates based on your local utility's pricing
        rate_per_unit = 5.00  # Example rate: Rs. 5.00 per unit
        fixed_charge = 50.00  # Example fixed charge: Rs. 50.00

        total_bill = (units_consumed * rate_per_unit) + fixed_charge
        result_label.config(text=f"Electricity Bill: Rs. {total_bill:.2f}")

    except ValueError:
        result_label.config(text="Please enter a valid numeric value for units consumed.")

def on_calculate_button_click():
    units_consumed = units_entry.get()
    calculate_electricity_bill(units_consumed)

# Create the main window
window = tk.Tk()
window.title("Electricity Bill Calculator (in Rupees)")

# Create and configure the frame
frame = ttk.Frame(window, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create and place widgets in the frame
units_label = ttk.Label(frame, text="Units Consumed:")
units_label.grid(column=0, row=0, sticky=tk.W)

units_entry = ttk.Entry(frame)
units_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate_button_click)
calculate_button.grid(column=0, row=1, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=2, columnspan=2)

# Start the Tkinter event loop
window.mainloop()