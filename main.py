import os
from tkinter import *
from tkinter.filedialog import askdirectory
from src.SentencesPlayer import SentencesPlayer
from src.StartupInstructionWindow import *

# Initialise the Tkinter Window
root = Tk()

directory = askdirectory()
os.chdir(directory)

# Set the Window Title
root.title("Intelligibility Software Module for SMILe Lab")

# Setting the Window
root.geometry("600x300+200+200")

# Set the Directory Window
InstructionWindow(root)

# Set the SentencePlayer Window
SentencesPlayer(root)

# End Main Tkinter window
root.mainloop()
