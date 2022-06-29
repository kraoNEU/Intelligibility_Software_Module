from tkinter import *
from src.SentencesPlayer import SentencesPlayer

root = Tk()
root.title("Intelligibility Software Module for SMILe Lab")
root.geometry("1000x200+200+200")
root.iconbitmap("Logo/Northeastern_University_seal.ico")

# Calling the SentencePlayer Package From src
SentencesPlayer(root)
root.mainloop()
