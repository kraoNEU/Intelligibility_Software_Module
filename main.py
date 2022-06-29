from tkinter import *
from src.SentencesPlayer import SentencesPlayer
# from src.TextBoxInput import TextBoxInput

root = Tk()
root.title("Intelligibility Software Module for SMILe Lab")
root.geometry("1000x200+200+200")
root.iconbitmap("Logo/Northeastern_University_seal.ico")

# Calling the SentencePlayer Package From src
SentencesPlayer(root)

# Calling the Text Box Input Widget
#TextBoxInput(root)

root.mainloop()
