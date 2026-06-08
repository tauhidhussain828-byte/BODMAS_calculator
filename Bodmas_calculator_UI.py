import tkinter as tk
from Bodmas_calculator_backend.py import calculator  # your custom calculator function

# ---- Main Window ----
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")  # dark background

# ---- Entry Box ----
entry = tk.Entry(root, font=("Helvetica", 24), borderwidth=3, relief="ridge",
                 justify="right", bg="#333333", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# ---- Button Colors ----
num_color = "#4d4d4d"      # numbers
op_color = "#ff9500"       # operators
action_color = "#ff3b30"   # clear button

# ---- Button Functions ----
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    try:
        result = calculator(expr)  # call your backend calculator
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "error boom!!!!!!")

# ---- Buttons ----
buttons = [
    ("7", num_color), ("8", num_color), ("9", num_color), ("/", op_color),
    ("4", num_color), ("5", num_color), ("6", num_color), ("*", op_color),
    ("1", num_color), ("2", num_color), ("3", num_color), ("-", op_color),
    ("0", num_color), (".", num_color), ("=", op_color), ("+", op_color)
]

row = 1
col = 0
for (text, color) in buttons:
    tk.Button(root, text=text, font=("Helvetica", 18), bg=color, fg="white",
              width=5, height=2,
              command=calculate if text == "=" else lambda x=text: button_click(x))\
        .grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col == 4:
        col = 0
        row += 1

# ---- Clear Button ----
tk.Button(root, text="C", font=("Helvetica", 18), bg=action_color, fg="white",
          width=22, height=2, command=clear)\
    .grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# ---- Make Grid Expandable ----
for i in range(5):  # 4 rows of buttons + entry
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
