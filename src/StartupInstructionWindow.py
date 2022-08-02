from tkinter import messagebox


class InstructionWindow:

    """
    Instruction Window Shows the Information on the Input
    Pop-up window before the Input of Sentences
    Return: None
    """
    def __init__(self, root):
        messagebox.showinfo(title="Instruction",
                            message="Before you begin:\n"
                                    "1) In this task, you will hear the same speaker say a series of sentence.  Each sentence consists of real words.\n"
                                    "2) After listening to each sentence, please type what you think the speaker said. Even if you aren't sure,"
                                    "try to write something for each sentence.  It's okay to guess!")
        return
