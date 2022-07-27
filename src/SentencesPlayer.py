from tkinter import messagebox
import pandas as pd
import pygame
from tkinter import *
import random
from csv import *


class SentencesPlayer:

    def __init__(self, root):
        """
        Initialised all the Tkinter Root and the Environment Variables.
        Randomised the Files for the Sentences and Weeks
        Created all the Background Widgets and the Labels for the GUI Module
        """
        self.root = root
        self.count = 0
        self.dataFrame = pd.DataFrame()

        # Week List
        Week_List = [1]

        # Sentences List
        Sentences_List = [1, 2, 3, 4, 5, 6]

        # Writing the Main Sentences from Text Box
        self.main_list = []

        # List for Serial Number and the Index
        self.Week_Sentences_List = []

        # Setting the Current Sentence Track
        self.current_sentence_number = int(0)
        self.current_sentence_number2 = self.current_sentence_number

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

                # Checking for the file path. Future Version to Deprecate this. Based on Dynamic File Placement
                # if os.path.isfile(path):
                #     print(list_For_Csv)
                self.complete_sentences_list.append(path)

        self.next_music = (self.complete_sentences_list[self.current_sentence_number + 1])
        self.current_sentence = (self.complete_sentences_list[self.current_sentence_number])

        # Creating the Background
        trackframe = LabelFrame(self.root, text="Sentences Input", font=("times new roman", 15),
                                bg="black",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

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

    def playSentence(self):
        """
        Sets the Current Main Track in the Loop and Loads the Music to the pygame library
        After Loads() the Pygame library plays the music
        :returns: Null
        """

        # Setting the Current Sentence as the Main Track
        current_sentence_playing = (self.complete_sentences_list[self.current_sentence_number])

        # Check for other Tracks in the List
        if pygame.mixer.get_init():
            if pygame.mixer.music.pause() is False:
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load(self.complete_sentences_list[self.current_sentence_number])
                pygame.mixer.music.play()
        else:
            pygame.mixer.init()
            pygame.mixer.music.load(f"{current_sentence_playing}")
            pygame.mixer.music.play()

    def nextSentence(self):
        """
        Button Label to go to the next sentence. Checks till the end of sentences
        Raises a Soft exception to handle to the message box()
        return: Null to handle the soft exception
        """

        # Exception Handling for the End of Sentences
        try:
            self.next_music = (self.Week_Sentences_List[self.current_sentence_number + 1])
        except IndexError:
            messagebox.showerror('End of the Sentences', 'You have completed all the sentences. Thank you!')
            self.csvSerialNumber()
            self.root.destroy()
            return

        self.current_sentence = (self.Week_Sentences_List[self.current_sentence_number])

        # Putting the Next Track in the List as the Main Track
        pygame.mixer.music.stop()
        self.current_sentence_number = int(self.current_sentence_number2 + 1)
        self.current_sentence_number2 = self.current_sentence_number

        current_sentence = (self.complete_sentences_list[self.current_sentence_number])
        pygame.mixer.music.load(current_sentence)

    def submitSentence(self):
        """
        The Text Box Input is read from the .get() method
        The File is Inputted through row-wise input
        The count is appended to the next row
        Return: None
        """

        if self.Input_Text != "":

            # get() the character from starting to end of character
            list_Text = self.Input_Text.get("1.0", 'end')
            self.main_list.append(list_Text)
            with open("/Users/cvkrishnarao/Desktop/Input_Sentences.csv", "a+", newline='\n') as file:

                if self.count == 0:
                    Writer = writer(file)
                    Writer.writerow(["Input_Text"])
                    Writer.writerow(self.main_list)
                    self.main_list = []
                    self.count += 1

                else:
                    Writer = writer(file)
                    Writer.writerow(self.main_list)
                    self.main_list = []

            file.close()

    def csvSerialNumber(self):
        """
        Reads the csv file with all the Inputted sentences
        Appends the Serial Numbers that is week and sentence numbers to the csv file
        return: Returns the csv file with the serial number
        """
        self.dataFrame = pd.read_csv("/Users/cvkrishnarao/Desktop/Input_Sentences.csv")
        self.dataFrame.insert(0, "Serial_Number", self.Week_Sentences_List)
        self.dataFrame.to_csv("/Users/cvkrishnarao/Desktop/Input_Sentences.csv")
