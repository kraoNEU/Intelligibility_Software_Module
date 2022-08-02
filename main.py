from tkinter import *
from src.SentencesPlayer import SentencesPlayer
from src.StartupInstructionWindow import *

# Initialise the Tkinter Window
root = Tk()

# Set the Window Title
root.title("Intelligibility Software Module for SMILe Lab")

# Setting the Window
root.geometry("600x200+200+200")

# Setting the Instruction Logo
img = PhotoImage(file='Logo/instruction_icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Set the Instruction Window
InstructionWindow(root)

# Set the Logo of the Model
# root.iconbitmap("/Users/cvkrishnarao/Desktop/RA/Intelligibility_Software_Module/Logo/Northeastern_Huskies_logo.png")

img = PhotoImage(file='/Users/cvkrishnarao/Desktop/RA/Intelligibility_Software_Module/Logo/Northeastern_Huskies_logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Set the SentencePlayer Window
SentencesPlayer(root)

# End Main Tkinter window
root.mainloop()
