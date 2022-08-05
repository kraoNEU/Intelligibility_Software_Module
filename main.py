import os
from tkinter import *
from tkinter.filedialog import askdirectory

from src.SentencesPlayer import SentencesPlayer
from src.StartupInstructionWindow import *

# Initialise the Tkinter Window
root = Tk()

scriptDir = os.getcwd()
directory = askdirectory()
os.chdir(directory)
os.chdir(scriptDir)

# Set the Window Title
root.title("Intelligibility Software Module for SMILe Lab")

# Setting the Window
root.geometry("600x200+200+200")

# Setting the Instruction Logo
img = PhotoImage(file='Logo/instruction_icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Set the Instruction Window
InstructionWindow(root)

img = PhotoImage(file='Logo/Northeastern_Huskies_logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Set the SentencePlayer Window
SentencesPlayer(root)

# End Main Tkinter window
root.mainloop()
