from tkinter import messagebox


class InstructionWindow:

    """
    Instruction Window Shows the Information on the Input
    Pop-up window before the Input of Sentences
    Return: None
    """
    def __init__(self, root):
        messagebox.showinfo(title="Instruction",
                            message="Before you begin\n"
                                    "This is a second Statement\n"
                                    "Multiple Line execution\n"
                                    "Check for Big Messages\n")
        return
