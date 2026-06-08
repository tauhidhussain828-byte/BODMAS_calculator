BODMAS Calculator with Tkinter GUI
A sleek, dark-themed desktop calculator application built from scratch in Python. This project utilizes a custom-built expression parser to evaluate mathematical expressions according to the standard BODMAS/PEMDAS rules, completely bypassing the native eval() function for a safe, educational backend architecture.
FEATURES:-
1) Custom Expression Parsing: Implements mutual parsing using custom buffer slots (bs) and main slots(ms) to split digits from operators seamlessly.
2) Nested parentheses Handling: Features a bracket_solver that recursively extracts, processes, and updates innermost nested brackets using .rfind() and .find().
3) BODMAS Order of Operatrions:Seperates evaluation into two algorithimic phases:
        i) Handles all multiplication(*) and division (/) operator first.
       ii) Loops back to process addition(+) and (-) with what remains.
4) Input Identification: includes a built_in safety check to make sure the expression only proceesses valid digits, operators, and brackets.
5) Modern Dark-Theme GUI: Built with Python's Tkinter Lib, featuring a fully  expandable layout, clean color-coded grid mapping, and intuitive control triggers.
Project Structure
The project is split into two cleanly separated files:
        i) Bodmas_calculator_backend.py:Contains the deep analytical logic(calculator(a), identification(a), bracket_solver(a), and evaluation(ms,op))
       ii) Bodmas_calculator_UI.py:Contains the Tkinter grid congiguration, graphical buttons, display controls, and links input directly to the calculator engine.
   
   



