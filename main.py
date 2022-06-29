from tkinter import *
from src.SentencesPlayer import SentencesPlayer


root = Tk()
root.title("Intelligibility Software Module for SMILe Lab")
root.geometry("1000x200+200+200")
root.iconbitmap("Logo/Northeastern_University_seal.ico")

# Calling the SentencePlayer Package From src
SentencesPlayer(root)
root.mainloop()

# print(File_Reader.file_reader.get_number_of_directories_in_a_path("/Users/cvkrishnarao/Desktop/RA"
#                                                                   "/Intelligibility_Software_Module/Test_File/Week_1"))
#
# pygame.mixer.init()
#
#
# def play():
#     pygame.mixer.music.load("Test_File/Week_1/Session_1.wav")
#     pygame.mixer.music.play(loops=0)
#
#
# my_botton = Button(root, text='Play', command=play)
# my_botton.pack()
#
# print(random.sample(range(1, 7), 6))
