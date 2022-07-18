import csv

import pygame
import os
from tkinter import *
import random
from csv import *


class SentencesPlayer:

    def __init__(self, root):

        self.root = root
        self.count = 0
        self.main_list = []

        # Initiating Pygame
        pygame.init()

        self.Input_Text = StringVar()

        # Initiating Pygame Mixer
        pygame.mixer.init()

        # Declaring track Variable
        self.track = StringVar()

        # Creating the Background
        trackframe = LabelFrame(self.root, text="Sentences Input", font=("times new roman", 15),
                                bg="Navyblue",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=800, height=100)

        # Creating a Test Widget For the Input
        self.Input_Text = Text(trackframe, width=83, height=5)
        self.Input_Text.grid(row=50, column=50)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)

        # Inserting Play Button
        Button(buttonframe, text="Play / Replay", command=self.playsong, width=10, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                    pady=5)
        # Inserting Next Button
        Button(buttonframe, text="Next", command=self.pausesong, width=8, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10,
                                                                                    pady=5)

        # Inserting Submit Button
        Button(buttonframe, text="Submit", command=self.submitSentence, width=10, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10,
                                                                                    pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root, text="Sentences Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)

        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)

        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)

        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        Week_List = [1, 2, 3, 4]
        Sentences_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        random.shuffle(Week_List)

        # Changing Directory for fetching Songs
        os.chdir(f"/Users/cvkrishnarao/Desktop/RA/Intelligibility_Software_Module/Test_File/Week_1")

        # Fetching Songs
        sentencesTrack = os.listdir()

        # Inserting Songs into Playlist Condition check to remove unwanted System Files eg: .DS_Store etc.
        for track in sentencesTrack:
            if track.startswith("S"):
                self.playlist.insert(END, track)

    def playsong(self):

        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))

        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))

        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):

        # Stopped Song
        pygame.mixer.music.stop()

    def nextsong(event):

        global index
        index += 1
        # pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()

    def pausesong(self):

        # Paused Song
        pygame.mixer.music.pause()

    def submitSentence(self):
        if self.Input_Text != "":

            # gets() the character from starting to end of character
            list_Text = self.Input_Text.get("1.0", 'end')
            self.main_list.append(list_Text)
            with open("/Users/cvkrishnarao/Desktop/data_entry.csv", "a+", newline='\n') as file:

                if self.count == 0:
                    Writer = writer(file)
                    Writer.writerow(["Input Text"])
                    Writer.writerow(self.main_list)
                    self.main_list = []
                    self.count += 1

                else:
                    Writer = writer(file)
                    Writer.writerow(self.main_list)
                    self.main_list = []
