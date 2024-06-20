import tkinter as tk
from tkinter import messagebox
import time

class WordsPerMinuteCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Words Per Minute Calculator")
        self.master.geometry("300x150")

        self.label_instruction = tk.Label(master, text="Type the given text below and press 'Calculate WPM'")
        self.label_instruction.pack(pady=5)

        self.text_entry = tk.Text(master, height=5, width=30)
        self.text_entry.pack(pady=5)

        self.button_calculate = tk.Button(master, text="Calculate WPM", command=self.calculate_wpm)
        self.button_calculate.pack(pady=5)

    def calculate_wpm(self):
        input_text = self.text_entry.get("1.0", "end-1c")
        words = input_text.split()
        word_count = len(words)

        if word_count == 0:
            messagebox.showerror("Error", "Please enter some text to calculate WPM.")
            return

        start_time = time.time()
        # Assume average reading speed of 200 words per minute
        time_taken = (word_count / 200) * 60  # Convert minutes to seconds
        end_time = time.time()

        wpm = word_count / ((end_time - start_time) / 60)

        messagebox.showinfo("Words Per Minute", f"Your WPM: {wpm:.2f}")

def main():
    root = tk.Tk()
    app = WordsPerMinuteCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()