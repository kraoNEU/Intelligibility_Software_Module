# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# root.title("Intelligibility Software Module for SMILe Lab")
# root.iconbitmap("Logo/Northeastern_University_seal.ico")
#
# e = Entry(root, bg='blue', fg='yellow')
# e.insert(1, "Enter Your Name: ")
# e.pack()
#
#
# def myClick():
#     myLabel = Label(root, text="Hello {0}".format(e.get()))
#     myLabel.pack()
#
#
# Bustton_quit = Button(root, text="Click me to exit", command=root.quit)
# myButton = Button(root, text="Click Me", command=myClick)
# my_img = ImageTk.PhotoImage()
# Bustton_quit.pack()
# myButton.pack()
#
# root.mainloop()

import File_Reader.file_reader

print(File_Reader.file_reader.get_number_of_directories_in_a_path("/Users/cvkrishnarao/Desktop/RA"
                                                                  "/Intelligibility_Software_Module/Test_File/Week_1"))
