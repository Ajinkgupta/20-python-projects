import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.resizable(False, False)
        master.configure(bg="#1F1D2B")

        # Create input box
        self.display = tk.Entry(master, width=35, borderwidth=0, font=("Helvetica", 20), justify=tk.RIGHT, bg="#CCCCCC", fg="#333333")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Define buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
        ]

        # Create and place buttons on the grid
        for label, row, col in buttons:
            button = tk.Button(master, text=label, command=lambda label=label: self.button_click(label), width=7, height=3, font=("Helvetica", 16), bg="#E0E0E0", fg="#333333", bd=0)
            button.grid(row=row, column=col, pady=5, padx=5)
            button.bind("<Enter>", lambda event, btn=button: btn.configure(background="#CCCCCC"))
            button.bind("<Leave>", lambda event, btn=button: btn.configure(background="#E0E0E0"))
            button.bind("<Button-1>", lambda event, btn=button: btn.configure(foreground="#E0E0E0", background="#333333"))
            button.bind("<ButtonRelease-1>", lambda event, btn=button: btn.configure(foreground="#333333", background="#CCCCCC"))
            button.bind("<FocusIn>", lambda event, btn=button: btn.configure(foreground="#E0E0E0", background="#333333"))
            button.bind("<FocusOut>", lambda event, btn=button: btn.configure(foreground="#333333", background="#E0E0E0"))

        self.equation = ""

    def button_click(self, label):
        if label == "C":
            self.equation = ""
            self.display.delete(0, tk.END)
        elif label == "=":
            try:
                result = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.equation += label
            self.display.insert(tk.END, label)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
