import tkinter as tk
from tkinter import ttk

class StylishCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🖤 Stylish Calculator")
        self.root.geometry("320x450")
        self.root.configure(bg="#000000")  # Pure black background

        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Entry styling
        self.style.configure("TEntry",
                             foreground="white",
                             fieldbackground="#1e1e1e",
                             font=("Consolas", 18))

        # Button styling
        self.style.configure("TButton",
                             font=("Segoe UI", 14),
                             padding=10,
                             background="#2c2c2c",
                             foreground="white")
        self.style.map("TButton",
                       background=[("active", "#00bcd4")],
                       foreground=[("active", "black")])

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Calculator", font=("Segoe UI", 20, "bold"),
                         bg="#000000", fg="#00bcd4")
        title.pack(pady=10)

        # Entry field
        self.entry = ttk.Entry(self.root, justify="right")
        self.entry.pack(padx=10, pady=10, fill="x")

        # Button grid
        button_frame = tk.Frame(self.root, bg="#000000")
        button_frame.pack(padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for btn in buttons:
            action = self.calculate if btn == '=' else lambda b=btn: self.append_to_entry(b)
            ttk.Button(button_frame, text=btn, command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear and Backspace
        ttk.Button(button_frame, text="C", command=self.clear_entry).grid(row=row, column=0, padx=5, pady=5, sticky="nsew")
        ttk.Button(button_frame, text="⌫", command=self.backspace).grid(row=row, column=1, padx=5, pady=5, sticky="nsew")

        # Fill remaining columns
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Footer
        footer = tk.Label(self.root, text="Made with ❤️ by Jahnavi", font=("Segoe UI", 10),
                          bg="#000000", fg="#555555")
        footer.pack(side="bottom", pady=5)

    def append_to_entry(self, char):
        self.entry.insert(tk.END, char)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = StylishCalculator(root)
    root.mainloop()
