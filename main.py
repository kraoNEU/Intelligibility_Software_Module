from tkinter import *
from playsound import playsoundd
import File_Reader.file_reader
import random

root = Tk()
root.title("Intelligibility Software Module for SMILe Lab")
root.iconbitmap("Logo/Northeastern_University_seal.ico")

print(File_Reader.file_reader.get_number_of_directories_in_a_path("/Users/cvkrishnarao/Desktop/RA"
                                                                  "/Intelligibility_Software_Module/Test_File/Week_1"))

pygame.mixer.init()

my_botton = Button(root, text='Play', command=play)
my_botton.pack()

print(random.sample(range(1, 7), 6))
