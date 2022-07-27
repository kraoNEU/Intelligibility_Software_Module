from tkinter import *
from src.SentencesPlayer import SentencesPlayer
from src.InstructionWindow import *

# Initialise the Tkinter Window
root = Tk()

# Set the Window Title
root.title("Intelligibility Software Module for SMILe Lab")

# Setting the Window
root.geometry("600x200+200+200")

# Set the Logo of the Model
root.iconbitmap("../Logo/Northeastern_University_seal.png")

# Set the Instruction Window
InstructionWindow(root)

# Calling the SentencePlayer Package From src
SentencesPlayer(root)

# End Main Tkinter window
root.mainloop()
