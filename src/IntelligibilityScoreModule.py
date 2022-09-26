from difflib import SequenceMatcher
import pandas as pd


class IntelligibilityModule:

    def __init__(self):
        self.dataFrame = pd.DataFrame()
        self.Intelligibility_List = []
        self.Intelligibility_df = pd.DataFrame()

    def ScoreModule(self):
        self.dataFrame = pd.read_csv("Input_Sentences/Sentences_Test.csv")
        self.dataFrame = self.dataFrame.drop('Unnamed: 0', axis=1)
        list_sentences = list(self.dataFrame['SENTENCE'])
        list_input_sentences = list(self.dataFrame['INPUT_SENTENCES'])
        for i in range(len(list_sentences)):
            ratio = SequenceMatcher(None, list_sentences[i].lower(), list_input_sentences[i].lower()).ratio()
            self.Intelligibility_List.append(ratio)

        self.Intelligibility_df = pd.DataFrame(self.Intelligibility_List)
        self.Intelligibility_df.to_csv("Input_Sentences/Intelligibility_Score.csv")
