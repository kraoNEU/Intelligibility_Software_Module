# &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Intelligibility Software GUI Module for SMILe Lab

### Request For Proposal


#### **Project Overview**

The objective of this project is to build a user-friendly experimental software for acquiring and analyzing listener ratings of speech intelligibility and naturalness for the Speech Motor Impairment and Learning (SMILe) Lab, under the direction of Dr. Kristen Allison.

#### **Project Goals**

The goals of the software are to accomplish the following functions:

1. Allow researchers to upload sets of .wav files of speakers producing known target sentences (or for the program to pull .wav files from a specified folder containing the files). The programs need to know the target sentences and have the correct .wav file associated with each sentence. It needs to be able to pull different sets of sentences for different speakers.
1. Collect intelligibility data from listeners. This involves having an interface that:
   1. presents .wav files to listeners (study participants) in a randomized order
   1. provides a space for listeners to type in what they think the speaker said in each .wav file
1. ` `Analyze intelligibility data. To do this the program must:
   1. Compare what the listener typed to the target sentence.
   1. Determine the number of words the listener got correct for each sentence.
   1. Calculate a % of words correctly identified across the entire sentence set. 
      1. For example, if the listener heard and transcribed 11 sentences totaling 80 words, the program should calculate the total % of words correctly transcribed by the listener across the 80 possible target words. 



#### **Scope of Work**

The Scope of work is a GUI based Intelligibility Program. The Work is divided into **Phase – I** and **Phase – II** as given in the figure 1.1 down below:

![Intelligibility GUI Module Workflow](Logo/software_workflow.png)

**Figure: 1.1: Process Workflow of the Intelligibility Software Module.**

Phase – I:

The Phase – I, which is a simple GUI Console Application which would be implemented first wherein the Application has a simple Text Box for the Input and the User will be able to click on “Next” button to proceed to the Input Text box for the next audio file. 

The Inputted text would be stored on an Excel sheet to be viewed. Later in the Phase – II module of the Program will be able to compare the Text Strings and to generate an Intelligibility Score of a particular Subject.


Phase – II:

The Phase – II, which is the Intelligibility Module which has the Text Comparison Operator which compares the word, **alphabet by alphabet** to general an Intelligibility score to the user.

This will generate the metric to the user to track the Subject’s progress in the Speech Training.

**Target Deliverable Schedule**

***Phase-I:** Version – 1 (2nd Week of July Planned, 2022)*<br>

***Phase-II:** Version – 1 (Last Week of August Planned, 2022)*<br>

***Phase-III:** Improvements (if any) and Bug Fixes and Version Updates:*

` `*(September, 2022 Planned)*







#### **Existing Roadblocks or Technical Issues**

- The Template for comparison needs to be Randomized.
- The GUI application complications should be taken into considerations.
- The alignment of the sentences according to “.WAV” files might lead to an Issue of Misalignment
- Since we are developing GUI based application it needs to be given system level permission to read / write and edit files. This might get flagged as a malware by IT department. Therefore, consideration with respect to IT should also be taken in.

#### **Evaluation Metrics**

*The project is divided into Phase – I and Phase - II*

**Phase – I:**

- Phase – I is expected to take in the Text Sentences and Import them to an Excel Sheet with Excel Spreadsheet with Unique Identifier names.

**Phase – II:**

- Phase – II is expected to take in the Text Sentences and calculate the Intelligibility Score based on the user input and the subject’s reading template


#### **Contact Information**

For questions or concerns connected to this RFP, we can be reached at:<br>

#### Prepared by:
**Name**: C V Krishna Rao, <BR>
**Email**: chelamkuri.v@northeastern.edu