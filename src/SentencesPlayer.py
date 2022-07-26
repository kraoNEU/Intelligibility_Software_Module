from tkinter import messagebox
import pygame
import os
from tkinter import *
import random
from csv import *


class SentencesPlayer:

    def __init__(self, root):

        self.root = root
        self.count = 0

        # Week List
        Week_List = [1]

        # Sentences List
        Sentences_List = [1, 2, 3, 4, 5, 6]

        # Writing the Main Sentences from Text Box
        self.main_list = []

        # List for Serial Number and the Index
        self.Week_Sentences_List = []

        self.music_number = int(0)
        self.music_number2 = self.music_number

        # Directory for the Sentences, Week Path
        self.complete_sentences_list = []

        # Initiating Pygame
        pygame.init()

        self.Input_Text = StringVar()

        # Initiating Pygame Mixer
        pygame.mixer.init()

        # Declaring track Variable
        self.track = StringVar()

        # Shuffle the Random Week
        random.shuffle(Week_List)

        # Shuffle the Random Sentences
        random.shuffle(Sentences_List)

        # Creating random week and sentences list
        for weeks in Week_List:
            for sentences in Sentences_List:
                list_For_Csv = f"W{weeks}_S{sentences}"
                self.Week_Sentences_List.append(list_For_Csv)
                path = f"/Users/cvkrishnarao/Desktop/RA/Intelligibility_Software_Module/Test_File/Week_{weeks}/Sentence_{sentences}.wav"

                # Checking for this path in the future version to check and then append to the file
                if os.path.isfile(path):
                    print("Path Available")
                    print(list_For_Csv)
                self.complete_sentences_list.append(path)

        self.next_music = (self.complete_sentences_list[self.music_number + 1])
        self.current_music = (self.complete_sentences_list[self.music_number])

        # Creating the Background
        trackframe = LabelFrame(self.root, text="Sentences Input", font=("times new roman", 15),
                                bg="Navyblue",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=800, height=100)

        # Creating a Text Widget For the Input
        self.Input_Text = Text(trackframe, width=83, height=5)
        self.Input_Text.grid(row=50, column=50)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)

        # Inserting Play Button
        Button(buttonframe, text="Play / Replay", command=self.playSentence, width=10, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                    pady=5)
        # Inserting Next Button
        Button(buttonframe, text="Next", command=self.nextSentence, width=8, height=1,
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

        # Inserting Songs into Playlist Condition check to remove unwanted System Files eg: .DS_Store etc.
        for track in self.complete_sentences_list:
            if track.startswith("S"):
                self.playlist.insert(END, track)

    def playSentence(self):

        current_sentence_playing = (self.complete_sentences_list[self.music_number])

        if pygame.mixer.get_init():
            if pygame.mixer.music.pause() is False:
                pygame.mixer.music.play()
                paused = True
            else:
                pygame.mixer.music.load(self.complete_sentences_list[self.music_number])
                pygame.mixer.music.play()
                paused = False
        else:
            pygame.mixer.init()
            pygame.mixer.music.load(f"{current_sentence_playing}")
            pygame.mixer.music.play()
            paused = False

    def nextSentence(self):

        try:
            self.next_music = (self.Week_Sentences_List[self.music_number + 1])
        except IndexError:
            messagebox.showerror('End of the Sentences', 'You have completed all the sentences!')

        self.current_music = (self.Week_Sentences_List[self.music_number])

        pygame.mixer.music.stop()
        self.music_number = int(self.music_number2 + 1)
        self.music_number2 = self.music_number
        current_music = (self.complete_sentences_list[self.music_number])
        pygame.mixer.music.load(current_music)

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
