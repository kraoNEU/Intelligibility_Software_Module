import csv
import os
from tkinter import messagebox
import pandas as pd
import pygame
from tkinter import *
import random


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
        self.set_current_csv_input_sentences_file_path = ''
        self.Person_Index_append = ''

        # Music Counter Checker
        self.sentence_count_repeat = 0

        # Week List
        Week_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

        # Sentences List
        Sentences_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

        # Writing the Main Sentences from Text Box
        self.main_list = []

        # Getting the File Name Dynamically from the cwd()
        self.set_current_csv_input_sentences_file_path = os.getcwd().split("/")[-1]

        # Getting the value to append the vallues to the Index columns of the csv and xlsx file
        self.Person_Index_append = self.set_current_csv_input_sentences_file_path[0] + \
                                   self.set_current_csv_input_sentences_file_path[-1]

        # List for Serial Number and the Index
        self.Week_Sentences_List = []

        # Setting the Current Sentence Track
        self.current_sentence_number = int(0)
        self.current_sentence_number2 = self.current_sentence_number

        # Directory for the Sentences, Week Path
        self.complete_sentences_list = []

        # Initiating Pygame
        pygame.init()

        # String Input for Text Box
        self.Input_Text = StringVar()

        # Initiating Pygame Mixer
        pygame.mixer.init()

        # Declaring track Variable
        self.track = StringVar()

        # Shuffle the Random Week
        random.shuffle(Week_List)

        # Shuffle the Random Sentences
        random.shuffle(Sentences_List)

        # Sentences Index List for the Index Update
        self.sentences_index_list = []

        # Creating random week and sentences list
        for weeks in Week_List:
            for sentences in Sentences_List:

                # Creating the list of directories for the list of sentences taken from the dynamic user input
                list_For_Csv = f"{self.Person_Index_append}_W{weeks}_S{sentences}"
                self.Week_Sentences_List.append(list_For_Csv)
                path = f"Week_{weeks}/Sentence_{sentences}.wav"

                # Condition Check for the Path. If not It will continue
                if os.path.isfile(path):
                    self.complete_sentences_list.append(path)
                    self.sentences_index_list.append(list_For_Csv)
                else:
                    continue

        # Keeping the music loaded onto the self.music platform
        self.next_music = (self.complete_sentences_list[self.current_sentence_number + 1])

        # Keeping the current frame in the list as well
        self.current_sentence = (self.complete_sentences_list[self.current_sentence_number])

        # Creating the Background
        trackframe = LabelFrame(self.root, text="Sentences Input", font=("times new roman", 15),
                                bg="black",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=100, width=600, height=100)

        # Creating a Text Widget For the Input
        self.Input_Text = Text(trackframe, width=83, height=5)
        self.Input_Text.grid(row=50, column=50)

        # Inserting Instruction Window
        text = Text(self.root, width=50, height=30, background=
        "gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
        text.place(x=0, y=0, width=600, height=100)

        # Insert the text at the beginning
        text.insert(INSERT, "Write Something About Yourself")

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=200, width=600, height=100)

        # Inserting Play Button
        Button(buttonframe, text="Play / Replay", command=self.playSentence, width=10, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                    pady=5)
        # Inserting Next Button
        Button(buttonframe, text="Next", command=self.nextSentence, width=8, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10,
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

            # Condition check for repetition, Repetition is allowed for only 2 times
            else:
                if self.sentence_count_repeat == 0 or self.sentence_count_repeat == 1:
                    pygame.mixer.music.load(self.complete_sentences_list[self.current_sentence_number])
                    pygame.mixer.music.play()
                    self.sentence_count_repeat += 1

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

            self.next_music = (self.sentences_index_list[self.current_sentence_number + 1])
            self.current_sentence = (self.sentences_index_list[self.current_sentence_number])
            if os.path.exists("Input_Sentences/"):
                if self.Input_Text != "":

                    # get() the character from starting to end of character
                    list_Text = self.Input_Text.get("1.0", 'end')
                    list_Text = list_Text.strip()
                    self.main_list.append(list_Text)
                    with open(f"Input_Sentences/Input_Sentences_{self.set_current_csv_input_sentences_file_path}.csv",
                              "a+") as file:

                        if self.count == 0:

                            self.main_list.append(self.sentences_index_list[self.count])
                            writer = csv.writer(file, delimiter=",")
                            writer.writerow(('Sentences', 'Index'))
                            writer.writerow(self.main_list)

                            self.main_list = []
                            self.count += 1
                            self.sentence_count_repeat = 0

                        else:

                            self.main_list.append(self.sentences_index_list[self.count])
                            writer = csv.writer(file, delimiter=",")
                            writer.writerow(self.main_list)

                            self.main_list = []
                            self.count += 1
                            self.sentence_count_repeat = 0
            else:
                os.mkdir("Input_Sentences/")
                if self.Input_Text != "":

                    # get() the character from starting to end of character
                    list_Text = self.Input_Text.get("1.0", 'end')
                    list_Text = list_Text.strip()
                    self.main_list.append(list_Text)
                    with open(f"Input_Sentences/Input_Sentences_{self.set_current_csv_input_sentences_file_path}.csv",
                              "a+") as file:

                        if self.count == 0:

                            self.main_list.append(self.sentences_index_list[self.count])
                            writer = csv.writer(file, delimiter=",")
                            writer.writerow(('Sentences', 'Index'))
                            writer.writerow(self.main_list)

                            self.main_list = []
                            self.count += 1
                            self.sentence_count_repeat = 0

                        else:

                            self.main_list.append(self.sentences_index_list[self.count])
                            writer = csv.writer(file, delimiter=",")
                            writer.writerows(self.main_list)

                            self.main_list = []
                            self.count += 1
                            self.sentence_count_repeat = 0

                file.close()
            self.Input_Text.delete('1.0', END)

        except IndexError:

            list_Text = self.Input_Text.get("1.0", 'end')
            list_Text = list_Text.strip()
            self.main_list.append(list_Text)
            with open(f"Input_Sentences/Input_Sentences_{self.set_current_csv_input_sentences_file_path}.csv",
                      "a+") as file:

                if self.count == 0:

                    self.main_list.append(self.sentences_index_list[self.count])
                    writer = csv.writer(file, delimiter=",")
                    writer.writerow(('Sentences', 'Index'))
                    writer.writerow(self.main_list)

                    self.main_list = []
                    self.count += 1
                    self.sentence_count_repeat = 0

                else:

                    self.main_list.append(self.sentences_index_list[self.count])
                    writer = csv.writer(file, delimiter=",")

                    writer.writerow(self.main_list)

                    self.main_list = []
                    self.count += 1
                    self.sentence_count_repeat = 0

            messagebox.showerror('End of the Sentences', 'You have completed all the sentences. Thank you!')
            self.csvSerialNumber()
            self.root.destroy()
            return

        # Putting the Next Track in the List as the Main Track
        pygame.mixer.music.stop()
        self.current_sentence_number = int(self.current_sentence_number2 + 1)
        self.current_sentence_number2 = self.current_sentence_number

        current_sentence = (self.complete_sentences_list[self.current_sentence_number])
        pygame.mixer.music.load(current_sentence)
        self.sentence_count_repeat = 0

    def csvSerialNumber(self):
        """
        Reads the csv file with all the Inputted sentences
        Appends the Serial Numbers that is week and sentence numbers to the csv file
        return: Returns the csv file with the serial number
        """
        self.dataFrame = pd.read_csv(
            f"Input_Sentences/Input_Sentences_{self.set_current_csv_input_sentences_file_path}.csv")
        self.dataFrame.to_excel(
            f"Input_Sentences/Input_Sentences_{self.set_current_csv_input_sentences_file_path}.xlsx", index=False)
