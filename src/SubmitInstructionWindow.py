from tkinter import messagebox


class InstructionWindow:
    """
    Instruction Window Shows the Information on the Input
    Pop-up window before Submit of each Sentences
    Return: None
    """

    def __init__(self, root):
        messagebox.showinfo(title="Instruction",
                            message="Before you begin:\n"
                                    "1) Please Listen Carefully!\n"
                                    "2) You may replay the sentence only one time.")
        return
