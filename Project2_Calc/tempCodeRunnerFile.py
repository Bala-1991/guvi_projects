import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display the input and result
        self.display = tk.Entry(root, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        # Variables to hold the current state
        self.current_input = ""  # To store the expression
        self.operator = None

        # Creating buttons
        self.create_buttons()

    def create_buttons(self):
        # Number buttons
        button_1 = self.create_button(1, 1, 0)
        button_2 = self.create_button(2, 1, 1)
        button_3 = self.create_button(3, 1, 2)
        button_4 = self.create_button(4, 2, 0)
        button_5 = self.create_button(5, 2, 1)
        button_6 = self.create_button(6, 2, 2)
        button_7 = self.create_button(7, 3, 0)
        button_8 = self.create_button(8, 3, 1)
        button_9 = self.create_button(9, 3, 2)
        button_0 = self.create_button(0, 4, 1)

        # Operator buttons
        button_add = self.create_button("+", 4, 3, lambda: self.button_click("+"))
        button_subtract = self.create_button("-", 3, 3, lambda: self.button_click("-"))
        button_multiply = self.create_button("*", 2, 3, lambda: self.button_click("*"))
        button_divide = self.create_button("/", 1, 3, lambda: self.button_click("/"))

        # Equal button
        button_equal = self.create_button("=", 4, 2, self.calculate)

        # Clear button
        button_clear = self.create_button("C", 4, 0, self.clear)

    def create_button(self, value, row, col, command=None):
        if command is None:
            command = lambda v=value: self.button_click(v)
        return tk.Button(self.root, text=value, padx=20, pady=20, command=command).grid(row=row, column=col)

    def button_click(self, value):
        # Append the clicked value (either a number or operator) to the current input
        self.current_input += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)

    def calculate(self):
        try:
            # Evaluate the expression in the current_input (e.g., "5+3*2")
            result = str(eval(self.current_input))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.current_input = result  # Reset the input to the result for further calculations
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.current_input = ""

    def clear(self):
        self.display.delete(0, tk.END)
        self.current_input = ""

# Create the main window
root = tk.Tk()

# Instantiate the calculator
calc = Calculator(root)

# Run the application
root.mainloop()
